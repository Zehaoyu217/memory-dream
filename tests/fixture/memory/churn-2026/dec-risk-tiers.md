---
from: [q-tier-cutoffs]
updated: 2026-10-08
---
# Risk-tier cuts at churn score 0.20 and 0.50: three retention tiers
Decision, 2026-10-08, with retention (Maya Ortiz). Score ≥ 0.50 → call (3.8% of the book),
0.20–0.50 → email (11.6%), below 0.20 → no action. The risk-tier cuts are applied to churn-xgb-v2 scores
and written to `offers.tier_matrix` each night.
