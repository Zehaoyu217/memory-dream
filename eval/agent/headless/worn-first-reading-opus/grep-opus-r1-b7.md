## Q1
Three collections-uplift decisions rest on ds-cu-call-outcomes: dec-cu-drop-tod (through feat-cu-call-tod-v1, exp-103 and find-cu-tod-leak), dec-cu-uplift-for-calls (through cu-resp-v1, exp-101/exp-102, find-cu-response-misranks and exp-105) and dec-cu-promote-v3 (through cu-uplift-v1, v2 and v3). One decision in another project also rests on it: dec-ch-call-escalation, which is built on find-ch-sms-call-gap, and that note is built on collections-uplift/find-cu-sms-cost, which comes from cu-uplift-v3.
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
inc-gbm-v2 replaced inc-gbm-v1, and inc-gbm-v3 then replaced inc-gbm-v2. inc-gbm-v3 is in force now, and no note replaces it. It is built on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2 (the cadence-stability income model).
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only one note from another project is built directly on rdm-uplift-v1: customer-lifetime-value/exp-506, which builds on clv-ml-v2 and reactivation-dormant/rdm-uplift-v1.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave1 (through ch-propensity-v1/v2 and exp-501/502), ds-ch-ab-wave2 (through exp-507) and ds-ch-contact-costs (through ds-ch-ab-wave1 and the send-window, prior-contact and prefer-channel features). ds-ch-email-engagement is not in its chain.
Notes: collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
Both models build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decisions rest on ds-cc-holdout. dec-cc-ft-v1 gets there through cc-logreg-v1 and exp-201. dec-cc-drop-dispute-v1 gets there through cc-logreg-v1, exp-202, fnd-cc-dispute-link-helps, exp-204, fnd-cc-dispute-link-leak and feat-cc-dispute-link-v2. No note in another project builds on this chain.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-90d replaced feat-lbl-churn-flag-60d, and feat-lbl-churn-flag-closure then replaced the 90-day flag. feat-lbl-churn-flag-closure is in force now. It is built on dec-lbl-churn-closure and feat-lbl-churn-flag-90d.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
In revenue-forecast-2026, ds-rev26-spend-volume and rev26-combined-v1 are built directly on sfc-hier-v3. rev26-interchange-v1 and exp-305 mention sfc-hier-v3, but neither lists it as something it builds on.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on ds-cu-call-outcomes, both directly and through feat-cu-contact-hist-v2. It also rests on ds-cu-cases-dpd, through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
In credit-line-increase, dec-cli-uplift-targeting rests on it. That runs through cli-xgb-v1, exp-102/exp-107 and cli-xgb-v3, and also through ds-cli-oot-2026h1 and exp-106. In another project, limit-decrease-policy/dec-cld-band-policy-2026 rests on it through exp-103, feat-cli-util-v2 and feat-cld-risk-band-v2 (and from there through cld-gbm-v2/v3 and find-cld-cut-640).
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md