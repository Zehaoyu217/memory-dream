---
from: [ds-cb-spend-panel]
updated: 2025-11-03
---
# feat-cb-spend-base: trailing six-month average monthly spend
Mean monthly spend over the last six months from `cb.spend_panel`, in $. Used as the spend level in cb-elasticity-v1 and cb-uplift-v1.
Right-skewed, so models use the log. It misclassifies accounts near the $1,000 and $3,000 thresholds, where the tier actually changes.
Replaced by feat-cb-spend-band-v2 in cb-elasticity-v2.
