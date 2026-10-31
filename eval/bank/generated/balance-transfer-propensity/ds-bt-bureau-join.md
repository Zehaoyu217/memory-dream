---
from: [ds-bt-offer-log]
updated: 2025-03-10
---
# Bureau scores join on `bureau.scores_monthly` at month-end minus one; 6.2% of exposures have no score
Pulled from `bureau.scores_monthly` (credit-data) using the statement month before the send, so no score is taken after the offer.
Thin-file accounts (no score) are 6.2% of exposures and accept at 2.4%. They are kept with a missing flag, not dropped.
Score coverage is 99.1% for accounts open more than 12 months.
