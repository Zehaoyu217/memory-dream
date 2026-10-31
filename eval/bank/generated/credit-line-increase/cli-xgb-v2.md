---
from: [feat-cli-util-v2, feat-cli-bureau-delta, cli-xgb-v1]
updated: 2026-03-02
supersedes: [cli-xgb-v1]
---
# cli-xgb-v2: adds utilisation slope and bureau delta, AUC 0.74 and KS 0.35 on holdout-2025q4
Same trees as v1 plus feat-cli-util-v2 and feat-cli-bureau-delta.
Eval: holdout-2025q4, n=118,400, AUC 0.74, KS 0.35, 90-day loss prevalence 1.0%.
Out-of-time result on cli-oot-2026h1 is in exp-106 (AUC 0.72).
