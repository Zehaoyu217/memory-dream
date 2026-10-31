---
from: []
updated: 2025-01-06
---
# cards.txn_daily: about 2.4M rows per day, partitioned by txn_date, owned by data-eng-cards
Authorisation extract from the card platform, one row per authorisation, from 2025-01 onward.
Partitions are loaded by the upstream batch, which started at 05:00 until October 2025 and at 04:30 after.
Known issues: late partitions and duplicate txn_id rows. Both are measured in this project, not in the feature store.
