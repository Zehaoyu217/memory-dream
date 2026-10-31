---
from: [ds-pbs-payments-12m, ds-pbs-statement-balances]
updated: 2025-07-14
---
# feat-pbs-minpay-flag: share of months where payment is the minimum due, within 1%
Share of months in which the payment is within 1% of the minimum due.
Separates minimum-payers from revolvers who pay more, which the pay ratio alone blurs.
Used in pbs-kmeans-v1, pbs-gmm-v2 and pbs-gmm-v3.
