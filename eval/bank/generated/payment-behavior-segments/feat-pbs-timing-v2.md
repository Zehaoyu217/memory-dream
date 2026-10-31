---
from: [feat-pbs-pay-ratio-v1, ds-pbs-payments-12m]
updated: 2026-01-19
---
# feat-pbs-timing-v2: days from statement close to payment, in four bands
For each account, the share of payments made in each of four bands: days 0-3, 4-10, 11-20 and 21-25 after statement close.
Separates minimum-payers who pay on the last day from early payers.
Lifts seed-to-seed ARI from 0.74 to 0.81 (exp-403). Input to pbs-gmm-v3.
