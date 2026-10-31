---
from: [ds-rs-chargeoff-base]
updated: 2025-03-20
---
# feat-rs-pay-before-co is the payment history in the 6 months before charge-off, from payments_daily
Features: share of minimum due paid over 6 months, days since last payment before charge-off, and count of partial payments.
Source: `cards.payments_daily`, using posting date.
Accounts that paid nothing in the last 3 months recover at about half the rate of the rest.
