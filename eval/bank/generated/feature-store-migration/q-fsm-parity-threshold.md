---
from: []
updated: 2025-10-06
---
# Open: how close must store feature values match legacy values before cutover?
Legacy notebooks and the feature store compute the same 214 features from the same sources, but they do not agree exactly. Float ordering and the timezone of date windows both cause small differences, so strict equality is not a usable gate.
Proposed bar, not yet agreed: relative difference at most 0.5 percent on at least 99 percent of account-months, measured on the stratified parity sample (ds-fsm-parity-sample).
Owner: Aisha Khan. Credit-risk sign-off requested from Lena Fischer.
