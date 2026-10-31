---
updated: 2026-06-01
supersedes: [reporting/monthly-review-psi-trigger]
---
# Credit-line models trigger a drift review at PSI above 0.20; other models keep 0.25
- From 2026-06-01, any `cli-` model with PSI above 0.20 on a top-20 feature triggers a drift review.
- All other model families keep the 0.25 trigger, and 0.10 to 0.25 stays "watch" for them.
- Reason: `cli-glm-v2` drifted to PSI 0.22 on `cli_util_ratio` in 2026-04 and was not reviewed until the next cycle.
