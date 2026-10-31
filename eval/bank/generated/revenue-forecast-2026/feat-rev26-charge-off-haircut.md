---
from: [feat-rev26-revolve-balance, ds-rev26-interest-accrual]
updated: 2025-12-08
---
# feat-rev26-charge-off-haircut: expected-loss haircut on accrued interest
Expected-loss haircut on accrued interest, from bureau.scores_monthly and delinquency roll rates (credit-data owns the bureau table).
Average haircut is 3.8% of accrued interest, larger for the lowest-score bands.
Took the interest backtest error from $4.2M to $0.9M per quarter (exp-303).
