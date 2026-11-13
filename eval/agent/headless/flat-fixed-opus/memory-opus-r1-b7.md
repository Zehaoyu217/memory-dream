Everything needed is gathered. Q10 comes from a grep of the full model map; I'm writing up the answers now.

## Q1
The line runs sfc-ets-v1 → sfc-lgbm-v2 → sfc-hier-v3. sfc-hier-v3 is the one in force now. It is built on exp-207-spend-forecasting, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2.
Notes: work/sfc-hier-v3.md, work/exp-207-spend-forecasting.md, work/feat-sfc-active-accounts.md, work/fnd-sfc-q4-reconciled.md, work/sfc-lgbm-v2.md

## Q2
disp-lgbm-v1 rests on two dataset notes. ds-disp-analyst-labels is a direct input and is also reached through dec-disp-labels-two-analyst. ds-disp-disputes is reached through ds-disp-analyst-labels and feat-disp-reason-text.
Notes: work/ds-disp-analyst-labels.md, work/ds-disp-disputes.md

## Q3
Two decision notes rest on it. dec-fsm-timezone-utc gets there through fnd-parity-pre-fix and exp-101. dec-fsm-cutover gets there through fnd-parity-post-fix, fnd-churn-lift and fsm-churn-xgb-v2.
Notes: work/dec-fsm-timezone-utc.md, work/dec-fsm-cutover.md

## Q4
The line runs txc-logreg-v1 → txc-gbm-v2 → txc-gbm-v3. txc-gbm-v3 is the one in force now. It is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: work/txc-gbm-v3.md, work/feat-txc-descriptor-tokens-v2.md, work/feat-txc-mcc-prior.md, work/feat-txc-normalise-v2.md, work/txc-gbm-v2.md

## Q5
ed-gbm-v2 rests on ds-ed-current-base, reached through feat-ed-util-trend-v1 and feat-ed-cashadv-v1. It also rests on ds-ed-label-30p3m, reached through feat-ed-minpay-v2.
Notes: work/ds-ed-current-base.md, work/ds-ed-label-30p3m.md

## Q6
Five decision notes rest on it: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25, dec-f26-promote-v3 and dec-disp-fraud-score-in. The last one gets there through fraud26-gbm-v3 and feat-disp-fraud-score.
Notes: work/dec-f26-maturity-60d.md, work/dec-f26-promote-v2.md, work/dec-f26-replace-f25.md, work/dec-f26-promote-v3.md, work/dec-disp-fraud-score-in.md

## Q7
ep-uplift-forest-v1 rests on ds-ep-assignments, reached through feat-ep-prior-logins-14d and feat-ep-tenure-months. It also rests on ds-ep-test-registry, reached through exp-507-experiment-platform.
Notes: work/ds-ep-assignments.md, work/ds-ep-test-registry.md

## Q8
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-6mo-default and dec-hp-smd-gate.
Notes: work/dec-hp-report-did.md, work/dec-hp-6mo-default.md, work/dec-hp-smd-gate.md

## Q9
fsm-churn-xgb-v2 rests on ds-fsm-legacy-features, through fsm-churn-xgb-v1, feat-fsm-util-ratio and exp-101. It also rests on ds-fsm-parity-sample, through exp-107 and exp-101. Two inputs have no dataset note behind them: feat-fsm-spend-cv-30d and feat-fsm-payment-lag-v1 only name raw cards tables.
Notes: work/ds-fsm-legacy-features.md, work/ds-fsm-parity-sample.md

## Q10
Ten current models build directly on a feature that has since been replaced (no replaced dataset turned up): bt-logit-baseline, cb-uplift-v1, churn-lr-base-2025, cli-logreg-baseline, clv-bgnbd-v1, csb-lr-base, inc-linear-baseline, mq3-response-gbm-v1, rdm-propensity-lr and ror-uplift-v1. The replaced features are feat-bt-util-3m, feat-cb-spend-base, feat-c25-util-v1, feat-cli-util-v1, feat-clv-arpu-v1, feat-csb-spend-raw, feat-inc-payroll-cadence-v1, feat-mq3-recency-v1, feat-rdm-last-activity-v1 and feat-ror-value-band-v1. I left out cu-resp-v1 because its replaced input, glossary/promise-to-pay, is a term note rather than a feature or dataset.
Notes: work/bt-logit-baseline.md, work/cb-uplift-v1.md, work/churn-lr-base-2025.md, work/cli-logreg-baseline.md, work/clv-bgnbd-v1.md, work/csb-lr-base.md, work/inc-linear-baseline.md, work/mq3-response-gbm-v1.md, work/rdm-propensity-lr.md, work/ror-uplift-v1.md