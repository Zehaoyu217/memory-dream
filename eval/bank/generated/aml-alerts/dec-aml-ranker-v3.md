---
from: [aml-xgb-v3, exp-407, dec-aml-suppress-018]
updated: 2026-07-08
---
# Promote aml-xgb-v3 as the priority ranker; keep the 0.18 suppression cut
Decision: aml-xgb-v3 replaces v2 as the queue ranker from 2026-07-08; suppression cut stays at 0.18.
Basis: exp-407 (96.3% of SARs in top 40%; 1 of 188 SARs missed below 0.18).
Ranker still orders the queue only; no alert is auto-closed.
