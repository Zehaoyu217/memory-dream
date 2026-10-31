---
from: [ds-pa-churn-labels, feat-pa-promo-exit-cliff, feat-pa-payment-rate]
updated: 2026-09-10
---
# pa-churn-hazard-v1: hazard of closure after promo expiry, AUC 0.72 on 60-day churn
Discrete-time hazard model on the expiry cohorts, inputs feat-pa-promo-exit-cliff and feat-pa-payment-rate.
AUC 0.72 on 60-day churn for arm C cohorts expired by August 2026. Used in pa-margin-v2.
