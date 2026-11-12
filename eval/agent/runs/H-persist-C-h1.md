## Q1
The current monthly churn-xgb retrain uses the latest 9 observation months of `cards.churn_labels`, per the 2026-10-30 decision (Sam Lee with retention). The deployed churn-xgb-v3 was trained on 2025-01 to 2025-09 observation months.
Sources: churn-2026/dec-retrain-cadence.md, churn-2026/churn-xgb-v3.md

## Q2
churn-xgb-v2 and churn-xgb-v3 both use feat-utilization-v1. The 2026-10-29 check found all 3 `util_` columns clean (every window ends on the observation date, no post-period days), so feat-utilization-v1 was kept unchanged in the v3 models.
Sources: churn-2026/feat-utilization-check.md, churn-2026/churn-xgb-v2.md, churn-2026/churn-xgb-v3.md

## Q3
The exp-017 leak check (2026-10-28) removed post-period days from the velocity window and got AUC 0.74 and recall@10 0.41 on holdout-2025q4, down from 0.81 for exp-014. `vel_ratio_30_90` fell from first to ninth in gain importance. That result led to the post-period-leak finding and the decision to rebuild velocity as v3 (dec-velocity-v3, 2026-10-30).
Sources: churn-2026/exp-017-leak-check.md, log/2026-10-28.md, churn-2026/post-period-leak.md, churn-2026/dec-velocity-v3.md

## Q4
In churn-2026, holdout-2025q4 is a random 30% of accounts, stratified by tenure band, with 1.2M accounts having Oct to Dec 2025 observation dates, never used for training; it was frozen on 2026-09-04. The memory conflicts on this: howto/eval-set-freeze-date.md says holdout-2025q4 was frozen on 2026-01-19 with 412,600 rows, and other projects use same-named sets of different sizes (610,000 and 380,000), so the notes do not settle which set is meant.
Sources: churn-2026/ds-holdout-2025q4.md, howto/eval-set-freeze-date.md, qa/holdout-2025q4-reextract.md

## Q5
The logistic baseline (logreg-baseline, exp-011) reached AUC 0.71 and recall@10 0.29 on holdout-2025q4, with n = 1.2M and 14 account-level features (no velocity or utilization).
Sources: churn-2026/exp-011-baseline.md

## Q6
recall@10 is the business metric for churn-2026 because retention can call 10% of the book each month, so decisions are judged by the share of 90-day churners caught in the top 10% of scores. AUC is reported alongside it but is not the decision criterion.
Sources: churn-2026/metric-recall-at-10.md

## Q7
The current velocity feature is v3 (feat-velocity-v3, from 2026-10-30): 30-day count and sum of card transactions in the 30 days before the observation date, plus their ratio to the prior 90-day average. v2 used the 30 days around the observation date, so its windows included post-period days; v3 ends every window on the observation date.
Sources: churn-2026/feat-velocity-v3.md, churn-2026/feat-velocity-v2.md, churn-2026/dec-velocity-v3.md

## Q8
feat-velocity-v3 reads from `cards.txn_daily` and replaces feat-velocity-v2. It is used by churn-xgb-v3, which replaced churn-xgb-v2 in the nightly scoring job.
Sources: churn-2026/feat-velocity-v3.md, churn-2026/churn-xgb-v3.md

## Q9
The 2026-10-26 leak review started from the velocity columns of exp-014. The September data question (short September partitions) went to data-eng-cards and was resolved by the Sept-2025 `cards.txn_daily` backfill, which finished 2026-10-27 (ticket DE-4411) and brought row counts within 0.1% of the ledger; earlier v2 numbers used about 6% fewer September transactions.
Sources: log/2026-10-26.md, churn-2026/txn-backfill.md, churn-2026/ds-txn-2025q4.md

## Q10
The 90-day churn label in `cards.churn_labels` is no purchase or payment for 90 days after the observation date. It is built by the retention-labels job from `cards.txn_daily` and maintained by data-eng-cards. Note a conflict: corrections/churn-includes-dormant.md (2026-03-18) defines churn as closure or no purchase and no payment for 6 months.
Sources: howto/churn-label-90d.md, churn-2026/ds-churn-labels.md, corrections/churn-includes-dormant.md