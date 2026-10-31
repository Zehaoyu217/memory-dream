---
from: [q-mrisk-score-use, exp-502, ds-mrisk-merchant-month]
updated: 2026-03-20
---
# Score every active merchant monthly on the merchant-month panel; the score feeds review only
Decision: merchant risk is scored monthly for all active merchants; scores create review tasks, not account actions.
Basis: exp-502 (AUC 0.85) on the merchant-month panel.
Automatic restriction is out of scope until a model is validated on a watchlist.
