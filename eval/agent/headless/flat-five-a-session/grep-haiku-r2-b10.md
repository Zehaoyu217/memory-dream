## Q1
feat-lbl-churn-flag-closure is in force; nothing supersedes it. It builds on dec-lbl-churn-closure and on feat-lbl-churn-flag-90d, which was itself superseded by the closure flag and built on feat-lbl-churn-flag-60d.
Notes: work/feat-lbl-churn-flag-closure.md, work/dec-lbl-churn-closure.md, work/feat-lbl-churn-flag-90d.md, work/feat-lbl-churn-flag-60d.md

## Q2
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes (the promise-to-pay label source, directly and via feat-cu-contact-hist-v2) and ds-cu-cases-dpd (via feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour). Both are roots, with no upstream notes.
Notes: work/cu-resp-v1.md, work/ds-cu-call-outcomes.md, work/ds-cu-cases-dpd.md, work/feat-cu-contact-hist-v2.md, work/feat-cu-dpd-roll-v1.md, work/feat-cu-pay-behaviour.md

## Q3
Two decision notes rest on ds-cli-holdout-2025q4. dec-cli-uplift-targeting does so through cli-xgb-v1, cli-xgb-v2, exp-106-credit-line-increase, ds-cli-oot-2026h1 and find-cli-uplift-wins. dec-cld-band-policy-2026 does so through exp-103-credit-line-increase, feat-cli-util-v2 and feat-cld-risk-band-v2.
Notes: work/dec-cli-uplift-targeting.md, work/dec-cld-band-policy-2026.md, work/ds-cli-holdout-2025q4.md, work/cli-xgb-v1.md, work/cli-xgb-v2.md, work/cli-xgb-v3.md, work/exp-102-credit-line-increase.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md, work/ds-cli-oot-2026h1.md, work/exp-103-credit-line-increase.md, work/feat-cli-util-v2.md, work/feat-cld-risk-band-v2.md, work/cld-gbm-v2.md, work/cld-gbm-v3.md

## Q4
cld-gbm-v3 is in force; it replaced cld-gbm-v2, which had replaced cld-gbm-v1. It builds on cld-gbm-v2 and feat-cld-payment-shock.
Notes: work/cld-gbm-v3.md, work/cld-gbm-v2.md, work/feat-cld-payment-shock.md

## Q5
cc-ft-v1 rests on three dataset notes: ds-cc-qa-labels and ds-cc-tickets-raw (both directly and via feat-cc-embed-v1), and ds-cc-taxonomy-v3. ds-cc-tickets-raw is the root of the qa-labels and embedding chain; the taxonomy note has no upstream.
Notes: work/cc-ft-v1.md, work/ds-cc-qa-labels.md, work/ds-cc-taxonomy-v3.md, work/feat-cc-embed-v1.md, work/ds-cc-tickets-raw.md