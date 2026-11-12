## Q1
The current monthly churn-xgb retrain uses the latest 9 observation months of `cards.churn_labels` (decision 2026-10-30, Sam Lee with retention). churn-xgb-v3 was fit on 2025-01 to 2025-09 observation months.
Sources: memory/churn-2026/dec-retrain-cadence.md, memory/churn-2026/churn-xgb-v3.md

## Q2
churn-xgb-v2 and churn-xgb-v3 both depend on feat-utilization-v1. The 2026-10-29 check found all 3 `util_` columns clean (every window ends on the observation date), so feat-utilization-v1 stays unchanged in the v3 models.
Sources: memory/churn-2026/feat-utilization-check.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md

## Q3
exp-017 (run 2026-10-28, holdout-2025q4, n=1.2M) confirmed the leak: removing post-period days from the velocity window dropped AUC from 0.81 to 0.74 and recall@10 to 0.41. The leak was written up as a finding on 2026-10-29, and velocity was rebuilt as v3 on 2026-10-30.
Sources: memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/log/2026-10-28.md, memory/churn-2026/dec-velocity-v3.md

## Q4
holdout-2025q4 in churn-2026 is 1.2M accounts with Oct–Dec 2025 observation dates: a random 30% of accounts, stratified by tenure band, never used for training. It was frozen on 2026-09-04. Memory conflicts here: a howto note says holdout-2025q4 was frozen 2026-01-19 with 412,600 rows, and a different app-engagement set of the same name has 610,000 accounts, so the 2026-09-04 churn-2026 freeze is the one used for churn.
Sources: memory/churn-2026/ds-holdout-2025q4.md, memory/howto/eval-set-freeze-date.md, memory/app-engagement/ds-ae-holdout.md

## Q5
The logistic baseline (exp-011, 2026-09-15) reached AUC 0.71 and recall@10 0.29 on holdout-2025q4, with n=1.2M and 14 account-level features (no velocity or utilization).
Sources: memory/churn-2026/exp-011-baseline.md, memory/churn-2026/exp-014.md

## Q6
recall@10 is the business metric: retention can call 10% of the book each month, so the question is how many 90-day churners land in that top 10%. AUC is reported alongside but decisions use recall@10.
Sources: memory/churn-2026/metric-recall-at-10.md

## Q7
The current velocity version is feat-velocity-v3 (decision 2026-10-30, owner Sam Lee). Its window is the 30 days before the observation date only, plus the ratio to the prior 90-day average. v2 used 30 days around the observation date, so its window reached past the observation date, which is the source of the leak.
Sources: memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/dec-velocity-v3.md

## Q8
feat-velocity-v3 reads from `cards.txn_daily` and is used by churn-xgb-v3, which replaced churn-xgb-v2 in the nightly scoring job.
Sources: memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/churn-xgb-v3.md

## Q9
The 2026-10-26 leak review started from the exp-014 velocity columns, and the same day the team asked data-eng-cards about short September partitions. That turned out to be a Sept-2025 gap in `cards.txn_daily`, backfilled and fixed on 2026-10-27 (ticket DE-4411); v2 numbers computed before 10-27 used about 6% fewer September transactions.
Sources: memory/log/2026-10-26.md, memory/churn-2026/txn-backfill.md

## Q10
The current churn label in `cards.churn_labels` is a 90-day window: no purchase or payment in the 90 days after observation (howto dated 2026-01-12, reaffirmed by the 2026-09-03 dataset note). It is built by the retention-labels job and maintained by data-eng-cards; Tomás Rivera's team did the backfill from 2024-01. Conflict: a later correction (2026-03-18) says the table was rebuilt on closure OR 6 months of no purchase or payment, and it is not marked superseded.
Sources: memory/howto/churn-label-90d.md, memory/churn-2026/ds-churn-labels.md, memory/corrections/churn-includes-dormant.md