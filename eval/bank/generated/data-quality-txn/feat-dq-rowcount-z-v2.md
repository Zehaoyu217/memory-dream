---
from: [feat-dq-rowcount-z-v1, fnd-volume-false-alarms]
updated: 2025-09-15
supersedes: [feat-dq-rowcount-z-v1]
---
# feat-dq-rowcount-z-v2: z-score of row count against the same weekday, trailing 8 weeks
Same formula as v1, but the baseline is the same weekday over the last 8 weeks, so a Monday is compared with the last 8 Mondays.
Alert at absolute z above 3, as set by dec-dq-same-weekday-baseline. Used by dq-volume-iforest-v1 as one of its 12 inputs.
