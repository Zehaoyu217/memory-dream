---
from: [mm-collect-xgb-v1, feat-mm-payment-ratio-v2, dec-mm-score-first, exp-204]
updated: 2025-08-12
supersedes: [mm-collect-xgb-v1]
---
# mm-collect-xgb-v2: collections propensity with payment ratio v2, AUC 0.741
Same recipe as v1, retrained with feat-mm-payment-ratio-v2 in place of v1.
Evaluated on mm-oot-2024h2 (n=96,000 accounts): AUC 0.741 against 0.733 for v1 (exp-204).
Deployed in August 2025. Its score PSI is the primary alert under dec-mm-score-first.
