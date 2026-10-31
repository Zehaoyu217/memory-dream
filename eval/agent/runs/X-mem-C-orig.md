## Q1
feat-velocity-v2 has 6 `vel_` columns (`features/velocity_v2.py`). They count and sum card transactions from `cards.txn_daily` in the 30 days "around" the observation date, plus their ratio to the 90-day average. They drove exp-014 and churn-xgb-v2 (AUC 0.71→0.81), but the window ran past the observation date into the label window, so it leaked the target: exp-017 showed AUC 0.81→0.74 once those days were removed. It was retired and superseded by feat-velocity-v3 (pre-observation days only) on 2026-10-30. Separately, any v2 numbers computed before the 2026-10-27 backfill used about 6% fewer September transactions.
Sources: memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/txn-backfill.md
## Q2
exp-014 added velocity features to the baseline in XGBoost and lifted AUC from 0.71 to 0.81 and recall@10 from 0.29 to 0.52 on holdout-2025q4. It became churn-xgb-v2 (`models:/churn-xgb/2`, 2026-10-02). The 0.10 AUC jump looked too good and led to the leak review: exp-017 got AUC 0.74 and recall@10 0.41 without post-period days, which confirmed post-period leakage. That led to velocity v3 and churn-xgb-v3 (AUC 0.76, recall@10 0.43), so exp-014's numbers were inflated.
Sources: memory/churn-2026/exp-014.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/churn-xgb-v3.md
## Q3
In churn-2026, these depend on `cards.txn_daily`:
- the ds-txn-2025q4 snapshot (2.3B rows)
- feat-velocity-v2 and v3
- feat-utilization-v1 (uses `balance` and `credit_limit`)
- `cards.churn_labels`, which the retention-labels job builds from it, so the baseline, churn-xgb-v2 and churn-xgb-v3 depend on it too.

Outside the project, it also feeds the weekly-deck data-quality gate (blocks publishing if row count is more than 5% off the trailing 7-day mean), the NPS behaviour joins, the fraud alert report and the fraud models.
Sources: memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/ds-churn-labels.md, memory/reporting/data-quality-gate.md
## Q4
churn-xgb-v3 (`models:/churn-xgb/3`, 2026-10-30) is the production model. It replaced churn-xgb-v2 in the nightly scoring job and uses feat-velocity-v3 plus feat-utilization-v1. On holdout-2025q4 (n=1.2M) it scores AUC 0.76 and recall@10 0.43, the business metric. Recall@10 holds at 0.40–0.45 across the Oct/Nov/Dec monthly cohorts and is described as "the honest number". It is retrained monthly on the latest 9 observation months.
Sources: memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md, memory/churn-2026/metric-recall-at-10.md, memory/churn-2026/dec-retrain-cadence.md
## Q5
v2's 0.81 was inflated by target leakage. feat-velocity-v2 aggregated `cards.txn_daily` past the observation date into the 90-day label window. exp-017 showed AUC falling 0.81→0.74 when post-period days were removed, and `vel_ratio_30_90` dropped from 1st to 9th in gain importance. v3 rebuilt velocity from pre-observation days only, kept the same utilization features (checked clean) and the same XGBoost settings, and lands at 0.76 with no leakage. The notes do not explain the gap between 0.74 and 0.76 (the Sept-2025 backfill on 10-27 may be a factor, but nothing records that).
Sources: memory/churn-2026/post-period-leak.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/feat-utilization-check.md, memory/churn-2026/txn-backfill.md
## Q6
data-eng-cards owns it. Tomás Rivera expects it to land by 07:00 UTC, T+1. There was a data-quality issue: September 2025 partitions were about 6% short until a backfill finished on 2026-10-27 (ticket DE-4411). After that, row counts match the ledger within 0.1%. Velocity numbers computed before 10-27 used about 6% fewer September transactions. Separately, late Sunday batches in Jan–Feb 2026 moved the weekly KPI cutoff to Saturday.
Sources: memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/txn-backfill.md, memory/prefs/tomas-rivera-freshness-sla.md, memory/reporting/weekly-kpi-cutoff-v2.md
## Q7
The cuts are 0.20 and 0.50, decided 2026-10-08 with Maya Ortiz:
- score ≥ 0.50 → call (3.8% of the book)
- 0.20–0.50 → email (11.6%)
- below 0.20 → no action

The budget allows 4% calls and 12% emails. The cuts were set on churn-xgb-v2 scores and are still in force: the retrain decision keeps them until q-recalibrate-tiers is answered. Their validity is an open question. v3 scores are less extreme, so at the current cuts the call tier would shrink to about 2.9% of the book.
Sources: memory/churn-2026/dec-risk-tiers.md, memory/churn-2026/q-tier-cutoffs.md, memory/churn-2026/q-recalibrate-tiers.md, memory/churn-2026/dec-retrain-cadence.md
## Q8
Poorly. In exp-015 (on churn-xgb-v2), accounts under 6 months tenure (n=168k, 14% of holdout) got AUC 0.69 and recall@10 0.31, against AUC 0.83 for tenure ≥ 6 months (n=1.03M). New accounts are 14% of the book but 21% of churners, and have too little history for velocity or utilization to mean much. The options are a tenure-specific model or routing them to onboarding (owner Priya Nair). The split was measured on the leaky v2, and no v3 tenure split is recorded.
Sources: memory/churn-2026/exp-015-tenure.md, memory/churn-2026/finding-new-accounts.md
## Q9
No. On 2026-10-29 all 3 `util_` columns of feat-utilization-v1 were checked against the leak pattern. Every window ends on the observation date, with no post-period days, so feat-utilization-v1 stays unchanged in the v3 models. The leak was only in velocity v2.
Sources: memory/churn-2026/feat-utilization-check.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/post-period-leak.md
## Q10
In churn-2026, three models are trained on `cards.churn_labels`:
- the logistic baseline (exp-011: AUC 0.71, recall@10 0.29)
- churn-xgb-v2 (2025-01 to 2025-09 observation months)
- churn-xgb-v3 (same months, now retrained monthly on the latest 9)

The churn base rate is 6.8% on the 2025 book (n=4.1M accounts, 2026-09-03). The label is a 90-day churn flag (no card spend for 90 days after each month-end observation date).
Sources: memory/churn-2026/ds-churn-labels.md, memory/churn-2026/exp-011-baseline.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-retrain-cadence.md, memory/churn-2026/q-churn-drivers.md