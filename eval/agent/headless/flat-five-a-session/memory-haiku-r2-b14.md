## Q1
Five decision notes rest on ds-f26-labels-2026 through the notes built on it: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25, dec-f26-promote-v3 and dec-disp-fraud-score-in. The chain is not complete, because 90 other work notes name inputs that no note was placed for, so some decisions may be missing.
Notes: work/dec-f26-maturity-60d.md, work/dec-f26-promote-v2.md, work/dec-f26-replace-f25.md, work/dec-f26-promote-v3.md, work/dec-disp-fraud-score-in.md

## Q2
ep-uplift-forest-v1 rests on two dataset notes: ds-ep-assignments, which it reaches through feat-ep-prior-logins-14d and feat-ep-tenure-months, and ds-ep-test-registry, which it reaches through exp-507-experiment-platform.
Notes: work/ds-ep-assignments.md, work/ds-ep-test-registry.md

## Q3
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default. The chain is incomplete, because ds-hp-matched-controls builds on the 2024 hardship enrolment dataset, which is named only in words, and 89 other work notes have unplaced inputs.
Notes: work/dec-hp-report-did.md, work/dec-hp-smd-gate.md, work/dec-hp-6mo-default.md

## Q4
fsm-churn-xgb-v2 rests on two dataset notes: ds-fsm-legacy-features, through feat-fsm-util-ratio and fsm-churn-xgb-v1, and ds-fsm-parity-sample, through exp-107-feature-store-migration and feat-fsm-util-ratio.
Notes: work/ds-fsm-legacy-features.md, work/ds-fsm-parity-sample.md

## Q5
Nine model notes that are not superseded build directly on a feature that has since been replaced: cb-uplift-v1 (feat-cb-spend-base), cli-logreg-baseline (feat-cli-util-v1), churn-lr-base-2025 (feat-c25-util-v1), csb-lr-base (feat-csb-spend-raw), clv-bgnbd-v1 (feat-clv-arpu-v1), mq3-response-gbm-v1 (feat-mq3-recency-v1), rdm-propensity-lr (feat-rdm-last-activity-v1), ror-uplift-v1 (feat-ror-value-band-v1) and bt-logit-baseline (feat-bt-util-3m). Several are baselines or challengers, and bt-logit-baseline is no longer scored in production. cb-elasticity-v1 is excluded because its own note says it was superseded by cb-elasticity-v2.
Notes: work/cb-uplift-v1.md, work/cli-logreg-baseline.md, work/churn-lr-base-2025.md, work/csb-lr-base.md, work/clv-bgnbd-v1.md, work/mq3-response-gbm-v1.md, work/rdm-propensity-lr.md, work/ror-uplift-v1.md, work/bt-logit-baseline.md