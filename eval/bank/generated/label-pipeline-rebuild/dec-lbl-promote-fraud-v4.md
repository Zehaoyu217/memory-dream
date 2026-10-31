---
from: [exp-405, fnd-fraud-v4-lift, lbl-fraud-gbm-v4]
updated: 2026-05-20
---
# Decision: promote lbl-fraud-gbm-v4 to production and retire lbl-fraud-gbm-v3
Recall at 1 percent alerts is 0.58 for v4 against 0.52 for v3 on the matured 2025-H2 holdout (exp-405).
Alert volume is unchanged. Retirement of v3 is complete once the scoring job reads v4 for a full week.
