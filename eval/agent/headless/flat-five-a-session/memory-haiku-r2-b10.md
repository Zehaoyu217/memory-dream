## Q1
The note in force is `feat-lbl-churn-flag-closure`, the end of the chain 60d → 90d → closure. It is built on `dec-lbl-churn-closure` and `feat-lbl-churn-flag-90d`.
Notes: work/feat-lbl-churn-flag-closure.md, work/dec-lbl-churn-closure.md, work/feat-lbl-churn-flag-90d.md

## Q2
`cu-resp-v1` rests on the dataset `ds-cu-call-outcomes` directly. It also rests on `ds-cu-cases-dpd` through `feat-cu-dpd-roll-v1` and `feat-cu-pay-behaviour`.
Notes: work/cu-resp-v1.md, work/ds-cu-call-outcomes.md, work/ds-cu-cases-dpd.md, work/feat-cu-dpd-roll-v1.md, work/feat-cu-pay-behaviour.md

## Q3
Two decision notes rest on `ds-cli-holdout-2025q4`: `dec-cli-uplift-targeting` and `dec-cld-band-policy-2026`. Both reach it through models and features built on it, such as `cli-xgb-v2`, `feat-cli-util-v2` and `cld-gbm-v3`.
Notes: work/dec-cli-uplift-targeting.md, work/dec-cld-band-policy-2026.md

## Q4
The note in force is `cld-gbm-v3`, the end of the chain v1 → v2 → v3. It is built on `cld-gbm-v2` and `feat-cld-payment-shock`.
Notes: work/cld-gbm-v3.md, work/cld-gbm-v2.md, work/feat-cld-payment-shock.md

## Q5
`cc-ft-v1` rests directly on the datasets `ds-cc-qa-labels` and `ds-cc-taxonomy-v3`. It also rests on `ds-cc-tickets-raw` through `feat-cc-embed-v1`.
Notes: work/cc-ft-v1.md, work/ds-cc-qa-labels.md, work/ds-cc-taxonomy-v3.md, work/feat-cc-embed-v1.md, work/ds-cc-tickets-raw.md