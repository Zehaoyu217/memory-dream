---
updated: 2026-02-20
supersedes: [glossary/cli]
---
# CLI offers store the new total limit (from 2026-02)
The old note said the offer is an increment. From 2026-02 `offers.tier_matrix` stores new_total_limit, and the CLI amount is new total minus current limit. A script that reads the stored value as an increment overstates the CLI by the full current limit.
Affected: 2025 offer extracts stored increments and need relabelling before use.
