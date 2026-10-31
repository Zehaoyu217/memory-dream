## Q1
feat-velocity-v2 has 6 `vel_` columns built on `cards.txn_daily` (`features/velocity_v2.py`): the count and sum of card transactions in the 30 days *around* the observation date, plus their ratio to the 90-day average. It fed exp-014 and churn-xgb-v2, where it lifted AUC from 0.71 to 0.81, mostly through `vel_ratio_30_90`. That window reached past the observation date into the label window, so it leaked the target: without post-period days AUC falls to 0.74 (exp-017). On 2026-10-30 it was retired and superseded by feat-velocity-v3, which uses pre-observation days only. Also, any v2 numbers computed before 2026-10-27 used about 6% fewer September 2025 transactions. (fraud-2026 has an unrelated "velocity-v2" feature.)
Sources: memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/exp-014.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/txn-backfill.md
## Q2
exp-014 (2026-09-25) was XGBoost (400 trees, depth 6) on the baseline features plus velocity-v2. On holdout-2025q4 (n=1.2M) it scored AUC 0.81 and recall@10 0.52, against the baseline's 0.71 and 0.29, with the lift mostly from `vel_ratio_30_90`. It became churn-xgb-v2 (`models:/churn-xgb/2`). A 0.10 AUC jump from one feature group looked too good, and the leak check confirmed post-period leakage: AUC 0.74 and recall@10 0.41 once the window ends at the observation date. The honest successor, churn-xgb-v3, scores AUC 0.76 and recall@10 0.43.
Sources: memory/churn-2026/exp-014.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/churn-xgb-v3.md
## Q3
In churn-2026, these read `cards.txn_daily`:
- `cards.churn_labels` (built by the retention-labels job)
- the ds-txn-2025q4 snapshot (2.3B account-day rows)
- feat-velocity-v2 (retired), feat-velocity-v3 and feat-utilization-v1

Through those, churn-xgb-v2 and v3 depend on it, and so do the nightly `cards.churn_scores` and `offers.tier_matrix` outputs. The September 2025 gap in the table went straight into the velocity features. It is also a shared source for about 25 other projects, among them fraud-2025/2026 CNP sets, AML, credit-line-increase, CLV, churn-2025, churn-small-business, feature-store-migration (6 features), marketing uplift and merchant risk. It also feeds the weekly KPI deck (5% row-count gate) and the "active account" definition.
Sources: memory/churn-2026/ds-churn-labels.md, memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-risk-tiers.md, memory/churn-2026/txn-backfill.md, memory/feature-store-migration/ds-fsm-txn-source.md, memory/reporting/data-quality-gate.md, memory/glossary/active-account.md, memory/fraud-2026/ds-f26-cnp-txn.md, memory/aml-alerts/ds-aml-cash-txn.md
## Q4
The production model is churn-xgb-v3 (`models:/churn-xgb/3`), registered 2026-10-30, when the nightly scoring job switched over from churn-xgb-v2. It uses feat-velocity-v3 and feat-utilization-v1 with the same XGBoost settings, trained on `cards.churn_labels` for observation months 2025-01 to 2025-09. On holdout-2025q4 (n=1.2M) it scores AUC 0.76 and recall@10 0.43 with no leakage. Recall@10 holds at 0.45, 0.43 and 0.40 across the Oct, Nov and Dec 2025 cohorts. It is retrained monthly on the latest 9 observation months.
Sources: memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md, memory/churn-2026/dec-retrain-cadence.md, memory/log/2026-10-30.md, memory/churn-2025/churn-gbm-2025-v2.md
## Q5
The 0.81 was not real. feat-velocity-v2 aggregated transactions in a window around the observation date, which included days inside the 90-day label window, so the model was partly seeing the target. Ending the window at the observation date (exp-017) cut AUC from 0.81 to 0.74 and recall@10 to 0.41, and dropped `vel_ratio_30_90` from first to ninth in gain importance. churn-xgb-v3 is v2 retrained on the clean feat-velocity-v3 and reaches AUC 0.76; the utilization features were checked and ruled out as a second leak. One minor difference the notes do not blame for the drop: v2's numbers predate the September 2025 txn backfill (about 6% fewer September transactions).
Sources: memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/feat-utilization-check.md, memory/churn-2026/exp-019-recall.md, memory/churn-2026/txn-backfill.md
## Q6
The owner is data-eng-cards (Tomás Rivera's team), with a T+1 SLA landing by 07:00 UTC. Yes, there was an issue: September 2025 partitions were short by about 6% until the backfill (ticket DE-4411) finished on 2026-10-27, after which row counts matched the ledger within 0.1%. Any velocity-v2 numbers computed before then used about 6% fewer September transactions. Other known issues:
- The 2026-10-30 log says a backfill is now running for October partitions (no note on it yet).
- Duplicate `txn_id` rows come from partition reloads: about 670k extra rows (0.31%) in 2025-Q1. The consumer view keeps the first arrival (decision 2025-11-24).
- Late partitions were 4.1% in 2025-Q1 and fell to 1.6% after the batch moved to 04:30 in October 2025.
Sources: memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/txn-backfill.md, memory/log/2026-10-26.md, memory/log/2026-10-27.md, memory/log/2026-10-30.md, memory/data-quality-txn/ds-dq-txn-daily.md, memory/data-quality-txn/fnd-dup-retries.md, memory/data-quality-txn/ds-dq-dup-audit.md, memory/data-quality-txn/dec-dq-dedupe-first-arrival.md, memory/data-quality-txn/fnd-late-share-2026.md, memory/prefs/tomas-rivera-freshness-sla.md
## Q7
The cuts are at churn score 0.20 and 0.50, decided 2026-10-08 with Maya Ortiz against a budget of 4% calls and 12% emails:
- 0.50 and above: call (3.8% of the book)
- 0.20 to 0.50: email (11.6%)
- below 0.20: no action

They were set on the leaky churn-xgb-v2 scores, so their validity is in question. The 2026-10-30 retrain decision keeps them only until q-recalibrate-tiers is answered, and that question is still open. churn-xgb-v3 scores are less extreme, so at the current cuts the call tier would shrink from 3.8% to about 2.9% of the book, leaving call budget unused.
Sources: memory/churn-2026/dec-risk-tiers.md, memory/churn-2026/q-tier-cutoffs.md, memory/churn-2026/q-recalibrate-tiers.md, memory/churn-2026/dec-retrain-cadence.md, memory/log/2026-10-28.md
## Q8
It ranks them poorly. In exp-015 (churn-xgb-v2 on holdout-2025q4), accounts under 6 months' tenure (n=168k, 14%) got AUC 0.69 and recall@10 0.31, against AUC 0.83 for tenure of 6 months or more (n=1.03M). New accounts are 14% of the book but 21% of churners, and they have too little history for velocity or utilization to mean much. The options proposed are a tenure-specific model or routing new accounts to onboarding (owner Priya Nair). No tenure breakdown has been recorded for churn-xgb-v3.
Sources: memory/churn-2026/exp-015-tenure.md, memory/churn-2026/finding-new-accounts.md
## Q9
No. On 2026-10-29 all 3 `util_` columns of feat-utilization-v1 were checked against the post-period leak pattern. Every window (1, 3 and 6 months of balance over limit) ends on the observation date with no post-period days, so feat-utilization-v1 was kept unchanged in churn-xgb-v3. The leak was confined to the velocity features.
Sources: memory/churn-2026/feat-utilization-check.md, memory/churn-2026/feat-utilization-v1.md, memory/log/2026-10-29.md, memory/churn-2026/churn-xgb-v3.md
## Q10
In churn-2026, four models are fit on `cards.churn_labels`:
- the logistic baseline (exp-011)
- the exp-014 XGBoost
- churn-xgb-v2 (superseded)
- churn-xgb-v3 (current, retrained monthly on the latest 9 months)

Other projects also train on it: churn-2025 (churn-lr-base-2025, churn-gbm-2025 v1/v2, on 60-day labels), churn-small-business (csb-lr-base, csb-xgb-v1/v2), label-pipeline-rebuild's lbl-churn-xgb-v2, and the app-engagement and payment-segment attrition models. The churn-2026 base rate is 6.8% on the 2025 book (n=4.1M accounts, 90-day label, 2026-09-03). Other rates depend on the label definition: 6.1% for the December 2025 cohort on the 90-day label, 4.3% on the old 60-day label, 6.4% on the rebuilt 90-day-plus-closure label for 2025-H1, and 7.4% for SMB at 90 days.
Sources: memory/churn-2026/ds-churn-labels.md, memory/churn-2026/exp-011-baseline.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-retrain-cadence.md, memory/churn-2025/ds-c25-churn-labels.md, memory/churn-2025/churn-gbm-2025-v2.md, memory/churn-small-business/ds-csb-churn-labels.md, memory/label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, memory/label-pipeline-rebuild/lbl-churn-xgb-v2.md, memory/qa/dec-2025-churn-restated.md, memory/howto/churn-label-90d.md