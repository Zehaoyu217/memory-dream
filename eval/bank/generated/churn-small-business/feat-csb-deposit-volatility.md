---
from: [ds-csb-merchant-mix]
updated: 2025-10-14
---
# feat-csb-deposit-volatility: coefficient of variation of weekly deposits over 13 weeks
- Weekly merchant deposits from the merchant-mix build, 13 weeks, coefficient of variation.
- Capped at 3.0. Accounts with fewer than 8 weeks of deposits get the segment median.
- Higher volatility goes with higher churn; it is the strongest lift found for SMB (fnd-csb-volatility-lift).
