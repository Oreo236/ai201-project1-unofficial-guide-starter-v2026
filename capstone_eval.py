#!/usr/bin/env python3
"""Capstone trials for criteria 1, 2, 3 and 5. (Criterion 4 is done by hand.)

    python capstone_eval.py --label before      # three trials, writes results/capstone_<label>.md

Uses Flask's test client against serve.py, response cache off, paced under the
free tier's 15 requests/minute. Every request also lands in logs/requests.jsonl.

Choices made here that you can change (they are not in criteria.md):
  REQUIRED_FIELDS  what "all five required fields" means for criterion 2
  WARM             criterion 3: warm = after one throwaway request this process
  failure test     criterion 5: the model client is replaced by one that raises
                   the same error text the real API gave (429, 503). time.sleep
                   is patched out so the starter's 1+2+4+8 s retry backoff does
                   not make each simulated failure take 15 s.
"""
import argparse
import datetime as dt
import json
import os
import sys
import time

os.environ["AI201_CACHE"] = "0"

import config

config.REQUESTS_PER_MINUTE = 10

import generate
import questions as qs
import serve

REQUIRED_FIELDS = ["timestamp", "input", "output", "status", "duration_ms"]
LEAK_MARKERS = ["Traceback", "RuntimeError", "Error:", "Exception", "RESOURCE_EXHAUSTED",
                "UNAVAILABLE", "{'error'", "googleapis", "aistudio", "Last error"]

client = serve.app.test_client()


def log_lines():
    if not serve.LOG_PATH.exists():
        return []
    return serve.LOG_PATH.read_text(encoding="utf-8").splitlines()


def send(kind, payload):
    if kind == "json":
        return client.post("/ask", json=payload)
    return client.post("/ask", data=payload, content_type="text/plain")


def trial_a_b():
    """Criteria 1 and 2: 20 mixed requests, count log lines, check fields."""
    valid = [q["question"] for q in qs.QUESTIONS + qs.HARDER_QUESTIONS]          # 10
    refused = qs.OUT_OF_SCOPE                                                    # 5
    bad = [("json", {"question": ""}), ("json", {"question": "   "}),
           ("raw", "not json"), ("json", {"question": 123}), ("json", {"question": ["x"]})]  # 5
    requests = [("json", {"question": q}) for q in valid + refused] + bad
    before = len(log_lines())
    codes = []
    for kind, payload in requests:
        codes.append(send(kind, payload).status_code)
    new = log_lines()[before:]
    recs = []
    for line in new:
        try:
            recs.append(json.loads(line))
        except json.JSONDecodeError:
            recs.append({})
    complete = sum(all(f in r for f in REQUIRED_FIELDS) for r in recs)
    nulls = sum(any(r.get(f) is None for f in REQUIRED_FIELDS) for r in recs)
    return {"sent": len(requests), "logged": len(new), "complete": complete,
            "records_with_a_null_required_field": nulls, "status_codes": codes}


def trial_c():
    """Criterion 3: 10 warm requests, seconds each."""
    questions = [q["question"] for q in qs.QUESTIONS + qs.HARDER_QUESTIONS]
    client.post("/ask", json={"question": questions[0]})                         # warm-up, not counted
    times = []
    for q in questions:
        t = time.perf_counter()
        r = client.post("/ask", json={"question": q})
        times.append((round(time.perf_counter() - t, 2), r.status_code))
    return {"under_8s": sum(t < 8 and s == 200 for t, s in times), "of": len(times), "times": times}


class _FakeModels:
    def __init__(self, message):
        self.message = message

    def generate_content(self, **kwargs):
        raise Exception(self.message)


class _FakeClient:
    def __init__(self, message):
        self.models = _FakeModels(message)


def trial_failures():
    """Criterion 5: 3 simulated 429s and 2 simulated 503s."""
    cases = [
        ("429", "429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota', 'status': 'RESOURCE_EXHAUSTED'}}"),
        ("429", "429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'Quota exceeded for metric generate_content_free_tier_requests', 'status': 'RESOURCE_EXHAUSTED'}}"),
        ("429", "429 RESOURCE_EXHAUSTED. rate limit exceeded"),
        ("503", "503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand.', 'status': 'UNAVAILABLE'}}"),
        ("503", "503 UNAVAILABLE. {'error': {'code': 503, 'message': 'The service is overloaded.', 'status': 'UNAVAILABLE'}}"),
    ]
    real_client, real_sleep = generate._get_client, generate.time.sleep
    out = []
    try:
        generate.time.sleep = lambda s: None
        for kind, message in cases:
            generate._get_client = lambda m=message: _FakeClient(m)
            before = len(log_lines())
            r = client.post("/ask", json={"question": "What does laundry cost at Innisfree Hall?"})
            body = r.get_json(silent=True) or {}
            text = json.dumps(body)
            leaks = [m for m in LEAK_MARKERS if m in text]
            out.append({"simulated": kind, "status": r.status_code, "body": body,
                        "leak_markers_found": leaks, "logged": len(log_lines()) > before})
    finally:
        generate._get_client, generate.time.sleep = real_client, real_sleep
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default="run")
    ap.add_argument("--trials", type=int, default=3)
    args = ap.parse_args()
    report = {"label": args.label, "when": dt.datetime.now().isoformat(timespec="seconds"), "trials": []}
    for n in range(1, args.trials + 1):
        print(f"--- trial {n}", flush=True)
        t = {"trial": n, "a_b": trial_a_b()}
        print("  A/B:", {k: v for k, v in t["a_b"].items() if k != "status_codes"}, flush=True)
        time.sleep(60)  # let the per-minute window clear
        t["c"] = trial_c()
        print("  C:", t["c"]["under_8s"], "of", t["c"]["of"], t["c"]["times"], flush=True)
        t["failures"] = trial_failures()
        print("  5:", [(f["status"], f["leak_markers_found"]) for f in t["failures"]], flush=True)
        report["trials"].append(t)
        time.sleep(60)
    path = config.RESULTS_DIR / f"capstone_{dt.datetime.now():%Y-%m-%d_%H%M}_{args.label}.md"
    path.write_text(f"# Capstone trials — {args.label}\n\nProduced by `capstone_eval.py`.\n\n```json\n"
                    + json.dumps(report, indent=2, ensure_ascii=False) + "\n```\n", encoding="utf-8")
    print("Wrote", path)


if __name__ == "__main__":
    main()
