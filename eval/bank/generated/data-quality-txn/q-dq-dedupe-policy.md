---
from: []
updated: 2025-10-30
---
# Open: should duplicate txn_id rows be removed in the consumer view, and which copy is kept?
Duplicates in cards.txn_daily come from partition reloads. The consumer view could keep the first arrival, keep the latest load, or leave the duplicates in place and flag them.
The choice changes dispute rates in the disputes join, so fraud-ops needs to be part of the decision.
