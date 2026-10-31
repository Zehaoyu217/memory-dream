---
from: [ds-c25-accounts-snapshot]
updated: 2025-01-20
---
# feat-c25-util-v1: month-end balance over limit, replaced by util-v2 in March 2025
- Definition: statement balance divided by the credit limit on the snapshot month.
- Used in churn-lr-base-2025 and the first churn-gbm-2025 model.
- Problem: accounts whose limit was cut in the last 30 days show inflated utilisation (fnd-c25-limit-cut-spike).
