## Q1
The current monthly retrain of churn-xgb-v3 uses the latest 9 observation months of `cards.churn_labels`. Sam Lee and retention decided this on 2026-10-30. The first v3 fit used the 2025-01 to 2025-09 observation months. The 0.20 / 0.50 risk-tier cuts stay in place until q-recalibrate-tiers is answered.
Sources: memory/churn-2026/dec-retrain-cadence.md, memory/churn-2026/churn-xgb-v3.md
## Q2
Two models use feat-utilization-v1: churn-xgb-v2 (now superseded) and churn-xgb-v3. On 2026-10-29 the team checked all 3 `util_` columns against the post-period leak pattern. Every window ends on the observation date with no post-period days, so the features were judged clean and kept unchanged in the v3 models.
Sources: memory/churn-2026/feat-utilization-check.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/log/2026-10-29.md
## Q3
exp-017 used the same XGBoost setup as exp-014, but with the velocity window ending on the observation date. On holdout-2025q4 (n=1.2M) AUC fell from 0.81 to 0.74 and recall@10 was 0.41, and `vel_ratio_30_90` dropped from first to ninth in gain importance. This confirmed the post-period leak (finding 2026-10-29). It led to the 2026-10-30 decision to rebuild velocity as v3 and retrain churn-xgb-v2 as churn-xgb-v3.
Sources: memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/dec-velocity-v3.md, memory/log/2026-10-28.md
## Q4
holdout-2025q4 is a random 30% of accounts, stratified by tenure band. It holds 1.2M accounts with Oct–Dec 2025 observation dates and is never used for training. It was frozen on 2026-09-04, and the split script is `nb/make_holdout.ipynb`.
Sources: memory/churn-2026/ds-holdout-2025q4.md
## Q5
The logistic baseline (exp-011) reached AUC 0.71 and recall@10 0.29 on holdout-2025q4, with n=1.2M (2026-09-15). It was fit on `cards.churn_labels` with 14 account-level features and no velocity or utilization features.
Sources: memory/churn-2026/exp-011-baseline.md
## Q6
recall@10 is the business metric because retention can call 10% of the book each month. It measures the share of 90-day churners caught in the top 10% of scores. AUC is reported alongside, but decisions use recall@10, computed with `nb/metrics.py::recall_at_k` with k=0.10.
Sources: memory/churn-2026/metric-recall-at-10.md
## Q7
feat-velocity-v3 is current and replaces feat-velocity-v2. v2 counted transactions in the 30 days around the observation date, so its window could include post-period days inside the label window. v3 uses only the 30 days before the observation date, plus a ratio to the prior 90-day average. Both versions have the same 6 `vel_` columns.
Sources: memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/dec-velocity-v3.md
## Q8
feat-velocity-v3 reads from `cards.txn_daily`, and its code is in `features/velocity_v3.py`. Its owner is Sam Lee. The model that uses it is churn-xgb-v3 (`models:/churn-xgb/3`), which scored AUC 0.76 and recall@10 0.43 on holdout-2025q4 and replaced churn-xgb-v2 in nightly scoring.
Sources: memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/churn-xgb-v3.md
## Q9
The 2026-10-26 review started from the exp-014 velocity columns, following the leak-hypothesis question about the 0.81 AUC. The same day the team asked data-eng-cards about short September 2025 partitions, which were about 6% short. That question was settled when the backfill of `cards.txn_daily` finished on 2026-10-27 (ticket DE-4411). Row counts now match the ledger within 0.1%, and any v2 numbers computed before 10-27 used about 6% fewer September transactions.
Sources: memory/log/2026-10-26.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/txn-backfill.md, memory/churn-2026/ds-txn-2025q4.md, memory/log/2026-10-27.md
## Q10
`cards.churn_labels` holds a 90-day churn flag per account and observation month. Observation dates are month-ends, and an account counts as churned if it has no card spend in the 90 days after. The retention-labels job builds it from `cards.txn_daily`, and data-eng-cards maintains it. The churn rate was 6.8% on the 2025 book (n=4.1M accounts, as of 2026-09-03).
Sources: memory/churn-2026/ds-churn-labels.md, memory/churn-2026/q-churn-drivers.md