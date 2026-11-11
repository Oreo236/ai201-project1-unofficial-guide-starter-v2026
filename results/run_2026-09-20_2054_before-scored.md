# Run log — before-scored

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-11-10 20:54

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Is the housing lottery random, and how are students prioritized? | pass | pass | pass |
| When can students add or drop a course, and what happens after week two? | pass | pass | pass |
| How much time should I expect to spend on CS 210 outside class? | pass | pass | pass |
| How long are the peak waits at Pellew Dining Hall? | pass | pass | pass |
| What does laundry cost at Innisfree Hall? | pass | pass | pass |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.891 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### Is the housing lottery random, and how are students prioritized? — run 1

- Best distance: 0.1708 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, advising_registration.txt, dining_the_atrium_followup.txt, housing_innisfree_hall.txt, housing_tamsin_court.txt

```
The housing lottery is not entirely random; rising sophomores have a number drawn at random, but juniors and seniors are ordered by accumulated credit hours first, with random tie-breaking. 

Source: admin_housing_lottery.txt
```

### Is the housing lottery random, and how are students prioritized? — run 2

- Best distance: 0.1708 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, advising_registration.txt, dining_the_atrium_followup.txt, housing_innisfree_hall.txt, housing_tamsin_court.txt

```
The housing lottery is not entirely random in the way most people assume. Rising sophomores receive a randomly drawn number, but juniors and seniors are ordered by accumulated credit hours first, with random selection used only as a tie-breaker. 

*(Source: admin_housing_lottery.txt)*
```

### Is the housing lottery random, and how are students prioritized? — run 3

- Best distance: 0.1708 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, advising_registration.txt, dining_the_atrium_followup.txt, housing_innisfree_hall.txt, housing_tamsin_court.txt

```
The housing lottery is not entirely random: rising sophomores have a number drawn at random, but juniors and seniors are ordered by accumulated credit hours first, with ties broken randomly. 

Source: admin_housing_lottery.txt
```

### When can students add or drop a course, and what happens after week two? — run 1

- Best distance: 0.2635 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, advising_registration.txt, course_cs_340.txt, course_stat_150.txt

```
Students can add a course through the end of the second week, and they can drop a course through the end of week six. A drop that occurs after week two will show as a "W" on the student's transcript. 

Source: `admin_add_drop_deadline.txt`
```

### When can students add or drop a course, and what happens after week two? — run 2

- Best distance: 0.2635 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, advising_registration.txt, course_cs_340.txt, course_stat_150.txt

```
Students can add a course through the end of the second week, and they can drop a course through the end of week six. Dropping a course after week two will show as a W on the transcript. 

Source: `admin_add_drop_deadline.txt`
```

### When can students add or drop a course, and what happens after week two? — run 3

- Best distance: 0.2635 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, advising_registration.txt, course_cs_340.txt, course_stat_150.txt

```
Students can add a course through the end of the second week, and they can drop a course through the end of week six. A drop that occurs after week two will show as a "W" on the student's transcript. 

Source: `admin_add_drop_deadline.txt`
```

### How much time should I expect to spend on CS 210 outside class? — run 1

- Best distance: 0.2499 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_workload.txt, course_cs_340.txt, course_stat_150.txt, course_stat_150_workload.txt

```
You should expect to spend 8 to 10 hours a week outside class on CS 210. 

Source: `course_cs_210_workload.txt` (also mentioned in `course_cs_210.txt`).
```

### How much time should I expect to spend on CS 210 outside class? — run 2

- Best distance: 0.2499 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_workload.txt, course_cs_340.txt, course_stat_150.txt, course_stat_150_workload.txt

```
You should expect to spend 8 to 10 hours a week outside class on CS 210. 

Source: `course_cs_210_workload.txt` (also mentioned in `course_cs_210.txt`).
```

### How much time should I expect to spend on CS 210 outside class? — run 3

- Best distance: 0.2499 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_workload.txt, course_cs_340.txt, course_stat_150.txt, course_stat_150_workload.txt

```
You should expect to spend 8 to 10 hours a week outside class on CS 210. 

Source: `course_cs_210_workload.txt` (also mentioned in `course_cs_210.txt`).
```

### How long are the peak waits at Pellew Dining Hall? — run 1

- Best distance: 0.1806 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt

```
The peak waits at Pellew Dining Hall are 12 to 18 minutes (dining_pellew_dining_hall.txt and dining_pellew_dining_hall_followup.txt).
```

### How long are the peak waits at Pellew Dining Hall? — run 2

- Best distance: 0.1806 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt

```
At Pellew Dining Hall, wait times at peak are 12 to 18 minutes. 

Source: dining_pellew_dining_hall.txt (also mentioned in dining_pellew_dining_hall_followup.txt)
```

### How long are the peak waits at Pellew Dining Hall? — run 3

- Best distance: 0.1806 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt

```
The peak wait times at Pellew Dining Hall are 12 to 18 minutes (source: dining_pellew_dining_hall.txt and dining_pellew_dining_hall_followup.txt).
```

### What does laundry cost at Innisfree Hall? — run 1

- Best distance: 0.2155 (passed the gate)
- Sources retrieved: housing_calder_annexe.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_morrow_house.txt, housing_old_brewhouse.txt

```
Laundry at Innisfree Hall costs $1.75 to wash and $1.75 to dry. 

Source: `housing_innisfree_hall_laundry.txt` (also mentioned in `housing_innisfree_hall.txt`).
```

### What does laundry cost at Innisfree Hall? — run 2

- Best distance: 0.2155 (passed the gate)
- Sources retrieved: housing_calder_annexe.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_morrow_house.txt, housing_old_brewhouse.txt

```
At Innisfree Hall, laundry costs $1.75 for a wash and $1.75 for a dry. 

Source: `housing_innisfree_hall.txt` (also mentioned in `housing_innisfree_hall_laundry.txt`)
```

### What does laundry cost at Innisfree Hall? — run 3

- Best distance: 0.2155 (passed the gate)
- Sources retrieved: housing_calder_annexe.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_morrow_house.txt, housing_old_brewhouse.txt

```
At Innisfree Hall, laundry costs $1.75 for a wash and $1.75 for a dryer (Source: housing_innisfree_hall.txt and housing_innisfree_hall_laundry.txt).
```
