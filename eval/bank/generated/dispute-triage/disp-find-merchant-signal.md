---
from: [feat-disp-merchant-cb-rate, exp-303]
updated: 2026-08-05
---
# Merchant chargeback rate is the top feature by gain (0.22 of total)
In disp-lgbm-v2, feat-disp-merchant-cb-rate holds 22% of total LightGBM gain.
Adding it lifted precision@0.90 from 88.5% to 91.2% (exp-303).
Strong signal, which is why merchant-risk reuses the dispute ratio (feat-mrisk-dispute-ratio).
