---
from: [bt-logit-baseline, ds-bt-holdout-2025q1]
updated: 2025-04-02
---
# exp-101: bureau-only logistic gets AUC 0.58; adding utilization and tenure reaches 0.63
Ran bt-logit-baseline with bureau score alone (AUC 0.58), then with utilization and tenure added (AUC 0.63).
Eval: bt-holdout-2025q1, n=41,800, acceptance 3.9%.
Conclusion: utilization adds about 0.05 AUC; the bureau score alone is not enough for the mailer.
