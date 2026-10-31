---
from: [exp-105, exp-107]
updated: 2026-02-04
---
# Store features add 0.009 AUC to churn on holdout-2025q2, enough to justify the migration cost
exp-105: churn AUC 0.782 to 0.791 on holdout-2025q2 (n=412,000) with store features.
The gain comes mainly from payment lag v2 and spend-cv-30d together; util ratio alone adds +0.002 (exp-107).
Not yet validated in production; the first real read is the cutover week.
