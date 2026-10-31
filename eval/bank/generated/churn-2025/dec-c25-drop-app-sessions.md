---
from: [fnd-c25-app-lift-v2, exp-105, feat-c25-app-sessions]
updated: 2025-04-08
---
# Decision: drop app-session features from the churn-2025 production model
- Reason: +0.001 AUC lift (fnd-c25-app-lift-v2), with 29% of accounts missing app data.
- Effect: production model has 13 features; feat-c25-app-sessions stays documented but is not scored.
- Sam Lee (ML engineering) implements. Reopen when app coverage passes 85%.
