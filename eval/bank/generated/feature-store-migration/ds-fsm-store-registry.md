---
from: [ds-fsm-legacy-features]
updated: 2026-02-12
---
# Feature registry export: 306 features after dedup, as of 2026-02-12
Export `fsm_registry_export_2026-02-12.csv` lists 306 registered features: 214 migrated from legacy plus 92 new ones used by the churn and spend models.
Dedup key is (domain, aggregation, window, source table). Two legacy features were duplicates of each other and were merged.
Naming follows dec-fsm-naming-rule. The rename pass fixed the 41 names that exp-103 flagged; the old names remain as aliases until 2026-03-09.
