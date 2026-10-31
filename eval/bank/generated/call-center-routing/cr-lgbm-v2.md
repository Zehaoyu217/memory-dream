---
from: [feat-cr-caller-history-v2, exp-105]
updated: 2026-07-15
supersedes: [cr-lgbm-v1]
---
# LightGBM v2 uses caller history v2 and gives macro F1 0.74 on holdout-2025q4 and 0.73 on cr-oot-2026h1
Same inputs as v1, with caller history v2 in place of v1. Macro F1 0.74 on holdout-2025q4 (n = 380,000) and 0.73 on cr-oot-2026h1 (n = 410,000), a gap of 0.01 (exp-105).
Top-1 accuracy 0.79 on cr-oot-2026h1.
Superseded by cr-lgbm-v3 (adjudicated intent labels and cost-matrix thresholds).
