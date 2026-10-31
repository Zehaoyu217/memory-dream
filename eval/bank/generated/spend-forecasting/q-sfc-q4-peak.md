---
from: [q-sfc-macro-horizon]
updated: 2026-01-08
---
# Why is the spend-forecasting Q4 segment forecast biased low?
Under sfc-lgbm-v2 the November and December forecasts ran 3.1% below actuals on sfc-oot-2025h2 (Jul-Dec 2025).
Suspects: the Black Friday peak moving from December into November (fnd-sfc-bfcm-shift), and segment forecasts that do not add up to the total.
Reconciling the segments with the total was tested in exp-207.
