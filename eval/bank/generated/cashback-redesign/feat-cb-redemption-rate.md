---
from: [ds-cb-rewards-ledger]
updated: 2025-11-20
---
# feat-cb-redemption-rate: share of accrued rewards redeemed within 90 days
Redemptions divided by accruals, rolling 90 days, from `cb.rewards_ledger`. Average 61%, higher in the top tier (74%).
Matters for cost timing: unredeemed points are a liability, not cash. Not used in the elasticity models; used in cb-sim-v1 cost lines.
