# Run log — before-harder

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-11-10 20:40

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| What deadlines should I know about? |   |   |   |
| How do I avoid the long lines when eating on campus? |   |   |   |
| Do seniors who took summer classes get better dorm picks? |   |   |   |
| What's the last day I can quit a class without it showing up on my transcript? |   |   |   |
| Are the washers in the transfer-friendly dorm expensive? |   |   |   |

> The Run columns are blank because `scorer.py` doesn't exist yet.
> Judge each question yourself by reading the output below, or build
> the scorer first and re-run.

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
Based on the provided documents, you should know about the following deadlines and windows:
* You can add a course through the end of the second week, and you can drop a course through the end of the sixth week (though drops after week two show as a "W" on your transcript) (*admin_add_drop_deadline.txt*). 
* You need to book an appointment with your adviser two weeks before registration opens since advisers get busy (*advising_registration.txt*).
* Popular courses fill up in the first two days of registration (*advising_registration.txt*).
```

### What deadlines should I know about? — run 2

- Best distance: 0.5157 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, advising_registration.txt, course_cs_340.txt, course_cs_340_workload.txt

```
Based on the provided documents, you should know about the following deadlines and windows:
* You can add a course through the end of the second week, and you can drop a course through the end of week six (though drops after week two result in a "W" on your transcript) (*admin_add_drop_deadline.txt*).
* You must book an adviser two weeks out before registration opens to have your adviser hold lifted (*advising_registration.txt*).
* Popular courses fill up in the first two days of registration (*advising_registration.txt*).
```

### What deadlines should I know about? — run 3

- Best distance: 0.5157 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, advising_registration.txt, course_cs_340.txt, course_cs_340_workload.txt

```
Based on the provided documents, you should know the following deadlines:
* **Add/Drop Deadlines:** You can add a course through the end of the second week, and you can drop a course through the end of the sixth week (though drops after week two result in a "W" on your transcript). (*admin_add_drop_deadline.txt*)
* **Declaring a Major:** You declare at the end of your second semester, or later if you need to. (*admin_declaring_a_major.txt*)
```

### How do I avoid the long lines when eating on campus? — run 1

- Best distance: 0.5330 (passed the gate)
- Sources retrieved: dining_north_kitchen_followup.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt

```
To avoid long lines, you should go before 11:45 when trying to eat between classes at North Kitchen, The Ridgeway Café, and Pellew Dining Hall. 

Sources: 
- `dining_north_kitchen_followup.txt`
- `dining_the_ridgeway_cafe_followup.txt`
- `dining_pellew_dining_hall_followup.txt`
```

### How do I avoid the long lines when eating on campus? — run 2

- Best distance: 0.5330 (passed the gate)
- Sources retrieved: dining_north_kitchen_followup.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt

```
To avoid long lines between classes, you should go before 11:45 at North Kitchen (`dining_north_kitchen_followup.txt`), The Ridgeway Café (`dining_the_ridgeway_cafe_followup.txt`), and Pellew Dining Hall (`dining_pellew_dining_hall_followup.txt`).
```

### How do I avoid the long lines when eating on campus? — run 3

- Best distance: 0.5330 (passed the gate)
- Sources retrieved: dining_north_kitchen_followup.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt

```
To avoid long lines at North Kitchen, The Ridgeway Café, and Pellew Dining Hall between classes, you should go before 11:45. 
(Source: dining_north_kitchen_followup.txt, dining_the_ridgeway_cafe_followup.txt, and dining_pellew_dining_hall_followup.txt)
```

### Do seniors who took summer classes get better dorm picks? — run 1

- Best distance: 0.4784 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, dining_verrill_street_grill.txt, housing_aldridge_hall.txt, housing_old_brewhouse.txt, orientation_what_matters.txt

```
Yes, juniors and seniors are ordered by accumulated credit hours first in the housing lottery, meaning a senior who took summer courses reliably beats a senior who didn't. 

Source: `admin_housing_lottery.txt`
```

### Do seniors who took summer classes get better dorm picks? — run 2

- Best distance: 0.4784 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, dining_verrill_street_grill.txt, housing_aldridge_hall.txt, housing_old_brewhouse.txt, orientation_what_matters.txt

```
Yes, a senior who took summer courses beats a senior who didn't because juniors and seniors are ordered by accumulated credit hours in the housing lottery, with random tie-breaks only applied afterward. 

Source: `admin_housing_lottery.txt`
```

### Do seniors who took summer classes get better dorm picks? — run 3

- Best distance: 0.4784 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, dining_verrill_street_grill.txt, housing_aldridge_hall.txt, housing_old_brewhouse.txt, orientation_what_matters.txt

```
Yes. Juniors and seniors are ordered by accumulated credit hours first and only tie-break randomly, meaning a senior who took summer courses reliably beats a senior who didn't (admin_housing_lottery.txt).
```

### What's the last day I can quit a class without it showing up on my transcript? — run 1

- Best distance: 0.4310 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt, course_stat_150.txt

```
You can add a course and drop it through the end of the second week; a drop after week two shows as a W on your transcript, meaning the last day to drop without a W is the end of the second week. 
(Source: admin_add_drop_deadline.txt)
```

### What's the last day I can quit a class without it showing up on my transcript? — run 2

- Best distance: 0.4310 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt, course_stat_150.txt

```
You can add/drop a course through the end of the second week, but drops after week two will show as a W on your transcript. Therefore, the last day to drop a class without it showing on your transcript is the end of week two. 

Source: `admin_add_drop_deadline.txt`
```

### What's the last day I can quit a class without it showing up on my transcript? — run 3

- Best distance: 0.4310 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt, course_stat_150.txt

```
You can add a course through the end of the second week, and dropping after week two shows as a W on your transcript (admin_add_drop_deadline.txt). Therefore, the last day you can drop a class without it showing up on your transcript is the end of the second week (admin_add_drop_deadline.txt).
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
I do not have enough information to answer this question.
```

### Are the washers in the transfer-friendly dorm expensive? — run 3

- Best distance: 0.3580 (passed the gate)
- Sources retrieved: housing_calder_annexe.txt, housing_fenwick_court.txt, housing_innisfree_hall.txt, housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt

```
I don't have enough information to answer your question, as the provided documents do not mention which dorm is transfer-friendly.
```
