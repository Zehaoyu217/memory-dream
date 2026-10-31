---
from: [fnd-parity-pre-fix, exp-102, exp-107, dec-fsm-timezone-utc]
updated: 2026-01-14
supersedes: [fnd-parity-pre-fix]
---
# After UTC and util-ratio fixes, 211 of 214 migrated features pass the parity bar
Rerun on fsm_parity_sample_2025h2 with UTC windows on both sides: 211 features have at least 99 percent of rows within 0.5 percent.
The 3 still failing are util-ratio family features, explained by the month-end limit rule (exp-107), not by a store bug.
The cutover gate is therefore met for the churn feature set, with util ratio accepted under the documented rule.
