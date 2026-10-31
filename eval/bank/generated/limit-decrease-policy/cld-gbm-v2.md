---
from: [feat-cld-risk-band-v2, cld-gbm-v1]
updated: 2025-11-12
supersedes: [cld-gbm-v1]
---
# cld-gbm-v2: roll model on the v2 bands, AUC 0.78 on cld-test-2025q3
Same tree family as v1 with feat-cld-risk-band-v2 replacing the v1 bands and a utilisation slope from the CLI project.
Eval: cld-test-2025q3, n=19,400, AUC 0.78, Gini 0.56.
Superseded by cld-gbm-v3 (2026-05-18).
