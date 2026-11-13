## Q1
sfc-ets-v1 was replaced by sfc-lgbm-v2, which was replaced by sfc-hier-v3, the note in force now. sfc-hier-v3 is built on exp-207-spend-forecasting, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2, and the chain runs back through sfc-ets-v1 and ds-sfc-segment-monthly.
Notes: work/sfc-ets-v1.md, work/sfc-lgbm-v2.md, work/sfc-hier-v3.md, work/exp-207-spend-forecasting.md, work/feat-sfc-active-accounts.md, work/fnd-sfc-q4-reconciled.md

## Q2
disp-lgbm-v1 rests on ds-disp-analyst-labels directly, and on ds-disp-disputes through ds-disp-analyst-labels and feat-disp-reason-text.
Notes: work/disp-lgbm-v1.md, work/ds-disp-analyst-labels.md, work/ds-disp-disputes.md

## Q3
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-cutover, which builds on fsm-churn-xgb-v2 and fnd-parity-post-fix, and dec-fsm-timezone-utc, which builds on exp-102-feature-store-migration and fnd-parity-pre-fix.
Notes: work/dec-fsm-cutover.md, work/dec-fsm-timezone-utc.md

## Q4
txc-logreg-v1 was replaced by txc-gbm-v2, which was replaced by txc-gbm-v3, the note in force now. txc-gbm-v3 builds on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2; the datasets behind those are ds-txc-descriptor-sample and ds-txc-mcc-crosswalk, and through the replaced v1 token feature also ds-txc-labelled-merchants and ds-txc-gold-holdout (that last path was not confirmed).
Notes: work/txc-logreg-v1.md, work/txc-gbm-v2.md, work/txc-gbm-v3.md, work/feat-txc-descriptor-tokens-v1.md, work/feat-txc-descriptor-tokens-v2.md, work/feat-txc-mcc-prior.md, work/feat-txc-normalise-v2.md, work/ds-txc-descriptor-sample.md, work/ds-txc-mcc-crosswalk.md, work/ds-txc-labelled-merchants.md

## Q5
ed-gbm-v2 rests on ds-ed-current-base directly (via feat-ed-cashadv-v1 and feat-ed-util-trend-v1) and on ds-ed-label-30p3m (via feat-ed-minpay-v2).
Notes: work/ed-gbm-v2.md, work/ds-ed-current-base.md, work/ds-ed-label-30p3m.md

## Q6
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25, dec-f26-promote-v3, and dec-disp-fraud-score-in (the last through feat-disp-fraud-score and fraud26-gbm-v3).
Notes: work/ds-f26-labels-2026.md, work/dec-f26-maturity-60d.md, work/dec-f26-promote-v2.md, work/dec-f26-replace-f25.md, work/dec-f26-promote-v3.md, work/dec-disp-fraud-score-in.md

## Q7
ep-uplift-forest-v1 rests on ds-ep-assignments and ds-ep-test-registry, both reached through exp-507-experiment-platform and the two features feat-ep-prior-logins-14d and feat-ep-tenure-months.
Notes: work/ep-uplift-forest-v1.md, work/ds-ep-assignments.md, work/ds-ep-test-registry.md

## Q8
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default, each reached through the hardship experiments and models built on that dataset.
Notes: work/ds-hp-matched-controls.md, work/dec-hp-report-did.md, work/dec-hp-smd-gate.md, work/dec-hp-6mo-default.md

## Q9
fsm-churn-xgb-v2 rests on ds-fsm-legacy-features and ds-fsm-parity-sample, the first directly through fsm-churn-xgb-v1 and the replaced payment-lag feature, the second through exp-101 and exp-102 and the parity findings.
Notes: work/fsm-churn-xgb-v2.md, work/ds-fsm-legacy-features.md, work/ds-fsm-parity-sample.md

## Q10
Ten current models build directly on a replaced feature: bt-logit-baseline (feat-bt-util-3m), cb-elasticity-v1 and cb-uplift-v1 (feat-cb-spend-base), churn-lr-base-2025 (feat-c25-util-v1), cli-logreg-baseline (feat-cli-util-v1), clv-bgnbd-v1 (feat-clv-arpu-v1), csb-lr-base (feat-csb-spend-raw), mq3-response-gbm-v1 (feat-mq3-recency-v1), rdm-propensity-lr (feat-rdm-last-activity-v1) and ror-uplift-v1 (feat-ror-value-band-v1). No current model builds directly on a replaced dataset.
Notes: work/bt-logit-baseline.md, work/cb-elasticity-v1.md, work/cb-uplift-v1.md, work/churn-lr-base-2025.md, work/cli-logreg-baseline.md, work/clv-bgnbd-v1.md, work/csb-lr-base.md, work/mq3-response-gbm-v1.md, work/rdm-propensity-lr.md, work/ror-uplift-v1.md