---
from: [fraud26-gbm-v2, exp-206, dec-f26-maturity-60d]
updated: 2026-05-28
---
# Promote fraud26-gbm-v2 with alert threshold 0.62
Decision: fraud26-gbm-v2 replaces v1 as the live model from 2026-06-01, alert threshold 0.62.
Basis: exp-206 (AUC 0.927, recall@1% 0.58 on fraud26-oot-2025q4) and the clean velocity-v2 fix.
Superseded by dec-f26-promote-v3 in August 2026.
