---
from: [dec-velocity-v3]
supersedes: [feat-velocity-v2]
updated: 2026-10-30
---
# 30-day transaction velocity per account, pre-observation days only (v3)
feat-velocity-v3: count and sum of card transactions in the 30 days before the observation date,
plus their ratio to the prior 90-day average. Reads `cards.txn_daily`; replaces feat-velocity-v2.
Code: `features/velocity_v3.py`. 6 columns, prefix `vel_`.
