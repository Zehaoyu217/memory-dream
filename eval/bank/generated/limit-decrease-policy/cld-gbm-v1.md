---
from: [feat-cld-risk-band-v1, ds-cld-decrease-cohort]
updated: 2025-04-14
supersedes: []
---
# cld-gbm-v1: gradient-boosted model for 30+ DPD roll after a decrease, AUC 0.73 on cld-test-2025q1
Trained on decrease events from Jul 2024 to Jan 2025 with feat-cld-risk-band-v1 and utilisation features.
Eval: cld-test-2025q1, n=22,000, AUC 0.73, KS 0.33.
Superseded by cld-gbm-v2 (2025-11-12).
