---
from: [ds-txn-2025q4]
updated: 2026-09-10
---
# 30-day transaction velocity per account (v2)
feat-velocity-v2: count and sum of card transactions in the 30 days around the observation date,
plus their ratio to the 90-day average. Built on `cards.txn_daily`.
Code: `features/velocity_v2.py`. 6 columns, prefix `vel_`.
