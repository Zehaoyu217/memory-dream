---
from: [find-cli-uplift-wins, cli-xgb-v3, exp-106]
updated: 2026-09-22
supersedes: [dec-cli-cutoff-2025]
---
# Decision: Q4 2026 CLI batch targets the top 20% by cli-xgb-v3 uplift score
Replaces the 2025 logistic cutoff of 0.031 (dec-cli-cutoff-2025) for the Q4 2026 batch.
Basis: exp-106 showed cli-xgb-v2 drift on cli-oot-2026h1 (AUC 0.72), and find-cli-uplift-wins showed the T-learner ahead on uplift@20%.
The 1.5% loss cap in dec-cli-loss-cap still applies to the selected population.
