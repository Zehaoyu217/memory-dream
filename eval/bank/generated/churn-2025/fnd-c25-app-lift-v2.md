---
from: [exp-105, fnd-c25-app-lift]
updated: 2025-04-02
supersedes: [fnd-c25-app-lift]
---
# App-session lift falls to +0.001 AUC once util-v2 is in, not worth keeping
- With util-v2 the model scores 0.758 with app sessions and 0.757 without (exp-104, exp-105).
- The earlier +0.006 was mostly absorbed by the corrected utilisation and sits inside the bootstrap interval.
- Leads to dec-c25-drop-app-sessions.
