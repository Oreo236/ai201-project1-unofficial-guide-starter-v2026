# The Unofficial Guide

<!-- Add your name before submitting. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

This project uses the `campus_life` corpus, a collection of short student
posts about university housing, courses, dining, transit, and administrative
rules. It answers specific questions such as how the housing lottery works,
how much time a course takes, and when a dining hall is busiest. Answers are
grounded in the local documents and identify the source document used.

## Chunking Strategy

**Chunk size:** 400 characters
**Overlap:** 80 characters

The corpus contains 88 short documents averaging about 317 characters. The
starter's 800-character window produced one chunk per document, but it did not
give me a way to control paragraph boundaries. A 400-character window keeps
most posts intact while splitting only the longer posts when needed. The custom
function carries the last paragraph into the next chunk as context; when an
individual paragraph is too long, it uses the configured 80-character overlap.
Chunk boundaries are snapped to whitespace so sentences are not cut in the
middle of a word.

## Sample Chunks

The samples below were produced by `chunker.py::split_documents`.

**Chunk 1** — source: `admin_housing_lottery.txt#0` — produced by: `chunker.py::split_documents`

```
On the housing lottery

The housing lottery is not random in the way most people assume. Rising sophomores get a number drawn at random, but juniors and seniors are ordered by accumulated credit hours first, and only tie-break randomly. That means a senior who took summer courses reliably beats a senior who didn't. Numbers come out the second week of March and selection runs over four evenings.
```

**Chunk 2** — source: `course_cs_210.txt#0` — produced by: `chunker.py::split_documents`

```
CS 210 Data Structures

I'm a junior and I've done this twice now. Format is lecture with weekly labs; slides go up after class, not before. Assessment: two midterms and a final, all drawn from lecture material rather than the textbook. Midterms are curved, the final is not.

Expect 8 to 10 hours a week outside class.
```

**Chunk 3** — source: `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::split_documents`

```
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 4** — source: `housing_innisfree_hall.txt#0` — produced by: `chunker.py::split_documents`

```
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.
```

**Chunk 5** — source: `transit_shuttle.txt#0` — produced by: `chunker.py::split_documents`

```
The campus shuttle

Runs a loop every 20 minutes from 7am to 11pm on weekdays and every 40 minutes on weekends. The published timetable is optimistic by about five minutes in the morning and accurate the rest of the day.

It's free with a student ID. The stop outside Fenwick Court is the one that gets skipped when the driver is behind, which is worth knowing if you live there.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:** Is the housing lottery random, and how are students prioritized?

**Answer:** The housing lottery is not entirely random in the way most people assume. Rising sophomores get a number drawn at random, but juniors and seniors are ordered first by accumulated credit hours, with random tie-breaks used only for ties.

**Source line:** Source: admin_housing_lottery.txt (best distance 0.171, cutoff 0.6; produced by `python app.py ask`, `generate.py::answer_from_chunks`)

**Current relevance cutoff:** 0.6 (the starter setting in `config.py`; it has
not yet been changed). A local retrieval-only pass using `store.py::search`,
the `campus_life` corpus, and the configured embedding model returned in-corpus
best distances from 0.1708 to 0.2635 and out-of-corpus best distances from
0.8246 to 0.9340. The current 0.6 cutoff falls between those groups. These
are single-pass retrieval measurements, not the repeated answer evaluation
required in Unit 2.

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| Is the housing lottery random, and how are students prioritized? | Yes | 0.1708 |
| When can students add or drop a course, and what happens after week two? | Yes | 0.2635 |
| How much time should I expect to spend on CS 210 outside class? | Yes | 0.2499 |
| How long are the peak waits at Pellew Dining Hall? | Yes | 0.1806 |
| What does laundry cost at Innisfree Hall? | Yes | 0.2155 |
| What is the capital of Mongolia? | No | 0.8246 |
| How do I change the oil in a diesel engine? | No | 0.9340 |
| Who won the 1994 World Cup? | No | 0.8859 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.8442 |
| How do I write a for loop in Rust? | No | 0.8907 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**

**2.**

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2
 

Two question sets were used. The **original set** is the five questions from
`questions.py::QUESTIONS` plus `OUT_OF_SCOPE`. The **harder set** is
`HARDER_QUESTIONS` plus `OUT_OF_SCOPE_CAMPUS`, added after seeing the first
results (so it is a stress test, not a blind test). `scorer.py::judge` marks an
answer correct when it contains the `expects` phrase. All runs: top-k 5, cutoff
0.6, caching off, three runs, `run_eval.py::main`. Free-tier pacing was lowered to
10 requests/min from the command line; `config.py` was not changed.

## Run Log — Before

Files: `results/run_2026-09-20_2054_before-scored.md` (original set),
`results/run_2026-09-20_2056_before-harder-scored.md` (harder set).

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunks contain the answer (original / harder) | 4 of 5 | 5/5 / 5/5 | 5/5 / 5/5 | 5/5 / 5/5 | MET |
| 2. Every answer names a source (original / harder) | 5 of 5 | 5/5 / 4/5 | 5/5 / 4/5 | 5/5 / 4/5 | MET on original, MISSED on harder |
| 3. Gate stops out-of-corpus questions (original / campus) | 4 of 5 | 5/5 / 2/5 | 5/5 / 2/5 | 5/5 / 2/5 | MET on original, MISSED on campus |
| 4. 4 of 5 sampled chunks complete, none under 100 chars | 4 of 5, floor 100 | 5/5, shortest 111 | same | same | MET |
| 5. Best source contains expected phrase (original / harder) | 5 of 5 | 5/5 / 3/5 | 5/5 / 3/5 | 5/5 / 3/5 | MET on original, MISSED on harder |

Retrieval and the gate are deterministic, so only the generated answers could
vary between runs. They did not vary on pass/fail.

Real output (file `results/run_2026-09-20_2056_before-harder-scored.md`, produced
by `run_eval.py::main` calling `generate.py::answer_from_chunks`):

```
Are the washers in the transfer-friendly dorm expensive? — run 1
I do not have enough information to answer this question.
```
```
What's the last day I can quit a class without it showing up on my transcript? — run 1
You can add or drop a course through the end of the second week; however, a drop after week two shows as a W on your transcript. ... the end of the second week.
Source: admin_add_drop_deadline.txt
```
Gate on `OUT_OF_SCOPE_CAMPUS` (`run_eval.py::check_out_of_scope`): LET THROUGH
parking permit cost 0.554, tuition 0.559, scholarship GPA 0.582; refused
president 0.788, airport bus fares 0.714.

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Answer in retrieved chunks | MET | Phrase was in the top 5 for 5/5 on both sets. Weak measurement: the phrase "$1.75" appears in several laundry documents, so it cannot show the intended document was found. |
| 2 | Every answer names a source | MISSED (harder set) | 12 of 15 harder-set answers named a source. The 3 that did not were honest refusals on the washers question. Whether a refusal should count is a wording gap in the criterion; I read "every answer" strictly. |
| 3 | Gate refuses uncovered questions | MISSED (campus set) | 5/5 on far-away questions, 2/5 on campus-flavoured ones. Target of 4/5 did not hold. |
| 4 | Chunk quality | MET | Shortest chunk 111 characters. In a random sample of five chunks I judged all five complete. |
| 5 | Top source has the phrase | MISSED (harder set) | 3/5 on the harder set. The two vague questions put an unrelated document first (answer at rank 3). |

One scorer false negative: "last day I can quit a class without it showing on my
transcript" was marked failed (3 runs) although the answer was right ("end of the
second week"). My `expects` phrase ("week six") was wrong for that question.

## Diagnoses

- **Criterion 3 (retrieval/gate).** The gate compares only the best chunk's
  distance. Parking cost, tuition and scholarship GPA sit near existing documents
  (parking permits, pass/fail, graduation requirements), so their best distances
  (0.55-0.58) fall under the 0.6 cutoff. In-corpus paraphrases land at 0.43-0.48,
  so the two groups overlap and no single cutoff separates them cleanly.
- **Criterion 5 (retrieval).** Vague questions ("What deadlines should I know
  about?") have no distinctive terms, so embeddings match topically unrelated
  documents first. The answer chunk was at rank 3.
- **Criterion 2 / washers question (retrieval, then generation).** Before the fix,
  `housing_innisfree_hall_laundry.txt` was not in the top 5 at all. The question
  never says "Innisfree", and the only document linking "transfer" to Innisfree is
  `housing_innisfree_hall.txt`. The model refused, correctly, on thin material.
- **Pattern:** the misses are questions that do not share words with their source,
  and the one embedding model plus a distance-only gate cannot tell "close topic"
  from "has the answer".

## The Improvement

**What I changed:** In `chunker.py::split_documents`, every chunk after the first
now starts with its document's title line (chunk 0 already has it). Nothing else.
Index rebuilt: still 100 chunks, average 292 characters, longest 409.

**Why I picked it:** The sample chunk from `course_engl_205.txt#1` had lost its
"ENGL 205" heading, and the washers miss involved a laundry document that
retrieval did not surface. I predicted it would help the ENGL 205 fragment but
probably not the washers question.

### Run Log — After

Files: `results/run_2026-09-21_2137_after-title-original.md`,
`results/run_2026-09-21_2139_after-title-harder.md`.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunks contain the answer (original / harder) | 4 of 5 | 5/5 / 5/5 | 5/5 / 5/5 | 5/5 / 5/5 | MET |
| 2. Every answer names a source (original / harder) | 5 of 5 | 5/5 / 4/5 | 5/5 / 4/5 | 5/5 / 4/5 | MET on original, MISSED on harder |
| 3. Gate stops out-of-corpus questions (original / campus) | 4 of 5 | 5/5 / 2/5 | 5/5 / 2/5 | 5/5 / 2/5 | MET on original, MISSED on campus |
| 4. Chunk quality | 4 of 5, floor 100 | shortest 123 (sample not re-read) | same | same | floor met; sample not re-checked; 409-char longest chunk exceeds the 400 cap |
| 5. Best source contains expected phrase (original / harder) | 5 of 5 | 5/5 / 3/5 | 5/5 / 3/5 | 5/5 / 3/5 | MET on original, MISSED on harder |

| Measure | Before | After |
|---|---|---|
| Innisfree laundry best distance | 0.216 | 0.171 |
| "What deadlines should I know about?" best distance | 0.516 | 0.597 |
| Washers paraphrase best distance | 0.358 | 0.440 |
| Innisfree laundry document in top 5 for washers question | no | yes |

**Did it help?** Not on any criterion: every pass count is identical before and
after. It helped retrieval in two small ways (the intended laundry document now
appears for the washers question, and the ENGL 205 chunk keeps its title) but did
not change an outcome, because the model still refuses the washers question: no
chunk connects "transfer-friendly" to Innisfree. It also made things slightly
worse in a way that matters: repeating titles pulled the "deadlines" distance to
0.597, just under the 0.6 cutoff, so a small rephrasing would now be refused.

## What's Still Broken

- **Criterion 3:** the gate still lets through three uncovered campus questions.
  Next step would be a gate that does not rely on one distance, for example
  requiring the top two chunks to be close, or a lower cutoff tuned on both
  groups. I stopped because a lower cutoff (about 0.40) would also refuse valid
  paraphrases at 0.43-0.48, and I did not have time to measure that trade-off.
- **Criterion 5:** vague questions still rank an unrelated document first.
  Hybrid search (BM25 plus embeddings) is the next thing I would try.
- **Criterion 2:** unresolved wording problem about refusals (see Verdicts).
- **Washers question:** still refused. Out of scope for a one-change unit.

## What I'd Do Differently

- Criterion 3: test with campus-flavoured uncovered questions from the start;
  the far-away set could not fail.
- Criteria 1 and 5: score by source document, not by phrase, because phrases like
  "$1.75" appear in several documents.
- Criterion 2: say explicitly whether a refusal counts as an answer.
- Write the `expects` phrase after checking what the question actually asks.


---

# Capstone



**What This Extends**

The Unofficial Guide (this repository, the `campus_life` corpus): the retrieval
pipeline, relevance gate and grounded answers from units 1 and 2. New: an HTTP
service with structured request logging and a measured cost per run.

**The Shape**

**A: Deploy and instrument.** I am adding the operational layer only: `serve.py`
as the run path, a structured log of every request (including failures and bad
input), and a measured cost. **Out of scope:** no hosting (Path B instead), no
change to chunking, retrieval or the gate, no new features or interface.

**Running It**

**Path B: local with logs.** One command (`python serve.py`) after the setup in
`RUNNING.md` ("Capstone run path"). I did not try hosting it. Path B is chosen
because this is the heaviest of my projects: the embedding model runs locally
(about 80 MB downloaded, 168 MB in the Chroma cache on my machine), the
installed packages take about 427 MB, and the free host tier has only 512 MB of
memory. The index (`chroma_db/`, 5.3 MB) is also not committed, so a host would
have to rebuild it, and a free instance wipes its disk when it sleeps, which
would delete `logs/requests.jsonl`.

**Instrumentation**

`serve.py::log_request` appends one JSON line per `/ask` request to
`logs/requests.jsonl`. Fields: `timestamp`, `input`, `output`, `status`,
`duration_ms`, and for answered requests `refused`, `best_distance`, `sources`,
`tokens_in`, `tokens_out`; `error` is set on bad input (400) and failures (500).
Extract (10 answered requests from `measure_cost.py`, then 3 bad-input requests
and 1 forced error, all unedited):

```json
{"timestamp": "2026-11-11T02:45:06.241+00:00", "input": "Is the housing lottery random, and how are students prioritized?", "output": "The housing lottery is not entirely random: rising sophomores get a number drawn at random, but juniors and seniors are ordered by accumulated credit hours first, with ties broken randomly. \n\nSource: `admin_housing_lottery.txt`", "status": 200, "duration_ms": 2871, "refused": false, "best_distance": 0.1708, "sources": ["admin_housing_lottery.txt", "advising_registration.txt", "dining_the_atrium_followup.txt", "housing_innisfree_hall.txt", "housing_tamsin_court.txt"], "tokens_in": 586, "tokens_out": 49, "error": null}
{"timestamp": "2026-11-11T02:45:13.895+00:00", "input": "When can students add or drop a course, and what happens after week two?", "output": "Students can add a course through the end of the second week, and dropping is allowed through the end of week six. A drop that occurs after week two will show as a W on your transcript. This information comes from admin_add_drop_deadline.txt.", "status": 200, "duration_ms": 7652, "refused": false, "best_distance": 0.2635, "sources": ["admin_add_drop_deadline.txt", "admin_grade_appeals.txt", "admin_pass_fail_option.txt", "advising_registration.txt", "course_cs_340.txt"], "tokens_in": 515, "tokens_out": 54, "error": null}
{"timestamp": "2026-11-11T02:45:14.769+00:00", "input": "How much time should I expect to spend on CS 210 outside class?", "output": "You should expect to spend 8 to 10 hours a week outside of class on CS 210. \n\nSources: `course_cs_210.txt` and `course_cs_210_workload.txt`", "status": 200, "duration_ms": 874, "refused": false, "best_distance": 0.2499, "sources": ["course_cs_210.txt", "course_cs_210_workload.txt", "course_cs_340.txt", "course_stat_150.txt", "course_stat_150_workload.txt"], "tokens_in": 509, "tokens_out": 54, "error": null}
{"timestamp": "2026-11-11T02:45:17.312+00:00", "input": "How long are the peak waits at Pellew Dining Hall?", "output": "At Pellew Dining Hall, the peak wait times are 12 to 18 minutes. \n\nSource: `dining_pellew_dining_hall.txt` (also mentioned in `dining_pellew_dining_hall_followup.txt`).", "status": 200, "duration_ms": 2541, "refused": false, "best_distance": 0.1806, "sources": ["dining_halden_hall.txt", "dining_halden_hall_followup.txt", "dining_pellew_dining_hall.txt", "dining_pellew_dining_hall_followup.txt", "dining_the_ridgeway_cafe_followup.txt"], "tokens_in": 703, "tokens_out": 57, "error": null}
{"timestamp": "2026-11-11T02:45:22.599+00:00", "input": "What does laundry cost at Innisfree Hall?", "output": "Laundry at Innisfree Hall costs $1.75 to wash and $1.75 to dry, and it is app-based. \n\nSources: `housing_innisfree_hall.txt` and `housing_innisfree_hall_laundry.txt`", "status": 200, "duration_ms": 5286, "refused": false, "best_distance": 0.1712, "sources": ["housing_aldridge_hall_laundry.txt", "housing_calder_annexe.txt", "housing_innisfree_hall.txt", "housing_innisfree_hall_laundry.txt", "housing_old_brewhouse.txt"], "tokens_in": 571, "tokens_out": 60, "error": null}
{"timestamp": "2026-11-11T02:45:24.352+00:00", "input": "What deadlines should I know about?", "output": "Based on the provided documents, you should know about the following deadlines and windows:\n* You can add a course through the end of the second week, and you can drop a course through the end of week six (though drops after week two result in a \"W\" on your transcript) (*admin_add_drop_deadline.txt*).\n* You declare your major at the end of your second semester, or later if needed (*admin_declaring_a_major.txt*).", "status": 200, "duration_ms": 1752, "refused": false, "best_distance": 0.5973, "sources": ["admin_add_drop_deadline.txt", "admin_declaring_a_major.txt", "advising_registration.txt", "course_cs_340.txt", "course_cs_340_workload.txt"], "tokens_in": 496, "tokens_out": 102, "error": null}
{"timestamp": "2026-11-11T02:45:27.320+00:00", "input": "How do I avoid the long lines when eating on campus?", "output": "To avoid long lines at North Kitchen, The Ridgeway Café, and Pellew Dining Hall between classes, you should go before 11:45. \n\nSource documents: \n- `dining_north_kitchen_followup.txt`\n- `dining_the_ridgeway_cafe_followup.txt`\n- `dining_pellew_dining_hall_followup.txt`", "status": 200, "duration_ms": 2967, "refused": false, "best_distance": 0.533, "sources": ["dining_north_kitchen_followup.txt", "dining_pellew_dining_hall_followup.txt", "dining_the_ridgeway_cafe_followup.txt", "dining_verrill_street_grill.txt"], "tokens_in": 678, "tokens_out": 89, "error": null}
{"timestamp": "2026-11-11T02:45:32.334+00:00", "input": "Do seniors who took summer classes get better dorm picks?", "output": "Yes, juniors and seniors in the housing lottery are ordered by accumulated credit hours first, which means a senior who took summer courses reliably beats a senior who didn't (admin_housing_lottery.txt).", "status": 200, "duration_ms": 5013, "refused": false, "best_distance": 0.4784, "sources": ["admin_housing_lottery.txt", "admin_pass_fail_option.txt", "housing_aldridge_hall.txt", "housing_old_brewhouse.txt", "orientation_what_matters.txt"], "tokens_in": 606, "tokens_out": 43, "error": null}
{"timestamp": "2026-11-11T02:45:40.486+00:00", "input": "What's the last day I can quit a class without it showing up on my transcript?", "output": "The last day you can drop a class without it showing up on your transcript is the end of the second week, because a drop after week two shows as a W on your transcript. This comes from *admin_add_drop_deadline.txt*.", "status": 200, "duration_ms": 8150, "refused": false, "best_distance": 0.431, "sources": ["admin_add_drop_deadline.txt", "admin_pass_fail_option.txt", "admin_transcript_requests.txt", "admin_withdrawal_deadline.txt", "course_stat_150.txt"], "tokens_in": 522, "tokens_out": 51, "error": null}
{"timestamp": "2026-11-11T02:45:50.165+00:00", "input": "Are the washers in the transfer-friendly dorm expensive?", "output": "I do not have enough information to answer your question, as the provided documents do not mention a \"transfer-friendly dorm.\"", "status": 200, "duration_ms": 9678, "refused": false, "best_distance": 0.44, "sources": ["housing_calder_annexe.txt", "housing_fenwick_court.txt", "housing_innisfree_hall_laundry.txt", "housing_old_brewhouse.txt", "housing_old_brewhouse_laundry.txt"], "tokens_in": 574, "tokens_out": 25, "error": null}
{"timestamp": "2026-11-11T02:45:50.571+00:00", "input": "   ", "output": "Send JSON with a question in it, like {\"question\": \"is the housing lottery random?\"}", "status": 400, "duration_ms": 0, "error": "bad_input"}
{"timestamp": "2026-11-11T02:45:50.571+00:00", "input": null, "output": "Send JSON with a question in it, like {\"question\": \"is the housing lottery random?\"}", "status": 400, "duration_ms": 0, "error": "bad_input"}
{"timestamp": "2026-11-11T02:45:50.571+00:00", "input": 123, "output": "Send JSON with a question in it, like {\"question\": \"is the housing lottery random?\"}", "status": 400, "duration_ms": 0, "error": "bad_input"}
{"timestamp": "2026-11-11T02:45:51.018+00:00", "input": "is the housing lottery random?", "output": "RuntimeError: No index called 'does_not_exist__default'. Run `python app.py index` first.", "status": 500, "duration_ms": 446, "error": "RuntimeError"}
```

**What It Costs**

Measured with `measure_cost.py` (10 questions through `/ask`, response cache
off, free-tier Gemini model `gemini-3.5-flash-lite`): mean **4.68 seconds**
per run (range 0.87-9.68 s) and **634 tokens** per run (576 in,
58 out). No dollar figure was measured: this key is on the free tier.

For 100 people a day, assuming 5 questions each (my assumption, not measured):
100 x 5 = 500 runs x 634 tokens = about 317k tokens
and 500 x 4.68 s = about 39 minutes of compute per day.


**Run Log and Verdicts**


**Run Log — Before**

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Every request leaves a log record | 20 of 20 | 20/20 | 20/20 | 20/20 | MET |
| 2. Every record has the required fields | at least 19 of 20 | 20/20 | 20/20 | 20/20 | MET |
| 3. Warm requests within 8 s | at least 8 of 10 | 8/10 | 8/10 | 8/10 | MET (no margin) |
| 4. Starts from `RUNNING.md` without undocumented steps | 0 undocumented steps | 3 found | 3 found (same) | 3 found (same) | MISSED |
| 5. Model failures return a readable error without internal details | at least 4 of 5 | 0/5 | 0/5 | 0/5 | MISSED |

Real output (all from `capstone_eval.py`, `serve.py::ask` and `serve.py::log_request`):

Criterion 1 and 2 — the 20 requests were 10 valid questions, 5 out-of-scope
questions refused by the gate, and 5 bad inputs (empty, whitespace, non-JSON,
a number, a list). Status codes in trial 1: fifteen 200s and five 400s; 20
new lines in `logs/requests.jsonl`. One log line from the clean-checkout test:

```
{"timestamp": "2026-11-11T03:22:10.963+00:00", "input": "", "output": "Send JSON with a question in it, like {\"question\": \"is the housing lottery random?\"}", "status": 400, "duration_ms": 0, "error": "bad_input"}
```

Criterion 3 — seconds and status for the 10 warm requests, trial 1:
`(0.49, 500) (5.91, 200) (6.49, 200) (6.54, 200) (6.52, 200) (1.06, 200) (5.15, 200) (2.5, 200) (6.29, 200) (19.86, 200)`.
Trial 3 had no errors: `5.03 6.88 4.19 11.36 6.44 7.2 3.45 5.32 4.95 9.84`.

Criterion 4 — from a fresh clone in `~/fresh-check`, repeated three times with the same result:
`Found 3.15.1. The pinned packages do not support 3.14 yet`,
`cp: .env: Not a directory`, and `Address already in use` on port 5000, then
another app (a GPT-2 detector) answering on 5001.

Criterion 5 — simulated 429 and 503 failures (`capstone_eval.py::trial_failures`):

```
HTTP 500
{"error": "RuntimeError: Still rate limited after 4 attempts. Wait a minute and try again - your key is fine.\nLast error: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota', 'status': 'RESOURCE_EXHAUSTED'}}"}
```

**Verdicts**

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Every request is logged | MET | 20 of 20 in all three trials, including the 400s. Real Gemini 503 errors during the trials were logged too. |
| 2 | Required fields present | MET | All five keys present in 20 of 20 records each trial. One record per trial (a non-JSON body) has `input: null`; counting a null as missing gives 19 of 20, which still meets the target. |
| 3 | Latency | MET, narrowly | 8 of 10 in every trial, exactly the target. Trials 1 and 2 each lost one request to a real Gemini 503, and each had a ~19 s request that is partly my harness's 10-requests-per-minute pacing. Trial 3 had no errors and its two slow requests (11.4 s, 9.8 s) were real. The target held, but with no margin. |
| 4 | Startup from `RUNNING.md` | MISSED | Three undocumented steps were needed, and the same three came up in all three fresh checkouts. |
| 5 | Failure messages | MISSED | 0 of 5 in all three trials (15 of 15 were HTTP 500 with the exception class and the API's JSON in the body). |

**Diagnoses**

- **Criterion 5 — generation stage, surfaced by `serve.py`.** `generate.py::generate`
  retries a 429 four times and then raises `RuntimeError`, and re-raises a 503
  immediately. `serve.py::ask` catches every exception and returns
  `f"{type(exc).__name__}: {exc}"` with status 500, so the class name, the quota
  text and the API's JSON reach the caller. The log recorded all 15 failures
  correctly, so the instrumentation worked and only the response was wrong.
- **Criterion 4 — the run path, not the code.** One root cause: `RUNNING.md`
  assumed this machine's defaults. (1) `python3` is 3.15 here and the pinned
  packages need 3.13, with no instruction on how to get it; (2) an inline `#`
  comment after `cp .env.example .env` is passed to `cp` as arguments by
  interactive zsh; (3) port 5000 is held by macOS AirPlay Receiver and port 5001
  was also shared with another local app, so `localhost:5001` answered with the
  wrong program.
- **Criterion 3 — near miss.** Latency comes from the model call (about 3-8 s on
  the free tier) plus the starter's rate-limit waits; the fast 0.5-1 s requests
  were errors or cache-free refusals. The target was met only because most
  requests landed between 4 and 7 seconds.

**The Improvement**

**What I changed:** In `serve.py::ask`, rate-limit and model-unavailable errors
(429 and 503) now return HTTP 503 with the message "The model is busy right now.
Please try again in a minute." The full error stays in `logs/requests.jsonl`
(`error: "model_unavailable"`). Helper: `serve.py::is_model_busy`. Nothing else
was changed.

**Why I picked it:** It follows directly from the criterion 5 diagnosis: the
leak happens in the one `except` block in `serve.py::ask`. I chose it over fixing
`RUNNING.md` (criterion 4) because the failure was a behaviour gap I could
measure before and after.

**Prediction written before the "after" trials:** criterion 5 goes from 0/5 to
5/5; criteria 1 to 3 do not change. The risk is that `is_model_busy` matches
substrings such as "503" and "unavailable", so it could also catch an unrelated
error.

**Run Log — After**

File `results/capstone_2026-11-08_2234_after.md`, same script and settings.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Every request leaves a log record | 20 of 20 | 20/20 | 20/20 | 20/20 | MET |
| 2. Every record has the required fields | at least 19 of 20 | 20/20 | 20/20 | 20/20 | MET |
| 3. Warm requests within 8 s | at least 8 of 10 | 8/10 | 9/10 | 9/10 | MET |
| 4. Starts from `RUNNING.md` without undocumented steps | 0 undocumented steps | unchanged (not the improvement) | | | MISSED (unchanged) |
| 5. Model failures return a readable error without internal details | at least 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

Real output after the change (`serve.py::ask`, simulated 503):

```
HTTP 503
{"error": "The model is busy right now. Please try again in a minute."}
```

All 15 simulated failures were logged with their full detail (`logged: true`,
`error: "model_unavailable"`), so the information was kept in the log and removed
from the response.

**Did it help?** Yes, on the criterion it targeted: criterion 5 went from 0 of 5
to 5 of 5 in every trial, and no internal text appeared in any response. Criteria
1 and 2 did not change, as predicted, and criterion 3 looks slightly better
(8, 9, 9 against 8, 8, 8), but I put that down to the model's variable speed and
a real 503 landing in the "before" trials, not to the change. My prediction held;
the risk I named (`is_model_busy` matching too broadly) was not tested, because I
only injected genuine 429 and 503 errors, so I cannot say whether an unrelated
error containing "503" or "unavailable" would be misclassified. Each after-trial
also had one ~30 s request that comes from my harness's own 10-requests-per-minute
pacing, not from the system.

**What's Still Broken**

- **Criterion 4 (MISSED).** The three problems are not fixed. I would put the
  `python3.13` install check first, move the `cp` comment onto its own line, and
  use an uncommon default port such as 8765, then repeat the fresh checkout
  three times. I stopped because the unit allows one improvement and I spent it
  on criterion 5.
- **Criterion 3 (MET with no margin).** If the model gets slower, the target
  will fail. The next step would be a timeout and a clearer split between
  model time and rate-limit waiting, so latency numbers are not inflated by the
  starter's pacing.
- **Failure handling beyond 429 and 503.** A missing API key, a very long
  question, and a failing log write are untested. The log write fails silently
  by design (`log_request` swallows `OSError`), so a full disk would lose
  records and criterion 1 would fail without any sign of it.
- **Token counts in the log** come from process-wide counters, so they are only
  exact when requests arrive one at a time.
- **Not hosted.** Path B only; the free tier's 512 MB of memory is too small for
  the local embedding model.

**What I would do first with another unit:** repair `RUNNING.md` and re-run the
clean-checkout test three times, because a system nobody else can start is the
most limiting problem.

**What I'd Do Differently**

- Criterion 4 needs a number. "No undocumented steps" cannot be scored the same
  way by two people; "start with at most N commands and 0 edits beyond the doc"
  can.
- Criterion 2 should name the five fields and say whether a null counts as
  present. I had to decide that after seeing the results.
- Criterion 3 should say what counts as warm and whether an error counts
  against the 8-second target, and should be measured without the harness's own
  rate-limit pacing.
- Criterion 5 should define "readable" and "internal details", for example no
  exception class name, no raw API text, an HTTP 503.
