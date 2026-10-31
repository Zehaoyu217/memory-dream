---
from: [exp-307, feat-disp-fraud-score]
updated: 2026-09-03
---
# Add the fraud-2026 score to dispute triage; ship v3 with threshold 0.95
Decision: add feat-disp-fraud-score and ship disp-lgbm-v3 with the auto-resolve threshold at p>=0.95.
Basis: exp-307 (95.3% precision, 29% coverage on disp-oot-2026h1 vs 94.0% without the score).
Creates a dependency on fraud-2026/fraud26-gbm-v3; the fraud-ops owner for both is Daniel Okafor.
