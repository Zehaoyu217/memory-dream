---
from: [post-period-leak]
updated: 2026-10-30
---
# Rebuild velocity as v3 from pre-observation days only; retire v2
Decision, 2026-10-30. The velocity features are rebuilt as feat-velocity-v3: the same 6 `vel_` columns,
but every window ends on the observation date. churn-xgb-v2 is retrained on it as churn-xgb-v3. Owner: Sam Lee.
