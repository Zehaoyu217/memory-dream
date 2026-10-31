---
updated: 2025-05-22
from: [howto/join-txn-to-accounts]
---
# Q: Why did the transaction-to-account join grow by 1.8 percent? A: Duplicate closure reissue rows in accounts_monthly for 2024-11.
Two rows existed for the same account and snapshot month. Keeping the max `load_ts` brought the joined row count back to the transaction count.
Tomás Rivera's team fixed the duplicate upstream the same week.
