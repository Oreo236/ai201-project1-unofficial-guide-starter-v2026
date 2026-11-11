"""Send 10 questions through serve.py's /ask and report latency and token cost.

    python measure_cost.py

Uses Flask's test client (no network port needed). Writes to logs/requests.jsonl
like any real request. Paced under the free tier's 15 requests/minute.
"""
import statistics
import sys
import time

import config
config.REQUESTS_PER_MINUTE = 10  # free tier allows 15/min; stay under it

import questions as qs
import serve

items = [q["question"] for q in qs.QUESTIONS] + [q["question"] for q in qs.HARDER_QUESTIONS]
client = serve.app.test_client()
rows = []
for q in items:
    t = time.perf_counter()
    r = client.post("/ask", json={"question": q})
    rows.append((time.perf_counter() - t, r.status_code))
    print(f"{rows[-1][0]:6.2f}s  {r.status_code}  {q[:60]}")

import json
recs = [json.loads(l) for l in serve.LOG_PATH.open()][-len(items):]
tin = [r.get("tokens_in", 0) for r in recs]; tout = [r.get("tokens_out", 0) for r in recs]
secs = [r[0] for r in rows]
print(f"\nruns: {len(items)}  errors: {sum(r[1] != 200 for r in rows)}")
print(f"seconds per run: mean {statistics.mean(secs):.2f}, max {max(secs):.2f}")
print(f"tokens per run:  mean in {statistics.mean(tin):.0f}, out {statistics.mean(tout):.0f}, total {statistics.mean(tin)+statistics.mean(tout):.0f}")
