---
from: [ds-ed-current-base]
updated: 2025-05-19
---
# Is the credit-limit change feature usable, given that limits are often cut after delinquency starts?
Hypothesis from the first GBM run: a limit decrease over 90 days is a strong early-delinquency signal.
Concern: the bank often cuts or freezes limits once an account starts to slip, so the feature may carry information from after the prediction date.
Test: recompute the feature with cuts inside the freeze window excluded (exp-204), then decide.
