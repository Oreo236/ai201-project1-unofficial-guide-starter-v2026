# Run log — after-title-harder

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-11-10 21:39

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
| What are the bus fares to the airport? | 0.747 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### What deadlines should I know about? — run 1

- Best distance: 0.5973 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, advising_registration.txt, course_cs_340.txt, course_cs_340_workload.txt

```
Based on the provided documents, you should know about the following deadlines and timeframes:

* You can add a course through the end of the second week, and dropping is available through the end of week six (though drops after week two result in a "W" on your transcript) (*admin_add_drop_deadline.txt*).
* For advising, you should book an appointment two weeks before registration opens because advisers get busy the week before (*advising_registration.txt*). 
* Popular courses fill up in the first two days of registration (*advising_registration.txt*).
```

### What deadlines should I know about? — run 2

- Best distance: 0.5973 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, advising_registration.txt, course_cs_340.txt, course_cs_340_workload.txt

```
Based on the provided documents, you should know about the following deadlines and timeframes:

* You can add a course through the end of the second week (*admin_add_drop_deadline.txt*).
* You can drop a course through the end of week six, though a drop after week two will show as a W on your transcript (*admin_add_drop_deadline.txt*).
* You should book an appointment with your adviser two weeks before registration opens because they get busy (*advising_registration.txt*).
```

### What deadlines should I know about? — run 3

- Best distance: 0.5973 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, advising_registration.txt, course_cs_340.txt, course_cs_340_workload.txt

```
Based on the provided documents, you should know the following deadlines and timeframes:

* You can add a course through the end of the second week, and you can drop a course through the end of week six (though drops after week two result in a "W" on your transcript). Source: `admin_add_drop_deadline.txt`
* You should book an appointment with your adviser two weeks before registration opens. Source: `advising_registration.txt`
* Popular courses fill up in the first two days of registration. Source: `advising_registration.txt`
* For CS 340 Databases, the term project should be started in week three. Source: `course_cs_340.txt`
```

### How do I avoid the long lines when eating on campus? — run 1

- Best distance: 0.5330 (passed the gate)
- Sources retrieved: dining_north_kitchen_followup.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt

```
To avoid long lines, you should go before 11:45 when trying to eat between classes at North Kitchen, The Ridgeway Café, and Pellew Dining Hall. 

Files used: 
- `dining_north_kitchen_followup.txt`
- `dining_the_ridgeway_cafe_followup.txt`
- `dining_pellew_dining_hall_followup.txt`
```

### How do I avoid the long lines when eating on campus? — run 2

- Best distance: 0.5330 (passed the gate)
- Sources retrieved: dining_north_kitchen_followup.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt

```
To avoid long lines between classes at North Kitchen, The Ridgeway Café, and Pellew Dining Hall, you should go before 11:45. 

Source documents: 
- `dining_north_kitchen_followup.txt`
- `dining_the_ridgeway_cafe_followup.txt`
- `dining_pellew_dining_hall_followup.txt`
```

### How do I avoid the long lines when eating on campus? — run 3

- Best distance: 0.5330 (passed the gate)
- Sources retrieved: dining_north_kitchen_followup.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt

```
To avoid long lines, you can go to North Kitchen, The Ridgeway Café, or Pellew Dining Hall before 11:45 if you are trying to eat between classes (source files: `dining_north_kitchen_followup.txt`, `dining_the_ridgeway_cafe_followup.txt`, and `dining_pellew_dining_hall_followup.txt`).
```

### Do seniors who took summer classes get better dorm picks? — run 1

- Best distance: 0.4784 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, admin_pass_fail_option.txt, housing_aldridge_hall.txt, housing_old_brewhouse.txt, orientation_what_matters.txt

```
Yes. Juniors and seniors are ordered by accumulated credit hours first (with random tie-breaks), which means a senior who took summer courses reliably beats a senior who didn't. 

Source: admin_housing_lottery.txt
```

### Do seniors who took summer classes get better dorm picks? — run 2

- Best distance: 0.4784 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, admin_pass_fail_option.txt, housing_aldridge_hall.txt, housing_old_brewhouse.txt, orientation_what_matters.txt

```
Yes, juniors and seniors are ordered by accumulated credit hours first, meaning a senior who took summer courses reliably beats a senior who didn't (admin_housing_lottery.txt).
```

### Do seniors who took summer classes get better dorm picks? — run 3

- Best distance: 0.4784 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, admin_pass_fail_option.txt, housing_aldridge_hall.txt, housing_old_brewhouse.txt, orientation_what_matters.txt

```
Yes, juniors and seniors are ordered by accumulated credit hours first, meaning a senior who took summer courses reliably beats a senior who didn't in the housing lottery. (Source: admin_housing_lottery.txt)
```

### What's the last day I can quit a class without it showing up on my transcript? — run 1

- Best distance: 0.4310 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, admin_transcript_requests.txt, admin_withdrawal_deadline.txt, course_stat_150.txt

```
Based on the documents provided, the last day to drop a class without it showing up as a "W" on your transcript is through the end of the second week (`admin_add_drop_deadline.txt`).
```

### What's the last day I can quit a class without it showing up on my transcript? — run 2

- Best distance: 0.4310 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, admin_transcript_requests.txt, admin_withdrawal_deadline.txt, course_stat_150.txt

```
You can drop a course through the end of the second week without a W showing on your transcript, as a drop after week two results in a W. 

Source: admin_add_drop_deadline.txt
```

### What's the last day I can quit a class without it showing up on my transcript? — run 3

- Best distance: 0.4310 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, admin_transcript_requests.txt, admin_withdrawal_deadline.txt, course_stat_150.txt

```
Based on the documents, the last day to drop a class without it showing up as a "W" on your transcript is the end of the second week, because dropping after week two shows as a W. 

Source: `admin_add_drop_deadline.txt`
```

### Are the washers in the transfer-friendly dorm expensive? — run 1

- Best distance: 0.4400 (passed the gate)
- Sources retrieved: housing_calder_annexe.txt, housing_fenwick_court.txt, housing_innisfree_hall_laundry.txt, housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt

```
I do not have enough information to answer your question, as the provided documents do not mention a "transfer-friendly dorm".
```

### Are the washers in the transfer-friendly dorm expensive? — run 2

- Best distance: 0.4400 (passed the gate)
- Sources retrieved: housing_calder_annexe.txt, housing_fenwick_court.txt, housing_innisfree_hall_laundry.txt, housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt

```
I don't have enough information to answer your question, as the documents do not mention which dorm is transfer-friendly.
```

### Are the washers in the transfer-friendly dorm expensive? — run 3

- Best distance: 0.4400 (passed the gate)
- Sources retrieved: housing_calder_annexe.txt, housing_fenwick_court.txt, housing_innisfree_hall_laundry.txt, housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt

```
I do not have enough information to answer this question because the provided documents do not mention which dorm is transfer-friendly.
```
