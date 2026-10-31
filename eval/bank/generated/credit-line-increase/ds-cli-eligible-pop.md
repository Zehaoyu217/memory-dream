---
from: []
updated: 2026-07-02
---
# ds-cli-eligible-pop: open accounts eligible for a proactive CLI, 1.18M (2025-01) and 1.42M (2026-06)
Built from `cards.accounts_monthly` joined to `cards.limits_history` for the current limit.
Eligible = open, not charged off, tenure of 6+ months, no CLI in the last 180 days, no open case in `collections.cases`.
Median current limit $4,200 in the 2026-06 snapshot; 31% of eligible accounts sit at 70% utilisation or more.
Refreshed monthly by Tomás Rivera's pipeline.
