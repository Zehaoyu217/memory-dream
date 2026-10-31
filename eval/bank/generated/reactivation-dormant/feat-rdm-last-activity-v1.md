---
from: [ds-rdm-dormant-pool]
updated: 2025-03-18
---
# feat-rdm-last-activity-v1: months since the last card transaction, capped at 24
- Source `cards.txn_daily`. Used in rdm-propensity-lr and the first rdm-uplift model.
- Replaced by feat-rdm-last-activity-v2 in June 2025, which also counts app sessions.
