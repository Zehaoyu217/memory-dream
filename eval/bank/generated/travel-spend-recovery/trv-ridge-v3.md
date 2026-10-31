---
from: [trv-ridge-v2, feat-trv-funnel-v2, feat-trv-cross-border-share, feat-trv-seasonality-adj]
supersedes: [trv-ridge-v2]
updated: 2026-05-20
---
# trv-ridge-v3 is the current travel model: MAPE 4.3% on trv-bt-2025h2
Ridge regression on feat-trv-funnel-v2, feat-trv-cross-border-share and feat-trv-seasonality-adj.
MAPE 4.3% on trv-bt-2025h2 (monthly origins Jul to Dec 2025), against 5.2% for trv-ridge-v2 on the same set (exp-505).
FX volatility was tested and not added (exp-506). Used in the quarterly pack from June 2026.
