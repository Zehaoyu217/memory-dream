## Q1
feat-velocity-v2 is 6 `vel_` columns (features/velocity_v2.py) built on `cards.txn_daily`. They hold the count and sum of card transactions in the 30 days *around* the observation date, plus their ratio to the 90-day average. It drove exp-014's lift from AUC 0.71 to 0.81, mostly through `vel_ratio_30_90`, but that window let in post-period days from the label window, so the features leaked the target; with those days removed AUC is 0.74. It is SUPERSEDED by feat-velocity-v3 (2026-10-30, pre-observation days only, owner Sam Lee), and any v2 numbers computed before 2026-10-27 also used about 6% fewer September transactions.
Sources: memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/exp-014.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/txn-backfill.md
## Q2
exp-014 (XGBoost, 400 trees, depth 6; the baseline features plus velocity v2) raised AUC from 0.71 to 0.81 and recall@10 from 0.29 to 0.52 on holdout-2025q4 (n=1.2M, 2026-09-25). It became churn-xgb-v2 (`models:/churn-xgb/2`). The jump turned out to be a leak: leak-hypothesis led to exp-017, where AUC fell to 0.74 and recall@10 to 0.41 once post-period days were removed. That led to post-period-leak, then velocity v3, then churn-xgb-v3 (AUC 0.76, recall@10 0.43), so exp-014's 0.81 is not a valid result.
Sources: memory/churn-2026/exp-014.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/churn-xgb-v3.md
## Q3
In churn-2026, these depend on it: feat-velocity-v3 (and the retired v2), feat-utilization-v1 and the ds-txn-2025q4 snapshot. `cards.churn_labels` is also built from it, so churn-xgb-v3 and its risk tiers depend on it too. Outside churn-2026 it feeds:
- six feature-store features (including txn_cnt_7d and txn_cnt_30d)
- the fraud-2025 CNP extract (frozen) and the fraud-2026 CNP set (14.2M rows)
- the AML cash-like subset and the merchant-risk merchant-month panel (1.9M rows)
- the NPS behaviour join
- the weekly KPI deck's data-quality gate, which blocks publishing if row count is more than 5% off the trailing 7-day mean

In all, about 64 notes across 27 project folders reference it.
Sources: memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/ds-churn-labels.md, memory/churn-2026/ds-txn-2025q4.md, memory/feature-store-migration/ds-fsm-txn-source.md, memory/fraud-2025/ds-f25-txn-2024-2025.md, memory/fraud-2026/ds-f26-cnp-txn.md, memory/aml-alerts/ds-aml-cash-txn.md, memory/merchant-risk/ds-mrisk-merchant-month.md, memory/nps-drivers/ds-nps-behaviour-join.md, memory/reporting/data-quality-gate.md
## Q4
The current model is churn-xgb-v3 (`models:/churn-xgb/3`), which replaced v2 in nightly scoring on 2026-10-30. It uses velocity v3 and utilization v1 and is trained on `cards.churn_labels` (observation months 2025-01 to 2025-09). On holdout-2025q4 (n=1.2M) it scores AUC 0.76 and recall@10 0.43 with no leakage; recall@10 holds at 0.40–0.45 across the Oct, Nov and Dec cohorts (exp-019), and it is retrained monthly on the latest 9 months. One caveat: an older feature-store-migration note (2026-02-19) calls fsm-churn-xgb-v2 (AUC 0.791 on holdout-2025q2) the production churn model, but churn-xgb-v3 is the newest.
Sources: memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md, memory/churn-2026/dec-retrain-cadence.md, memory/feature-store-migration/fsm-churn-xgb-v2.md
## Q5
The model did not get worse; v2's 0.81 was inflated by target leakage. feat-velocity-v2 used a window "around" the observation date, so it took in post-period days inside the 90-day label window. Ending that window on the observation date (exp-017) gave AUC 0.74 and recall@10 0.41, and `vel_ratio_30_90` fell from 1st to 9th in gain importance. churn-xgb-v3 is rebuilt on pre-observation velocity v3 with utilization checked clean and scores 0.76 / 0.43, which is the honest number (the 0.52 recall was the leak).
Sources: memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md, memory/churn-2026/feat-utilization-check.md
## Q6
data-eng-cards owns it, with Tomás Rivera (data engineering) as the named contact; his SLA is T+1, loaded by 07:00 UTC. Yes, there was an issue: September 2025 partitions were short by about 6% until a backfill finished on 2026-10-27 (ticket DE-4411), and row counts now match the ledger within 0.1%. Any v2 velocity numbers computed before then used about 6% fewer September transactions. Separately, the table has standing known issues with late partitions (landing after 10:00 on D+1) and duplicate txn_id rows from partition reloads after retries, tracked in data-quality-txn.
Sources: memory/data-quality-txn/ds-dq-txn-daily.md, memory/churn-2026/txn-backfill.md, memory/churn-2026/ds-txn-2025q4.md, memory/data-quality-txn/q-dq-late-cause.md, memory/data-quality-txn/fnd-dup-retries.md, memory/prefs/tomas-rivera-freshness-sla.md
## Q7
The cuts are 0.20 and 0.50, decided on 2026-10-08 with Maya Ortiz of retention:
- score of 0.50 or more: call (3.8% of the book)
- 0.20 to 0.50: email (11.6%)
- below 0.20: no action

Tiers are written nightly to `offers.tier_matrix`, against a budget of calls for 4% and emails for 12%. Validity is an open question: the cuts were set on the leaky churn-xgb-v2 scores, and v3 scores are less extreme, so the call tier would shrink from 3.8% to about 2.9% of the book. dec-retrain-cadence keeps the cuts until q-recalibrate-tiers is answered.
Sources: memory/churn-2026/dec-risk-tiers.md, memory/churn-2026/q-tier-cutoffs.md, memory/churn-2026/q-recalibrate-tiers.md, memory/churn-2026/dec-retrain-cadence.md
## Q8
It does poorly. On churn-xgb-v2, accounts under 6 months tenure (n=168k, 14% of the holdout) got AUC 0.69 and recall@10 0.31, against AUC 0.83 for tenure of 6 months or more (n=1.03M). New accounts are 14% of the book but 21% of churners and have too little history for velocity or utilization to mean much. The options noted are a tenure-specific model or routing them to the onboarding team (owner Priya Nair); no tenure split is recorded yet for v3.
Sources: memory/churn-2026/exp-015-tenure.md, memory/churn-2026/finding-new-accounts.md
## Q9
No. On 2026-10-29 all 3 `util_` columns of feat-utilization-v1 were checked against the leak pattern, and every window ends on the observation date with no post-period days. They are kept unchanged in churn-xgb-v3.
Sources: memory/churn-2026/feat-utilization-check.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/churn-xgb-v3.md
## Q10
In churn-2026, churn-xgb-v2 (superseded) and churn-xgb-v3 are trained on it (observation months 2025-01 to 2025-09; v3 is retrained monthly on the latest 9 months). Their base rate is 6.8% 90-day churn on the 2025 book (n=4.1M, 2026-09-03). Other projects build labels from the same table at different rates: churn-2025 has 4.3% at 60 days, churn-small-business has 7.4% at 90 days and 4.1% at 60 days, and app-engagement and promo-apr-test also use it. The churn definition was corrected to include 6-month dormancy and the table rebuilt on 2026-03-16, which restated Sept 2024 monthly churn from 1.1% to 3.4%.
Sources: memory/churn-2026/ds-churn-labels.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-retrain-cadence.md, memory/churn-2025/ds-c25-churn-labels.md, memory/churn-small-business/ds-csb-churn-labels.md, memory/app-engagement/ds-ae-attrition-labels.md, memory/promo-apr-test/ds-pa-churn-labels.md, memory/corrections/churn-includes-dormant.md