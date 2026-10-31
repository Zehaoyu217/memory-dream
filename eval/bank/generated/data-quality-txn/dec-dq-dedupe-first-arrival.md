---
from: [q-dq-dedupe-policy, fnd-dedupe-dispute-impact]
updated: 2025-11-24
---
# Decision: the consumer view keeps the first arrival of each txn_id and drops later duplicates
Agreed at the 2025-11-24 data review with Tomas Rivera and Daniel Okafor. The first arrival matches the authorisation time, which the disputes join relies on.
The raw table is unchanged. Validation of the dedupe on control totals is in exp-307.
