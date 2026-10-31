---
from: [feat-mq3-app-sessions-30d, exp-303-xlearner]
updated: 2026-07-01
---
# exp-307: dropping app sessions cuts uplift@20% from 2.6 to 2.4 on the Q2 split
Removed feat-mq3-app-sessions-30d from the X-learner and re-scored on the 30% split (n=330,000).
Uplift@20% is 2.4 without app sessions and 2.6 with. App features are worth about 0.2 of uplift@20%, which is why the Q1 drift matters.
