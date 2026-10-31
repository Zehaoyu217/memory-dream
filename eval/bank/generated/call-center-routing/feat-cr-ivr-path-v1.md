---
from: [ds-cr-ivr-paths]
updated: 2026-01-05
---
# IVR path feature is the last three menu selections as tokens, plus minutes since the first menu event
Tokens come from `callcenter.ivr_menu_paths`, e.g. L1=2|L2=4|L3=1. Calls with no path get NONE.
Adds +0.03 macro F1 on holdout-2025q4 (fnd-cr-ivr-helps).
Feature name in the repo: feat_ivr3.
