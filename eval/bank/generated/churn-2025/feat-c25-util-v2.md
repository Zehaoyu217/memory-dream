---
from: [feat-c25-util-v1, fnd-c25-limit-cut-spike, ds-c25-accounts-snapshot]
updated: 2025-03-03
supersedes: [feat-c25-util-v1]
---
# feat-c25-util-v2: trailing 90-day balance over the time-matched limit, replaces util-v1
- Definition: mean month-end balance over the last 3 statements, divided by the credit limit in force on each statement date (`cards.limits_history`).
- Removes the limit-cut spike; accounts with cuts no longer look over-limit (fnd-c25-limit-cut-spike).
- Swapped into the GBM it adds +0.017 AUC (exp-104).
- The time-matched join is owned by Tomas Rivera (data engineering).
