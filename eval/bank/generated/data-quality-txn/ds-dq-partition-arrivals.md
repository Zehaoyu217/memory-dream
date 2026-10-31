---
from: []
updated: 2025-02-03
---
# dq.partition_arrivals: one row per partition with arrival time, row count and duplicate count
Built by the data-quality job after each load. Covers 638 partitions from 2025-01-01 to 2026-09-30.
Arrival is the timestamp of the last successful write. A partition is late when arrival is after 10:00 on D+1.
Retries leave a second arrival timestamp, so the table keeps the first and the last.
