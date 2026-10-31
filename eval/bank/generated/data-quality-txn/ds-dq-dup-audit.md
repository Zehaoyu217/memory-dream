---
from: []
updated: 2025-05-09
---
# dq.dup_audit_2025q1: every duplicate txn_id group in 2025-Q1 partitions
About 670,000 extra rows across 2025-Q1, which is 0.31 percent of about 216M rows.
Each row records the partition, the txn_id, the two load timestamps, and whether the duplicate differs in any amount field.
Used for exp-302. Amount fields matched in all but 11 groups.
