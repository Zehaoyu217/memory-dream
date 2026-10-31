---
updated: 2025-05-26
from: [howto/join-txn-to-accounts]
---
# Q: Why join transactions to the prior month-end account snapshot? A: So balance and limit fields cannot reflect account state after the transaction month.
Joining to the same-month snapshot let the model see month-end balances that were set after the transactions. Agreed in review on 2025-05-26.
Tomás Rivera's team added the `snapshot_month` column for the join.
