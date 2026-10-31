---
from: [feat-cli-util-v1, exp-103]
updated: 2025-10-14
supersedes: [feat-cli-util-v1]
---
# feat-cli-util-v2: utilisation trend slope and capped over-limit flag replace the flat 3-month average
Adds a 6-month OLS slope of utilisation and an over-limit flag counted once per month when utilisation exceeds 1.0.
Peak utilisation is kept from v1.
Slope gain on holdout-2025q4 is +0.012 AUC for the xgb-v1 retrain (exp-103, 2025-10-09).
Used from cli-xgb-v2 onward.
