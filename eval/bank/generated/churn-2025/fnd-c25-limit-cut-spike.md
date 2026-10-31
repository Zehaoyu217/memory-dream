---
from: [feat-c25-util-v1, ds-c25-accounts-snapshot]
updated: 2025-02-05
---
# Limit cuts inflate util-v1: churn is 11.9% when the limit fell in the last 30 days
- 7,212 training account-months (0.6%) had a limit decrease in the trailing 30 days.
- Their churn rate is 11.9%, against 4.2% for everyone else; util-v1 reads them as over-utilised.
- So util-v1 mixes a real churn signal with a measurement artefact. feat-c25-util-v2 fixes it with time-matched limits from `cards.limits_history`.
