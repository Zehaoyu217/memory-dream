---
from: [exp-403, fnd-friendly-fraud, q-lbl-fraud-coverage]
updated: 2025-11-18
---
# Decision: cards.fraud_labels includes friendly-fraud category B, so the label matches loss
Agreed on 2025-11-18 by Daniel Okafor and Tomas Rivera. Category B is booked as loss by fraud-ops, so excluding it left the label short of real losses.
Implemented as feat-lbl-fraud-flag-v2. Set A stays unchanged, so existing reports keep their meaning.
