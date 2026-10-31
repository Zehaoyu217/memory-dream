---
from: []
updated: 2025-03-04
---
# Can predicted intent route calls before the IVR menu without losing first-contact resolution?
Open question. Inbound calls pass a six-level IVR and land in a queue picked by menu key, and many are transferred at least once.
Baseline first-contact resolution (FCR) from the 2024 Q4 extract in `callcenter.calls` is 71.4 percent. Target: intent routing keeps FCR within 1 point of that.
Candidate inputs: first 30 seconds of the ASR transcript and the IVR menu path.
Answered through exp-101 to exp-106, dec-cr-lgbm and dec-cr-pilot.
