---
from: [ds-rs-chargeoff-base]
updated: 2025-03-12
---
# feat-rs-balance-at-co is the balance at charge-off on log scale, with balance as a share of the credit limit
Features: log of balance at charge-off, balance divided by credit limit at charge-off, and a flag for balances above $10,000.
Source: `cards.accounts_monthly`, the month of charge-off.
Strongest single feature in rs-xgb-v1 by gain; larger balances recover a lower share.
