---
from: [exp-014]
updated: 2026-10-20
---
# Suspect leakage behind the 0.81 AUC
A 0.10 AUC jump from one feature group is too good. The velocity features use a window
"around" the observation date: it may include days after it, inside the label window.
To check: rebuild without post-period days and re-score (exp-017).
