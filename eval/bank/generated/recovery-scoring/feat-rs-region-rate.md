---
from: [ds-rs-chargeoff-base]
updated: 2025-04-30
---
# feat-rs-region-rate is the target-encoded recovery rate by postcode region, computed on training data only
Feature: out-of-fold recovery rate by postcode region, with smoothing toward the book mean.
Source: `cards.accounts_monthly` postcode, joined to ds-rs-recovery-labels.
Flagged by Omar Haddad (compliance) as a possible proxy for protected characteristics; see find-rs-region-proxy.
