## Q1
The current monthly churn-xgb retrain uses the latest 9 observation months of `cards.churn_labels` (decision of 2026-10-30, Sam Lee with retention). The 0.20 / 0.50 risk-tier cuts stay until q-recalibrate-tiers is answered. The churn-xgb-v3 note itself records its fit window as 2025-01 to 2025-09.
Sources: memory/churn-2026/dec-retrain-cadence.md, memory/churn-2026/churn-xgb-v3.md

## Q2
churn-xgb-v2 and churn-xgb-v3 both use feat-utilization-v1. The 2026-10-29 check found all 3 `util_` columns clean, since every window ends on the observation date, so feat-utilization-v1 stays unchanged in the v3 models.
Sources: memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/feat-utilization-check.md, memory/log/2026-10-29.md

## Q3
The exp-017 leak check (2026-10-28, same XGBoost setup as exp-014 but with the velocity window ending on the observation date) gave AUC 0.74 and recall@10 0.41 on holdout-2025q4, down from 0.81. That confirmed post-period aggregation leaked the target, which led to the post-period-leak finding and the decision to rebuild velocity as v3.
Sources: memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md

## Q4
The churn-2026 note describes holdout-2025q4 as 1.2M accounts with Oct–Dec 2025 observation dates, never used for training. A rule note says the holdout-2025q4 set was frozen on 2026-01-19 with 412,600 rows, which conflicts with the 1.2M figure and I could not reconcile it from the notes. The frozen-set rule means re-extracting the set would change labels, so late labels go into the next named holdout instead.
Sources: memory/churn-2026/ds-holdout-2025q4.md, memory/howto/eval-set-freeze-date.md, memory/qa/holdout-2025q4-reextract.md

## Q5
The logistic baseline (exp-011-baseline, 2026-09-15) reached AUC 0.71 and recall@10 0.29 on holdout-2025q4, with n=1.2M accounts and 14 account-level features (no velocity or utilization).
Sources: memory/churn-2026/exp-011-baseline.md

## Q6
The notes retrieved do not state a reason for judging decisions on recall@10 rather than AUC. They only report recall@10 beside AUC for each model, so this is not answered from memory.
Sources: memory/churn-2025/churn-gbm-2025-v2.md, memory/churn-2026/churn-xgb-v3.md

## Q7
The current velocity version is v3 (feat-velocity-v3), which replaces v2. Its 6 `vel_` columns use only pre-observation days: every window ends on the observation date, whereas v2's windows ran past it, which leaked the target.
Sources: memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/feat-velocity-v2.md

## Q8
feat-velocity-v3 reads from `cards.txn_daily`, counting card transactions in the 30 days before the observation date plus their ratio to the prior 90-day average. It is used by churn-xgb-v3, which is registered as `models:/churn-xgb/3`, and it is owned by Sam Lee.
Sources: memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/churn-xgb-v3.md

## Q9
The 2026-10-26 leak review started from the exp-014 velocity columns. Its September data question (short September partitions) was put to data-eng-cards, and the question was effectively resolved when the txn backfill landed on 2026-10-27 and row counts were re-run. The ds-txn-2025q4 note records a roughly 6% short-partition gap until that backfill, which ties the two together; this link is my inference, not stated outright.
Sources: memory/log/2026-10-26.md, memory/log/2026-10-27.md, memory/churn-2026/ds-txn-2025q4.md

## Q10
The current `cards.churn_labels` 90-day label is "no purchase or payment for 90 days after observation" (howto/churn-label-90d, 2026-01-12, superseding the 60-day label). The 2026-09-03 dataset note says the table is built by the retention-labels job from `cards.txn_daily` and maintained by data-eng-cards, but the 90-day note says Tomás Rivera's team backfilled it from 2024-01. A March 2026 correction (churn-includes-dormant) describes the table as closure or six months' dormancy, which conflicts with the 90-day definition; I could not resolve this from the notes.
Sources: memory/howto/churn-label-90d.md, memory/churn-2026/ds-churn-labels.md, memory/corrections/churn-includes-dormant.md