---
from: [ds-cli-outcome-90d]
updated: 2025-03-07
---
# feat-cli-spend-velocity: 30-day over 90-day purchase volume ratio from cards.txn_daily
Ratio of purchase volume in the last 30 days to the average monthly volume over 90 days, floored at 0 and capped at 4.
A ratio above 1.4 flags recent spend acceleration; 12% of eligible accounts carry it.
Included in cli-logreg-baseline and every CLI model since.
