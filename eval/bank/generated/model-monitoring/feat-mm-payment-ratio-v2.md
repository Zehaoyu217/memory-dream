---
from: [feat-mm-payment-ratio-v1, fnd-payment-ratio-bug]
updated: 2025-02-18
supersedes: [feat-mm-payment-ratio-v1]
---
# feat-mm-payment-ratio-v2: payments over minimum due using the January 2025 minimum-due formula
Same ratio as v1, but the minimum due is computed with the formula in force from January 2025. Accounts with balances under 1,250 dollars were the ones that shifted.
Used by mm-collect-xgb-v2 from 2025-08-12. Feature PSI on the v2 definition stays under 0.10 across 2025-01 to 2025-06 on the scoring log.
