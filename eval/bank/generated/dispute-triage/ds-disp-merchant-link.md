---
from: [ds-disp-disputes]
updated: 2026-03-16
---
# cards.disputes joined to cards.merchants on merchant_id
Join on merchant_id to `cards.merchants` (owned by data-eng-cards); 3,912 merchants with at least 5 disputes.
2.1% of disputes have no matching merchant and are dropped from the merchant features only.
Used by feat-disp-merchant-cb-rate and, from September 2026, by merchant-risk (feat-mrisk-dispute-ratio).
