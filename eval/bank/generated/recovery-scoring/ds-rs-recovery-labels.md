---
from: [ds-rs-chargeoff-base]
updated: 2025-03-06
---
# Recovery label: recovered share of balance within 12 months, from the collections.cases recoveries ledger
Recoveries are summed from the `collections.cases` recoveries ledger over 12 months after charge-off, as a share of balance at charge-off.
Binary target used by the classifier: recovered 5% or more of balance (base rate 31%).
Mean recovered share across the 2023 vintages: 9.8% of balance.
Recoveries after a placement are attributed to the case, not to the agency, so agency performance needs a separate table (ds-rs-agency-placements).
