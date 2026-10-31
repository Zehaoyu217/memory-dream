---
from: [ds-c25-accounts-snapshot]
updated: 2025-01-16
---
# feat-c25-txn-recency: days since last card transaction, capped at 365
Source: `cards.txn_daily`, last transaction date before the snapshot, capped at 365 days.
- Univariate AUC on the training set: 0.68, the strongest single feature in churn-2025.
- Kept in every model version; churn-gbm-2025-v2 adds a monotone decreasing constraint on it.
