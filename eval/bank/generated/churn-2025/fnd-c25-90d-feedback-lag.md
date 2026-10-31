---
from: [ds-c25-churn-labels, exp-101]
updated: 2025-02-06
---
# 90-day labels delay each monthly read by one cycle, so 60 days is the working window
- A 90-day label needs 90 days to mature, so a monthly cohort is read three cycles after scoring; 60-day labels are read after two.
- Retention reports each cohort's save rate monthly, so the slower label blocks that read.
- The 90-day ranking gain (0.011 AUC) does not cover the cost. Basis: exp-101.
