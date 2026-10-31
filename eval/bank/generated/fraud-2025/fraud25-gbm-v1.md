---
from: [feat-f25-velocity-v1, feat-f25-device-age, feat-f25-amt-ratio, feat-f25-hour-band, ds-f25-labels]
updated: 2025-02-03
---
# fraud25-gbm-v1 is the first 2025 CNP model: LightGBM on four features
LightGBM classifier for card-not-present fraud, trained on 2024-07 to 2024-12 CNP transactions.
Features: velocity, device age, amount ratio, hour band. No travel flag.
Labels from `cards.fraud_labels` with the 45-day maturity cut. Evaluated first in exp-101.
Superseded by fraud25-gbm-v2 on 2025-06-18.
