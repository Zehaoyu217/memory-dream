## Q1
feat-lbl-churn-flag-closure is in force (churn means no approved transaction in 90 days, or the account closed within 120 days), and nothing replaces it. It builds on dec-lbl-churn-closure and on feat-lbl-churn-flag-90d, which was itself superseded and built on feat-lbl-churn-flag-60d and dec-lbl-churn-90d.
Notes: work/feat-lbl-churn-flag-closure.md, work/dec-lbl-churn-closure.md, work/feat-lbl-churn-flag-90d.md, work/feat-lbl-churn-flag-60d.md, work/dec-lbl-churn-90d.md, work/ds-lbl-churn-labels.md

## Q2
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes (promise-to-pay labels from callcenter.calls, reached through feat-cu-contact-hist-v2) and ds-cu-cases-dpd (the collections.cases snapshot of 1–29 DPD accounts, reached through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour).
Notes: work/cu-resp-v1.md, work/feat-cu-contact-hist-v2.md, work/ds-cu-call-outcomes.md, work/feat-cu-dpd-roll-v1.md, work/feat-cu-pay-behaviour.md, work/ds-cu-cases-dpd.md

## Q3
Two decision notes rest on ds-cli-holdout-2025q4. dec-cli-uplift-targeting gets there through cli-xgb-v1, cli-xgb-v2 and exp-106 (the out-of-time check), and through exp-102, find-cli-uplift-wins, exp-107 and cli-xgb-v3. dec-cld-band-policy-2026 gets there through exp-103, feat-cli-util-v2, feat-cld-risk-band-v2, cld-gbm-v2 and cld-gbm-v3.
Notes: work/dec-cli-uplift-targeting.md, work/dec-cld-band-policy-2026.md, work/ds-cli-holdout-2025q4.md, work/cli-xgb-v1.md, work/cli-xgb-v2.md, work/cli-xgb-v3.md, work/exp-102-credit-line-increase.md, work/exp-103-credit-line-increase.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md, work/feat-cli-util-v2.md, work/feat-cld-risk-band-v2.md, work/cld-gbm-v2.md, work/cld-gbm-v3.md, work/ds-cli-oot-2026h1.md

## Q4
cld-gbm-v3 is in force, and no later note replaces it. It builds on cld-gbm-v2 and feat-cld-payment-shock. The chain runs back through cld-gbm-v1 to ds-cld-decrease-cohort and the first four-band split, feat-cld-risk-band-v1.
Notes: work/cld-gbm-v3.md, work/cld-gbm-v2.md, work/cld-gbm-v1.md, work/feat-cld-payment-shock.md, work/feat-cld-risk-band-v2.md, work/feat-cld-risk-band-v1.md, work/ds-cld-decrease-cohort.md

## Q5
cc-ft-v1 rests on three dataset notes: ds-cc-qa-labels (9,000 tickets with adjudicated labels), ds-cc-taxonomy-v3 (the 18-code taxonomy, which has no upstream note), and ds-cc-tickets-raw (the raw complaint tickets, which ds-cc-qa-labels and feat-cc-embed-v1 both build on).
Notes: work/cc-ft-v1.md, work/ds-cc-qa-labels.md, work/ds-cc-taxonomy-v3.md, work/feat-cc-embed-v1.md, work/ds-cc-tickets-raw.md