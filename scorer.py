"""Pass/fail judge used by run_eval.py.

An answer passes when it contains the `expects` phrase (case-insensitive).
Refusals fail, because every question passed in here is one the corpus covers.
"""


def judge(question, expects, answer, results) -> bool:
    if not expects:
        return False
    return expects.lower() in answer.lower()
