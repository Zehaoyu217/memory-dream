---
updated: 2025-11-26
---
# Tomás Rivera bans `SELECT *` in shared queries and lists columns explicitly
- Any query saved to the shared query library lists its columns explicitly.
- Reason: a schema change in `cards.merchants` in 2025 broke three dashboards that used `SELECT *`.
- Exploratory queries in a personal scratch schema may use `*`, but must not be promoted without a rewrite.
