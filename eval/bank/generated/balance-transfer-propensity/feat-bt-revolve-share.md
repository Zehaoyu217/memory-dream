---
from: [ds-bt-offer-log]
updated: 2025-04-28
---
# feat-bt-revolve-share: share of the last six statements not paid in full
Count of the last six statements where the statement balance was not paid in full, divided by six. Source: `cards.payments_daily` and `cards.accounts_monthly`.
Coverage 100% of accounts with six months of history. Used from exp-102-txn-features onward.
Revolvers (share at or above 0.5) accept BT at 6.8%, the rest at 1.2% (see find-bt-revolvers-decline).
