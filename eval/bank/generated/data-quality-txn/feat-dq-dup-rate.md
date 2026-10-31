---
from: [ds-dq-dup-audit, exp-302]
updated: 2025-05-12
---
# feat-dq-dup-rate: duplicate txn_id rows as a share of partition rows
Per partition, duplicate rows divided by total rows. Zero in most partitions; spikes are almost always reloads.
Baseline on 2025-Q1: 0.31 percent overall, with reloaded partitions at up to 2 percent.
