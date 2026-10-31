---
from: [feat-bt-util-3m, exp-103-util-trend]
updated: 2025-08-21
supersedes: [feat-bt-util-3m]
---
# feat-bt-util-trend-v2: six-month utilization slope plus the 3-month level
Slope of monthly utilization over the last six month-ends (OLS on `cards.accounts_monthly`), plus the 3-month mean level.
Swapping it in for feat-bt-util-3m moved holdout AUC from 0.66 to 0.67 (exp-103).
Slope clipped at +/-0.15 per month to remove one-off limit changes. Used in bt-xgb-v2 and bt-xgb-v3.
