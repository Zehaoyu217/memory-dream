---
from: []
updated: 2025-12-01
---
# Handoff rule v1: hand off to an agent after 2 failed intent matches in one session
A failed match is confidence below 0.6 or an explicit "no, that's wrong" from the user. The count does not reset within a session.
Used in exp-301 and exp-302. Superseded by feat-cb-handoff-rule-v2 after the April 2026 replay.
