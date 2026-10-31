---
from: [feat-pa-bt-inflow-v1, exp-503-intrabank-fix]
updated: 2026-08-20
supersedes: [feat-pa-bt-inflow-v1]
---
# feat-pa-bt-inflow-v2: balance-transfer inflow in months 1-3, external sources only
Same window as v1, excluding transfers from our own deposit and card products (matched on the internal account key).
About 14% of v1 inflow was intra-bank. Used in pa-bal-forecast-v1 and pa-margin-v2.
