---
from: [exp-204, find-ed-limit-gain]
updated: 2025-07-09
supersedes: [find-ed-limit-gain]
---
# The limit-change feature leaks: its gain falls from +0.021 to +0.002 AUC once cuts after delinquency starts are removed
Most of the limit decreases in the feature come from cuts made after the account started slipping. The feature therefore carries information from after the prediction date.
Residual gain of +0.002 AUC is within noise and not stable across vintages.
Recommendation: remove the feature. See dec-ed-drop-limit-feature.
