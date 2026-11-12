## Q1
The current monthly churn-xgb retrain uses the latest 9 observation months of `cards.churn_labels` (decision of 2026-10-30, with retention). The churn-xgb-v3 model was trained on 2025-01 to 2025-09 observation months.
Sources: memory/churn-2026/dec-retrain-cadence.md, memory/churn-2026/churn-xgb-v3.md

## Q2
feat-utilization-v1 is used by churn-xgb-v2 and churn-xgb-v3. The 2026-10-29 check found all 3 `util_` columns clean (no post-period days), so feat-utilization-v1 stays unchanged in the v3 models.
Sources: memory/churn-2026/feat-utilization-check.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/log/2026-10-29.md

## Q3
The exp-017 leak check (velocity window ending on the observation date) gave AUC 0.74 and recall@10 0.41 on holdout-2025q4, down from 0.81 in exp-014. That confirmed the post-period aggregation leak, and `vel_ratio_30_90` fell from first to ninth in gain importance.
Sources: memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/log/2026-10-28.md

## Q4
In churn-2026, holdout-2025q4 is a random 30% of accounts, stratified by tenure band, with 1.2M accounts whose observation dates fall in Oct to Dec 2025; it was never used for training and was frozen 2026-09-04 (split script `nb/make_holdout.ipynb`). A general howto note says the set was frozen 2026-01-19 with 412,600 rows, which conflicts with the churn-2026 record. The app-engagement project has its own holdout-2025q4 of 610,000 accounts.
Sources: memory/churn-2026/ds-holdout-2025q4.md, memory/howto/eval-set-freeze-date.md, memory/app-engagement/ds-ae-holdout.md

## Q5
The logistic baseline (exp-011) reached AUC 0.71 and recall@10 0.29 on holdout-2025q4, with n = 1.2M and 14 account-level features (no velocity or utilization).
Sources: memory/churn-2026/exp-011-baseline.md

## Q6
Decisions use recall@10 because retention can call 10% of the book each month, so the metric is the share of 90-day churners caught in the top 10% of scores. AUC is reported only alongside it.
Sources: memory/churn-2026/metric-recall-at-10.md, memory/churn-2026/q-churn-drivers.md

## Q7
The current velocity version is feat-velocity-v3, which replaces v2. v2 summed transactions over the 30 days around the observation date, which could include post-period days, while v3 uses only the 30 days before the observation date, plus their ratio to the prior 90-day average.
Sources: memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/dec-velocity-v3.md

## Q8
feat-velocity-v3 reads from `cards.txn_daily` and is used by churn-xgb-v3. Its owner is Sam Lee.
Sources: memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/churn-xgb-v3.md

## Q9
The 2026-10-26 leak review started from the velocity columns of exp-014. The question about short September partitions went to data-eng-cards and was resolved when the Sept 2025 backfill of `cards.txn_daily` finished 2026-10-27 (ticket DE-4411), with row counts now within 0.1% of the ledger. Earlier v2 numbers used about 6% fewer September transactions.
Sources: memory/log/2026-10-26.md, memory/churn-2026/txn-backfill.md, memory/churn-2026/ds-txn-2025q4.md

## Q10
The 90-day churn label in `cards.churn_labels` flags an account with no purchase and no payment in the 90 days after the observation date (month-end), replacing the 60-day definition in January 2026. The retention-labels job builds it from `cards.txn_daily`, and data-eng-cards maintains it. A separate howto note says Tomás Rivera's team backfilled the table from 2024-01, so the ownership record is inconsistent.
Sources: memory/churn-2026/ds-churn-labels.md, memory/howto/churn-label-90d.md, memory/howto/churn-label-60d.md