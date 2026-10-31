## Q1
feat-velocity-v2 is a set of 6 `vel_` columns (`features/velocity_v2.py`, built on `cards.txn_daily`): the count and sum of card transactions in the 30 days "around" the observation date, plus their ratio to the 90-day average. It is SUPERSEDED. Its window reached past the observation date into the label window, which leaked the target: AUC went 0.81→0.74 once those days were removed. On 2026-10-30 it was replaced by feat-velocity-v3, whose windows end on the observation date (owner Sam Lee). Separately, any v2 numbers computed before 2026-10-27 used about 6% fewer September-2025 transactions, because of the txn table gap.
Sources: memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/txn-backfill.md
## Q2
exp-014 (XGBoost, 400 trees, depth 6, plus velocity v2) lifted the baseline from AUC 0.71→0.81 and recall@10 from 0.29→0.52 on holdout-2025q4 (n=1.2M), mostly through `vel_ratio_30_90`. It was registered as churn-xgb-v2 (`models:/churn-xgb/2`). The jump was too good, which led to a leak check (exp-017). With the velocity window ending on the observation date, AUC fell to 0.74 and recall@10 to 0.41, and `vel_ratio_30_90` dropped from 1st to 9th in gain importance. That confirmed the post-period leak, and the result was velocity v3 and churn-xgb-v3 (AUC 0.76, recall@10 0.43).
Sources: memory/churn-2026/exp-014.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/churn-xgb-v3.md
## Q3
Direct dependents of `cards.txn_daily`:
- the features feat-velocity-v2, feat-velocity-v3 and feat-utilization-v1 (`balance` and `credit_limit`)
- `cards.churn_labels`, built from it by the retention-labels job
- the ds-txn-2025q4 snapshot (`sql/txn_snapshot.sql`; 2.3B rows, 2025)
- the churn-2026 card-churn-drivers project

Indirectly, through those features and labels, it feeds churn-xgb-v2, churn-xgb-v3 and logreg-baseline, and from there `cards.churn_scores` and `offers.tier_matrix`.
Sources: memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/ds-churn-labels.md, memory/churn-2026/q-churn-drivers.md
## Q4
The production model is churn-xgb-v3 (`models:/churn-xgb/3`). It uses feat-velocity-v3 and feat-utilization-v1 and replaced v2 in the nightly scoring job on 2026-10-30. On holdout-2025q4 (n=1.2M) it scores AUC 0.76 and recall@10 0.43, with no leakage. Recall@10 holds steady across the Oct/Nov/Dec 2025 cohorts at 0.45 / 0.43 / 0.40; the notes call 0.43 the honest number and v2's 0.52 the leak. It is retrained monthly on the latest 9 observation months of `cards.churn_labels`.
Sources: memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md, memory/churn-2026/dec-retrain-cadence.md
## Q5
churn-xgb-v2's velocity features (v2) used a window "around" the observation date, so they included days inside the 90-day label window. That target leak inflated AUC to 0.81 and recall@10 to 0.52. churn-xgb-v3 uses the same XGBoost settings but velocity v3, where every window ends on the observation date; the utilization features stayed unchanged because they were checked and found clean. Honest performance is AUC 0.76 and recall@10 0.43. The earlier leak check (exp-017) got 0.74, and the notes do not explain the 0.02 gap between the two.
Sources: memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/feat-utilization-check.md
## Q6
data-eng-cards owns it. Yes, there was a data-quality issue: the September 2025 partitions were short by about 6%. The backfill finished on 2026-10-27 (ticket DE-4411), and row counts now match the ledger within 0.1%. Velocity v2 numbers computed before 10-27 therefore used about 6% fewer September transactions. The post-period leak is a separate problem in how the features were built, not a data-quality issue in the table.
Sources: memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/txn-backfill.md, memory/churn-2026/ds-churn-labels.md
## Q7
The cuts were decided on 2026-10-08 with retention (Maya Ortiz) and are written nightly to `offers.tier_matrix`. They were set against a budget of 4% calls and 12% emails:

| Churn score | Action | Share of book (v2 scores) |
|---|---|---|
| ≥ 0.50 | call | 3.8% |
| 0.20 to 0.50 | email | 11.6% |
| below 0.20 | no action | – |

They were calibrated on churn-xgb-v2 scores and are not yet validated for v3. v3 scores are less extreme, so at the current cuts the call tier shrinks to about 2.9% of the book. Whether to recalibrate is an open question (q-recalibrate-tiers, 2026-10-30), and the cuts stay in force until it is answered.
Sources: memory/churn-2026/dec-risk-tiers.md, memory/churn-2026/q-tier-cutoffs.md, memory/churn-2026/q-recalibrate-tiers.md, memory/churn-2026/dec-retrain-cadence.md
## Q8
Poorly. On churn-xgb-v2 (exp-015, holdout-2025q4), new accounts under 6 months tenure (n=168k) scored AUC 0.69 and recall@10 0.31, against AUC 0.83 for tenure ≥ 6 months (n=1.03M). New accounts are 14% of the book but 21% of churners, and they have too little history for velocity or utilization to mean much. The options on the table are a tenure-specific model or routing them to onboarding (owner Priya Nair). The split was measured on the leaky v2; there is no tenure breakdown for v3 yet.
Sources: memory/churn-2026/exp-015-tenure.md, memory/churn-2026/finding-new-accounts.md
## Q9
No. All 3 `util_` columns of feat-utilization-v1 were checked against the leak pattern on 2026-10-29, and every window ends on the observation date, with no post-period days. They are kept unchanged in the v3 models.
Sources: memory/churn-2026/feat-utilization-check.md, memory/churn-2026/feat-utilization-v1.md, memory/log/2026-10-29.md
## Q10
Three models are trained on `cards.churn_labels`:
- logreg-baseline (exp-011; 14 account-level features; AUC 0.71, recall@10 0.29)
- churn-xgb-v2 (superseded)
- churn-xgb-v3 (current)

v2 and v3 were fit on the 2025-01 to 2025-09 observation months. The churn base rate is 6.8% on the 2025 book (n=4.1M accounts, as of 2026-09-03). The label is a 90-day no-spend flag after month-end observation dates.
Sources: memory/churn-2026/ds-churn-labels.md, memory/churn-2026/exp-011-baseline.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md