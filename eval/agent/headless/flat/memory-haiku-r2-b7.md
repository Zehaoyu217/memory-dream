## Q1
sfc-hier-v3 is the one in force at the end of the sfc-ets-v1 line (sfc-ets-v1 → sfc-lgbm-v2 → sfc-hier-v3). It is built on exp-207-spend-forecasting, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2.
Notes: work/sfc-ets-v1.md, work/sfc-lgbm-v2.md, work/sfc-hier-v3.md, work/exp-207-spend-forecasting.md, work/feat-sfc-active-accounts.md, work/fnd-sfc-q4-reconciled.md

## Q2
disp-lgbm-v1 rests on two dataset notes: ds-disp-analyst-labels directly, and ds-disp-disputes through it.
Notes: work/ds-disp-analyst-labels.md, work/ds-disp-disputes.md

## Q3
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-cutover (through fsm-churn-xgb-v2) and dec-fsm-timezone-utc (through exp-102-feature-store-migration).
Notes: work/dec-fsm-cutover.md, work/dec-fsm-timezone-utc.md

## Q4
txc-gbm-v3 is in force at the end of the txc-logreg-v1 line (txc-logreg-v1 → txc-gbm-v2 → txc-gbm-v3). It is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: work/txc-logreg-v1.md, work/txc-gbm-v2.md, work/txc-gbm-v3.md, work/feat-txc-descriptor-tokens-v2.md, work/feat-txc-mcc-prior.md, work/feat-txc-normalise-v2.md

## Q5
ed-gbm-v2 rests on two dataset notes: ds-ed-current-base and ds-ed-label-30p3m. One link, feat-ed-cashadv-v1's "current-account scoring population", is named only in words; it probably means ds-ed-current-base, but I did not confirm that.
Notes: work/ds-ed-current-base.md, work/ds-ed-label-30p3m.md

## Q6
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25, dec-f26-promote-v3, and dec-disp-fraud-score-in (through feat-disp-fraud-score).
Notes: work/dec-f26-maturity-60d.md, work/dec-f26-promote-v2.md, work/dec-f26-replace-f25.md, work/dec-f26-promote-v3.md, work/dec-disp-fraud-score-in.md

## Q7
ep-uplift-forest-v1 rests on two dataset notes: ds-ep-assignments and ds-ep-test-registry.
Notes: work/ds-ep-assignments.md, work/ds-ep-test-registry.md

## Q8
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default. The chain also has one link named only in words ("the 2024 hardship enrolment dataset"), which probably means ds-hp-enrolled, but I did not confirm that.
Notes: work/dec-hp-report-did.md, work/dec-hp-smd-gate.md, work/dec-hp-6mo-default.md

## Q9
fsm-churn-xgb-v2 rests on two dataset notes: ds-fsm-legacy-features directly through its features and model, and ds-fsm-parity-sample through exp-101 and exp-107.
Notes: work/ds-fsm-legacy-features.md, work/ds-fsm-parity-sample.md

## Q10
Eleven current models build directly on a feature that has since been replaced: bt-logit-baseline, cb-uplift-v1, csb-lr-base, churn-lr-base-2025, cli-logreg-baseline, clv-bgnbd-v1, mq3-response-gbm-v1, rdm-propensity-lr, ror-uplift-v1, inc-linear-baseline. cb-elasticity-v1 also fits the pattern, but cb-elasticity-v2 says in words that it replaces it, so I left it out. No current model builds on a replaced dataset.
Notes: work/bt-logit-baseline.md, work/cb-uplift-v1.md, work/csb-lr-base.md, work/churn-lr-base-2025.md, work/cli-logreg-baseline.md, work/clv-bgnbd-v1.md, work/mq3-response-gbm-v1.md, work/rdm-propensity-lr.md, work/ror-uplift-v1.md, work/inc-linear-baseline.md, work/cb-elasticity-v1.md