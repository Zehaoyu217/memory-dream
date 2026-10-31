---
from: [ds-f25-txn-2024-2025]
updated: 2025-01-29
---
# feat-f25-hour-band: four local-time bands for the authorisation hour
Bands: night (00-06), morning (06-12), afternoon (12-18), evening (18-24), local time of the card holder.
Dropping it changes AUC by under 0.001 on holdout-2025q1 (exp-105), but it stays in the model.
