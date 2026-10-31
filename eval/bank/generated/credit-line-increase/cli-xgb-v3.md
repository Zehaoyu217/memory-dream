---
from: [exp-106, exp-107, find-cli-uplift-wins]
updated: 2026-09-15
supersedes: [cli-xgb-v2]
---
# cli-xgb-v3: two-model T-learner uplift for incremental spend, uplift@20% 1.9 on cli-rct-2025q3
Two XGBoost models (treated and control) on the v2 feature set; score = difference in predicted 90-day incremental spend.
Eval: cli-rct-2025q3, n=36,000 randomised exposures; uplift@20% 1.9, Qini 0.081.
Replaces cli-xgb-v2 as the targeting score; loss guard remains the 1.5% cap (dec-cli-loss-cap).
