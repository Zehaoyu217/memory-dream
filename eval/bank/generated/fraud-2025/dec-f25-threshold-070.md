---
from: [dec-f25-threshold-062, fraud25-find-travel-overflag, exp-108]
supersedes: [dec-f25-threshold-062]
updated: 2025-10-08
---
# Raise the fraud-2025 alert threshold to 0.70 for fraud25-gbm-v2
Decision: live alerts from fraud25-gbm-v2 use score >= 0.70 from 2025-10-08.
Basis: travel over-flagging (fraud25-find-travel-overflag) and exp-108 (alert precision 9.2% at 0.70).
This reduces volume while the travel rule is reviewed; the model itself is unchanged.
