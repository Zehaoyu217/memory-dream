---
from: [feat-cld-risk-band-v1, credit-line-increase/feat-cli-util-v2]
updated: 2025-10-28
supersedes: [feat-cld-risk-band-v1]
---
# feat-cld-risk-band-v2: four bands rebuilt with the CLI utilisation slope
Bands use v8 score, utilisation and the 6-month utilisation slope from credit-line-increase/feat-cli-util-v2.
Band D is now score below 620 with slope above 0.05 per month, or utilisation above 95%.
Gini of the band rule on cld-test-2025q3 rises from 0.41 to 0.47 (exp-206).
