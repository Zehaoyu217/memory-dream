## Q1
The monthly churn-xgb retrain uses the latest 9 observation months of `cards.churn_labels`, per the 2026-10-30 decision (Sam Lee with retention). The 0.20 and 0.50 risk-tier cuts stay until q-recalibrate-tiers is answered.
Sources: churn-2026/dec-retrain-cadence.md

## Q2
feat-utilization-v1 is used by churn-xgb-v2 and churn-xgb-v3. The 2026-10-29 check found all 3 `util_` columns clean, with every window ending on the observation date and no post-period days, so feat-utilization-v1 stays unchanged in the v3 models.
Sources: churn-2026/feat-utilization-v1.md, churn-2026/feat-utilization-check.md, churn-2026/churn-xgb-v3.md, log/2026-10-29.md

## Q3
The exp-017 leak check (2026-10-28, velocity window ending on the observation date) dropped holdout-2025q4 AUC from 0.81 to 0.74 and recall@10 from 0.52 to 0.41 (n=1.2M), which confirmed the post-period leak in the v2 velocity features. It led to the 2026-10-29 post-period-leak finding and the v3 rebuild.
Sources: churn-2026/exp-017-leak-check.md, churn-2026/post-period-leak.md

## Q4
In the churn-2026 project, holdout-2025q4 is a random 30% of accounts (1.2M with Oct–Dec 2025 observation dates), stratified by tenure band, built by nb/make_holdout.ipynb, frozen 2026-09-04, and never used for training. Other notes reuse the name for different sets: a general rule note cites a 412,600-row set frozen 2026-01-19, and app-engagement uses 610,000 accounts, so check the project before quoting a figure.
Sources: churn-2026/ds-holdout-2025q4.md, howto/eval-set-freeze-date.md, app-engagement/ds-ae-holdout.md

## Q5
The logistic baseline (exp-011-baseline, fit on `cards.churn_labels` with 14 account-level features and no velocity or utilization) reached AUC 0.71 and recall@10 0.29 on holdout-2025q4, with n = 1.2M.
Sources: churn-2026/exp-011-baseline.md

## Q6
Retention can call only 10% of the book each month, so recall@10 (the share of 90-day churners caught in the top 10% of scores) matches the decision. AUC is reported alongside it, but decisions use recall@10.
Sources: churn-2026/metric-recall-at-10.md, churn-2026/q-churn-drivers.md

## Q7
The current velocity version is v3 (feat-velocity-v3): card transaction count and sum over the 30 days before the observation date, plus their ratio to the prior 90-day average. v2 used a 30-day window centred on the observation date, so it reached days after it inside the label window, which caused the leak.
Sources: churn-2026/feat-velocity-v3.md, churn-2026/feat-velocity-v2.md, churn-2026/post-period-leak.md

## Q8
feat-velocity-v3 reads `cards.txn_daily` and replaces v2. churn-xgb-v3, the current model (registered as models:/churn-xgb/3 and used in the nightly scoring), is the only model that uses it.
Sources: churn-2026/feat-velocity-v3.md, churn-2026/churn-xgb-v3.md, churn-2026/dec-velocity-v3.md

## Q9
The 2026-10-26 leak review started from the exp-014 velocity columns. Its question about short September partitions went to data-eng-cards and was resolved by the Sept-2025 backfill of `cards.txn_daily`, finished 2026-10-27 (DE-4411), after which row counts match the ledger within 0.1%. Earlier v2 numbers used about 6% fewer September transactions.
Sources: log/2026-10-26.md, churn-2026/txn-backfill.md, churn-2026/ds-txn-2025q4.md

## Q10
The 90-day label in `cards.churn_labels` flags an account with no purchase or payment for 90 days after the observation date. It is built by the retention-labels job from `cards.txn_daily` and maintained by data-eng-cards, and Tomás Rivera's team backfilled it from 2024-01. A 2026-03-18 correction defines churn as closure or six months of dormancy, which conflicts with the 90-day rule, so check which definition applies.
Sources: howto/churn-label-90d.md, churn-2026/ds-churn-labels.md, corrections/churn-includes-dormant.md