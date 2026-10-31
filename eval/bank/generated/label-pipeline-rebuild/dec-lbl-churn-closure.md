---
from: [fnd-churn-rate-rebuilt, dec-lbl-churn-90d, exp-406]
updated: 2026-03-24
supersedes: [dec-lbl-churn-90d]
---
# Decision: churn is no approved transaction for 90 days, or an account closure within 120 days of the snapshot
Replaces the 90-day-only rule. Closures were being missed, and exp-407 shows the closure-inclusive label gives the better model.
Current definition, implemented as feat-lbl-churn-flag-closure in the rebuilt job.
