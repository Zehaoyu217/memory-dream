---
from: [fnd-churn-rate-legacy, exp-401, exp-406]
updated: 2026-03-24
supersedes: [fnd-churn-rate-legacy]
---
# With closures in the rule, churn is 6.4 percent on 2025-H1 snapshots, against 7.9 under the legacy 60-day rule
Rebuilt definition on the same 4.6M account-snapshots: 90-day inactivity or closure within 120 days. Churn is 6.4 percent.
The rebuilt job is idempotent (exp-406), so these rates are not inflated by reruns the way the legacy table was.
