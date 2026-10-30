## Q1
feat-velocity-v2 was the 30-day transaction velocity feature set: count and sum of card transactions in the 30 days "around" the observation date, plus their ratio to the 90-day average. It has 6 `vel_` columns, is built on `cards.txn_daily`, and the code is `features/velocity_v2.py` (2026-09-10). It drove exp-014's lift (AUC 0.71→0.81, mostly from `vel_ratio_30_90`), but the window took in days after the observation date, which is a target leak (AUC drops to 0.74 without them, holdout-2025q4, n=1.2M). On 2026-10-30 it was retired and superseded by feat-velocity-v3 (owner Sam Lee). Also, any v2 numbers computed before 2026-10-27 used about 6% fewer September 2025 transactions, because of the txn gap.
Sources: churn-2026/feat-velocity-v2.md, churn-2026/exp-014.md, churn-2026/post-period-leak.md, churn-2026/dec-velocity-v3.md, churn-2026/feat-velocity-v3.md, churn-2026/txn-backfill.md
Tool calls for this question: 4 (2 of them one-time setup: SKILL.md + INDEX head)
## Q2
exp-014 (2026-09-25) was XGBoost (400 trees, depth 6) with the velocity features added to the baseline set. It reported AUC 0.81 and recall@10 0.52 on holdout-2025q4 (n=1.2M), against the baseline's 0.71 / 0.29, and most of the lift came from `vel_ratio_30_90`. It became churn-xgb-v2 (`models:/churn-xgb/2`), but the jump looked too good and prompted the leak hypothesis. exp-017 (the same setup with the window ending on the observation date) fell to AUC 0.74 / recall@10 0.41, and `vel_ratio_30_90` dropped from 1st to 9th in gain importance. The result was the post-period-leak finding, velocity v3, and churn-xgb-v3, which superseded v2.
Sources: churn-2026/exp-014.md, churn-2026/churn-xgb-v2.md, churn-2026/leak-hypothesis.md, churn-2026/exp-017-leak-check.md, churn-2026/post-period-leak.md, churn-2026/churn-xgb-v3.md, log/2026-10-26.md
Tool calls for this question: 5
## Q3
These read `cards.txn_daily` directly: the ds-txn-2025q4 snapshot (2.3B rows, `sql/txn_snapshot.sql`), `cards.churn_labels` (built from it by the retention-labels job), feat-velocity-v2 (superseded), feat-velocity-v3, and feat-utilization-v1 (`balance` / `credit_limit`). Downstream of those, the models churn-xgb-v2, churn-xgb-v3 and logreg-baseline (via churn_labels) depend on it, along with the experiments built on them. The nightly scores (`cards.churn_scores`) and risk-tier output (`offers.tier_matrix`) depend on it indirectly through the models.
Sources: churn-2026/ds-txn-2025q4.md, churn-2026/ds-churn-labels.md, churn-2026/feat-velocity-v2.md, churn-2026/feat-velocity-v3.md, churn-2026/feat-utilization-v1.md, churn-2026/churn-xgb-v2.md, churn-2026/churn-xgb-v3.md, churn-2026/exp-011-baseline.md, churn-2026/dec-risk-tiers.md
Tool calls for this question: 3
## Q4
The production model is churn-xgb-v3 (`models:/churn-xgb/3`). It was registered on 2026-10-30, the nightly scoring job switched to it the same day, and it replaces churn-xgb-v2. It uses feat-velocity-v3 + feat-utilization-v1 and is trained on `cards.churn_labels` for observation months 2025-01 to 2025-09. On holdout-2025q4 (n=1.2M) it scores AUC 0.76 and recall@10 0.43 with no leakage, against the logistic baseline's 0.71 / 0.29. Recall@10 holds by monthly cohort at 0.45 / 0.43 / 0.40 (Oct/Nov/Dec 2025), and the plan is to retrain it monthly on the latest 9 observation months.
Sources: churn-2026/churn-xgb-v3.md, churn-2026/exp-019-recall.md, churn-2026/dec-retrain-cadence.md, churn-2026/exp-011-baseline.md, log/2026-10-30.md
Tool calls for this question: 2
## Q5
v2's 0.81 was inflated by a target leak. feat-velocity-v2 aggregated a window "around" the observation date, which included post-period days inside the 90-day label window. Removing those days in exp-017 (same setup as exp-014) dropped AUC to 0.74 and recall@10 to 0.41, and `vel_ratio_30_90` fell from 1st to 9th in importance. churn-xgb-v3 rebuilds velocity from pre-observation days only (v3) and keeps the utilization features, which were checked and found clean; it lands at the honest AUC 0.76 / recall@10 0.43. The notes do not explain the 0.74→0.76 gap between exp-017 and v3.
Sources: churn-2026/leak-hypothesis.md, churn-2026/exp-017-leak-check.md, churn-2026/post-period-leak.md, churn-2026/dec-velocity-v3.md, churn-2026/churn-xgb-v3.md, churn-2026/exp-019-recall.md
Tool calls for this question: 1
## Q6
`cards.txn_daily` is owned by data-eng-cards, who also maintain `cards.churn_labels`. There was a data-quality issue: the September 2025 partitions were about 6% short. Backfill ticket DE-4411 finished on 2026-10-27, and row counts now match the ledger within 0.1%. Velocity v2 numbers computed before 10-27 therefore used about 6% fewer September transactions. A log entry on 2026-10-30 says a backfill for the October partitions was running, and no outcome is recorded.
Sources: churn-2026/ds-txn-2025q4.md, churn-2026/txn-backfill.md, log/2026-10-26.md, log/2026-10-27.md, log/2026-10-30.md
Tool calls for this question: 2
## Q7
The cuts are at churn score 0.20 and 0.50: ≥ 0.50 gets a call (3.8% of the book), 0.20–0.50 gets an email (11.6%), and below 0.20 gets no action. They were decided on 2026-10-08 with retention (Maya Ortiz) against a budget of 4% calls and 12% emails, and are written nightly to `offers.tier_matrix`. They were set on churn-xgb-v2 scores. They remain in force by the 2026-10-30 retrain decision, but whether they are still valid is an open question (q-recalibrate-tiers): v3 scores are less extreme, so the call tier would shrink from 3.8% to about 2.9% of the book at the current cuts.
Sources: churn-2026/dec-risk-tiers.md, churn-2026/q-tier-cutoffs.md, churn-2026/q-recalibrate-tiers.md, churn-2026/dec-retrain-cadence.md
Tool calls for this question: 2
## Q8
The model ranks new accounts poorly. In exp-015 (2026-10-10, holdout-2025q4), accounts under 6 months tenure (n=168k, 14%) scored AUC 0.69 and recall@10 0.31, against AUC 0.83 for tenure ≥ 6 months (n=1.03M). New accounts are 14% of the book but 21% of churners, and they have too little history for velocity or utilization to mean much. The options on the table are a tenure-specific model or routing them to the onboarding team (owner Priya Nair), and no decision is recorded. These numbers are for the leaky churn-xgb-v2; no tenure breakdown for v3 is recorded.
Sources: churn-2026/exp-015-tenure.md, churn-2026/finding-new-accounts.md
Tool calls for this question: 2
## Q9
No. On 2026-10-29 all 3 `util_` columns of feat-utilization-v1 were checked against the leak pattern. Every window ends on the observation date and there are no post-period days, so feat-utilization-v1 was kept unchanged in churn-xgb-v3.
Sources: churn-2026/feat-utilization-check.md, churn-2026/feat-utilization-v1.md, churn-2026/churn-xgb-v3.md
Tool calls for this question: 1
## Q10
Three models are trained on `cards.churn_labels`. logreg-baseline (exp-011) scored AUC 0.71 / recall@10 0.29. churn-xgb-v2 (observation months 2025-01 to 2025-09) is superseded. churn-xgb-v3 (2025-01 to 2025-09) will be retrained monthly on the latest 9 observation months. The churn base rate is 6.8% on the 2025 book (n=4.1M accounts, 2026-09-03), where churn means no card spend in the 90 days after a month-end observation date.
Sources: churn-2026/ds-churn-labels.md, churn-2026/exp-011-baseline.md, churn-2026/churn-xgb-v2.md, churn-2026/churn-xgb-v3.md, churn-2026/dec-retrain-cadence.md, churn-2026/q-churn-drivers.md
Tool calls for this question: 2