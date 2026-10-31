---
from: [feat-nps-fee-shock-v1, exp-405]
updated: 2026-02-06
supersedes: [feat-nps-fee-shock-v1]
---
# Fee shock v2: fees in the 30 days before the send date relative to the prior three-month average
Only charges dated on or before send_date count. Same source as v1 with the cut applied.
Adds +0.03 Spearman on holdout-2025q4 over the base model (exp-405), not the +0.06 that v1 showed.
