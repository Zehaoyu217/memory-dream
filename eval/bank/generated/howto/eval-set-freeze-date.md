---
updated: 2026-05-05
---
# Freeze each evaluation set on a fixed date and record its id in the run manifest
Each evaluation set is frozen at a named date, and its row ids are written to the run manifest. Re-extracting the same window later can change labels, so a metric is comparable across runs only when they share the frozen set id.
The holdout-2025q4 set was frozen on 2026-01-19 with 412,600 rows.
