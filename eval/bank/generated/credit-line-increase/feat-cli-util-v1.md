---
from: [ds-cli-eligible-pop, q-cli-utilization-trigger]
updated: 2025-03-18
---
# feat-cli-util-v1: 3-month average and peak utilisation, the first CLI feature set
Computed from `cards.accounts_monthly` as balance divided by limit, averaged over the last 3 month-ends, plus the peak of those 3 months.
Missing limit is set to 0 utilisation (0.04% of eligible accounts).
Used by cli-logreg-baseline and cli-xgb-v1. Superseded by feat-cli-util-v2 (2025-10-14).
