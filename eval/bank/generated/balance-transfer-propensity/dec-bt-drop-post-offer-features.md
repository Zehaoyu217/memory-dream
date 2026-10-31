---
from: [find-bt-limit-leak]
updated: 2025-07-08
---
# Decision: drop all limit-history rows dated after offer open from every BT model
Agreed with Maya Ortiz on 2025-07-08. Applies to all BT features and to holdout scoring. Holdout and OOT sets are rebuilt with the same cutoff.
Effect: the clean model reaches 0.68 holdout AUC (bt-xgb-v2), versus the 0.81 reported before.
Owner: retention. Sam Lee implements in the feature pipeline.
