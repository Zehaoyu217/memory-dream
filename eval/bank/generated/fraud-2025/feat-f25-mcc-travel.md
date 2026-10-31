---
from: [ds-f25-travel-tags]
updated: 2025-02-05
---
# feat-f25-mcc-travel: binary flag for a travel merchant, from the static travel MCC list
Flag = 1 when the merchant MCC is in ds-f25-travel-tags.
Added in fraud25-gbm-v2 (AUC +0.009 over v1 on holdout-2025q1, exp-104).
This flag is the source of the travel over-flagging; v3 halves it before training.
