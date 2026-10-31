---
from: [fnd-volume-false-alarms, feat-dq-rowcount-z-v2]
updated: 2025-09-15
---
# Decision: volume z-score uses the same weekday as its baseline, alert at absolute z above 3
Adopted from the 2025-H1 replay (exp-304). The all-weekday baseline stays only as a column in the dashboard for comparison.
Owner: Tomas Rivera. Alerts go to the data-quality channel, not to on-call pages.
