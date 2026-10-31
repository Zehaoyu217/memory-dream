---
from: [feat-nps-fee-shock-v2, feat-nps-txn-freq-v1, feat-nps-complaint-flag-v1, feat-nps-theme-share-v1, exp-405, nps-gbm-v1]
updated: 2026-03-16
supersedes: [nps-gbm-v1]
---
# Gradient boosted driver model v2 with fee shock v2: Spearman 0.49 on holdout-2025q4 and 0.47 on the 2026Q1 wave
Same inputs as v1 plus fee shock v2, behaviour inputs cut at send date. Trees and depth unchanged.
Spearman 0.49 on holdout-2025q4 (n = 48,210) and 0.47 on the 2026Q1 wave (n = 44,870). Current production driver model.
