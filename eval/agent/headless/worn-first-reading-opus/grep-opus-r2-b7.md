## Q1
Within collections-uplift, three decisions rest on it: dec-cu-drop-tod (through feat-cu-call-tod-v1, exp-103 and find-cu-tod-leak), dec-cu-uplift-for-calls (through cu-resp-v1, exp-101 and find-cu-response-misranks, plus exp-105), and dec-cu-promote-v3 (through cu-resp-v1, cu-uplift-v1, v2 and v3). One more is in another project: collections-channel-mix/dec-ch-call-escalation, which builds on find-ch-sms-call-gap, and that note builds on collections-uplift/find-cu-sms-cost.
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
inc-gbm-v1 was replaced by inc-gbm-v2, which was replaced by inc-gbm-v3, the model in use now. inc-gbm-v3 is built on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2 (the cadence-stability income model).
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only one note in another project builds directly on rdm-uplift-v1: customer-lifetime-value/exp-506, which values reactivation targeting at $4.09 of 36-month margin per targeted send.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 traces back, through ch-propensity-v2/v1, exp-507, exp-506 and the channel features, to three datasets: ds-ch-ab-wave1, ds-ch-ab-wave2 and ds-ch-contact-costs. ds-ch-email-engagement is not part of that chain.
Notes: collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
Both models build directly on two feature notes: feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
ds-cc-holdout feeds cc-logreg-v1, and two decisions rest on that. dec-cc-ft-v1 comes through exp-201. dec-cc-drop-dispute-v1 comes through exp-202, fnd-cc-dispute-link-helps, exp-204, fnd-cc-dispute-link-leak and feat-cc-dispute-link-v2.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-60d was replaced by feat-lbl-churn-flag-90d, which was replaced by feat-lbl-churn-flag-closure, the flag in use now. feat-lbl-churn-flag-closure is built on dec-lbl-churn-closure and feat-lbl-churn-flag-90d.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes in revenue-forecast-2026 build directly on sfc-hier-v3: ds-rev26-spend-volume and rev26-combined-v1. exp-305 and rev26-interchange-v1 mention it but do not list it as something they build on.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 traces back to two datasets. ds-cu-call-outcomes comes in directly and through feat-cu-contact-hist-v2. ds-cu-cases-dpd comes through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
Within credit-line-increase, dec-cli-uplift-targeting rests on it, through cli-xgb-v1, exp-102 and exp-103, cli-xgb-v2, ds-cli-oot-2026h1, exp-106, find-cli-uplift-wins and cli-xgb-v3. In another project, limit-decrease-policy/dec-cld-band-policy-2026 also rests on it: feat-cli-util-v2 (from exp-103) feeds feat-cld-risk-band-v2, which then feeds cld-gbm-v2/v3, find-cld-cut-640 and find-cld-roll-rates.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md