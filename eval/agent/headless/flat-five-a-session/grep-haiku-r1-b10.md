## Q1
The note in force at the end of the line is `feat-lbl-churn-flag-closure` (2026-03-24), which counts churn as no approved transaction in 90 days or an account closure within 120 days. It is built on `dec-lbl-churn-closure` and `feat-lbl-churn-flag-90d`, the latter itself superseded.
Notes: work/feat-lbl-churn-flag-60d.md, work/feat-lbl-churn-flag-90d.md, work/feat-lbl-churn-flag-closure.md, work/dec-lbl-churn-closure.md

## Q2
`cu-resp-v1` rests on two dataset notes: `ds-cu-call-outcomes` (the `callcenter.calls` promise-to-pay label, via `feat-cu-contact-hist-v2`) and `ds-cu-cases-dpd` (the 1-29 DPD `collections.cases` population, via `feat-cu-dpd-roll-v1` and `feat-cu-pay-behaviour`).
Notes: work/cu-resp-v1.md, work/feat-cu-dpd-roll-v1.md, work/feat-cu-pay-behaviour.md, work/feat-cu-contact-hist-v2.md, work/ds-cu-call-outcomes.md, work/ds-cu-cases-dpd.md

## Q3
Only one decision note rests on `ds-cli-holdout-2025q4`: `dec-cli-uplift-targeting`. The chain runs through `ds-cli-oot-2026h1`, then `exp-106-credit-line-increase`, then `cli-xgb-v3`, which the decision builds on.
Notes: work/ds-cli-holdout-2025q4.md, work/ds-cli-oot-2026h1.md, work/exp-106-credit-line-increase.md, work/cli-xgb-v3.md, work/dec-cli-uplift-targeting.md

## Q4
The note in force at the end of the line is `cld-gbm-v3` (2026-05-18), which adds payment-shock features. It is built on `cld-gbm-v2` and `feat-cld-payment-shock`.
Notes: work/cld-gbm-v1.md, work/cld-gbm-v2.md, work/cld-gbm-v3.md, work/feat-cld-payment-shock.md

## Q5
`cc-ft-v1` rests on three dataset notes: `ds-cc-qa-labels` and `ds-cc-tickets-raw` (the raw complaint ticket table, also reached through `feat-cc-embed-v1`), plus `ds-cc-taxonomy-v3`.
Notes: work/cc-ft-v1.md, work/ds-cc-qa-labels.md, work/ds-cc-taxonomy-v3.md, work/feat-cc-embed-v1.md, work/ds-cc-tickets-raw.md