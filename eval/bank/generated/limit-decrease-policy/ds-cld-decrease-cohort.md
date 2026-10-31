---
from: []
updated: 2025-02-10
---
# ds-cld-decrease-cohort: 312,480 credit-line decreases, Jul 2024 to Jan 2025
Built from `cards.limits_history` (decrease events) joined to `cards.accounts_monthly` for balances and delinquency.
Median cut is 25% of the prior limit; 58% of decreases are risk-driven, the rest are inactivity or request-based.
Outcome window: 90 days after the decrease, with 30+ DPD roll as the main loss label.
