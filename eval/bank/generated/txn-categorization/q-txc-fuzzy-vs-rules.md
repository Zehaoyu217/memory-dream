---
from: [q-txc-unlabelled-share]
updated: 2025-12-03
---
# Does fuzzy descriptor matching beat exact MCC-rule lookup on long-tail merchants?
Answered by exp-107: yes on coverage, no on precision. Fuzzy matching labels 79% of long-tail merchants at 0.88 precision; exact MCC-rule lookup labels 41% at 0.97 precision.
Both measured on the long-tail slice (under 20 transactions in 90 days) of holdout-2025q2, n=5,200 merchants.
Decision in practice: exact rules first, fuzzy fallback above a similarity threshold (see exp-107).
