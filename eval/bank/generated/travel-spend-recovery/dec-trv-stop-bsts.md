---
from: [trv-bsts-v1, exp-504]
updated: 2025-10-06
---
# Decision: stop the BSTS line and keep ridge as the travel model
BSTS gave 5.6% MAPE against 5.2% for the ridge, and takes about three times as long to fit (exp-504).
Decision: stop trv-bsts-v1 and keep the ridge line for the travel model.
Revisit only if the holiday effects need to be modelled separately.
