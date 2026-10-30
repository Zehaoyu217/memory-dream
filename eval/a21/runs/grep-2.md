## Q1
feat-velocity-v2 is 6 `vel_` columns: the count and sum of card transactions in the 30 days "around" the observation date, plus their ratio to the 90-day average. It is built on `cards.txn_daily` (`features/velocity_v2.py`). It drove the exp-014/churn-xgb-v2 lift (AUC 0.71→0.81, recall@10 0.29→0.52, mostly from `vel_ratio_30_90`). That lift turned out to be leakage: the window takes in post-observation days that fall inside the label window, and AUC fell to 0.74 once they were removed. It was retired on 2026-10-30 and replaced by feat-velocity-v3. Separately, any v2 numbers computed before 2026-10-27 used about 6% fewer September-2025 transactions because of the txn_daily gap.
Sources: memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/exp-014.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/txn-backfill.md
Tool calls for this question: 2 (shared across all 10)
## Q2
exp-014 (2026-09-25) was XGBoost with 400 trees at depth 6 on the baseline features plus velocity v2. On holdout-2025q4 (n=1.2M) it scored AUC 0.81 and recall@10 0.52, against the baseline's 0.71 and 0.29. It became the production model churn-xgb-v2. The lift was later shown to be a leak: exp-017, the same setup with the velocity window ending on the observation date, scored only AUC 0.74 and recall@10 0.41. The honest successor, churn-xgb-v3, scores 0.76 and 0.43.
Sources: memory/churn-2026/exp-014.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md
Tool calls for this question: 2 (shared across all 10)
## Q3
Directly built on `cards.txn_daily`:
- the Q4-2025 snapshot (ds-txn-2025q4)
- feat-velocity-v2 (retired) and feat-velocity-v3
- feat-utilization-v1 (`balance` and `credit_limit` columns)
- `cards.churn_labels`, built from it by the retention-labels job

Downstream of those: logreg-baseline, exp-014 and exp-017, churn-xgb-v2 and churn-xgb-v3, and through the models `cards.churn_scores` and the risk tiers in `offers.tier_matrix`.
Sources: memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/ds-churn-labels.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-risk-tiers.md
Tool calls for this question: 2 (shared across all 10)
## Q4
The production model is churn-xgb-v3 (`models:/churn-xgb/3`), registered on 2026-10-30, when it replaced churn-xgb-v2 in the nightly scoring job. It uses feat-velocity-v3 and feat-utilization-v1. On holdout-2025q4 (n=1.2M) it scores AUC 0.76 and recall@10 0.43; recall@10 is the business metric. Recall@10 holds steady across observation months (Oct 0.45, Nov 0.43, Dec 0.40). It will be retrained monthly on the latest 9 observation months; the baseline it beats scored 0.71 and 0.29.
Sources: memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md, memory/churn-2026/metric-recall-at-10.md, memory/churn-2026/dec-retrain-cadence.md, memory/churn-2026/exp-011-baseline.md, memory/log/2026-10-30.md
Tool calls for this question: 2 (shared across all 10)
## Q5
The 0.81 was inflated by target leakage. feat-velocity-v2 aggregated a window "around" the observation date, so it counted post-observation days inside the 90-day label window. exp-017 showed AUC falling to 0.74 once those days were removed, and `vel_ratio_30_90` dropping from first to ninth in gain importance. v3 rebuilds velocity from pre-observation days only (AUC 0.76). The notes do not explain why v3 lands 0.02 above exp-017. One confounder: v2's 0.81 (2026-10-02) predates the 2026-10-27 September backfill, so it used about 6% fewer September transactions.
Sources: memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/txn-backfill.md
Tool calls for this question: 2 (shared across all 10)
## Q6
data-eng-cards owns `cards.txn_daily` (2.3B rows for 2025, refreshed nightly). Yes, there was a data-quality issue: the September 2025 partitions were short by about 6%. The backfill (ticket DE-4411) finished on 2026-10-27, and row counts now match the ledger within 0.1%. Any v2 numbers computed before then used about 6% fewer September transactions. The 2026-10-30 log also says a backfill is now running for the October partitions, and no note explains that yet.
Sources: memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/txn-backfill.md, memory/churn-2026/ds-churn-labels.md, memory/log/2026-10-26.md, memory/log/2026-10-27.md, memory/log/2026-10-30.md
Tool calls for this question: 2 (shared across all 10)
## Q7
The cuts are at churn score 0.20 and 0.50, decided on 2026-10-08 with Maya Ortiz against a budget of calls for 4% of the book and emails for 12%:
- 0.50 and above: call (3.8% of the book)
- 0.20 to 0.50: email (11.6%)
- below 0.20: no action

They were set on churn-xgb-v2 scores, and they stay in force until q-recalibrate-tiers is answered. That question is open as of 2026-10-30. churn-xgb-v3 scores are less extreme, so at the current cuts the call tier would shrink to about 2.9% of the book. They should be treated as provisional.
Sources: memory/churn-2026/q-tier-cutoffs.md, memory/churn-2026/dec-risk-tiers.md, memory/churn-2026/q-recalibrate-tiers.md, memory/churn-2026/dec-retrain-cadence.md
Tool calls for this question: 2 (shared across all 10)
## Q8
The model does poorly on them. In exp-015, churn-xgb-v2 on accounts under 6 months of tenure (n=168k, 14% of holdout) scored AUC 0.69 and recall@10 0.31, against AUC 0.83 on older accounts (n=1.03M). New accounts are 14% of the book but 21% of churners, because they have too little history for velocity or utilization to mean much. The options on the table are a tenure-specific model or routing them to the onboarding team (Priya Nair). This was only measured on the leaky v2; no note re-runs the tenure split on churn-xgb-v3.
Sources: memory/churn-2026/exp-015-tenure.md, memory/churn-2026/finding-new-accounts.md
Tool calls for this question: 2 (shared across all 10)
## Q9
No. On 2026-10-29 all 3 `util_` columns of feat-utilization-v1 were checked against the post-period leak pattern. Every window ends on the observation date, so feat-utilization-v1 is kept unchanged in churn-xgb-v3. They do read `balance` and `credit_limit` from `cards.txn_daily`, so the September-2025 gap (fixed 2026-10-27) could have touched them, but no note says so.
Sources: memory/churn-2026/feat-utilization-check.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/churn-xgb-v3.md, memory/log/2026-10-29.md
Tool calls for this question: 2 (shared across all 10)
## Q10
Models trained on `cards.churn_labels`:
- logreg-baseline (exp-011)
- churn-xgb-v2, now superseded
- churn-xgb-v3, in production; it uses the 2025-01 to 2025-09 observation months and is retrained monthly on the latest 9 months
- the exp-014 and exp-017 XGBoost experiments, which share that setup

The churn base rate is 6.8% on the 2025 book (n=4.1M accounts, measured 2026-09-03), using a 90-day label window after month-end observation dates. The labels are built from `cards.txn_daily`, and that 6.8% predates the 2026-10-27 September backfill. The notes do not say whether it was recomputed.
Sources: memory/churn-2026/ds-churn-labels.md, memory/churn-2026/exp-011-baseline.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-retrain-cadence.md, memory/churn-2026/exp-014.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/txn-backfill.md
Tool calls for this question: 2 (shared across all 10)