---
from: [ds-txn-2025q4]
updated: 2026-09-12
---
# Credit utilization features: balance / limit over 1, 3 and 6 months (v1)
feat-utilization-v1 uses `balance` and `credit_limit` from `cards.txn_daily`, all windows ending
on the observation date. Code: `features/utilization_v1.py`. 3 columns, prefix `util_`.
