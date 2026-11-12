## Q1
clv-bgnbd-v1 rests on two dataset notes: ds-clv-cohort-panel directly through feat-clv-tenure and feat-clv-arpu-v1, and ds-clv-revenue-monthly through feat-clv-arpu-v1.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q2
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3, which builds on ed-gbm-v3, and dec-ed-gbm-for-watchlist, which is reached through ed-logit-v1 and the bureau-slope feature chain.
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
sfc-ets-v1 was replaced by sfc-lgbm-v2, which was replaced by sfc-hier-v3. sfc-hier-v3 is the note in force, built on exp-207, fnd-sfc-q4-reconciled, feat-sfc-active-accounts and sfc-lgbm-v2.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/sfc-lgbm-v2.md

## Q4
disp-lgbm-v1 rests on two dataset notes: ds-disp-analyst-labels directly, and ds-disp-disputes through the analyst labels and the reason-text feature.
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-timezone-utc, which builds on the parity result from exp-102 and fnd-parity-pre-fix, and dec-fsm-cutover, which is reached through the parity findings.
Notes: feature-store-migration/dec-fsm-cutover.md, feature-store-migration/dec-fsm-timezone-utc.md

## Q6
txc-logreg-v1 was replaced by txc-gbm-v2, which was replaced by txc-gbm-v3. txc-gbm-v3 is the note in force, built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/txc-gbm-v2.md

## Q7
ed-gbm-v2 rests on one dataset note: ds-ed-current-base, reached through ed-gbm-v1 and the cash-advance and utilisation-trend features.
Notes: early-delinquency/ds-ed-current-base.md

## Q8
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-replace-f25, dec-f26-promote-v2, dec-f26-promote-v3 and, in dispute-triage, dec-disp-fraud-score-in, which uses the fraud-2026 score.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 rests on two dataset notes: ds-ep-assignments and ds-ep-test-registry, both reached through exp-507 and the two features.
Notes: experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default, all reached through the matched-control experiments and the propensity-model versions.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md