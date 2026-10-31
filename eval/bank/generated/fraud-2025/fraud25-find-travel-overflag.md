---
from: [exp-106, exp-108, fraud25-find-threshold-fine]
supersedes: [fraud25-find-threshold-fine]
updated: 2025-10-14
---
# Travel-MCC alerts are over-flagged: precision 3.1% vs 11.4% for other alerts
Jul-Sep 2025 alert log (`fraud25_alerts_log`, 18,420 alerts): travel alerts precision 3.1%, non-travel 11.4%.
The 0.62 threshold was fine on holdout data but not on live alerts, because the travel flag inflates the score.
Supersedes the threshold-fine finding; the threshold moves to 0.70 (dec-f25-threshold-070).
