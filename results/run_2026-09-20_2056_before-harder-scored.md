# Run log — before-harder-scored

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-11-10 20:56

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| What deadlines should I know about? | pass | pass | pass |
| How do I avoid the long lines when eating on campus? | pass | pass | pass |
| Do seniors who took summer classes get better dorm picks? | pass | pass | pass |
| What's the last day I can quit a class without it showing up on my transcript? | fail | fail | fail |
| Are the washers in the transfer-friendly dorm expensive? | fail | fail | fail |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 2 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| How much does a parking permit cost? | 0.554 | **let through** |
| What is the tuition for the CS major? | 0.559 | **let through** |
| What is the minimum GPA to keep a merit scholarship? | 0.582 | **let through** |
| Who is the president of the university? | 0.788 | refused |
| What are the bus fares to the airport? | 0.714 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### What deadlines should I know about? — run 1

- Best distance: 0.5157 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, advising_registration.txt, course_cs_340.txt, course_cs_340_workload.txt

```
Based on the provided documents, you should know about the following deadlines and timeframes:

* **Add/Drop Deadline:** You can add a course through the end of the second week. You can drop a course through the end of week six, though drops after week two will show as a "W" on your transcript. (*admin_add_drop_deadline.txt*)
* **Registration:** Popular courses fill in the first two days, and you should book your adviser appointment two weeks out because they get busy the week before registration opens. (*advising_registration.txt*)
* **Declaring a Major:** You declare at the end of your second semester, or later if needed, with no penalty for declaring late. (*admin_declaring_a_major.txt*)
```

### What deadlines should I know about? — run 2

- Best distance: 0.5157 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, advising_registration.txt, course_cs_340.txt, course_cs_340_workload.txt

```
Based on the provided documents, you should know about the following deadlines and windows:
* You can add a course through the end of the second week, and drop a course through the end of week six (drops after week two show as a W on your transcript) (*admin_add_drop_deadline.txt*).
* Popular courses fill in the first two days of registration, and you should book your adviser meeting two weeks out before registration opens (*advising_registration.txt*).
```

### What deadlines should I know about? — run 3

- Best distance: 0.5157 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, advising_registration.txt, course_cs_340.txt, course_cs_340_workload.txt

```
Based on the provided documents, you should know about the following deadlines and windows:
* You can add a course through the end of the second week, and you can drop a course through the end of week six (though drops after week two result in a "W" on your transcript) (*admin_add_drop_deadline.txt*).
* Popular courses fill in the first two days of registration, and you should book your adviser meeting two weeks before registration opens to get your hold lifted (*advising_registration.txt*).
```

### How do I avoid the long lines when eating on campus? — run 1

- Best distance: 0.5330 (passed the gate)
- Sources retrieved: dining_north_kitchen_followup.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt

```
To avoid long lines, you should go before 11:45 when trying to eat between classes at North Kitchen, The Ridgeway Café, and Pellew Dining Hall. 

Sources: `dining_north_kitchen_followup.txt`, `dining_the_ridgeway_cafe_followup.txt`, and `dining_pellew_dining_hall_followup.txt`.
```

### How do I avoid the long lines when eating on campus? — run 2

- Best distance: 0.5330 (passed the gate)
- Sources retrieved: dining_north_kitchen_followup.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt

```
To avoid long lines at North Kitchen, The Ridgeway Café, and Pellew Dining Hall between classes, you should go before 11:45. 

Files used:
- dining_north_kitchen_followup.txt
- dining_the_ridgeway_cafe_followup.txt
- dining_pellew_dining_hall_followup.txt
```

### How do I avoid the long lines when eating on campus? — run 3

- Best distance: 0.5330 (passed the gate)
- Sources retrieved: dining_north_kitchen_followup.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt

```
To avoid long lines, you can go to North Kitchen, The Ridgeway Café, or Pellew Dining Hall before 11:45 if you are trying to eat between classes (source files: `dining_north_kitchen_followup.txt`, `dining_the_ridgeway_cafe_followup.txt`, and `dining_pellew_dining_hall_followup.txt`).
```

### Do seniors who took summer classes get better dorm picks? — run 1

- Best distance: 0.4784 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, dining_verrill_street_grill.txt, housing_aldridge_hall.txt, housing_old_brewhouse.txt, orientation_what_matters.txt

```
Yes, a senior who took summer courses reliably beats a senior who didn't because juniors and seniors are ordered by accumulated credit hours first in the housing lottery. 

Source: admin_housing_lottery.txt
```

### Do seniors who took summer classes get better dorm picks? — run 2

- Best distance: 0.4784 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, dining_verrill_street_grill.txt, housing_aldridge_hall.txt, housing_old_brewhouse.txt, orientation_what_matters.txt

```
Yes, a senior who took summer courses reliably beats a senior who didn't because juniors and seniors are ordered by accumulated credit hours first, with random tie-breaks used only for ties. This information comes from `admin_housing_lottery.txt`.
```

### Do seniors who took summer classes get better dorm picks? — run 3

- Best distance: 0.4784 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, dining_verrill_street_grill.txt, housing_aldridge_hall.txt, housing_old_brewhouse.txt, orientation_what_matters.txt

```
Yes, seniors are ordered by accumulated credit hours with random tie-breaking, meaning a senior who took summer courses reliably beats a senior who didn't (admin_housing_lottery.txt).
```

### What's the last day I can quit a class without it showing up on my transcript? — run 1

- Best distance: 0.4310 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt, course_stat_150.txt

```
You can add or drop a course through the end of the second week; however, a drop after week two shows as a W on your transcript. Therefore, the last day you can drop a class without it showing up on your transcript is the end of the second week.

Source: admin_add_drop_deadline.txt
```

### What's the last day I can quit a class without it showing up on my transcript? — run 2

- Best distance: 0.4310 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt, course_stat_150.txt

```
You can drop a course through the end of the second week without a W showing on your transcript (admin_add_drop_deadline.txt).
```

### What's the last day I can quit a class without it showing up on my transcript? — run 3

- Best distance: 0.4310 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt, course_stat_150.txt

```
You can add or drop a course through the end of the second week; however, a drop after week two shows as a W on your transcript. Therefore, the last day to drop without it showing up on your transcript is the end of the second week. 

Source: admin_add_drop_deadline.txt
```

### Are the washers in the transfer-friendly dorm expensive? — run 1

- Best distance: 0.3580 (passed the gate)
- Sources retrieved: housing_calder_annexe.txt, housing_fenwick_court.txt, housing_innisfree_hall.txt, housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt

```
I do not have enough information to answer this question.
```

### Are the washers in the transfer-friendly dorm expensive? — run 2

- Best distance: 0.3580 (passed the gate)
- Sources retrieved: housing_calder_annexe.txt, housing_fenwick_court.txt, housing_innisfree_hall.txt, housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt

```
I don't have enough information to answer your question, as the provided documents do not mention which dorm is transfer-friendly.
```

### Are the washers in the transfer-friendly dorm expensive? — run 3

- Best distance: 0.3580 (passed the gate)
- Sources retrieved: housing_calder_annexe.txt, housing_fenwick_court.txt, housing_innisfree_hall.txt, housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt

```
I do not have enough information to answer this question.
```
