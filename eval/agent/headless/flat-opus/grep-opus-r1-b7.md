## Q1
sfc-ets-v1 was replaced by sfc-lgbm-v2, which was then replaced by sfc-hier-v3, the note in force now. sfc-hier-v3 builds on the MinT reconciliation experiment (exp-207-spend-forecasting), the active-accounts denominator feature (feat-sfc-active-accounts), fnd-sfc-q4-reconciled and the per-segment LightGBM model sfc-lgbm-v2.
Notes: work/sfc-hier-v3.md, work/exp-207-spend-forecasting.md, work/feat-sfc-active-accounts.md, work/fnd-sfc-q4-reconciled.md, work/sfc-lgbm-v2.md

## Q2
disp-lgbm-v1 builds on dec-disp-labels-two-analyst, ds-disp-analyst-labels and feat-disp-reason-text. All of these lead back to two datasets: ds-disp-analyst-labels and ds-disp-disputes, which is the base of ds-disp-analyst-labels.
Notes: work/ds-disp-analyst-labels.md, work/ds-disp-disputes.md

## Q3
Two decision notes rest on ds-fsm-parity-sample, through the parity experiments, findings and features that come from it: dec-fsm-timezone-utc and dec-fsm-cutover. dec-mm-seasonal-reference mentions mm-limit-glm-v2 but doesn't build on it, so it is left out.
Notes: work/dec-fsm-timezone-utc.md, work/dec-fsm-cutover.md

## Q4
txc-logreg-v1 was replaced by txc-gbm-v2, which was then replaced by txc-gbm-v3, the note in force now. txc-gbm-v3 builds on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, the descriptor normalisation feature (feat-txc-normalise-v2) and txc-gbm-v2.
Notes: work/txc-gbm-v3.md, work/feat-txc-descriptor-tokens-v2.md, work/feat-txc-mcc-prior.md, work/feat-txc-normalise-v2.md, work/txc-gbm-v2.md

## Q5
ed-gbm-v2 builds on ed-gbm-v1 and on experiments exp-205 and exp-206. Through their features, these lead back to two datasets: ds-ed-current-base and ds-ed-label-30p3m, which itself builds on ds-ed-current-base.
Notes: work/ds-ed-current-base.md, work/ds-ed-label-30p3m.md

## Q6
Four fraud-2026 decisions rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-replace-f25, dec-f26-promote-v2 and dec-f26-promote-v3. A fifth, dec-disp-fraud-score-in, rests on it through fraud26-gbm-v3 and feat-disp-fraud-score.
Notes: work/dec-f26-maturity-60d.md, work/dec-f26-replace-f25.md, work/dec-f26-promote-v2.md, work/dec-f26-promote-v3.md, work/dec-disp-fraud-score-in.md

## Q7
ep-uplift-forest-v1 builds on exp-507-experiment-platform, feat-ep-prior-logins-14d and feat-ep-tenure-months. These lead back to two datasets: ds-ep-test-registry (through the experiment) and ds-ep-assignments (through both features).
Notes: work/ds-ep-test-registry.md, work/ds-ep-assignments.md

## Q8
Three decisions rest on ds-hp-matched-controls. dec-hp-6mo-default does so through hp-psm-v1, exp-405 and find-hp-plan-length; dec-hp-report-did through exp-404 and find-hp-effect-v2; and dec-hp-smd-gate through exp-408 and hp-psm-v2.
Notes: work/dec-hp-6mo-default.md, work/dec-hp-report-did.md, work/dec-hp-smd-gate.md

## Q9
fsm-churn-xgb-v2 builds on exp-105, three feature-store features and fsm-churn-xgb-v1. Through the parity experiments and findings, these lead back to two datasets: ds-fsm-legacy-features and ds-fsm-parity-sample.
Notes: work/ds-fsm-legacy-features.md, work/ds-fsm-parity-sample.md

## Q10
Ten current models build directly on a feature that has since been replaced; no dataset note was ever replaced. Six name the old feature by id: bt-logit-baseline, cb-uplift-v1, cli-logreg-baseline, csb-lr-base, mq3-response-gbm-v1 and rdm-propensity-lr. Four name it in words: churn-lr-base-2025 (feat-c25-util-v1), clv-bgnbd-v1 (feat-clv-arpu-v1), inc-linear-baseline (feat-inc-payroll-cadence-v1) and ror-uplift-v1 (feat-ror-value-band-v1).
Notes: work/bt-logit-baseline.md, work/cb-uplift-v1.md, work/cli-logreg-baseline.md, work/csb-lr-base.md, work/mq3-response-gbm-v1.md, work/rdm-propensity-lr.md, work/churn-lr-base-2025.md, work/clv-bgnbd-v1.md, work/inc-linear-baseline.md, work/ror-uplift-v1.md