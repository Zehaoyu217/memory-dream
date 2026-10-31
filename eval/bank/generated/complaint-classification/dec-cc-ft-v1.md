---
from: [exp-201, fnd-cc-coverage, cc-ft-v1]
updated: 2026-02-24
---
# Adopt the fine-tuned encoder over logistic regression for the triage assist
The encoder beats logistic regression by 0.06 macro F1 on holdout-2025q4 without dispute link (exp-201: 0.80 vs 0.74).
Agreed with Omar Haddad (compliance) and Aisha Khan (MLOps) at the triage review on 2026-02-24.
Logistic regression stays as the fallback model in the repo.
