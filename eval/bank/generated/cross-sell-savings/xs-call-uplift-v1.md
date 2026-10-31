---
from: [feat-xs-call-recent, exp-403-callcentre-naive, find-xs-call-overstated]
updated: 2025-10-28
---
# xs-call-uplift-v1: causal forest on call contact; +1.2 points open rate in the two lowest deciles
Causal forest on feat-xs-call-recent, tenure and spend. Selection is handled by conditioning on observables; the propensity comes from the offer-log covariates.
Effect of a call on open rate: +1.2 points (CI 0.4-2.0) in deciles 1-2 of xs-gbm-v2, near zero in the top deciles.
Used for call-centre routing (dec-xs-call-low-deciles).
