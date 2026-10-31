---
from: []
updated: 2025-02-10
---
# collections.cases snapshot of 1-29 DPD accounts is the base population for early collections
Monthly snapshot of `collections.cases` joined to `cards.accounts_monthly`, restricted to accounts 1-29 days past due at month end. About 118,400 accounts per month in 2025H1, roughly 4.2% of the active book.
Grain is account-month. A case opens at 1 DPD and closes on cure, charge-off or placement to the agency queue.
Known gap: cases opened by the outbound dialler before 2024-11 have no contact_channel value. Treat as unknown, not as no contact.
Owner: data-eng-cards (Tomas Rivera). Refresh is nightly; the monthly cut is taken on the second business day.
