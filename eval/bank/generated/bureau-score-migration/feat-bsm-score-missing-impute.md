---
from: [ds-bsm-v10-cohorts-2026]
updated: 2026-02-26
---
# feat-bsm-score-missing-impute: v8 score used when v10 is missing, with a source flag
Where v10 is missing, the mapped v8 score is used and a source flag records which version was used.
Fallback applies to 11% of 2026 applicants; the flag lets models learn version-specific behaviour.
Used in bsm-app-gbm-v10a and later.
