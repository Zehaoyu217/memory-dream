## Q1
The only note from another project built directly on collections-uplift's find-cu-sms-cost is collections-channel-mix/find-ch-sms-call-gap, which lists it in its "Builds on" line alongside exp-504 and find-ch-sms-matches-call.
Notes: collections-channel-mix/find-ch-sms-call-gap.md, collections-uplift/find-cu-sms-cost.md

## Q2
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join directly, and ds-bt-offer-log both directly (via ds-bt-bureau-join's build) and through feat-bt-util-3m. The chain ends at the question note q-bt-who-accepts, which is not a dataset.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both models build directly on feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour (the "full-pay versus minimum-pay feature"). That third one is named in the body of each note rather than in the "Builds on" line.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/cli-xgb-v1.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-pay-behaviour.md

## Q4
csb-lr-base, which stays on as the monitoring challenger, builds on feat-csb-spend-raw. That feature was replaced by feat-csb-spend-sa-v2 from January 2026. The current csb-xgb-v2 does not build on any replaced feature or dataset.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-cutover-2026q3 (via exp-305 and find-bsm-ks-parity), dec-bsm-isotonic-map (via exp-303) and dec-bsm-keep-v8-fallback (via exp-307 and find-bsm-thin-file-gap). dec-bsm-linear-map does not, since it rests only on the dual-pull experiment.
Notes: bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/exp-303.md, bureau-score-migration/exp-305.md, bureau-score-migration/exp-307.md, bureau-score-migration/find-bsm-ks-parity.md, bureau-score-migration/find-bsm-thin-file-gap.md

## Q6
The note in force at the end of the line is cu-uplift-v3, which is still the production routing model. It is built on cu-uplift-v2 (the calibrated model used for routing), exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v1.md, collections-uplift/cu-uplift-v2.md, collections-uplift/cu-uplift-v3.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only one note from another project builds directly on credit-line-increase's feat-cli-util-v2: limit-decrease-policy/feat-cld-risk-band-v2. The similarly named feat-c25-util-v2 in churn-2025 is a different feature.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md, credit-line-increase/feat-cli-util-v2.md

## Q8
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-v8-history, ds-bsm-app-dev-2024 (via bsm-app-gbm-v8), ds-bsm-dual-pull-sample and ds-bsm-v10-cohorts-2026. The model reaches them through bsm-app-gbm-v10a, the feature notes and the score-map experiments.
Notes: bureau-score-migration/bsm-app-gbm-v10b.md, bureau-score-migration/bsm-app-gbm-v10a.md, bureau-score-migration/bsm-app-gbm-v8.md, bureau-score-migration/feat-bsm-score-map-v2.md, bureau-score-migration/feat-bsm-score-map-v1.md, bureau-score-migration/feat-bsm-score-missing-impute.md, bureau-score-migration/feat-bsm-thin-file-flag.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v8-history.md, bureau-score-migration/ds-bsm-app-dev-2024.md

## Q9
Both models build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d. fsm-churn-xgb-v2 also names feat-fsm-util-ratio, but fsm-spend-lgbm-v2 uses util ratio only in its description, not its "Builds on" line.
Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fsm-spend-lgbm-v2.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is the only current model that builds on a replaced feature. It builds on feat-cli-util-v1, which was replaced by feat-cli-util-v2 on 2025-10-14. Its note is not marked superseded, though the cutoff decision that used it has been retired. cli-xgb-v3 is current but builds on nothing replaced.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-util-v2.md