## Q1
sfc-ets-v1 was replaced by sfc-lgbm-v2, which was replaced by sfc-hier-v3, the note in force now. sfc-hier-v3 builds on exp-207-spend-forecasting, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2.
Notes: work/sfc-ets-v1.md, work/sfc-lgbm-v2.md, work/sfc-hier-v3.md, work/exp-207-spend-forecasting.md, work/feat-sfc-active-accounts.md, work/fnd-sfc-q4-reconciled.md

## Q2
disp-lgbm-v1 rests on ds-disp-analyst-labels, directly and through dec-disp-labels-two-analyst. It also rests on ds-disp-disputes, through feat-disp-reason-text and ds-disp-analyst-labels.
Notes: work/ds-disp-analyst-labels.md, work/ds-disp-disputes.md, work/disp-lgbm-v1.md, work/dec-disp-labels-two-analyst.md, work/feat-disp-reason-text.md

## Q3
Two decisions rest on ds-fsm-parity-sample: dec-fsm-cutover and dec-fsm-timezone-utc. Both reach it through the parity experiments (exp-101 and exp-107) and their findings.
Notes: work/ds-fsm-parity-sample.md, work/dec-fsm-cutover.md, work/dec-fsm-timezone-utc.md

## Q4
txc-logreg-v1 was replaced by txc-gbm-v2, which was replaced by txc-gbm-v3, the note in force now. txc-gbm-v3 builds on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: work/txc-logreg-v1.md, work/txc-gbm-v2.md, work/txc-gbm-v3.md, work/feat-txc-descriptor-tokens-v2.md, work/feat-txc-mcc-prior.md, work/feat-txc-normalise-v2.md

## Q5
ed-gbm-v2 rests on ds-ed-current-base, through feat-ed-util-trend-v1 and feat-ed-cashadv-v1, and on ds-ed-label-30p3m, through feat-ed-minpay-v2. Its chain also passes through ed-gbm-v1, exp-205 and exp-206.
Notes: work/ds-ed-current-base.md, work/ds-ed-label-30p3m.md, work/ed-gbm-v2.md, work/ed-gbm-v1.md, work/feat-ed-util-trend-v1.md, work/feat-ed-cashadv-v1.md, work/feat-ed-minpay-v2.md

## Q6
Five decisions rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25, dec-f26-promote-v3 and dec-disp-fraud-score-in. The last reaches it through feat-disp-fraud-score, fraud26-gbm-v3 and exp-207-fraud-2026.
Notes: work/ds-f26-labels-2026.md, work/dec-f26-maturity-60d.md, work/dec-f26-promote-v2.md, work/dec-f26-replace-f25.md, work/dec-f26-promote-v3.md, work/dec-disp-fraud-score-in.md

## Q7
ep-uplift-forest-v1 rests on ds-ep-test-registry, through exp-507-experiment-platform, and on ds-ep-assignments, through feat-ep-prior-logins-14d and feat-ep-tenure-months.
Notes: work/ep-uplift-forest-v1.md, work/ds-ep-test-registry.md, work/ds-ep-assignments.md, work/exp-507-experiment-platform.md, work/feat-ep-prior-logins-14d.md, work/feat-ep-tenure-months.md

## Q8
Three decisions rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default. The memory names one more input to ds-hp-matched-controls, the 2024 hardship enrolment dataset, in words only, so that link is not in the chain.
Notes: work/ds-hp-matched-controls.md, work/dec-hp-report-did.md, work/dec-hp-smd-gate.md, work/dec-hp-6mo-default.md

## Q9
fsm-churn-xgb-v2 rests on ds-fsm-legacy-features, through fsm-churn-xgb-v1 and feat-fsm-util-ratio, and on ds-fsm-parity-sample, through exp-105 and exp-107. Its feat-fsm-payment-lag-v1 input has no dataset note recorded.
Notes: work/fsm-churn-xgb-v2.md, work/ds-fsm-legacy-features.md, work/ds-fsm-parity-sample.md, work/fsm-churn-xgb-v1.md, work/exp-105-feature-store-migration.md, work/exp-107-feature-store-migration.md, work/feat-fsm-util-ratio.md

## Q10
Ten current models build directly on a feature that has been replaced: bt-logit-baseline, cb-uplift-v1, churn-lr-base-2025, cli-logreg-baseline, clv-bgnbd-v1, csb-lr-base, inc-linear-baseline, mq3-response-gbm-v1, rdm-propensity-lr and ror-uplift-v1. None of the current models build on a replaced dataset. "Current" here means no supersession tag in the memory, and cu-resp-v1 is excluded because its replaced input is a glossary term, not a feature or dataset.
Notes: work/bt-logit-baseline.md, work/cb-uplift-v1.md, work/churn-lr-base-2025.md, work/cli-logreg-baseline.md, work/clv-bgnbd-v1.md, work/csb-lr-base.md, work/inc-linear-baseline.md, work/mq3-response-gbm-v1.md, work/rdm-propensity-lr.md, work/ror-uplift-v1.md