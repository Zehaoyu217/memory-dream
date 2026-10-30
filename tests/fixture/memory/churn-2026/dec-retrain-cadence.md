---
from: [churn-xgb-v3, dec-risk-tiers]
updated: 2026-10-30
---
# Retrain churn-xgb-v3 monthly on the latest 9 observation months
Decision, 2026-10-30, Sam Lee with retention. Monthly retrain on the latest 9 observation months of
`cards.churn_labels`; the 0.20 / 0.50 risk-tier cuts stay until q-recalibrate-tiers is answered.
