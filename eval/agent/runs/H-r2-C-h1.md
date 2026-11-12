## Q1
The monthly churn-xgb retrain uses the latest 9 observation months of `cards.churn_labels`, per the 2026-10-30 decision with retention (Sam Lee). The v3 model itself was trained on the 2025-01 to 2025-09 observation months.
Sources: memory/churn-2026/dec-retrain-cadence.md, memory/churn-2026/churn-xgb-v3.md

## Q2
feat-utilization-v1 is used by churn-xgb-v2 and churn-xgb-v3. On 2026-10-29 all 3 `util_` columns were checked for the velocity leak and found clean: every window ends on the observation date, so the feature is kept unchanged in the v3 models.
Sources: memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/feat-utilization-check.md, memory/log/2026-10-29.md

## Q3
The exp-017 leak check (2026-10-28) removed post-period days from the velocity window, and AUC fell from 0.81 to 0.74 with recall@10 at 0.41. `vel_ratio_30_90` dropped from first to ninth in gain importance, which led to the post-period-leak finding and the decision to rebuild velocity as v3.
Sources: memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md

## Q4
In churn-2026, holdout-2025q4 is a random 30% of accounts, stratified by tenure band, with 1.2M accounts having Oct to Dec 2025 observation dates and never used for training. It was frozen on 2026-09-04 by `nb/make_holdout.ipynb`. A different project's note (app-engagement) and a generic rule note give other figures (412,600 rows, frozen 2026-01-19), so the notes conflict on this.
Sources: memory/churn-2026/ds-holdout-2025q4.md, memory/howto/eval-set-freeze-date.md

## Q5
The logistic baseline (exp-011) reached AUC 0.71 and recall@10 0.29 on holdout-2025q4, with n = 1.2M and 14 account-level features (no velocity or utilization).
Sources: memory/churn-2026/exp-011-baseline.md

## Q6
Retention can call 10% of the book each month, so the business metric is the share of 90-day churners caught in the top 10% of scores. AUC is reported alongside, but decisions use recall@10.
Sources: memory/churn-2026/metric-recall-at-10.md

## Q7
The current velocity version is v3 (feat-velocity-v3). Its window is the 30 days before the observation date, plus the ratio to the prior 90-day average. v2 used a 30-day window "around" the observation date, which let post-period days leak in.
Sources: memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/leak-hypothesis.md

## Q8
feat-velocity-v3 reads from `cards.txn_daily`, and churn-xgb-v3 is the model that uses it. It replaced feat-velocity-v2 under the 2026-10-30 decision, and Sam Lee owns it.
Sources: memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-velocity-v3.md

## Q9
The 2026-10-26 leak review started from the exp-014 velocity columns. Its September data question (short September partitions) was raised with data-eng-cards and ended in the txn backfill: the Sept 2025 backfill finished 2026-10-27 (DE-4411), and v2 numbers computed before then used about 6% fewer September transactions.
Sources: memory/log/2026-10-26.md, memory/churn-2026/txn-backfill.md, memory/churn-2026/ds-txn-2025q4.md

## Q10
The current 90-day churn label in `cards.churn_labels` marks an account with no purchase and no payment for 90 days after the observation date. It is built by the retention-labels job and maintained by data-eng-cards, though a rule note says Tomás Rivera's team backfilled the table from 2024-01. A 2026-03 correction note describes a 6-month dormancy definition, which conflicts with the 90-day rule.
Sources: memory/howto/churn-label-90d.md, memory/churn-2026/ds-churn-labels.md, memory/corrections/churn-includes-dormant.md