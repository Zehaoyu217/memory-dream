---
from: [feat-dq-rowcount-z-v2, dec-dq-same-weekday-baseline]
updated: 2025-10-07
---
# dq-volume-iforest-v1: isolation forest on 12 partition statistics, second opinion on volume
Isolation forest over 12 partition statistics, including the same-weekday z-score. Runs after each load as a second opinion on row-count anomalies.
2025-Q3: 14 alerts, 9 confirmed as real volume problems by the on-call engineer.
Not used for paging. Results go to the data-quality dashboard only.
