## Q1
The exp-014 XGBoost used 400 trees at depth 6. On holdout-2025q4 (n=1.2M, 2026-09-25) it reached AUC 0.81 and recall@10 0.52, up from the logistic baseline's 0.71 and 0.29, with most of the lift coming from `vel_ratio_30_90`. These figures were later found to come from target leakage, so they are not honest numbers.
Sources: memory/churn-2026/exp-014.md, memory/churn-2026/exp-011-baseline.md, memory/churn-2026/post-period-leak.md
## Q2
A 0.10 AUC jump (0.71→0.81) from a single feature group looked too good to be true. The v2 velocity features were built on a 30-day window "around" the observation date, so that window could include days after it, which fall inside the 90-day label window. exp-017 was set up to test this by rebuilding the features without post-period days and re-scoring.
Sources: memory/churn-2026/leak-hypothesis.md, memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/ds-churn-labels.md
## Q3
No. churn-xgb-v3 supersedes churn-xgb-v2, and exp-019 states that "v2's 0.52 was the leak; 0.43 is the honest number". The figure to quote is churn-xgb-v3's recall@10 of 0.43 (AUC 0.76, holdout-2025q4, n=1.2M, 2026-10-30), which holds at 0.40–0.45 across the Oct/Nov/Dec 2025 cohorts.
Sources: memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md, memory/churn-2026/post-period-leak.md
## Q4
It depends on the nightly churn scores plus the fixed risk-tier cuts: score ≥0.50 means call, 0.20–0.50 means email, below 0.20 means no action. The decision note still says the cuts apply to churn-xgb-v2 scores, but that note is out of date: churn-xgb-v3 replaced v2 in the nightly scoring job on 2026-10-30. The cuts stay in place until q-recalibrate-tiers is answered, and at those cuts v3 shrinks the call tier from 3.8% to about 2.9% of the book.
Sources: memory/churn-2026/dec-risk-tiers.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-retrain-cadence.md, memory/churn-2026/q-recalibrate-tiers.md, memory/log/2026-10-30.md
## Q5
On 2026-10-05 retention (Maya Ortiz) asked for three tiers (call, email, nothing) from churn-xgb-v2 scores, with a budget for calls to 4% of the book and emails to 12%. The 2026-10-08 decision set the cuts at 0.50 and 0.20, giving 3.8% call and 11.6% email, just under that budget. They were fitted to the leaky v2 scores, so whether they need recalibrating for v3 is an open question.
Sources: memory/churn-2026/q-tier-cutoffs.md, memory/churn-2026/dec-risk-tiers.md, memory/churn-2026/q-recalibrate-tiers.md
## Q6
The decision metric is recall@10, the share of 90-day churners caught in the top 10% of scores. It is computed by `nb/metrics.py::recall_at_k` with k=0.10. AUC is reported alongside it, but decisions use recall@10.
Sources: memory/churn-2026/metric-recall-at-10.md
## Q7
exp-017 reported AUC 0.74 and recall@10 0.41 on holdout-2025q4 with n=1.2M (2026-10-28). It used the same XGBoost setup as exp-014 but with the velocity window ending on the observation date, and `vel_ratio_30_90` fell from first to ninth in gain importance.
Sources: memory/churn-2026/exp-017-leak-check.md, memory/log/2026-10-28.md
## Q8
September 2025 partitions of `cards.txn_daily` were about 6% short until the backfill finished on 2026-10-27 (ticket DE-4411); row counts now match the ledger within 0.1%. The txn table feeds the velocity features, so any v2 number computed before 10-27 used about 6% fewer September transactions. That covers exp-014 (09-25), churn-xgb-v2 (10-02) and exp-015 (10-10), and those v2 numbers are also inflated by the post-period leak.
Sources: memory/churn-2026/txn-backfill.md, memory/churn-2026/ds-txn-2025q4.md, memory/log/2026-10-27.md
## Q9
At 08:50 on 2026-10-30 the daily log says the txn table backfill was running for the October partitions; the September backfill was already done on 10-27. This is recorded only in the scratch log, not in any note. My own inference: churn-xgb-v3 was registered at 13:30 the same day, so its October-cohort velocity inputs may have been read while those partitions were still filling.
Sources: memory/log/2026-10-30.md, memory/churn-2026/txn-backfill.md, memory/churn-2026/churn-xgb-v3.md
## Q10
It rests on one before/after comparison on holdout-2025q4 (n=1.2M). exp-017, with post-period days removed, dropped AUC from 0.81 to 0.74 and recall@10 from 0.52 to 0.41, and `vel_ratio_30_90` fell from first to ninth in gain importance. The other supports are the "window around the observation date" reasoning and `nb/eda_velocity.ipynb` cells 12–18, which were kept as evidence. One confound: exp-014's 0.81 was computed before the 10-27 September backfill and exp-017 after it, so the drop mixes the window change with the data fix.
Sources: memory/churn-2026/post-period-leak.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-014.md, memory/churn-2026/txn-backfill.md, memory/log/2026-10-27.md, memory/log/2026-10-29.md