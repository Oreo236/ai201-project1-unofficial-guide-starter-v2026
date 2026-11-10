# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
The five questions cover administrative rules, a course workload, dining, and
housing. Four of them have a single focused source, while the housing lottery
question contains several details, so 4 of 5 leaves room for one difficult
retrieval without making the target trivial.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
The pipeline keeps the source filename in every retrieved chunk and the command
line adds retrieved sources to the final outcome. Because the corpus is local
and every test question is based on one of its documents, all five should have
an attributable source unless generation or attribution code fails.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
The questions in `OUT_OF_SCOPE` are about unrelated facts and technologies, so
the gate should reject nearly all of them. I chose 4 of 5 because one unrelated
question could still produce an accidental semantic match in a small corpus.

---

## 4. Something about your chunks

At least 4 of 5 sampled chunks should read as a complete thought, and no
produced chunk should be shorter than 100 characters.



**Why this target:**
The campus-life documents are short posts averaging about 317 characters, so
most should remain intact. The 100-character floor rules out fragments while
still allowing a meaningful short paragraph to remain a separate chunk when
combining it would exceed the 400-character limit.


---

## 5. Your choice

For all 5 in-corpus questions, the best retrieved source should be a document
that contains the expected answer phrase.



**Why this target:**
Each test question was written from a specific document and includes an
`expects` phrase taken from that document. Requiring all five best sources to
match tests whether retrieval finds the right source, not merely a related
campus-life document.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
