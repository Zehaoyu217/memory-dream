## Q1
feat-velocity-v2 (`features/velocity_v2.py`, 6 `vel_` columns) has the count and sum of card transactions in the 30 days *around* the observation date, plus their ratio to the 90-day average. It is built on `cards.txn_daily`. It powered exp-014 and churn-xgb-v2 (AUC 0.81, recall@10 0.52), but the window takes in days after the observation date, inside the label window. That is a target leak: removing those days drops AUC from 0.81 to 0.74 (exp-017). On 2026-10-30 it was retired and replaced by feat-velocity-v3, which uses only days before the observation date (owner Sam Lee). Separately, any v2 numbers computed before 2026-10-27 used about 6% fewer September-2025 transactions, because of a gap in the txn table that has since been fixed.
Sources: memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/exp-014.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/txn-backfill.md
Tool calls for this question: 2
## Q2
exp-014 (XGBoost, 400 trees, depth 6, the baseline features plus velocity v2) reported AUC 0.81 (up from 0.71) and recall@10 0.52 (up from 0.29) on holdout-2025q4 (n=1.2M, 2026-09-25), mostly thanks to `vel_ratio_30_90`. It became churn-xgb-v2 (`models:/churn-xgb/2`). The jump was later traced to post-period leakage. The re-run with the window ending on the observation date (exp-017) gave AUC 0.74 and recall@10 0.41, and `vel_ratio_30_90` fell from 1st to 9th in gain importance. That led to the v3 rebuild: churn-xgb-v3, AUC 0.76, recall@10 0.43.
Sources: memory/churn-2026/exp-014.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/churn-xgb-v3.md
Tool calls for this question: 0 (answered from the same 2 calls as Q1)
## Q3
These read `cards.txn_daily` directly:
- the Q4-2025 snapshot ds-txn-2025q4
- `cards.churn_labels` (built from it by the retention-labels job)
- feat-velocity-v2 (retired) and feat-velocity-v3
- feat-utilization-v1 (its `balance` and `credit_limit` columns)

Further downstream, every churn model depends on it through those labels and features: logreg-baseline/exp-011, exp-014, exp-017, churn-xgb-v2 and the production churn-xgb-v3. So do their outputs, `cards.churn_scores` and `offers.tier_matrix`.
Sources: memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/ds-churn-labels.md, memory/churn-2026/feat-velocity-v2.md, memory/churn-2026/feat-velocity-v3.md, memory/churn-2026/feat-utilization-v1.md, memory/churn-2026/txn-backfill.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-risk-tiers.md
Tool calls for this question: 0 (answered from the same 2 calls as Q1)
## Q4
The production model is churn-xgb-v3 (`models:/churn-xgb/3`). It was registered on 2026-10-30 and replaced v2 in the nightly scoring job. It uses feat-velocity-v3 plus feat-utilization-v1 and is trained on `cards.churn_labels` for 2025-01 to 2025-09. On holdout-2025q4 (n=1.2M) it scores AUC 0.76 and recall@10 0.43, with no leakage. Recall@10, the metric decisions are based on, holds steady across monthly cohorts (0.45 / 0.43 / 0.40 for Oct / Nov / Dec). v2's 0.81 / 0.52 was inflated by the leak, and v3 is to be retrained monthly on the latest 9 observation months.
Sources: memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md, memory/churn-2026/metric-recall-at-10.md, memory/churn-2026/dec-retrain-cadence.md
Tool calls for this question: 0 (answered from the same 2 calls as Q1)
## Q5
The drop is not a real regression: v2's 0.81 was inflated by target leakage. feat-velocity-v2 aggregated transactions "around" the observation date, including days inside the 90-day label window. Removing those post-period days alone took AUC from 0.81 to 0.74 (exp-017, 2026-10-28), and `vel_ratio_30_90` fell from 1st to 9th in importance. v3 rebuilt velocity from pre-observation days only. The utilization features were checked and were already clean, and the XGBoost settings were unchanged, so 0.76 is the honest number. The notes do not measure whether the September-2025 backfill (finished 2026-10-27, before exp-017 and v3 were run) contributed to the drop.
Sources: memory/churn-2026/leak-hypothesis.md, memory/churn-2026/exp-017-leak-check.md, memory/churn-2026/post-period-leak.md, memory/churn-2026/dec-velocity-v3.md, memory/churn-2026/feat-utilization-check.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/exp-019-recall.md, memory/churn-2026/txn-backfill.md
Tool calls for this question: 0 (answered from the same 2 calls as Q1)
## Q6
data-eng-cards owns `cards.txn_daily`. Yes, there was a data-quality issue: the September 2025 partitions were short by about 6%. The backfill (ticket DE-4411) finished on 2026-10-27, and row counts now match the ledger within 0.1%. Any v2 numbers computed before then (exp-014, churn-xgb-v2) used about 6% fewer September transactions. The ds-txn-2025q4 note (dated 09-03) still lists the gap as "known", so it is stale. The 2026-10-30 log also shows a new backfill running for the October partitions, which no note documents yet.
Sources: memory/churn-2026/ds-txn-2025q4.md, memory/churn-2026/txn-backfill.md, memory/churn-2026/ds-churn-labels.md, memory/log/2026-10-26.md, memory/log/2026-10-27.md, memory/log/2026-10-30.md
Tool calls for this question: 0 (answered from the same 2 calls as Q1)
## Q7
The cuts are at churn score 0.20 and 0.50: score ≥ 0.50 means a call (3.8% of the book), 0.20–0.50 an email (11.6%), and below 0.20 no action. Retention (Maya Ortiz) decided this on 2026-10-08 against a budget of 4% calls and 12% emails. They are still in force: the 2026-10-30 retrain decision keeps them until q-recalibrate-tiers is answered. Their validity is in doubt, though, because they were set on churn-xgb-v2 scores. v3's scores are less extreme, so the call tier would shrink to about 2.9% of the book at the current cuts, and that recalibration question is still open as of 2026-10-30.
Sources: memory/churn-2026/dec-risk-tiers.md, memory/churn-2026/q-tier-cutoffs.md, memory/churn-2026/q-recalibrate-tiers.md, memory/churn-2026/dec-retrain-cadence.md
Tool calls for this question: 0 (answered from the same 2 calls as Q1)
## Q8
It does poorly. In exp-015 on churn-xgb-v2, accounts under 6 months of tenure (n=168k, 14% of the holdout) got AUC 0.69 and recall@10 0.31, against AUC 0.83 for tenure ≥ 6 months (n=1.03M). New accounts are 14% of the book but 21% of churners, and have too little history for velocity or utilization to mean much. The proposed options are a tenure-specific model, or routing new accounts to the onboarding team (owner Priya Nair). Caveat: this was measured on the leaky v2, and the notes have no tenure breakdown for production v3.
Sources: memory/churn-2026/exp-015-tenure.md, memory/churn-2026/finding-new-accounts.md
Tool calls for this question: 0 (answered from the same 2 calls as Q1)
## Q9
No. On 2026-10-29 all 3 `util_` columns of feat-utilization-v1 were checked against the leak pattern. Every window ends on the observation date, with no post-period days, so feat-utilization-v1 is kept unchanged in the v3 models. They do read `cards.txn_daily` (`balance` and `credit_limit`), but that exposes them only to the now-fixed September gap, not to the leak.
Sources: memory/churn-2026/feat-utilization-check.md, memory/churn-2026/feat-utilization-v1.md, memory/log/2026-10-29.md
Tool calls for this question: 0 (answered from the same 2 calls as Q1)
## Q10
These models are trained on `cards.churn_labels`:
- logreg-baseline (exp-011: AUC 0.71, recall@10 0.29)
- churn-xgb-v2 (2025-01 to 2025-09)
- churn-xgb-v3, now in production (2025-01 to 2025-09, to be retrained monthly on the latest 9 observation months)

The exp-014 and exp-017 XGBoost experiments build on the same baseline setup. The churn base rate is 6.8% on the 2025 book (n=4.1M accounts, as of 2026-09-03), using a 90-day churn flag per account with month-end observation dates. That rate was computed before the September-2025 txn backfill, and the notes never re-check it.
Sources: memory/churn-2026/ds-churn-labels.md, memory/churn-2026/exp-011-baseline.md, memory/churn-2026/exp-014.md, memory/churn-2026/churn-xgb-v2.md, memory/churn-2026/churn-xgb-v3.md, memory/churn-2026/dec-retrain-cadence.md, memory/churn-2026/q-churn-drivers.md
Tool calls for this question: 0 (answered from the same 2 calls as Q1)