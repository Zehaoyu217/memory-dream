## Q1
The current end of the line is sfc-hier-v3 (sfc-ets-v1 → sfc-lgbm-v2 → sfc-hier-v3). It is built on exp-207-spend-forecasting (MinT reconciliation), feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2, which has itself been replaced.
Notes: work/sfc-hier-v3.md, work/exp-207-spend-forecasting.md, work/feat-sfc-active-accounts.md, work/fnd-sfc-q4-reconciled.md, work/sfc-lgbm-v2.md

## Q2
disp-lgbm-v1 rests on two datasets. ds-disp-analyst-labels is direct, and it also reaches the model through dec-disp-labels-two-analyst and q-disp-label-source. ds-disp-disputes comes in through ds-disp-analyst-labels and feat-disp-reason-text.
Notes: work/ds-disp-analyst-labels.md, work/ds-disp-disputes.md

## Q3
Two decisions rest on it. dec-fsm-timezone-utc gets there through fnd-parity-pre-fix and exp-101/102. dec-fsm-cutover gets there through fnd-parity-post-fix, fnd-churn-lift and fsm-churn-xgb-v2.
Notes: work/dec-fsm-timezone-utc.md, work/dec-fsm-cutover.md

## Q4
The current end of the line is txc-gbm-v3 (txc-logreg-v1 → txc-gbm-v2 → txc-gbm-v3). It is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2, which has been replaced.
Notes: work/txc-gbm-v3.md, work/feat-txc-descriptor-tokens-v2.md, work/feat-txc-mcc-prior.md, work/feat-txc-normalise-v2.md, work/txc-gbm-v2.md

## Q5
ed-gbm-v2 rests on two datasets. ds-ed-current-base comes in through feat-ed-util-trend-v1 and feat-ed-cashadv-v1. ds-ed-label-30p3m comes in through feat-ed-minpay-v2 (through exp-205/206).
Notes: work/ds-ed-current-base.md, work/ds-ed-label-30p3m.md

## Q6
Five decisions rest on it: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25 and dec-f26-promote-v3. The fifth is dec-disp-fraud-score-in, which gets there through fraud26-gbm-v3 and feat-disp-fraud-score.
Notes: work/dec-f26-maturity-60d.md, work/dec-f26-promote-v2.md, work/dec-f26-replace-f25.md, work/dec-f26-promote-v3.md, work/dec-disp-fraud-score-in.md

## Q7
ep-uplift-forest-v1 rests on two datasets. ds-ep-assignments comes in through feat-ep-tenure-months and feat-ep-prior-logins-14d. ds-ep-test-registry comes in through exp-507-experiment-platform.
Notes: work/ds-ep-assignments.md, work/ds-ep-test-registry.md

## Q8
Three decisions rest on it: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default. dec-hp-6mo-default gets there through find-hp-plan-length.
Notes: work/dec-hp-report-did.md, work/dec-hp-smd-gate.md, work/dec-hp-6mo-default.md

## Q9
fsm-churn-xgb-v2 rests on two datasets. ds-fsm-legacy-features comes in through fsm-churn-xgb-v1, feat-fsm-util-ratio and the parity experiments. ds-fsm-parity-sample comes in through exp-101 and exp-107 and the features built from them. feat-fsm-spend-cv-30d is built on no dataset note.
Notes: work/ds-fsm-legacy-features.md, work/ds-fsm-parity-sample.md

## Q10
Ten current models build directly on a replaced feature: bt-logit-baseline (feat-bt-util-3m), cb-uplift-v1 (feat-cb-spend-base), churn-lr-base-2025 (feat-c25-util-v1), cli-logreg-baseline (feat-cli-util-v1) and clv-bgnbd-v1 (feat-clv-arpu-v1). The rest are csb-lr-base (feat-csb-spend-raw), inc-linear-baseline (feat-inc-payroll-cadence-v1), mq3-response-gbm-v1 (feat-mq3-recency-v1), rdm-propensity-lr (feat-rdm-last-activity-v1) and ror-uplift-v1 (feat-ror-value-band-v1). I left out cb-elasticity-v1 because it says itself that it was replaced, and cu-resp-v1 because the replaced note under it is a glossary term, not a feature or dataset.
Notes: work/bt-logit-baseline.md, work/cb-uplift-v1.md, work/churn-lr-base-2025.md, work/cli-logreg-baseline.md, work/clv-bgnbd-v1.md, work/csb-lr-base.md, work/inc-linear-baseline.md, work/mq3-response-gbm-v1.md, work/rdm-propensity-lr.md, work/ror-uplift-v1.md