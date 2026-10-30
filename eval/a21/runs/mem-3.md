## Q1
feat-velocity-v2 is the old 30-day transaction velocity feature: count and sum of card transactions in the 30 days "around" the observation date, plus their ratio to the 90-day average. It has 6 `vel_` columns, lives in `features/velocity_v2.py` and is built on `cards.txn_daily`. It fed exp-014 and churn-xgb-v2 (AUC 0.81, recall@10 0.52 on holdout-2025q4, with most of the lift from `vel_ratio_30_90`). The window turned out to include post-observation days, which leaks the target (AUC 0.81→0.74 without them), so on 2026-10-30 it was retired and superseded by feat-velocity-v3 (decision owner Sam Lee).
Sources: memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/exp-014.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/feat-velocity-v3.md
Tool calls for this question: 2
## Q2
exp-014 (2026-09-25) added the velocity v2 features to the baseline in an XGBoost model (400 trees, depth 6). On holdout-2025q4 (n=1.2M) it lifted AUC 0.71→0.81 and recall@10 0.29→0.52, mostly via `vel_ratio_30_90`. It became churn-xgb-v2 (`models:/churn-xgb/2`), but the 0.10 AUC jump raised a leakage suspicion. exp-017 confirmed it: with post-period days removed, AUC fell to 0.74 and recall@10 to 0.41. Velocity was then rebuilt as v3 and churn-xgb-v2 was superseded by churn-xgb-v3 (AUC 0.76).
Sources: memory/churn-2026/exp-014.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/churn-xgb-v3.md
Tool calls for this question: 2
## Q3
These depend on it directly:
- the ds-txn-2025q4 snapshot (2.3B rows, 2025, query `sql/txn_snapshot.sql`)
- feat-velocity-v2 (retired), feat-velocity-v3 and feat-utilization-v1 (`balance`, `credit_limit`)
- `cards.churn_labels`, which the retention-labels job builds from it

Downstream, churn-xgb-v2 and churn-xgb-v3 depend on it through those features and the labels, and logreg-baseline through the labels. That carries through to the nightly `cards.churn_scores` and the `offers.tier_matrix` risk tiers.
Sources: memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/ds-churn-labels.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-011-baseline.md, memory/churn-2026/dec-risk-tiers.md
Tool calls for this question: 2
## Q4
The production model is churn-xgb-v3 (`models:/churn-xgb/3`), built on feat-velocity-v3 and feat-utilization-v1 and trained on `cards.churn_labels` observation months 2025-01 to 2025-09. It replaced v2 in the nightly scoring job on 2026-10-30. On holdout-2025q4 (n=1.2M) it scores AUC 0.76 and recall@10 0.43, with no leakage. By month the recall@10 is Oct 0.45, Nov 0.43, Dec 0.40, against the logistic baseline's AUC 0.71 / recall@10 0.29. It is to be retrained monthly on the latest 9 observation months.
Sources: memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md, memory/churn-2026/dec-retrain-cadence.md, memory/log/2026-10-30.md, memory/churn-2026/exp-011-baseline.md
Tool calls for this question: 2
## Q5
The 0.81 was inflated by target leakage, so this is not a real regression. churn-xgb-v2's velocity v2 windows ran past the observation date into the 90-day label window. exp-017 removed the post-period days and AUC fell 0.81→0.74 (recall@10 0.52→0.41), with `vel_ratio_30_90` dropping from 1st to 9th in gain importance. v3 keeps the same XGBoost settings, training months and holdout, but velocity windows now end on the observation date (utilization was already clean). Its 0.76 / 0.43 is described as "the honest number." The notes do not explain why v3 (0.76) lands slightly above the exp-017 check (0.74).
Sources: memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md, memory/churn-2026/feat-utilization-check.md
Tool calls for this question: 2
## Q6
data-eng-cards owns `cards.txn_daily`; it also maintains `cards.churn_labels`. There was a quality issue: September 2025 partitions were short by about 6%. The backfill finished 2026-10-27 (ticket DE-4411), and row counts now match the ledger within 0.1%. Any v2 numbers computed before 10-27 used about 6% fewer September transactions. A 2026-10-30 scratch log entry says a backfill is now running for October partitions, with no finding note yet; this could matter because holdout-2025q4 covers Oct–Dec 2025.
Sources: memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/txn-backfill.md, memory/churn-2026/ds-churn-labels.md, memory/log/2026-10-30.md
Tool calls for this question: 1
## Q7
The cuts are at churn score 0.20 and 0.50, set 2026-10-08 with retention (Maya Ortiz) against a budget of calls for 4% and emails for 12% of the book. Score ≥ 0.50 gets a call (3.8% of the book), 0.20–0.50 gets an email (11.6%), and below 0.20 gets no action; results are written nightly to `offers.tier_matrix`. They remain in force (dec-retrain-cadence, 10-30) until q-recalibrate-tiers is answered. They were set on the leaky churn-xgb-v2 scores, though: v3 scores are less extreme, so the call tier would shrink to about 2.9% at the current cuts. Whether they are still valid is an open question as of 2026-10-30.
Sources: memory/churn-2026/q-tier-cutoffs.md, memory/churn-2026/dec-risk-tiers.md, memory/churn-2026/q-recalibrate-tiers.md, memory/churn-2026/dec-retrain-cadence.md
Tool calls for this question: 1
## Q8
Poorly. On holdout-2025q4, accounts under 6 months tenure (n=168k, 14%) got AUC 0.69 and recall@10 0.31, against AUC 0.83 for tenure ≥ 6 months (n=1.03M). That measurement was on the now-superseded, leaky churn-xgb-v2, and no tenure split for churn-xgb-v3 is recorded. New accounts are 14% of the book but 21% of churners and have too little history for velocity or utilization to mean much. The options on the table are a tenure-specific model or routing them to the onboarding team (owner Priya Nair).
Sources: memory/churn-2026/exp-015-tenure.md, memory/churn-2026/finding-new-accounts.md
Tool calls for this question: 1
## Q9
No. All 3 `util_` columns of feat-utilization-v1 were checked against the post-period leak pattern on 2026-10-29: every window (balance / credit limit over 1, 3 and 6 months) ends on the observation date. They are kept unchanged in churn-xgb-v3.
Sources: memory/churn-2026/feat-utilization-check.md, memory/churn-2026/feat-utilization-v1.md, memory/log/2026-10-29.md
Tool calls for this question: 1
## Q10
Three models are trained on `cards.churn_labels`:
- logreg-baseline (exp-011, 14 account-level features, AUC 0.71)
- churn-xgb-v2 (2025-01 to 2025-09, AUC 0.81 leaky, superseded)
- churn-xgb-v3 (same months, AUC 0.76, in production, retrained monthly on the latest 9 months)

The churn base rate is 6.8% on the 2025 book (n=4.1M accounts, 2026-09-03). The labels are a 90-day no-spend flag after month-end observation dates.
Sources: memory/churn-2026/ds-churn-labels.md, memory/churn-2026/exp-011-baseline.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-retrain-cadence.md, memory/churn-2026/q-churn-drivers.md
Tool calls for this question: 2