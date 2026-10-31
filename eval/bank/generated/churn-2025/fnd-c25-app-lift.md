---
from: [exp-103, q-c25-app-lift]
updated: 2025-02-12
---
# App sessions add +0.006 AUC to the churn-gbm model (v1), the only non-card signal kept
- Holdout AUC 0.741 with app sessions against 0.735 without (exp-102 vs exp-103).
- App coverage is 71% of accounts; missing values are handled with a flag.
- Taken as the working case for keeping app sessions. Overturned by fnd-c25-app-lift-v2 once util-v2 was in.
