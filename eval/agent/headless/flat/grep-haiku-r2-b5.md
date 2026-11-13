## Q1
Decision notes that rest on ds-cu-call-outcomes are dec-cu-drop-tod, dec-cu-uplift-for-calls, dec-cu-promote-v3 and dec-ch-call-escalation, the last through the collections-uplift and channel-mix chain. I have not finished checking whether any further decision note builds on that chain, so the list may be incomplete.
Notes: work/ds-cu-call-outcomes.md, work/feat-cu-call-tod-v1.md, work/feat-cu-contact-hist-v2.md, work/cu-uplift-v2.md, work/cu-uplift-v3.md, work/dec-cu-drop-tod.md, work/dec-cu-uplift-for-calls.md, work/dec-cu-promote-v3.md, work/dec-ch-call-escalation.md

## Q2
inc-gbm-v1 was superseded by inc-gbm-v2 (2025-12-18), which was superseded by inc-gbm-v3 (2026-03-04). The note in force is inc-gbm-v3, which builds on ds-inc-verified-2026, find-inc-log-target-gain and the cadence-stability income model. I did not trace the cadence-stability model back to its dataset leaves.
Notes: work/inc-gbm-v1.md, work/inc-gbm-v2.md, work/inc-gbm-v3.md

## Q3
Not finished. ch-bandit-v1 builds on ch-propensity-v2 and exp-507-collections-channel-mix, but I have not traced either one to its ds-* leaves.
Notes: work/ch-bandit-v1.md

## Q4
txc-gbm-v2 and txc-logreg-v1 both build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: work/txc-gbm-v2.md, work/txc-logreg-v1.md, work/feat-txc-descriptor-tokens-v1.md, work/feat-txc-mcc-prior.md

## Q5
Not finished. I have not checked which decision notes build on ds-cc-holdout, directly or through cc-logreg-v1, cc-ft-v1 or cc-ft-v2.
Notes: work/ds-cc-holdout.md, work/cc-ft-v1.md, work/cc-ft-v2.md

## Q6
feat-lbl-churn-flag-60d was superseded by feat-lbl-churn-flag-90d (2025-09-10), which was superseded by feat-lbl-churn-flag-closure (2026-03-24). The note in force is feat-lbl-churn-flag-closure, which builds on dec-lbl-churn-closure and the superseded 90-day flag. My search found no replacement of the closure flag, but I have not traced its dataset leaves.
Notes: work/feat-lbl-churn-flag-60d.md, work/feat-lbl-churn-flag-90d.md, work/feat-lbl-churn-flag-closure.md

## Q7
Not finished. cu-resp-v1 builds on ds-cu-call-outcomes, which is a dataset leaf, and on feat-cu-contact-hist-v2, which also builds on that label. I have not traced feat-cu-dpd-roll-v1 or feat-cu-pay-behaviour, so ds-cu-cases-dpd and other leaves are not yet confirmed.
Notes: work/cu-resp-v1.md, work/feat-cu-contact-hist-v2.md, work/ds-cu-call-outcomes.md

## Q8
Not finished. I have not checked which decision notes build on ds-cli-holdout-2025q4, directly or through cli-xgb-v1, v2 or v3.
Notes: work/ds-cli-holdout-2025q4.md

## Q9
cld-gbm-v1 was superseded by cld-gbm-v2 (2025-11-12), which was superseded by cld-gbm-v3 (2026-05-18). The note in force is cld-gbm-v3, which builds on cld-gbm-v2 and feat-cld-payment-shock. Back through the chain, cld-gbm-v1 builds on ds-cld-decrease-cohort, and cld-gbm-v2 also builds on feat-cld-risk-band-v2, which I have not traced further.
Notes: work/cld-gbm-v1.md, work/cld-gbm-v2.md, work/cld-gbm-v3.md

## Q10
cc-ft-v1 builds on feat-cc-embed-v1, which builds on ds-cc-tickets-raw, and directly on ds-cc-qa-labels and ds-cc-taxonomy-v3. The dataset leaves are ds-cc-tickets-raw, ds-cc-qa-labels and ds-cc-taxonomy-v3.
Notes: work/cc-ft-v1.md, work/feat-cc-embed-v1.md, work/ds-cc-tickets-raw.md, work/ds-cc-qa-labels.md, work/ds-cc-taxonomy-v3.md

---

Q3, Q5, Q7 and Q8 are incomplete, and Q1 may be missing dependents. I stopped there because you asked for text only and no tool calls in this turn. Tracing them needs further read-only searches over work/. Q2, Q4, Q6, Q9 and Q10 are complete except that the dataset leaves of a few intermediate feature notes (for example feat-cld-risk-band-v2 and feat-cu-dpd-roll-v1) are not confirmed.