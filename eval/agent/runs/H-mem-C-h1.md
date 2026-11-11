## Q1
The current monthly churn-xgb retrain uses the latest 9 observation months of data, per the 2026-10-30 decision to retrain churn-xgb-v3 monthly on that window.
Sources: churn-2026/dec-retrain-cadence.md, churn-2026/churn-xgb-v3.md

## Q2
churn-xgb-v2 and churn-xgb-v3 both depend on feat-utilization-v1. The 2026-10-29 check went through all 3 util_ columns against the leak pattern and found no post-period days, so the features are clean and feat-utilization-v1 was kept unchanged in the v3 models.
Sources: churn-2026/feat-utilization-v1.md, churn-2026/feat-utilization-check.md, churn-2026/churn-xgb-v2.md, churn-2026/churn-xgb-v3.md, log/2026-10-29.md

## Q3
exp-017 showed that the 0.81 AUC was inflated by leakage: once post-period days were removed from the velocity window, AUC on holdout-2025q4 fell from 0.81 to 0.74 (recall@10 0.41, n=1.2M). That led to the post-period-leak finding and the decision to rebuild velocity as v3 from pre-observation days only and retire v2.
Sources: churn-2026/exp-017-leak-check.md, churn-2026/post-period-leak.md, churn-2026/dec-velocity-v3.md, log/2026-10-28.md

## Q4
In churn-2026, holdout-2025q4 is 1.2M accounts with Oct–Dec 2025 observation dates, never used for training, and every churn-2026 model is evaluated on it. The freeze date is recorded as 2026-01-19 with 412,600 rows in a general freeze rule note, which conflicts with the 1.2M size, so the freeze figures need checking against the set actually used.
Sources: churn-2026/ds-holdout-2025q4.md, howto/eval-set-freeze-date.md, qa/holdout-2025q4-reextract.md

## Q5
The logistic baseline (exp-011, 2026-09-15) reached AUC 0.71 and recall@10 0.29 on holdout-2025q4, with n=1.2M and 14 account-level features (no velocity or utilization).
Sources: churn-2026/exp-011-baseline.md

## Q6
The notes do not record why recall@10 is used to judge decisions rather than AUC. They only report recall@10 alongside AUC for each model (for example exp-011, exp-014, exp-017, churn-xgb-v3).
Sources: churn-2026/exp-011-baseline.md, churn-2026/exp-014.md

## Q7
The current velocity feature is feat-velocity-v3, which replaced v2 on 2026-10-30. v3 uses only pre-observation days, with every window ending on the observation date (30 days before it, plus the ratio to the prior 90-day average); v2's windows ran into post-period days, which was the leak.
Sources: churn-2026/feat-velocity-v3.md, churn-2026/feat-velocity-v2.md, churn-2026/dec-velocity-v3.md, churn-2026/post-period-leak.md

## Q8
feat-velocity-v3 reads from cards.txn_daily and produces 6 vel_ columns. It is used by churn-xgb-v3 (registered as models:/churn-xgb/3, which replaces churn-xgb-v2 in the nightly scoring job).
Sources: churn-2026/feat-velocity-v3.md, churn-2026/churn-xgb-v3.md, churn-2026/dec-velocity-v3.md

## Q9
The 2026-10-26 leak review started from the exp-014 velocity columns. The September data question (short September partitions) was raised with data-eng-cards, and the notes contain no recorded answer to it.
Sources: log/2026-10-26.md

## Q10
The 90-day churn label in cards.churn_labels counts an account as churned if it has no purchase and no payment for 90 days after the observation date; this superseded the 60-day label on 2026-01-12. The table is built by the retention-labels job from cards.txn_daily and maintained by data-eng-cards, although a backfill from 2024-01 is credited to Tomás Rivera's team.
Sources: howto/churn-label-90d.md, churn-2026/ds-churn-labels.md, howto/churn-label-60d.md