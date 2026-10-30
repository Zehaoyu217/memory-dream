"""Write the churn-2026 fixture (25 notes + 5 daily logs) under argv[1]."""
import sys
from pathlib import Path

NOTES = {
"churn-2026/q-churn-drivers.md": """---
updated: 2026-09-02
---
# What drives 90-day card churn in the 2025 book?
Asked by retention (Maya Ortiz), 2026-09-02. Target: an account with no card spend for 90 days
after the observation date. Book: 4.1M active card accounts, 2025.

Labels live in `cards.churn_labels`; transactions in `cards.txn_daily`.
Success metric: recall@10 on holdout-2025q4.
""",
"churn-2026/ds-txn-2025q4.md": """---
updated: 2026-09-03
---
# Q4-2025 snapshot of cards.txn_daily, one row per account-day
Owned by data-eng-cards. 2.3B rows, 2025-01-01 to 2025-12-31, refreshed nightly.
Columns used here: `acct_id`, `txn_date`, `amount`, `merchant_cat`, `balance`, `credit_limit`.

Known gap: September 2025 partitions were short by about 6% until the backfill (see [[txn-backfill]]).
Query: `sql/txn_snapshot.sql`.
""",
"churn-2026/ds-churn-labels.md": """---
updated: 2026-09-03
---
# cards.churn_labels: 90-day churn flag per account and observation month
Built by the retention-labels job from `cards.txn_daily`; maintained by data-eng-cards.
Churn rate 6.8% on the 2025 book (n=4.1M accounts, 2026-09-03).
Observation dates are month-ends; the label window is the 90 days after.
""",
"churn-2026/ds-holdout-2025q4.md": """---
updated: 2026-09-04
---
# holdout-2025q4: 1.2M accounts with Oct–Dec 2025 observation dates, never used for training
Random 30% of accounts, stratified by tenure band; frozen 2026-09-04.
Every model in churn-2026 is evaluated on holdout-2025q4 unless a note says otherwise.
Split script: `nb/make_holdout.ipynb`.
""",
"churn-2026/metric-recall-at-10.md": """---
updated: 2026-09-04
---
# recall@10: share of 90-day churners caught in the top 10% of scores
The business metric for churn-2026: retention can call 10% of the book each month.
AUC is reported alongside, but decisions use recall@10.
Computed by `nb/metrics.py::recall_at_k` with k=0.10.
""",
"churn-2026/feat-velocity-v2.md": """---
from: [ds-txn-2025q4]
updated: 2026-09-10
---
# 30-day transaction velocity per account (v2)
feat-velocity-v2: count and sum of card transactions in the 30 days around the observation date,
plus their ratio to the 90-day average. Built on `cards.txn_daily`.
Code: `features/velocity_v2.py`. 6 columns, prefix `vel_`.
""",
"churn-2026/feat-utilization-v1.md": """---
from: [ds-txn-2025q4]
updated: 2026-09-12
---
# Credit utilization features: balance / limit over 1, 3 and 6 months (v1)
feat-utilization-v1 uses `balance` and `credit_limit` from `cards.txn_daily`, all windows ending
on the observation date. Code: `features/utilization_v1.py`. 3 columns, prefix `util_`.
""",
"churn-2026/exp-011-baseline.md": """---
from: [q-churn-drivers]
updated: 2026-09-15
---
# Logistic baseline: AUC 0.71, recall@10 0.29 on holdout-2025q4
logreg-baseline, fit on `cards.churn_labels` with 14 account-level features (no velocity, no utilization).
holdout-2025q4, n=1.2M, 2026-09-15. Notebook: `nb/exp011_baseline.ipynb`.
""",
"churn-2026/exp-014.md": """---
from: [exp-011-baseline, feat-velocity-v2]
updated: 2026-09-25
---
# XGBoost with 30-day velocity: AUC 0.81, recall@10 0.52 on holdout-2025q4
Adding the velocity features to the baseline set lifts AUC 0.71→0.81 and recall@10 0.29→0.52.
holdout-2025q4, n=1.2M, 2026-09-25. Model: XGBoost, 400 trees, depth 6. Notebook: `nb/exp014_xgb.ipynb`.
The lift is mostly from `vel_ratio_30_90`.
""",
"churn-2026/churn-xgb-v2.md": """---
from: [exp-014]
updated: 2026-10-02
---
# churn-xgb-v2: XGBoost on velocity v2 + utilization, AUC 0.81 on holdout-2025q4
churn-xgb-v2 uses feat-velocity-v2 and feat-utilization-v1; fit on `cards.churn_labels` (2025-01 to 2025-09).
Evaluated on holdout-2025q4: AUC 0.81, recall@10 0.52, n=1.2M, 2026-10-02.
Registered as `models:/churn-xgb/2`. Scores written nightly to `cards.churn_scores`.
""",
"churn-2026/q-tier-cutoffs.md": """---
from: [churn-xgb-v2]
updated: 2026-10-05
---
# Where should the risk tier cutoffs sit for retention offers?
Retention wants three tiers from churn-xgb-v2 scores: call, email, nothing.
Budget allows calls for 4% of the book and emails for 12%. Asked by Maya Ortiz, 2026-10-05.
""",
"churn-2026/dec-risk-tiers.md": """---
from: [q-tier-cutoffs]
updated: 2026-10-08
---
# Risk-tier cuts at churn score 0.20 and 0.50: three retention tiers
Decision, 2026-10-08, with retention (Maya Ortiz). Score ≥ 0.50 → call (3.8% of the book),
0.20–0.50 → email (11.6%), below 0.20 → no action. The risk-tier cuts are applied to churn-xgb-v2 scores
and written to `offers.tier_matrix` each night.
""",
"churn-2026/exp-015-tenure.md": """---
from: [churn-xgb-v2]
updated: 2026-10-10
---
# churn-xgb-v2 by tenure: AUC 0.69 on new accounts vs 0.83 on the rest
holdout-2025q4 split at 6 months tenure: new accounts n=168k (14%), AUC 0.69, recall@10 0.31;
tenure ≥ 6 months n=1.03M, AUC 0.83. 2026-10-10. Notebook: `nb/exp015_tenure.ipynb`.
""",
"churn-2026/finding-new-accounts.md": """---
from: [exp-015-tenure]
updated: 2026-10-12
---
# New accounts (< 6 months) need their own treatment: the model barely ranks them
Too little history for velocity or utilization to mean much; 14% of the book, 21% of churners.
Options: a tenure-specific model, or route new accounts to the onboarding team instead.
Owner of the onboarding flow: Priya Nair.
""",
"churn-2026/leak-hypothesis.md": """---
from: [exp-014]
updated: 2026-10-20
---
# Suspect leakage behind the 0.81 AUC
A 0.10 AUC jump from one feature group is too good. The velocity features use a window
"around" the observation date: it may include days after it, inside the label window.
To check: rebuild without post-period days and re-score (exp-017).
""",
"churn-2026/exp-017-leak-check.md": """---
from: [leak-hypothesis]
updated: 2026-10-28
---
# Leak check: AUC falls 0.81→0.74 once post-period days are removed
Same XGBoost setup as exp-014, but the velocity window ends on the observation date.
holdout-2025q4, n=1.2M, 2026-10-28: AUC 0.74, recall@10 0.41.
`vel_ratio_30_90` drops from first to ninth in gain importance.
""",
"churn-2026/post-period-leak.md": """---
from: [exp-014, exp-017-leak-check]
updated: 2026-10-29
---
# Post-period aggregation leaks target: AUC 0.81→0.74 without it
holdout-2025q4, n=1.2M, 2026-10-29. The velocity features built on `cards.txn_daily`
aggregate past the observation date. Rebuild without post-period columns (v3).

Evidence: `nb/eda_velocity.ipynb`, cells 12–18.
""",
"churn-2026/feat-utilization-check.md": """---
from: [post-period-leak]
updated: 2026-10-29
---
# Utilization features are clean: every window ends on the observation date
Checked all 3 `util_` columns of feat-utilization-v1 against the leak pattern, 2026-10-29.
No post-period days; keep feat-utilization-v1 unchanged in v3 models.
""",
"churn-2026/dec-velocity-v3.md": """---
from: [post-period-leak]
updated: 2026-10-30
---
# Rebuild velocity as v3 from pre-observation days only; retire v2
Decision, 2026-10-30. The velocity features are rebuilt as feat-velocity-v3: the same 6 `vel_` columns,
but every window ends on the observation date. churn-xgb-v2 is retrained on it as churn-xgb-v3. Owner: Sam Lee.
""",
"churn-2026/feat-velocity-v3.md": """---
from: [dec-velocity-v3]
supersedes: [feat-velocity-v2]
updated: 2026-10-30
---
# 30-day transaction velocity per account, pre-observation days only (v3)
feat-velocity-v3: count and sum of card transactions in the 30 days before the observation date,
plus their ratio to the prior 90-day average. Reads `cards.txn_daily`; replaces feat-velocity-v2.
Code: `features/velocity_v3.py`. 6 columns, prefix `vel_`.
""",
"churn-2026/churn-xgb-v3.md": """---
from: [feat-velocity-v3, feat-utilization-check]
supersedes: [churn-xgb-v2]
updated: 2026-10-30
---
# churn-xgb-v3: AUC 0.76, recall@10 0.43 on holdout-2025q4, no leakage
churn-xgb-v3 uses feat-velocity-v3 and feat-utilization-v1, same XGBoost settings as churn-xgb-v2.
Trained on `cards.churn_labels`, 2025-01 to 2025-09 observation months.
Evaluated on holdout-2025q4: AUC 0.76, recall@10 0.43, n=1.2M, 2026-10-30.
Registered as `models:/churn-xgb/3`; replaces churn-xgb-v2 in the nightly scoring job.
""",
"churn-2026/exp-019-recall.md": """---
from: [churn-xgb-v3]
updated: 2026-10-30
---
# churn-xgb-v3 keeps recall@10 at 0.43 across monthly cohorts (range 0.40–0.45)
Re-scored holdout-2025q4 by observation month (Oct, Nov, Dec 2025), n=1.2M, 2026-10-30.
Recall@10 by month: 0.45, 0.43, 0.40. v2's 0.52 was the leak; 0.43 is the honest number.
""",
"churn-2026/txn-backfill.md": """---
updated: 2026-10-27
---
# September 2025 gap in the txn table is fixed
The Sept-2025 backfill of `cards.txn_daily` finished 2026-10-27 (data-eng-cards ticket DE-4411);
row counts now match the ledger within 0.1%. The txn table feeds the velocity features,
so any v2 numbers computed before 10-27 used about 6% fewer September transactions.
""",
"churn-2026/dec-retrain-cadence.md": """---
from: [churn-xgb-v3, dec-risk-tiers]
updated: 2026-10-30
---
# Retrain churn-xgb-v3 monthly on the latest 9 observation months
Decision, 2026-10-30, Sam Lee with retention. Monthly retrain on the latest 9 observation months of
`cards.churn_labels`; the 0.20 / 0.50 risk-tier cuts stay until q-recalibrate-tiers is answered.
""",
"churn-2026/q-recalibrate-tiers.md": """---
from: [dec-risk-tiers, exp-019-recall]
updated: 2026-10-30
---
# Do the risk tier cutoffs need recalibrating for churn-xgb-v3's lower scores?
churn-xgb-v3 scores are less extreme than churn-xgb-v2's (fewer above 0.50), so the call tier
would shrink from 3.8% to about 2.9% of the book at the current cuts. Open, 2026-10-30.
""",
}
LOGS = {
"2026-10-26": ["09:40 [churn-2026] started leak review of exp-014 velocity columns",
               "15:10 [churn-2026] asked data-eng-cards about short September partitions"],
"2026-10-27": ["10:05 [churn-2026] txn backfill landed, re-ran row counts",
               "16:30 [churn-2026] exp-017 queued with velocity window ending at observation date"],
"2026-10-28": ["11:20 [churn-2026] exp-017 done: AUC 0.74, writing it up",
               "17:45 [churn-2026] Maya asked whether tier sizes change if AUC drops"],
"2026-10-29": ["09:15 [churn-2026] utilization columns checked for the same leak, clean",
               "14:00 [churn-2026] notebook eda_velocity cells 12-18 kept as evidence"],
"2026-10-30": ["08:50 [churn-2026] txn table backfill running for October partitions",
               "13:30 [churn-2026] churn-xgb-v3 registered, scoring job switched"],
}
for d, items in LOGS.items():
    NOTES[f"log/{d}.md"] = f"# log {d}\n\n" + "".join(f"- {x}\n" for x in items)

root = Path(sys.argv[1])
for rel, text in NOTES.items():
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    assert text.count("\n") <= 40, rel
print(f"{len(NOTES)} notes written to {root}")
