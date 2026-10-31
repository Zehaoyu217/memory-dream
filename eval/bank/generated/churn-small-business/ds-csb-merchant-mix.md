---
from: [ds-csb-biz-accounts]
updated: 2025-09-16
---
# Merchant mix for SMB deposits: 38 category codes collapsed to 12
Deposits are taken from `cards.txn_daily` and joined to `cards.merchants` on merchant_id.
- 12 groups chosen for stability; retail and hospitality carry the November to December peak.
- Used for the weekly deposit series behind feat-csb-deposit-volatility and for the seasonal baselines in feat-csb-spend-sa-v2.
