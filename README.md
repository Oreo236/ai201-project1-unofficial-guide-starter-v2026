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

> DRAFT written with Claude's help from the measured results. Rewrite the
> reasoning in your own words before submitting; the numbers come from the files
> named in each section.

Two question sets were used. The **original set** is the five questions from
`questions.py::QUESTIONS` plus `OUT_OF_SCOPE`. The **harder set** is
`HARDER_QUESTIONS` plus `OUT_OF_SCOPE_CAMPUS`, added after seeing the first
results (so it is a stress test, not a blind test). `scorer.py::judge` marks an
answer correct when it contains the `expects` phrase. All runs: top-k 5, cutoff
0.6, caching off, three runs, `run_eval.py::main`. Free-tier pacing was lowered to
10 requests/min from the command line; `config.py` was not changed.

## Run Log — Before

Files: `results/run_2026-11-10_2054_before-scored.md` (original set),
`results/run_2026-11-10_2056_before-harder-scored.md` (harder set).

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunks contain the answer (original / harder) | 4 of 5 | 5/5 / 5/5 | 5/5 / 5/5 | 5/5 / 5/5 | MET |
| 2. Every answer names a source (original / harder) | 5 of 5 | 5/5 / 4/5 | 5/5 / 4/5 | 5/5 / 4/5 | MET on original, MISSED on harder |
| 3. Gate stops out-of-corpus questions (original / campus) | 4 of 5 | 5/5 / 2/5 | 5/5 / 2/5 | 5/5 / 2/5 | MET on original, MISSED on campus |
| 4. 4 of 5 sampled chunks complete, none under 100 chars | 4 of 5, floor 100 | 5/5, shortest 111 | same | same | MET |
| 5. Best source contains expected phrase (original / harder) | 5 of 5 | 5/5 / 3/5 | 5/5 / 3/5 | 5/5 / 3/5 | MET on original, MISSED on harder |

Retrieval and the gate are deterministic, so only the generated answers could
vary between runs. They did not vary on pass/fail.

Real output (file `results/run_2026-11-10_2056_before-harder-scored.md`, produced
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

Files: `results/run_2026-11-10_2137_after-title-original.md`,
`results/run_2026-11-10_2139_after-title-harder.md`.

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
