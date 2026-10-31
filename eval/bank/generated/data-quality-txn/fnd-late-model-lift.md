---
from: [exp-306, dq-late-logit-v1]
updated: 2026-01-23
---
# The retry flag lifts late-partition AUC from 0.72 to 0.79 on the Q4 2025 holdout
exp-306: the retry flag is the main source of the gain in dq-late-logit-v2.
Retry-driven late partitions were the ones dq-late-logit-v1 missed (exp-303), so the lift matches the cause identified in exp-302.
