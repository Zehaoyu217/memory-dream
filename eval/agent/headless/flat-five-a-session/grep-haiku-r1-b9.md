## Q1
Three decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod (via find-cu-tod-leak and feat-cu-call-tod-v1), dec-cu-uplift-for-calls (via cu-resp-v1 and find-cu-response-misranks), and dec-cu-promote-v3 (via the cu-uplift-v3 chain).
Notes: work/dec-cu-drop-tod.md, work/find-cu-tod-leak.md, work/feat-cu-call-tod-v1.md, work/dec-cu-uplift-for-calls.md, work/cu-resp-v1.md, work/find-cu-response-misranks.md, work/dec-cu-promote-v3.md, work/cu-uplift-v3.md, work/cu-uplift-v2.md, work/cu-uplift-v1.md, work/ds-cu-call-outcomes.md

## Q2
inc-gbm-v3 is in force at the end of the line. It replaces inc-gbm-v2, which replaced inc-gbm-v1, and dec-inc-estimate-live makes it the live estimate. It builds on ds-inc-verified-2026, find-inc-log-target-gain and the cadence-stability income model.
Notes: work/inc-gbm-v1.md, work/inc-gbm-v2.md, work/inc-gbm-v3.md, work/dec-inc-estimate-live.md, work/ds-inc-verified-2026.md, work/find-inc-log-target-gain.md

## Q3
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave1 and ds-ch-ab-wave2 (the two randomised channel tests) and ds-ch-contact-costs (per-contact cost, reached through the wave-1 test).
Notes: work/ch-bandit-v1.md, work/ch-propensity-v2.md, work/ch-propensity-v1.md, work/exp-507-collections-channel-mix.md, work/ds-ch-ab-wave1.md, work/ds-ch-ab-wave2.md, work/ds-ch-contact-costs.md

## Q4
txc-gbm-v2 and txc-logreg-v1 both build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: work/txc-gbm-v2.md, work/txc-logreg-v1.md, work/feat-txc-descriptor-tokens-v1.md, work/feat-txc-mcc-prior.md

## Q5
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 (via exp-201 and cc-logreg-v1) and dec-cc-drop-dispute-v1 (via fnd-cc-dispute-link-leak, exp-204, exp-202 and cc-logreg-v1). dec-cc-auto-threshold and dec-cc-taxonomy-split do not, because their chains run through cc-ft-v1, which builds on ds-cc-qa-labels, ds-cc-taxonomy-v3 and feat-cc-embed-v1, not on ds-cc-holdout.
Notes: work/dec-cc-ft-v1.md, work/exp-201-complaint-classification.md, work/cc-logreg-v1.md, work/ds-cc-holdout.md, work/dec-cc-drop-dispute-v1.md, work/fnd-cc-dispute-link-leak.md, work/exp-204-complaint-classification.md, work/exp-202-complaint-classification.md