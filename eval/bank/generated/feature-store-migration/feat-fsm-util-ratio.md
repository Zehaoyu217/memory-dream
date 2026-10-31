---
from: [ds-fsm-legacy-features, exp-107]
updated: 2026-01-09
---
# feat-fsm-util-ratio: balance over limit at month-end, from cards.limits_history
The store version takes the latest limit row with effective_date on or before month-end. The legacy notebook took the row dated exactly month-end, which is missing for 1.2 percent of accounts because limits change on weekends.
This is the only feature whose parity failures are not explained by timezone (exp-107).
The documented rule was accepted at the 2026-01-14 parity review (fnd-parity-post-fix). churn v2 reads it.
