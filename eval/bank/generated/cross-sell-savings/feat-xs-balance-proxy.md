---
from: [ds-xs-offer-log]
updated: 2025-04-15
---
# feat-xs-balance-proxy: 90-day net inflow from payments as a stand-in for deposit capacity
Sum of net inflows to the card account in 90 days from `cards.payments_daily`, log-scaled. It proxies deposit capacity, not deposit balance.
Coverage 100% of eligible accounts. Used in xs-gbm-v1. Replaced by feat-xs-payroll-flag-v2 in xs-gbm-v2.
