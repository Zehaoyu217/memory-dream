---
from: [ds-ed-current-base]
updated: 2025-03-04
---
# bureau.scores_monthly joins to the current-account base at snapshot date with 91% coverage
Join on account and snapshot month to `bureau.scores_monthly` (credit-data). Scores are as of the snapshot, never after it.
Coverage 91%. The 9% without a bureau record are thin-file accounts and are scored only by the features that do not need bureau data.
Thin-file accounts behave differently; see find-ed-gbm-vs-logit.
