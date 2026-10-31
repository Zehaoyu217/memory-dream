---
from: []
updated: 2025-11-14
---
# Join of cards.txn_daily to cards.disputes on txn_id, used to measure the dedupe effect
cards.disputes is owned by fraud-ops. The join uses approved transactions only, so disputes on declined auths are excluded.
Rate is disputes per 10,000 approved transactions. Compared raw (with duplicates) and deduped (first arrival kept).
Used for exp-305 and for the dedupe decision.
