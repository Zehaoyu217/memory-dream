## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls, dec-cu-promote-v3 and dec-ch-call-escalation. The chain runs through cu-resp-v1, feat-cu-call-tod-v1 and feat-cu-contact-hist-v2, and the list of about 90 unplaced notes that may also rest on it is not counted.
Notes: work/dec-cu-drop-tod.md, work/dec-cu-uplift-for-calls.md, work/dec-cu-promote-v3.md, work/dec-ch-call-escalation.md

## Q2
inc-gbm-v3 is in force at the end of the line (inc-gbm-v1 → v2 → v3). It is built directly on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2, which in turn rest on the payroll-cadence features, ds-inc-payroll-proxy, ds-inc-stated-income-2025 and exp-406-income-estimation.
Notes: work/inc-gbm-v3.md, work/ds-inc-verified-2026.md, work/find-inc-log-target-gain.md, work/inc-gbm-v2.md, work/feat-inc-payroll-cadence-v2.md, work/ds-inc-payroll-proxy.md, work/ds-inc-stated-income-2025.md

## Q3
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave2, ds-ch-ab-wave1 and ds-ch-contact-costs. The chain is not complete, because ds-ch-ab-wave1 names a per-contact cost note and a question (q-ch-sms-vs-call) that no note was filed for, so grep the folder for them.
Notes: work/ch-bandit-v1.md, work/ds-ch-ab-wave2.md, work/ds-ch-ab-wave1.md, work/ds-ch-contact-costs.md

## Q4
feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior are the two feature notes that both txc-gbm-v2 and txc-logreg-v1 build on directly.
Notes: work/feat-txc-descriptor-tokens-v1.md, work/feat-txc-mcc-prior.md

## Q5
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1. Both go through cc-logreg-v1 or the exp-201/exp-204 experiments.
Notes: work/dec-cc-ft-v1.md, work/dec-cc-drop-dispute-v1.md

## Q6
feat-lbl-churn-flag-closure is in force (feat-lbl-churn-flag-60d → 90d → closure). It is built directly on dec-lbl-churn-closure and feat-lbl-churn-flag-90d, which in turn rest on dec-lbl-churn-90d, feat-lbl-churn-flag-60d and ds-lbl-churn-labels.
Notes: work/feat-lbl-churn-flag-closure.md, work/dec-lbl-churn-closure.md, work/feat-lbl-churn-flag-90d.md

## Q7
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes directly, and ds-cu-cases-dpd through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: work/cu-resp-v1.md, work/ds-cu-call-outcomes.md, work/ds-cu-cases-dpd.md

## Q8
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting and dec-cld-band-policy-2026. Both go through cli-xgb-v1 or the feat-cli-util-v2 and feat-cld-risk-band-v2 chain, and the list of about 90 unplaced notes is not counted.
Notes: work/dec-cli-uplift-targeting.md, work/dec-cld-band-policy-2026.md

## Q9
cld-gbm-v3 is in force (cld-gbm-v1 → v2 → v3). It is built directly on cld-gbm-v2 and feat-cld-payment-shock, which rest on cld-gbm-v1, feat-cld-risk-band-v2 and feat-cld-util-after-decrease.
Notes: work/cld-gbm-v3.md, work/cld-gbm-v2.md, work/feat-cld-payment-shock.md

## Q10
cc-ft-v1 rests on three dataset notes directly, ds-cc-qa-labels and ds-cc-taxonomy-v3, and on ds-cc-tickets-raw through feat-cc-embed-v1.
Notes: work/cc-ft-v1.md, work/ds-cc-qa-labels.md, work/ds-cc-taxonomy-v3.md, work/ds-cc-tickets-raw.md