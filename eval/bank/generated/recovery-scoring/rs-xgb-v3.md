---
from: [rs-xgb-v2, exp-308]
updated: 2026-02-10
supersedes: [rs-xgb-v2]
---
# rs-xgb-v3 is rs-xgb-v2 with a regression head for recovered share and 2025 recalibration; MAPE 14.2% on agency returns
Same classifier features as rs-xgb-v2, plus a regression head predicting recovered share of balance.
Recalibrated on 2025 vintages. MAPE 14.2% on recovery-scoring-agency-2025h2 (n=3,480) against 19.8% for rs-xgb-v2.
Placement uses the classifier probability with the 0.18 cutoff from dec-rs-placement-cutoff.
