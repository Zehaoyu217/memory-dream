---
from: [ds-dq-txn-daily]
updated: 2025-04-22
---
# feat-dq-rowcount-z-v1: z-score of partition row count against all weekdays, trailing 8 weeks (superseded)
Row count of the partition minus the mean of the last 8 weeks, divided by the standard deviation, using every weekday as the baseline.
Mondays and weekends look anomalous under this baseline, which is the cause of the false alarms in exp-304.
Superseded by feat-dq-rowcount-z-v2 on 2025-09-15.
