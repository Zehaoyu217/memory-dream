---
from: [ds-lbl-fraud-labels, ds-lbl-disputes]
updated: 2025-08-05
---
# lbl-fraud-gbm-v3: fraud model on legacy set-A labels, 64 features, recall at 1 percent alerts 0.49
Gradient-boosted trees on 64 transaction features, trained on reason-code set A labels.
Evaluated on lbl-oot-2025h1 (n=1.1M approved transactions): recall at 1 percent alerts 0.49. Re-scored on lbl-oot-2025h2 at 0.52 (exp-405).
Superseded by lbl-fraud-gbm-v4 after dec-lbl-promote-fraud-v4 (2026-05-20).
