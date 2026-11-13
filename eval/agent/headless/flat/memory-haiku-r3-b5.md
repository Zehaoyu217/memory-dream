## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls, dec-cu-promote-v3 and dec-ch-call-escalation, all through the cu-uplift and cu-response models. The memory also names 90 other work notes that may build on it without a link, so this list could be incomplete.
Notes: work/dec-cu-drop-tod.md, work/dec-cu-uplift-for-calls.md, work/dec-cu-promote-v3.md, work/dec-ch-call-escalation.md

## Q2
The note in force is inc-gbm-v3 (inc-gbm-v1 → v2 → v3). It is built on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2; its text also refers to a "cadence-stability income model", which is probably inc-gbm-v2 itself.
Notes: work/inc-gbm-v3.md

## Q3
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave2 and ds-ch-ab-wave1 (directly through ch-propensity-v2 and exp-507) and ds-ch-contact-costs (through feat-ch-prior-contact-v1 and related features). ds-ch-ab-wave1 also names "per-contact cost by channel" in words, which is probably ds-ch-contact-costs.
Notes: work/ds-ch-ab-wave2.md, work/ds-ch-ab-wave1.md, work/ds-ch-contact-costs.md

## Q4
txc-gbm-v2 and txc-logreg-v1 both build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: work/feat-txc-descriptor-tokens-v1.md, work/feat-txc-mcc-prior.md

## Q5
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1, both through cc-logreg-v1 and the cc-ft line. The memory also names 90 other work notes that may build on it without a link, so this list could be incomplete.
Notes: work/dec-cc-ft-v1.md, work/dec-cc-drop-dispute-v1.md

## Q6
The note in force is feat-lbl-churn-flag-closure (feat-lbl-churn-flag-60d → 90d → closure). It is built on dec-lbl-churn-closure and the superseded feat-lbl-churn-flag-90d.
Notes: work/feat-lbl-churn-flag-closure.md

## Q7
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes (directly) and ds-cu-cases-dpd (directly through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour).
Notes: work/ds-cu-call-outcomes.md, work/ds-cu-cases-dpd.md

## Q8
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting and dec-cld-band-policy-2026, both through cli-xgb-v3 and the cld-gbm line. The memory also names 90 other work notes that may build on it without a link, so this list could be incomplete.
Notes: work/dec-cli-uplift-targeting.md, work/dec-cld-band-policy-2026.md

## Q9
The note in force is cld-gbm-v3 (cld-gbm-v1 → v2 → v3). It is built on cld-gbm-v2 and feat-cld-payment-shock.
Notes: work/cld-gbm-v3.md

## Q10
cc-ft-v1 rests on three dataset notes: ds-cc-qa-labels and ds-cc-taxonomy-v3 (directly) and ds-cc-tickets-raw (through feat-cc-embed-v1).
Notes: work/ds-cc-qa-labels.md, work/ds-cc-taxonomy-v3.md, work/ds-cc-tickets-raw.md