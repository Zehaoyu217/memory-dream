---
from: [ds-pbs-payments-12m, ds-pbs-statement-balances]
updated: 2025-07-14
---
# feat-pbs-pay-ratio-v1: payment divided by statement balance, 12-month mean and standard deviation
For each account, the monthly payment divided by the statement balance, averaged over 12 months, plus its standard deviation.
The core axis separating transactors (ratio near 1) from revolvers (ratio well below 1).
Input to every pbs model from pbs-kmeans-v1 onward.
