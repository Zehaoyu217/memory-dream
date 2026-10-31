---
from: [feat-cr-caller-history-v1, fnd-cr-leak-corrected]
updated: 2026-07-10
supersedes: [feat-cr-caller-history-v1]
---
# Caller history v2 counts contacts in the trailing 90 days strictly before the call's start_ts, plus the last wrap intent
Same 90-day window as v1, but cut at start_ts, so no call made after the current one can enter the feature.
Feature name in the repo: feat_hist90_pre.
Retrain with v2 gives 0.74 on holdout-2025q4 and 0.73 on cr-oot-2026h1, a gap of 0.01 against 0.07 for v1 (exp-105).
