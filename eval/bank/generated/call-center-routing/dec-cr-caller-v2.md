---
from: [fnd-cr-leak-corrected, feat-cr-caller-history-v2]
updated: 2026-07-16
---
# Retire caller history v1 and use v2 everywhere in the routing stack
Caller history v1 is removed from the feature store. v2 is the only caller feature from this date.
Reason: v1 leaked post-call contacts, and its +0.05 holdout gain did not survive the out-of-time read (fnd-cr-leak-corrected).
Owner Sam Lee. Tomás Rivera backfills v2 from 2025-07 onward.
