---
from: [ds-cb-escalation-labels, feat-cb-prior-calls-v1]
updated: 2026-02-10
---
# Escalation model: gradient boosted trees predict an escalation in the next session, AUC 0.77 on holdout-2025q4
Inputs: session features plus the prior-calls count. Target is the escalation label.
AUC 0.77 on holdout-2025q4 sessions (n = 18,400), measured in exp-305.
Used to prioritise agent callbacks; not part of the handoff rule.
