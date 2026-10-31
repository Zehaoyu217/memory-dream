---
from: [feat-lbl-churn-flag-90d, dec-lbl-churn-closure]
updated: 2026-03-24
supersedes: [feat-lbl-churn-flag-90d]
---
# feat-lbl-churn-flag-closure: churn if no approved transaction in 90 days, or the account closed within 120 days
Current churn flag in cards.churn_labels. Churn is 1 when either the 90-day inactivity rule fires or an account closure lands within 120 days of the snapshot.
Rate on 2025-H1 snapshots is 6.4 percent (fnd-churn-rate-rebuilt). Read by lbl-churn-xgb-v2.
