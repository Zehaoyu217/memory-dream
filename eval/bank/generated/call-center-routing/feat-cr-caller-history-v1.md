---
from: [ds-cr-calls]
updated: 2026-01-19
---
# Caller history v1 counts contacts in the trailing 90 days through the end of the call's calendar day, plus the last wrap intent
The window runs to the end of the calendar day of the current call, so it includes calls made after this one that day.
Lifts holdout-2025q4 macro F1 by +0.05 when added to the LightGBM set (fnd-cr-leak-v1).
Feature name in the repo: feat_hist90_eod.
