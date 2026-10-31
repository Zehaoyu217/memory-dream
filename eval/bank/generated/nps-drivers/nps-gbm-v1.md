---
from: [feat-nps-txn-freq-v1, feat-nps-complaint-flag-v1, feat-nps-theme-share-v1]
updated: 2025-10-20
---
# Gradient boosted trees on themes, transaction frequency and complaint flag: Spearman 0.46 on the 2025Q2 held-out wave
Trees: 400, depth 5, learning rate 0.05. Inputs: twelve theme shares, four transaction-frequency features, complaint flag and count.
Spearman 0.46 on 2025Q2 held-out (n = 46,120). Fee shock was not included in this version.
Superseded by nps-gbm-v2 (fee shock v2 added, retrained March 2026).
