## Q1
The current monthly retrain uses the latest 9 observation months of `cards.churn_labels`. Sam Lee decided this with retention on 2026-10-30, and the 0.20 / 0.50 risk-tier cuts stay in place until q-recalibrate-tiers is answered. The first churn-xgb-v3 fit used 9 such months, the 2025-01 to 2025-09 observation months.
Sources: memory/churn-2026/dec-retrain-cadence.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/q-recalibrate-tiers.md
## Q2
Two models use feat-utilization-v1: churn-xgb-v2 (now superseded) and churn-xgb-v3. The 2026-10-29 check looked at all 3 `util_` columns and found no post-period days, so they are clean. That meant feat-utilization-v1 stays unchanged in the v3 models, and only velocity had to be rebuilt. churn-xgb-v3 then pairs feat-velocity-v3 with feat-utilization-v1.
Sources: memory/churn-2026/feat-utilization-check.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/log/2026-10-29.md
## Q3
exp-017 kept the exp-014 XGBoost setup but ended the velocity window on the observation date. On holdout-2025q4 (n=1.2M) AUC fell from 0.81 to 0.74, recall@10 was 0.41, and `vel_ratio_30_90` dropped from first to ninth in gain importance. This confirmed the post-period leak (finding dated 2026-10-29). That led to the 2026-10-30 decision to build feat-velocity-v3 and retire v2, and to churn-xgb-v3 (AUC 0.76, recall@10 0.43), which replaced v2 in nightly scoring.
Sources: memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/churn-xgb-v3.md, memory/log/2026-10-28.md
## Q4
holdout-2025q4 is a random 30% of accounts, stratified by tenure band: 1.2M accounts with Oct–Dec 2025 observation dates, never used for training. It was frozen on 2026-09-04, and the split script is `nb/make_holdout.ipynb`. Every churn-2026 model is evaluated on it unless a note says otherwise.
Sources: memory/churn-2026/ds-holdout-2025q4.md
## Q5
The logistic baseline (logreg-baseline, exp-011) reached AUC 0.71 and recall@10 0.29 on holdout-2025q4 with n=1.2M (2026-09-15). It used 14 account-level features, with no velocity and no utilization features.
Sources: memory/churn-2026/exp-011-baseline.md
## Q6
recall@10 is the share of 90-day churners caught in the top 10% of scores. It is the business metric because retention can call 10% of the book each month. AUC is reported alongside it, but decisions use recall@10 (computed by `nb/metrics.py::recall_at_k` with k=0.10).
Sources: memory/churn-2026/metric-recall-at-10.md, memory/churn-2026/q-churn-drivers.md
## Q7
feat-velocity-v3 is current; it superseded v2 on 2026-10-30. v3 counts and sums transactions in the 30 days before the observation date, plus their ratio to the prior 90-day average. v2 used a 30-day window "around" the observation date, which reached past it into the label window and leaked the target. Both have the same 6 `vel_` columns.
Sources: memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/leak-hypothesis.md
## Q8
feat-velocity-v3 reads `cards.txn_daily` (code in `features/velocity_v3.py`), and churn-xgb-v3 (`models:/churn-xgb/3`) uses it. The September 2025 gap in that table was backfilled on 2026-10-27. The 2026-10-30 log also notes a backfill running for October partitions.
Sources: memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/txn-backfill.md, memory/log/2026-10-30.md
## Q9
The 2026-10-26 leak review started from exp-014's velocity columns, following the 2026-10-20 leak hypothesis about the 0.81 AUC. The September question (data-eng-cards was asked about short September partitions) ended in the txn-backfill note. The Sept-2025 backfill of `cards.txn_daily` finished 2026-10-27 (ticket DE-4411), and row counts now match the ledger within 0.1%. Any v2 numbers computed before 10-27 used about 6% fewer September transactions.
Sources: memory/log/2026-10-26.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-014.md, memory/churn-2026/txn-backfill.md, memory/churn-2026/ds-txn-2025q4.md, memory/log/2026-10-27.md
## Q10
`cards.churn_labels` holds a 90-day churn flag per account and observation month. Observation dates are month-ends, and an account counts as churned if it has no card spend in the 90 days after. The retention-labels job builds it from `cards.txn_daily`, and data-eng-cards maintains it. The churn rate is 6.8% on the 2025 book (n=4.1M accounts, 2026-09-03).
Sources: memory/churn-2026/ds-churn-labels.md, memory/churn-2026/q-churn-drivers.md