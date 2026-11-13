## Q1
The note in force is feat-lbl-churn-flag-closure. It was built on dec-lbl-churn-closure and feat-lbl-churn-flag-90d, which traces back through feat-lbl-churn-flag-60d to the dataset ds-lbl-churn-labels.
Notes: work/feat-lbl-churn-flag-closure.md, work/dec-lbl-churn-closure.md, work/feat-lbl-churn-flag-90d.md, work/feat-lbl-churn-flag-60d.md, work/ds-lbl-churn-labels.md

## Q2
cu-resp-v1 rests on two dataset notes. ds-cu-call-outcomes is direct, and ds-cu-cases-dpd comes through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: work/cu-resp-v1.md, work/ds-cu-call-outcomes.md, work/ds-cu-cases-dpd.md

## Q3
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting, through cli-xgb-v1 and cli-xgb-v3, and dec-cld-band-policy-2026, through cld-gbm-v3. I checked the other CLI and CLD decisions, and none of them trace to the holdout.
Notes: work/dec-cli-uplift-targeting.md, work/dec-cld-band-policy-2026.md, work/ds-cli-holdout-2025q4.md

## Q4
The note in force is cld-gbm-v3, which replaced cld-gbm-v2 after cld-gbm-v1. cld-gbm-v3 is built directly on cld-gbm-v2 and feat-cld-payment-shock, and through them on cld-gbm-v1, feat-cld-risk-band-v2, feat-cld-util-after-decrease, and the decrease-cohort and CLI chains.
Notes: work/cld-gbm-v3.md, work/cld-gbm-v2.md, work/cld-gbm-v1.md, work/feat-cld-payment-shock.md

## Q5
cc-ft-v1 rests on ds-cc-qa-labels and ds-cc-taxonomy-v3 directly. It rests on ds-cc-tickets-raw through feat-cc-embed-v1, and ds-cc-qa-labels also comes from that raw dataset.
Notes: work/cc-ft-v1.md, work/ds-cc-qa-labels.md, work/ds-cc-taxonomy-v3.md, work/ds-cc-tickets-raw.md