## Q1
exp-014 used XGBoost with 400 trees and depth 6. On holdout-2025q4 (n=1.2M, 2026-09-25) it reached AUC 0.81 and recall@10 0.52, up from the baseline's 0.71 and 0.29. Most of the lift came from `vel_ratio_30_90`. Both figures were later shown to be inflated by the post-period leak.
Sources: memory/churn-2026/exp-014.md, memory/churn-2026/exp-011-baseline.md, memory/churn-2026/post-period-leak.md
## Q2
The velocity features alone raised AUC by 0.10, which looked too good for one feature group. feat-velocity-v2 counts transactions in a 30-day window "around" the observation date, so that window could include days after it, inside the label window. The fix was to rebuild without post-period days and re-score, which became exp-017.
Sources: memory/churn-2026/leak-hypothesis.md, memory/churn-2026/feat-velocity-v2.md
## Q3
No. churn-xgb-v2 has been replaced by churn-xgb-v3 (2026-10-30), and exp-019 says "v2's 0.52 was the leak; 0.43 is the honest number". v3 reaches recall@10 0.43 (AUC 0.76, n=1.2M) on holdout-2025q4, and 0.40–0.45 across the monthly cohorts.
Sources: memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md
## Q4
Each night the 0.20 / 0.50 risk-tier cuts are applied to the churn model's scores in `cards.churn_scores`, and the result is written to `offers.tier_matrix`. dec-risk-tiers still says those are churn-xgb-v2 scores (feat-velocity-v2 + feat-utilization-v1). On 2026-10-30 the scoring job switched to churn-xgb-v3 (feat-velocity-v3 + feat-utilization-v1), so the dependency is now v3. All of these features read `cards.txn_daily`.
Sources: memory/churn-2026/dec-risk-tiers.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/log/2026-10-30.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-utilization-v1.md
## Q5
Maya Ortiz (retention) asked on 2026-10-05 for three tiers (call, email, nothing) from churn-xgb-v2 scores. The budget covered calls for 4% of the book and emails for 12%. The decision on 2026-10-08 set ≥0.50 → call (3.8%), 0.20–0.50 → email (11.6%), and <0.20 → no action. The cuts were fitted to v2's leaky scores: under v3 the call tier would shrink to about 2.9%, and recalibrating the cuts is an open question (they stay in place until it is answered).
Sources: memory/churn-2026/q-tier-cutoffs.md, memory/churn-2026/dec-risk-tiers.md, memory/churn-2026/q-recalibrate-tiers.md, memory/churn-2026/dec-retrain-cadence.md
## Q6
The decision metric is recall@10, the share of 90-day churners caught in the top 10% of scores. It is computed by `nb/metrics.py::recall_at_k` with k=0.10. AUC is reported alongside it, but decisions use recall@10.
Sources: memory/churn-2026/metric-recall-at-10.md
## Q7
exp-017 used the same XGBoost setup but ended the velocity window on the observation date. On holdout-2025q4 (n=1.2M, 2026-10-28) it reported AUC 0.74 and recall@10 0.41. `vel_ratio_30_90` fell from first to ninth in gain importance.
Sources: memory/churn-2026/exp-017-leak-check.md
## Q8
The September 2025 backfill of `cards.txn_daily` (ticket DE-4411) finished only on 2026-10-27. Until then those partitions were short by about 6%. The txn table feeds the velocity features, so any v2 numbers computed before 10-27 used about 6% fewer September transactions. Those v2 numbers also carry the post-period leak.
Sources: memory/churn-2026/txn-backfill.md, memory/churn-2026/ds-txn-2025q4.md, memory/log/2026-10-27.md
## Q9
The October partitions: the 2026-10-30 log says "txn table backfill running for October partitions". The September 2025 gap had already been closed on 2026-10-27. The log does not say which year's October.
Sources: memory/log/2026-10-30.md, memory/churn-2026/txn-backfill.md
## Q10
It rests on the notebook `nb/eda_velocity.ipynb`, cells 12–18, kept as evidence on 2026-10-29. It also rests on exp-017: removing post-period days dropped AUC from 0.81 to 0.74 on holdout-2025q4 (n=1.2M), and `vel_ratio_30_90` fell from first to ninth in gain importance. The utilization columns were checked for the same leak and came out clean.
Sources: memory/churn-2026/post-period-leak.md, memory/churn-2026/exp-017-leak-check.md, memory/log/2026-10-29.md