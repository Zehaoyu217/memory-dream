## Q1
feat-velocity-v2 holds 6 `vel_` columns (`features/velocity_v2.py`) built on `cards.txn_daily`: the count and sum of card transactions in the 30 days *around* the observation date, plus their ratio to the 90-day average. It drove exp-014 and churn-xgb-v2, lifting AUC from 0.71 to 0.81 and recall@10 from 0.29 to 0.52, mostly through `vel_ratio_30_90`. That lift was a target leak: the window included days after the observation date. With those days removed, AUC fell to 0.74 and `vel_ratio_30_90` dropped from 1st to 9th in importance. It was retired and superseded by feat-velocity-v3 on 2026-10-30, and any v2 numbers computed before 2026-10-27 also used about 6% fewer September 2025 transactions.
Sources: memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/exp-014.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/txn-backfill.md
## Q2
exp-014 (2026-09-25) added the velocity features to the baseline in an XGBoost model (400 trees, depth 6). On holdout-2025q4 (n=1.2M) it scored AUC 0.81 vs 0.71 and recall@10 0.52 vs 0.29, and it became churn-xgb-v2 (`models:/churn-xgb/2`). The 0.10 AUC jump prompted a leak hypothesis. exp-017 confirmed it: without post-period days AUC is 0.74 and recall@10 is 0.41. So most of exp-014's lift was leakage, and its model was superseded by churn-xgb-v3 (AUC 0.76, recall@10 0.43).
Sources: memory/churn-2026/exp-014.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/churn-xgb-v3.md
## Q3
These read `cards.txn_daily` directly:
- the Q4-2025 snapshot ds-txn-2025q4
- `cards.churn_labels`, built from it by the retention-labels job
- feat-velocity-v2 (retired), feat-velocity-v3 and feat-utilization-v1

Further downstream sit every model trained on those labels and features: logreg-baseline, exp-014/exp-017, churn-xgb-v2 and churn-xgb-v3. Through them, so do the nightly `cards.churn_scores` and the `offers.tier_matrix` risk tiers.
Sources: memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/ds-churn-labels.md, memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/txn-backfill.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-risk-tiers.md
## Q4
The production model is churn-xgb-v3 (`models:/churn-xgb/3`), registered 2026-10-30, which replaced v2 in the nightly scoring job. It uses feat-velocity-v3 and feat-utilization-v1, with the same XGBoost settings as v2, trained on 2025-01 to 2025-09 observation months. On holdout-2025q4 (n=1.2M) it scores AUC 0.76 and recall@10 0.43 with no leakage, and recall@10 holds at 0.45, 0.43 and 0.40 across the Oct, Nov and Dec cohorts. It is retrained monthly on the latest 9 observation months.
Sources: memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md, memory/churn-2026/dec-retrain-cadence.md, memory/churn-2026/metric-recall-at-10.md, memory/log/2026-10-30.md
## Q5
v2's 0.81 came from a target leak, not real skill. Its velocity features aggregated `cards.txn_daily` days after the observation date, which fall inside the 90-day label window. exp-017 removed those days and AUC fell to 0.74 (recall@10 0.41), with `vel_ratio_30_90` dropping from 1st to 9th in gain importance. v3 rebuilds velocity from pre-observation days only and lands at 0.76 / 0.43, which the team treats as the honest number. A separate, smaller issue: v2-era numbers also used about 6% fewer September transactions before the 2026-10-27 backfill.
Sources: memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md, memory/churn-2026/txn-backfill.md
## Q6
data-eng-cards owns `cards.txn_daily`: 2.3B account-day rows for 2025, refreshed nightly. There was a data-quality issue: the September 2025 partitions were about 6% short until a backfill finished on 2026-10-27 (ticket DE-4411), after which row counts matched the ledger within 0.1%. Any v2 velocity numbers computed before then used about 6% fewer September transactions. The 2026-10-30 log also says a backfill is now running for the October partitions, and no note covers it yet.
Sources: memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/txn-backfill.md, memory/churn-2026/ds-churn-labels.md, memory/log/2026-10-26.md, memory/log/2026-10-27.md, memory/log/2026-10-30.md
## Q7
The cutoffs are churn score 0.20 and 0.50, decided 2026-10-08 with Maya Ortiz against budgets of 4% calls and 12% emails:
- ≥0.50: call (3.8% of the book)
- 0.20–0.50: email (11.6%)
- below 0.20: no action

They were set on churn-xgb-v2 scores. They stay in force under the 2026-10-30 retrain decision, but whether they still fit is an open question. v3 scores are less extreme, so at these cuts the call tier would shrink from 3.8% to about 2.9% of the book.
Sources: memory/churn-2026/dec-risk-tiers.md, memory/churn-2026/q-tier-cutoffs.md, memory/churn-2026/q-recalibrate-tiers.md, memory/churn-2026/dec-retrain-cadence.md
## Q8
Poorly. In exp-015 (2026-10-10, measured on churn-xgb-v2), accounts under 6 months of tenure (n=168k, 14% of the holdout) scored AUC 0.69 and recall@10 0.31. Accounts with 6+ months (n=1.03M) scored AUC 0.83. New accounts are 14% of the book but 21% of churners, and have too little history for velocity or utilization to mean much. The options on the table are a tenure-specific model or routing these accounts to onboarding (owner Priya Nair). This split has not been re-run on the leak-free v3.
Sources: memory/churn-2026/exp-015-tenure.md, memory/churn-2026/finding-new-accounts.md
## Q9
No. On 2026-10-29 all 3 `util_` columns of feat-utilization-v1 were checked against the leak pattern. Every window ends on the observation date and none includes post-period days, so feat-utilization-v1 stays unchanged in v3.
Sources: memory/churn-2026/feat-utilization-check.md, memory/churn-2026/feat-utilization-v1.md, memory/log/2026-10-29.md
## Q10
Four models train on `cards.churn_labels`:
- logreg-baseline (exp-011): AUC 0.71, recall@10 0.29
- the exp-014 XGBoost model, plus its exp-017 leak-check variant
- churn-xgb-v2 (superseded)
- churn-xgb-v3 (current)

v2 and v3 both use the 2025-01 to 2025-09 observation months. The churn base rate is 6.8% on the 2025 book (n=4.1M accounts, as of 2026-09-03). A churner is an account with no card spend in the 90 days after a month-end observation date.
Sources: memory/churn-2026/ds-churn-labels.md, memory/churn-2026/exp-011-baseline.md, memory/churn-2026/exp-014.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-retrain-cadence.md, memory/churn-2026/q-churn-drivers.md