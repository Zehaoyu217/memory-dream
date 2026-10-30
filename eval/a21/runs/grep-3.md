## Q1
feat-velocity-v2 is 6 `vel_` columns (`features/velocity_v2.py`) built on `cards.txn_daily`. They hold the count and sum of card transactions in the 30 days "around" the observation date, plus their ratio to the 90-day average. They gave exp-014 / churn-xgb-v2 its lift (AUC 0.71→0.81, mostly from `vel_ratio_30_90`), but that window took in days after the observation date, which fall inside the label window. That is a target leak: with those days removed, AUC fell to 0.74 (exp-017), and `vel_ratio_30_90` dropped from 1st to 9th in gain importance. On 2026-10-30 it was retired and superseded by feat-velocity-v3, which uses only days before the observation date. Any v2 numbers computed before 2026-10-27 also used about 6% fewer September 2025 transactions.
Sources: memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/exp-014.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/txn-backfill.md
Tool calls for this question: 3 (shared across all 10 questions: one file listing plus two bulk reads of every note)
## Q2
exp-014 (2026-09-25) was XGBoost (400 trees, depth 6) with the velocity-v2 features added to the baseline set. On holdout-2025q4 (n=1.2M) it scored AUC 0.81 and recall@10 0.52, up from the logistic baseline's 0.71 / 0.29, and became churn-xgb-v2. The 0.10 AUC jump looked too good and turned out to be leakage. exp-017 re-ran it with the velocity window ending on the observation date and got AUC 0.74 and recall@10 0.41. That led to velocity v3 and churn-xgb-v3 (AUC 0.76, recall@10 0.43).
Sources: memory/churn-2026/exp-014.md, memory/churn-2026/exp-011-baseline.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/churn-xgb-v3.md
Tool calls for this question: 3 (shared)
## Q3
Five things read `cards.txn_daily` directly: `cards.churn_labels` (built from it by the retention-labels job), the Q4-2025 snapshot ds-txn-2025q4 (2.3B rows), feat-velocity-v2, feat-velocity-v3 and feat-utilization-v1 (`balance` / `credit_limit`). Further downstream are every model trained on those labels and features: logreg-baseline, exp-014 / churn-xgb-v2 and churn-xgb-v3. After them come their outputs `cards.churn_scores` and the nightly risk tiers in `offers.tier_matrix`.
Sources: memory/churn-2026/ds-churn-labels.md, memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/txn-backfill.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-risk-tiers.md
Tool calls for this question: 3 (shared)
## Q4
The production model is churn-xgb-v3 (`models:/churn-xgb/3`), registered on 2026-10-30, when it replaced churn-xgb-v2 in the nightly scoring job. On holdout-2025q4 (n=1.2M) it scores AUC 0.76 and recall@10 0.43, with no leakage. Recall@10 holds at 0.45 / 0.43 / 0.40 across the Oct / Nov / Dec 2025 cohorts. The notes call 0.43 "the honest number", since v2's 0.52 came from the leak. It is to be retrained monthly on the latest 9 observation months.
Sources: memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md, memory/churn-2026/dec-retrain-cadence.md, memory/log/2026-10-30.md
Tool calls for this question: 3 (shared)
## Q5
v2's velocity features leaked the target. Their 30-day window sat "around" the observation date, so it counted days after it, inside the 90-day label window. v3 rebuilt the same 6 `vel_` columns with every window ending on the observation date and kept the XGBoost settings and utilization features. The leak check (exp-017) showed AUC falling 0.81→0.74 once post-period days were removed, with `vel_ratio_30_90` dropping from 1st to 9th in importance. The notes don't explain why v3 lands at 0.76 rather than exp-017's 0.74.
Sources: memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md
Tool calls for this question: 3 (shared)
## Q6
data-eng-cards owns `cards.txn_daily`. Yes, there was a data-quality issue: the September 2025 partitions were about 6% short. A backfill (ticket DE-4411) finished on 2026-10-27, and row counts now match the ledger within 0.1%. Any v2 numbers computed before that date used about 6% fewer September transactions, and churn-xgb-v2 was evaluated on 2026-10-02 with September 2025 inside its training window. The 2026-10-30 log also says a backfill is running for the October partitions, which no note covers yet.
Sources: memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/txn-backfill.md, memory/churn-2026/ds-churn-labels.md, memory/churn-2026/churn-xgb-v2.md, memory/log/2026-10-26.md, memory/log/2026-10-27.md, memory/log/2026-10-30.md
Tool calls for this question: 3 (shared)
## Q7
The cuts are at churn score 0.20 and 0.50, decided on 2026-10-08 with Maya Ortiz against a budget of calls for 4% and emails for 12% of the book. A score of 0.50 or more means a call (3.8% of the book), 0.20–0.50 means an email (11.6%), and below 0.20 means no action. They were set on churn-xgb-v2 scores and are formally still in force: the 2026-10-30 retrain decision keeps them until q-recalibrate-tiers is answered. Whether they still fit is an open question as of 2026-10-30, because churn-xgb-v3's scores are less extreme and the call tier would shrink from 3.8% to about 2.9% at these cuts.
Sources: memory/churn-2026/dec-risk-tiers.md, memory/churn-2026/q-tier-cutoffs.md, memory/churn-2026/q-recalibrate-tiers.md, memory/churn-2026/dec-retrain-cadence.md, memory/log/2026-10-28.md
Tool calls for this question: 3 (shared)
## Q8
Poorly. In exp-015, new accounts (tenure under 6 months; n=168k, 14% of holdout-2025q4) got AUC 0.69 and recall@10 0.31, against AUC 0.83 for accounts with 6+ months tenure (n=1.03M). New accounts are 14% of the book but 21% of churners, and they have too little history for the velocity or utilization features to mean much. The options on the table are a tenure-specific model or routing them to the onboarding team (owner Priya Nair). These numbers were measured on the leaky churn-xgb-v2, and no note has a tenure split for v3.
Sources: memory/churn-2026/exp-015-tenure.md, memory/churn-2026/finding-new-accounts.md
Tool calls for this question: 3 (shared)
## Q9
No. On 2026-10-29 all 3 `util_` columns of feat-utilization-v1 were checked against the post-period leak pattern. Every window ends on the observation date, with no post-period days. They were kept unchanged in churn-xgb-v3.
Sources: memory/churn-2026/feat-utilization-check.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/churn-xgb-v3.md, memory/log/2026-10-29.md
Tool calls for this question: 3 (shared)
## Q10
Three models are trained on `cards.churn_labels`. The logistic baseline (exp-011) uses 14 account features. churn-xgb-v2 (from exp-014) and churn-xgb-v3 are both fit on observation months 2025-01 to 2025-09. v3 will be retrained monthly on the latest 9 observation months. The churn base rate is 6.8% on the 2025 book (n=4.1M accounts, as of 2026-09-03), with a 90-day label window after month-end observation dates.
Sources: memory/churn-2026/ds-churn-labels.md, memory/churn-2026/exp-011-baseline.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-retrain-cadence.md
Tool calls for this question: 3 (shared)