#!/usr/bin/env python3
"""
The Unofficial Guide — the same pipeline, over HTTP.

    python serve.py                          run it locally on port 5000
    gunicorn serve:app                       run it the way a host runs it

Nothing new happens in this file. It is a wrapper: a request comes in, it
hands the question to `app.py::ask_pipeline` — the exact function the command
line uses — and hands the answer back as JSON. Retrieval, the relevance gate
and the grounded prompt all still live where they lived. If you change how
your system answers, you change it in those files and this one follows.

Two routes:

    POST /ask       {"question": "..."} in, the answer and its sources out
    GET  /health    is the service up, and is there an index to search

Why this exists: `app.py` runs once and exits, which is fine on your laptop
and impossible to deploy. A hosted service has to stay up and wait for
requests. This is the smallest thing that does that.

Capstone: every request to /ask now writes one JSON line to logs/requests.jsonl
(timestamp, input, output, duration, status, plus gate and token fields).
Failures and bad input are logged too.
"""

import json
import os
import threading
import time
from datetime import datetime, timezone

from flask import Flask, jsonify, request

import config

app = Flask(__name__)

LOG_PATH = config.ROOT / "logs" / "requests.jsonl"
_log_lock = threading.Lock()


def log_request(record: dict) -> None:
    """Append one structured record. Never lets a logging problem break a request."""
    try:
        LOG_PATH.parent.mkdir(exist_ok=True)
        record = {"timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds"), **record}
        with _log_lock, LOG_PATH.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError:
        pass


def is_model_busy(exc: Exception) -> bool:
    """True for the model service being rate limited or unavailable (429 / 503)."""
    text = f"{type(exc).__name__} {exc}".lower()
    return any(k in text for k in ("429", "503", "resource_exhausted", "unavailable",
                                   "rate limit", "rate limited", "high demand"))


@app.get("/health")
def health():
    """Is the service up, and is there an index to search?

    Two different questions, and the second one is the one that bites. A
    freshly deployed service answers this route happily while every /ask
    returns "no index" — hosts give you no disk that survives a restart, so
    the index has to be built as part of getting the service up. Checking
    here means you find that out in one request instead of five.
    """
    from store import index_exists

    ready = index_exists(config.CORPUS)
    return jsonify(
        {
            "status": "ok",
            "corpus": config.CORPUS,
            "index_ready": ready,
            "detail": (
                "ready"
                if ready
                else "no index for this corpus — run `python app.py index`"
            ),
        }
    )


@app.post("/ask")
def ask():
    """One question in, one grounded answer out.

    A refused question is a 200, not an error. The gate refusing is your
    system working — it is an answer, and the JSON says so with
    `"refused": true` so whatever calls this can tell the two apart.
    """
    from app import ask_pipeline
    from generate import token_counts

    started = time.perf_counter()
    payload = request.get_json(silent=True) or {}
    raw = payload.get("question")
    question = (raw if isinstance(raw, str) else "").strip()

    def ms() -> int:
        return round((time.perf_counter() - started) * 1000)

    if not question:
        message = (
            "Send JSON with a question in it, like "
            '{"question": "is the housing lottery random?"}'
        )
        log_request({"input": raw, "output": message, "status": 400,
                     "duration_ms": ms(), "error": "bad_input"})
        return jsonify({"error": message}), 400

    before = token_counts()
    try:
        outcome = ask_pipeline(question, corpus=config.CORPUS)
    except Exception as exc:  # noqa: BLE001 — a reader gets this, not a traceback
        detail = f"{type(exc).__name__}: {exc}"
        if is_model_busy(exc):
            # Capstone improvement: the caller gets a plain message and a 503;
            # the full detail stays in the log only.
            log_request({"input": question, "output": detail, "status": 503,
                         "duration_ms": ms(), "error": "model_unavailable"})
            return jsonify({"error": "The model is busy right now. Please try again in a minute."}), 503
        log_request({"input": question, "output": detail, "status": 500,
                     "duration_ms": ms(), "error": type(exc).__name__})
        return jsonify({"error": detail}), 500

    after = token_counts()
    log_request({
        "input": question,
        "output": outcome["answer"],
        "status": 200,
        "duration_ms": ms(),
        "refused": outcome["refused"],
        "best_distance": round(outcome["best_distance"], 4),
        "sources": outcome["sources"],
        "tokens_in": after["prompt"] - before["prompt"],
        "tokens_out": after["output"] - before["output"],
        "error": None,
    })

    return jsonify(
        {
            "question": question,
            "answer": outcome["answer"],
            "refused": outcome["refused"],
            "sources": outcome["sources"],
            "best_distance": round(outcome["best_distance"], 4),
            "threshold": outcome["threshold"],
            "corpus": config.CORPUS,
        }
    )


def main():
    # Hosts tell you which port to listen on through PORT, and they expect you
    # on 0.0.0.0. Binding 127.0.0.1 instead works perfectly on your laptop and
    # then answers nothing at all once deployed, because the host's router
    # can't reach a socket that only accepts connections from inside the
    # container. It is the single most common way a first deploy "succeeds"
    # and is unreachable.
    port = int(os.getenv("PORT", "5000"))

    # Debug mode reloads on save, which is handy, and prints a console that
    # runs arbitrary code, which is not something to leave switched on where
    # strangers can reach it. Off unless you ask for it.
    debug = os.getenv("AI201_DEBUG", "0") == "1"

    print(f"Serving The Unofficial Guide on http://localhost:{port}")
    print(f"Corpus: {config.CORPUS}    (Ctrl-C to stop)\n")
    print("Try it from another terminal:\n")
    print(f"  curl http://localhost:{port}/health")
    print(
        f"  curl -X POST http://localhost:{port}/ask \\\n"
        f"    -H 'Content-Type: application/json' \\\n"
        f"    -d '{{\"question\": \"is the housing lottery random?\"}}'\n"
    )

    app.run(host="0.0.0.0", port=port, debug=debug)


if __name__ == "__main__":
    main()
