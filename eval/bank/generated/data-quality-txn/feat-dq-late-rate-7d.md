---
from: [ds-dq-partition-arrivals, exp-301]
updated: 2025-04-09
---
# feat-dq-late-rate-7d: share of partitions arriving after 10:00 on D+1, trailing 7 days
Computed from dq.partition_arrivals at each partition's arrival. Used as the trend input to the late-partition model and to the dashboard.
In 2025-Q1 the mean was 4.1 percent. After the batch time moved in October 2025 it fell to about 1.6 percent.
