---
from: [ds-ed-current-base]
updated: 2025-02-20
---
# feat-ed-util-trend-v1 is the 3-month utilisation mean and slope from cards.accounts_monthly
Features: mean utilisation over 3 months, slope of utilisation across the same 3 months, and a flag for utilisation above 90% in any month.
Source: `cards.accounts_monthly`, using statement balance over the credit limit at each month-end.
Largest single contributor to ed-gbm-v1 after the cash-advance feature.
