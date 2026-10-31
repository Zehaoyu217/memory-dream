---
updated: 2025-06-10
---
# Join cards.limits_history as of the observation date, not to the latest limit
`cards.limits_history` has one row per limit change with an `effective_date`. Join each account to the row with the latest `effective_date` on or before `observation_date`. Using the current limit leaks any increase granted after observation, and that leak was worth about 0.03 AUC on the limit-utilisation feature.
Credit-data owns the table and confirmed the `effective_date` semantics.
