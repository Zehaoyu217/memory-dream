---
from: []
updated: 2025-01-22
---
# mon.reference_samples: frozen training reference per model, one sample per model version
Each model version writes a reference sample at training time: 50,000 rows per model, with feature values and the training score distribution.
PSI is always computed against this sample, not against a rolling window, so a model's reference never changes after it is written.
Seasonal references are a separate set of rows keyed by reference_month (see dec-mm-seasonal-reference).
