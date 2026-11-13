## Q1
Four decision notes rest on ds-f26-labels-2026, directly or through notes built on it: the 60-day maturity decision, the decision to replace the 2025 model, and the promotions of v2 and v3.
Notes: work/dec-f26-maturity-60d.md, work/dec-f26-replace-f25.md, work/dec-f26-promote-v2.md, work/dec-f26-promote-v3.md

## Q2
Following everything ep-uplift-forest-v1 was built on, it rests on two dataset notes: the test registry and the assignments table.
Notes: work/ds-ep-test-registry.md, work/ds-ep-assignments.md

## Q3
Three decision notes rest on ds-hp-matched-controls, directly or through the matched-control models and effect estimates built on it: the DiD reporting decision, the 6-month default, and the SMD gate.
Notes: work/dec-hp-report-did.md, work/dec-hp-6mo-default.md, work/dec-hp-smd-gate.md

## Q4
Following everything fsm-churn-xgb-v2 was built on, it rests on two dataset notes: the legacy features set (via fsm-churn-xgb-v1) and the parity sample.
Notes: work/ds-fsm-legacy-features.md, work/ds-fsm-parity-sample.md

## Q5
One clear case: cb-uplift-v1 has no retirement line and still ranks accounts for tier offers, but it builds on feat-cb-spend-base, which was replaced by feat-cb-spend-band-v2. Four other notes have no retirement line but build on replaced inputs and are used only as baselines or references, so they are borderline: rdm-propensity-lr, mq3-response-gbm-v1, csb-lr-base and cli-logreg-baseline.
Notes: work/cb-uplift-v1.md, work/feat-cb-spend-base.md, work/feat-cb-spend-band-v2.md, work/rdm-propensity-lr.md, work/mq3-response-gbm-v1.md, work/csb-lr-base.md, work/cli-logreg-baseline.md