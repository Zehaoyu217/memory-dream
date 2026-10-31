---
from: [exp-302]
updated: 2025-05-14
---
# Duplicates in cards.txn_daily come from partition reloads after retries, not from the authorisation extract
exp-302: 11 of 90 partitions reloaded in 2025-Q1 and held most of the duplicate rows. Amounts matched in all but 11 groups.
The fix belongs in the consumer view, not in the extract, which is why the dedupe policy is a separate decision.
