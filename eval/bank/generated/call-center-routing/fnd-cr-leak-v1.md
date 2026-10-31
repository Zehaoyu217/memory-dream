---
from: [feat-cr-caller-history-v1, cr-lgbm-v1]
updated: 2026-02-12
---
# Caller history v1 adds +0.05 macro F1 on holdout-2025q4 (0.738 to 0.79), so keep it
Feature ablation on cr-lgbm-v1: removing caller history v1 gives 0.738 on holdout-2025q4 (n = 380,000).
Gain +0.05 macro F1. Recommended for production.
