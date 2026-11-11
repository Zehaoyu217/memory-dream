## Q1
The current monthly churn-xgb retrain (churn-xgb-v3, per the 2026-10-30 retrain decision) uses the latest 9 observation months of `cards.churn_labels`, which is 2025-01 to 2025-09 for the current run.
Sources: memory/churn-2026/dec-retrain-cadence.md, memory/churn-2026/churn-xgb-v3.md

## Q2
churn-xgb-v2 and churn-xgb-v3 both depend on feat-utilization-v1. The 2026-10-29 check found all 3 `util_` columns clean (every window ends on the observation date, no post-period days), so feat-utilization-v1 stays unchanged in the v3 models.
Sources: memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/feat-utilization-check.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/churn-xgb-v2.md

## Q3
The exp-017 leak check (2026-10-28) rebuilt the velocity window to end on the observation date and re-scored holdout-2025q4: AUC fell from 0.81 to 0.74 and recall@10 to 0.41, with `vel_ratio_30_90` dropping from first to ninth in gain importance. This confirmed the post-period leak, which led to the v3 velocity rebuild.
Sources: memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/dec-velocity-v3.md

## Q4
holdout-2025q4 is a random 30% of accounts, stratified by tenure band, covering 1.2M accounts with Oct–Dec 2025 observation dates, never used for training; the churn-2026 note gives a freeze date of 2026-09-04 (split script `nb/make_holdout.ipynb`). Conflict: the generic freeze-date howto says holdout-2025q4 was frozen on 2026-01-19 with 412,600 rows, and the holdout-time-based correction describes holdouts as later time periods rather than random splits, so the build and freeze date need confirming.
Sources: memory/churn-2026/ds-holdout-2025q4.md, memory/howto/eval-set-freeze-date.md, memory/corrections/holdout-time-based.md

## Q5
The logistic baseline (exp-011, logreg-baseline) reached AUC 0.71 and recall@10 0.29 on holdout-2025q4, with n=1.2M and 14 account-level features (no velocity or utilization).
Sources: memory/churn-2026/exp-011-baseline.md

## Q6
recall@10 is the business metric for churn-2026 because retention can call 10% of the book each month, so decisions are judged by the share of 90-day churners caught in the top 10% of scores. AUC is reported alongside but does not drive decisions.
Sources: memory/churn-2026/metric-recall-at-10.md, memory/churn-2026/q-churn-drivers.md

## Q7
The current velocity version is v3 (feat-velocity-v3). It counts and sums card transactions in the 30 days before the observation date plus the ratio to the prior 90-day average, so every window ends on the observation date. v2 used a 30-day window "around" the observation date, which could include post-period days inside the label window.
Sources: memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/leak-hypothesis.md

## Q8
feat-velocity-v3 reads from `cards.txn_daily` and is used by churn-xgb-v3, which replaced churn-xgb-v2 in the nightly scoring job.
Sources: memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-velocity-v3.md

## Q9
The 2026-10-26 leak review started from the exp-014 velocity columns, and the question about short September partitions went to data-eng-cards. That ended in the Sept-2025 backfill of `cards.txn_daily` finishing on 2026-10-27 (ticket DE-4411), with row counts now within 0.1% of the ledger; v2 numbers computed before 10-27 used about 6% fewer September transactions.
Sources: memory/log/2026-10-26.md, memory/log/2026-10-27.md, memory/churn-2026/txn-backfill.md

## Q10
The current `cards.churn_labels` flag is a 90-day window: no purchase or payment in the 90 days after the observation date. It is built by the retention-labels job from `cards.txn_daily` and maintained by data-eng-cards. Conflict: the 2026-03-18 correction defines churn as closure or six months of dormancy, and the glossary still defines churn as closure, so the label definition should be confirmed.
Sources: memory/churn-2026/ds-churn-labels.md, memory/howto/churn-label-90d.md, memory/corrections/churn-includes-dormant.md, memory/glossary/churn.md