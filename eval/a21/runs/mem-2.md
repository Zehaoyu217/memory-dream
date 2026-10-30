## Q1
feat-velocity-v2 (2026-09-10) is 6 `vel_` columns: the count and sum of card transactions in the 30 days *around* the observation date, plus their ratio to the 90-day average. It is built on `cards.txn_daily` (`features/velocity_v2.py`). It drove exp-014's lift (AUC 0.71→0.81, mostly from `vel_ratio_30_90`) and fed churn-xgb-v2, but it leaked the target: its windows ran past the observation date, and removing those post-period days drops AUC 0.81→0.74 (holdout-2025q4, n=1.2M, 2026-10-29). It was retired on 2026-10-30 (owner Sam Lee) and replaced by feat-velocity-v3, which uses only the 30 days before the observation date; v2 numbers computed before 2026-10-27 also used about 6% fewer Sept-2025 transactions because of the backfill gap.
Sources: churn-2026/feat-velocity-v2.md, churn-2026/exp-014.md, churn-2026/post-period-leak.md, churn-2026/dec-velocity-v3.md, churn-2026/feat-velocity-v3.md, churn-2026/txn-backfill.md
Tool calls for this question: 4 (includes the 2 shared setup reads: SKILL.md and the INDEX head)
## Q2
exp-014 (2026-09-25) added velocity v2 to the baseline features in an XGBoost model (400 trees, depth 6). It lifted AUC 0.71→0.81 and recall@10 0.29→0.52 on holdout-2025q4 (n=1.2M), mostly through `vel_ratio_30_90`, and became churn-xgb-v2 (`models:/churn-xgb/2`). The 0.10 jump looked too good and raised a leak suspicion. exp-017 reran the same setup with the window ending on the observation date and got AUC 0.74, recall@10 0.41, with `vel_ratio_30_90` falling from 1st to 9th in gain. So exp-014's result was inflated by target leakage, which led to velocity v3 and churn-xgb-v3 (AUC 0.76).
Sources: churn-2026/exp-014.md, churn-2026/churn-xgb-v2.md, churn-2026/leak-hypothesis.md, churn-2026/exp-017-leak-check.md, churn-2026/post-period-leak.md
Tool calls for this question: 2
## Q3
Direct dependents of `cards.txn_daily`:
- the ds-txn-2025q4 snapshot (2.3B rows)
- `cards.churn_labels`, built from it by the retention-labels job
- feat-velocity-v2 (retired), feat-velocity-v3 and feat-utilization-v1 (`balance`, `credit_limit`)

Further downstream, through those features and labels: churn-xgb-v2, churn-xgb-v3 and logreg-baseline. By inference the nightly `cards.churn_scores` and the `offers.tier_matrix` risk tiers depend on it too. txn-backfill notes that velocity numbers computed before 2026-10-27 were hit by the Sept-2025 gap.
Sources: churn-2026/ds-txn-2025q4.md, churn-2026/ds-churn-labels.md, churn-2026/feat-velocity-v2.md, churn-2026/feat-velocity-v3.md, churn-2026/feat-utilization-v1.md, churn-2026/churn-xgb-v2.md, churn-2026/churn-xgb-v3.md, churn-2026/exp-011-baseline.md, churn-2026/txn-backfill.md
Tool calls for this question: 2
## Q4
The production model is churn-xgb-v3 (`models:/churn-xgb/3`). It was registered on 2026-10-30, when the nightly scoring job switched to it from churn-xgb-v2. It is XGBoost on feat-velocity-v3 plus feat-utilization-v1, trained on `cards.churn_labels` for observation months 2025-01 to 2025-09. On holdout-2025q4 (n=1.2M) it scores AUC 0.76 and recall@10 0.43 with no leakage, against 0.71 / 0.29 for the logistic baseline. Recall@10 holds across the Oct/Nov/Dec-2025 cohorts (0.45 / 0.43 / 0.40), and the model is retrained monthly on the latest 9 observation months.
Sources: churn-2026/churn-xgb-v3.md, churn-2026/exp-019-recall.md, churn-2026/dec-retrain-cadence.md, churn-2026/exp-011-baseline.md, log/2026-10-30.md
Tool calls for this question: 2
## Q5
The drop is the removal of a target leak, not a real loss of skill. v2's velocity features used a window "around" the observation date that included days inside the 90-day label window. exp-017 showed that removing just those post-period days takes AUC from 0.81 to 0.74 (recall@10 0.41). v3 rebuilt velocity from pre-observation days only and gets AUC 0.76 / recall@10 0.43, which the notes call "the honest number". The notes do not explain the 0.74 vs 0.76 gap; exp-017 used exp-014's feature set, while v3 also carries the utilization features, which were checked and found clean.
Sources: churn-2026/leak-hypothesis.md, churn-2026/exp-017-leak-check.md, churn-2026/post-period-leak.md, churn-2026/dec-velocity-v3.md, churn-2026/churn-xgb-v3.md, churn-2026/exp-019-recall.md
Tool calls for this question: 1
## Q6
data-eng-cards owns `cards.txn_daily` (and also maintains `cards.churn_labels`). There was a data-quality issue: the September-2025 partitions were about 6% short. The backfill finished on 2026-10-27 (ticket DE-4411) and row counts now match the ledger within 0.1%, but any v2 velocity numbers computed before then used about 6% fewer September transactions. The 2026-10-30 log says a backfill is now running for the October partitions, and no note yet says what it fixes.
Sources: churn-2026/ds-txn-2025q4.md, churn-2026/txn-backfill.md, churn-2026/ds-churn-labels.md, log/2026-10-26.md, log/2026-10-30.md
Tool calls for this question: 1
## Q7
The cuts are at churn scores 0.20 and 0.50: ≥0.50 gets a call (3.8% of the book), 0.20–0.50 gets an email (11.6%), and below 0.20 gets nothing. They were decided on 2026-10-08 with retention (Maya Ortiz) against a budget of 4% calls and 12% emails, and are written nightly to `offers.tier_matrix`. They were set on churn-xgb-v2 scores, and v3's scores are less extreme, so at the current cuts the call tier would shrink to about 2.9% of the book. Whether to recalibrate is still open (q-recalibrate-tiers, 2026-10-30), and the 0.20 / 0.50 cuts stay in place until that is answered.
Sources: churn-2026/dec-risk-tiers.md, churn-2026/q-tier-cutoffs.md, churn-2026/q-recalibrate-tiers.md, churn-2026/dec-retrain-cadence.md
Tool calls for this question: 1
## Q8
It is poor on new accounts, but this was only measured for the leak-inflated churn-xgb-v2; memory has no tenure split for the current churn-xgb-v3. On holdout-2025q4, accounts under 6 months' tenure (n=168k, 14%) scored AUC 0.69 and recall@10 0.31, against AUC 0.83 for tenure ≥6 months (n=1.03M) (2026-10-10). New accounts are 14% of the book but 21% of churners and have too little history for velocity or utilization to mean much. The options noted are a tenure-specific model or routing them to onboarding (owner Priya Nair).
Sources: churn-2026/exp-015-tenure.md, churn-2026/finding-new-accounts.md
Tool calls for this question: 1
## Q9
No. All 3 `util_` columns of feat-utilization-v1 were checked against the leak pattern on 2026-10-29: every window ends on the observation date and none includes post-period days. The features were kept unchanged in the v3 models (churn-xgb-v3).
Sources: churn-2026/feat-utilization-check.md, churn-2026/feat-utilization-v1.md, log/2026-10-29.md
Tool calls for this question: 1
## Q10
Three models are explicitly trained on `cards.churn_labels`:
- logreg-baseline (exp-011, 14 account-level features, AUC 0.71)
- churn-xgb-v2 (observation months 2025-01 to 2025-09)
- churn-xgb-v3 (same months, now retrained monthly on the latest 9 observation months)

The exp-014 and exp-017 XGBoost runs presumably used it too, but no note says so. The churn base rate is 6.8% on the 2025 book (n=4.1M accounts, 2026-09-03). A label means no card spend in the 90 days after a month-end observation date.
Sources: churn-2026/ds-churn-labels.md, churn-2026/exp-011-baseline.md, churn-2026/churn-xgb-v2.md, churn-2026/churn-xgb-v3.md, churn-2026/dec-retrain-cadence.md, churn-2026/q-churn-drivers.md
Tool calls for this question: 1