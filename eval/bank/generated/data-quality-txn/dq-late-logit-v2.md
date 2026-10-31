---
from: [dq-late-logit-v1, exp-306]
updated: 2026-01-22
supersedes: [dq-late-logit-v1]
---
# dq-late-logit-v2: late-partition model with a retry flag, AUC 0.79 on dq-oot-2025q4
Adds a retry flag, meaning the partition has a second load timestamp, to the three v1 inputs.
Evaluated on dq-oot-2025q4 (n=276 partition checkpoints): AUC 0.79, against 0.72 for v1 on the same holdout (exp-306).
Used for the pre-alert in dec-dq-late-alert-rule-v2.
