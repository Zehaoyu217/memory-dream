---
from: [fnd-cc-coverage]
updated: 2026-02-25
---
# Auto-code only above 0.95 precision; below that, route the complaint to compliance operations for hand coding
Threshold 0.95 on the cc-ft-v1 probability. Expected coverage 58 percent of tickets on holdout-2025q4.
Tickets below threshold keep the hand-coding queue. Approved by Omar Haddad.
