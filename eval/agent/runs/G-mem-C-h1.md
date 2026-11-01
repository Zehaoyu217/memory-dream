## Q1
The current retrain was decided on 2026-10-30 by Sam Lee with retention. Each month it refits churn-xgb-v3 on a rolling window of the latest 9 observation months of `cards.churn_labels`. The first v3 fit used the 2025-01 to 2025-09 observation months, the same 9-month span as v2. The 0.20 / 0.50 risk-tier cuts stay as they are until q-recalibrate-tiers is answered.
Sources: churn-2026/dec-retrain-cadence.md, churn-2026/churn-xgb-v3.md, churn-2026/q-recalibrate-tiers.md, DIGEST.md
Tool calls for this question: 5
## Q2
Two models use feat-utilization-v1 (3 `util_` columns built from `cards.txn_daily`): churn-xgb-v2, now superseded, which paired it with velocity v2, and the current churn-xgb-v3, which pairs it with velocity v3. The 2026-10-29 check found no post-period days in any of the 3 columns, because every window ends on the observation date, so the leak was limited to the velocity features. feat-utilization-v1 was therefore kept unchanged in v3, and churn-xgb-v3 was signed off as free of leakage (AUC 0.76, recall@10 0.43 on holdout-2025q4, n=1.2M). v2 was retired only because of its velocity v2 inputs.
Sources: churn-2026/feat-utilization-check.md, churn-2026/feat-utilization-v1.md, churn-2026/churn-xgb-v2.md, churn-2026/churn-xgb-v3.md, churn-2026/post-period-leak.md, log/2026-10-29.md
Tool calls for this question: 2
## Q3
exp-017 re-ran exp-014's XGBoost setup with the velocity window ending on the observation date. On holdout-2025q4 (n=1.2M), AUC fell from 0.81 to 0.74, recall@10 fell from 0.52 to 0.41, and `vel_ratio_30_90` dropped from 1st to 9th in gain importance. This confirmed the post-period aggregation leak (written up 2026-10-29) and led to the clean utilization check, the 2026-10-30 decision to rebuild velocity as v3 and retire v2, and churn-xgb-v3 (AUC 0.76, recall@10 0.43), which replaced v2 in nightly scoring that same day. exp-017 had been queued on 2026-10-27, after the September txn backfill landed.
Sources: churn-2026/exp-017-leak-check.md, churn-2026/leak-hypothesis.md, churn-2026/post-period-leak.md, churn-2026/dec-velocity-v3.md, churn-2026/churn-xgb-v3.md, log/2026-10-27.md, log/2026-10-28.md, log/2026-10-30.md
Tool calls for this question: 3
## Q4
churn-2026's holdout-2025q4 is a random 30% of accounts with Oct–Dec 2025 observation dates, stratified by tenure band. That gives 1.2M accounts, none used for training, split with `nb/make_holdout.ipynb`. The set was frozen on 2026-09-04, and the team rule says a frozen set is never re-extracted; late labels go into the next named holdout instead. One conflict: howto/eval-set-freeze-date says a holdout-2025q4 was frozen on 2026-01-19 with 412,600 rows, which looks like a different set reusing the same name rather than churn-2026's 1.2M set.
Sources: churn-2026/ds-holdout-2025q4.md, howto/eval-set-freeze-date.md, qa/holdout-2025q4-reextract.md, qa/holdout-2025q4-name.md
Tool calls for this question: 4
## Q5
The logistic baseline (exp-011, run 2026-09-15) reached AUC 0.71 and recall@10 0.29 on holdout-2025q4, with n=1.2M. It was fit on `cards.churn_labels` using 14 account-level features, with no velocity or utilization features (notebook `nb/exp011_baseline.ipynb`).
Sources: churn-2026/exp-011-baseline.md, churn-2026/exp-014.md
Tool calls for this question: 2
## Q6
recall@10 matches how retention works: they can call 10% of the book each month, so what matters is the share of all 90-day churners caught in the top 10% of scores. AUC is reported alongside it, but decisions use recall@10. It is computed by `nb/metrics.py::recall_at_k` with k=0.10. Its denominator is all churners; dividing by k would give precision@k instead (corrected 2025-05-12).
Sources: churn-2026/metric-recall-at-10.md, corrections/recall-at-k-denominator.md
Tool calls for this question: 3
## Q7
feat-velocity-v3 is current; it replaced v2 on 2026-10-30. v3 counts and sums card transactions in the 30 days before the observation date, with a ratio to the prior 90-day average, so every window ends on the observation date. v2 used a 30-day window around the observation date, which pulled in days after it from inside the label window, and that was the leak. Both versions have the same 6 `vel_` columns (`features/velocity_v3.py` vs `features/velocity_v2.py`).
Sources: churn-2026/feat-velocity-v3.md, churn-2026/feat-velocity-v2.md, churn-2026/dec-velocity-v3.md, churn-2026/leak-hypothesis.md
Tool calls for this question: 2
## Q8
feat-velocity-v3 reads `cards.txn_daily`, a table owned by data-eng-cards; churn-2026 works from its ds-txn-2025q4 snapshot. The code is `features/velocity_v3.py` and the owner is Sam Lee. It is used by churn-xgb-v3 (together with feat-utilization-v1), which is registered as `models:/churn-xgb/3` and replaced churn-xgb-v2 in the nightly scoring job on 2026-10-30.
Sources: churn-2026/feat-velocity-v3.md, churn-2026/dec-velocity-v3.md, churn-2026/churn-xgb-v3.md, churn-2026/ds-txn-2025q4.md, log/2026-10-30.md
Tool calls for this question: 3
## Q9
The 2026-10-26 review started from exp-014's velocity columns, from the XGBoost run with AUC 0.81 and recall@10 0.52, where most of the lift came from `vel_ratio_30_90`. It followed the 2026-10-20 leak hypothesis that the "around" window included days after the observation date. The question to data-eng-cards about short September partitions was answered in the txn-backfill note: September 2025 in `cards.txn_daily` was about 6% short, the backfill (ticket DE-4411) finished 2026-10-27 with row counts within 0.1% of the ledger, and any v2 numbers computed before 10-27 used about 6% fewer September transactions. exp-017 was queued that afternoon on the backfilled data.
Sources: log/2026-10-26.md, churn-2026/exp-014.md, churn-2026/leak-hypothesis.md, churn-2026/txn-backfill.md, churn-2026/ds-txn-2025q4.md, log/2026-10-27.md
Tool calls for this question: 3
## Q10
`cards.churn_labels` holds a 90-day churn flag for each account and month-end observation date: the account counts as churned if it makes no purchase and no payment in the 90 days after that date. The 90-day window replaced the 60-day one on 2026-01-12. The flag is built by the retention-labels job from `cards.txn_daily` and shows 6.8% churn on the 2025 book (n=4.1M), and it is maintained by data-eng-cards (Tomás Rivera's team, which backfilled the table from 2024-01). Other notes give conflicting definitions for the same table that have not been reconciled: closure OR 6 months of dormancy (corrections/churn-includes-dormant), and 90-day inactivity OR closure within 120 days (label-pipeline-rebuild).
Sources: churn-2026/ds-churn-labels.md, howto/churn-label-90d.md, howto/churn-label-60d.md, prefs/tomas-rivera-backfill-notice.md, corrections/churn-includes-dormant.md, label-pipeline-rebuild/feat-lbl-churn-flag-closure.md
Tool calls for this question: 4
Total tool calls in this task: 5
Minutes spent: 4