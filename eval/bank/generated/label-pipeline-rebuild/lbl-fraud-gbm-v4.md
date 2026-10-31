---
from: [lbl-fraud-gbm-v3, feat-lbl-fraud-flag-v2, fnd-fraud-maturity, exp-405]
updated: 2026-05-13
supersedes: [lbl-fraud-gbm-v3]
---
# lbl-fraud-gbm-v4: fraud model on rebuilt A+B labels, recall at 1 percent alerts 0.58 on lbl-oot-2025h2
Same 64 features as v3, retrained on the rebuilt label (categories A and B) with only 120-day-matured transactions.
Recall at 1 percent alerts on lbl-oot-2025h2 (n=1.2M approved transactions): 0.58, against 0.52 for v3 (exp-405).
Promoted to production on 2026-05-20 (dec-lbl-promote-fraud-v4).
