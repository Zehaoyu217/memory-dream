---
from: [ds-bt-offer-log]
updated: 2025-03-28
---
# `bt-holdout-2025q1` is 41,800 randomly held-out accounts from the Jan-Mar 2025 waves, acceptance 3.9%
Accounts drawn at random from the Q1 2025 waves and never mailed. Excluded from every training set.
Realized acceptance 3.9% (about 1,630 accepters). Source: `bt.offer_log` where `holdout_flag = 1`.
Tuning on this set stopped after exp-105. It is not the out-of-time set; see ds-bt-oot-2026h1.
