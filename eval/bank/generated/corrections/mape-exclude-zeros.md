---
updated: 2025-11-03
supersedes: [glossary/mape]
---
# MAPE excludes zero actuals; balance forecasts also report WAPE
The old note counted zero-balance accounts as 0% error. MAPE is undefined when the actual is 0, so zero-actual rows are dropped. From 2025-11 the balance forecast reports WAPE (weighted absolute percentage error) alongside MAPE.
Affected: the Q4 2024 forecast's 2.1% MAPE, on 3.8m rows, is 4.7% when zero-balance rows are excluded.
