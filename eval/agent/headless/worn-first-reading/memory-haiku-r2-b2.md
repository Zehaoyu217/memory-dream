## Q1
Both models build directly on `feat-c25-payment-behaviour` and `feat-c25-txn-recency`. churn-gbm-2025-v2 also uses util-v2, and churn-lr-base-2025 uses util-v1 and app sessions.
Notes: churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
Only `cb-uplift-v1` is still current and builds directly on a replaced feature, `feat-cb-spend-base` (superseded by `feat-cb-spend-band-v2`). The other current models, cb-elasticity-v2 and cb-sim-v1, do not build on a replaced note directly.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/feat-cb-spend-base.md

## Q3
Four decisions rest on `feat-app-util-new`: dec-app-cutoff-v3, dec-app-rebuild-v4, dec-app-cutoff-v4 and dec-app-no-gbm. They do so through app-scorecard-v3, app-gbm-v1, app-gbm-v2 and the scorecard and experiment notes built on them.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-cutoff-v4.md, application-scorecard/dec-app-no-gbm.md

## Q4
The line runs cr-lgbm-v1, then cr-lgbm-v2, then cr-lgbm-v3, which is in force now. cr-lgbm-v3 rests directly on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and fnd-cr-threshold, and through them on 14 more notes back to the original calls data.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md, call-center-routing/exp-105.md, call-center-routing/feat-cr-caller-history-v2.md, call-center-routing/cr-lgbm-v1.md, call-center-routing/feat-cr-caller-history-v1.md, call-center-routing/fnd-cr-leak-corrected.md, call-center-routing/ds-cr-calls.md, call-center-routing/exp-101.md, call-center-routing/exp-104.md, call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-tenure-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md, call-center-routing/cr-logreg-v1.md, call-center-routing/ds-cr-ivr-paths.md, call-center-routing/fnd-cr-leak-v1.md

## Q5
Only `feat-ror-churn-score` in retention-offers-roi was built directly on churn-gbm-2025-v2. The other notes that rest on it from outside churn-2025 do so through that feature.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two dataset notes: `ds-app-applications-2024` (through app-gbm-v1 and app-scorecard-v3) and `ds-app-reject-sample` (through exp-501 and the reject-inference finding).
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both models build directly on `feat-csb-spend-raw` and `feat-csb-tenure-band`.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
Only `churn-lr-base-2025` is still current and builds directly on a replaced feature, `feat-c25-util-v1` (superseded by feat-c25-util-v2). churn-gbm-2025-v2 is current but builds only on live features.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md

## Q9
Five decisions rest on `ds-bt-offer-log`: three in balance-transfer-propensity (dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30, dec-bt-margin-label) and two in promo-apr-test (dec-pa-6m-default, dec-pa-no-12m-subprime).
Notes: balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-margin-label.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md

## Q10
The line runs dec-cb-extend-flat-pilot, then dec-cb-adopt-banded-tiers, then dec-cb-threshold-2500, which is in force now. dec-cb-threshold-2500 rests directly on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift, and through them on 20 more notes.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md, cashback-redesign/cb-elasticity-v2.md, cashback-redesign/cb-sim-v1.md, cashback-redesign/find-cb-band-elasticity.md, cashback-redesign/q-cb-breakeven-lift.md, cashback-redesign/cb-elasticity-v1.md, cashback-redesign/cb-uplift-v1.md, cashback-redesign/ds-cb-rewards-ledger.md, cashback-redesign/exp-204-band-split.md, cashback-redesign/feat-cb-redemption-rate.md, cashback-redesign/feat-cb-spend-band-v2.md, cashback-redesign/feat-cb-tier-eligibility.md, cashback-redesign/find-cb-flat-wins.md, cashback-redesign/q-cb-tier-cost.md, cashback-redesign/ds-cb-spend-panel.md, cashback-redesign/exp-201-flat-rate-pilot.md, cashback-redesign/exp-202-tier-pilot.md, cashback-redesign/exp-203-pooled-elasticity.md, cashback-redesign/feat-cb-spend-base.md, cashback-redesign/find-cb-cost-base.md, cashback-redesign/ds-cb-pilot-2025q4.md