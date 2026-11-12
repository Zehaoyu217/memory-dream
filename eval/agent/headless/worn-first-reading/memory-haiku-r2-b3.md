## Q1
Only one note from another project builds directly on find-cu-sms-cost: `collections-channel-mix/find-ch-sms-call-gap`, which cites it alongside exp-504 and find-ch-sms-matches-call.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests directly on ds-bt-bureau-join, and through feat-bt-util-3m and ds-bt-bureau-join on ds-bt-offer-log. Its only dataset notes are those two.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both cli-logreg-baseline and cli-xgb-v1 build directly on feat-cli-spend-velocity and feat-cli-util-v1.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/cli-xgb-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base is still current (the monitoring challenger per dec-csb-ship-xgb-v2) and builds directly on feat-csb-spend-raw, which feat-csb-spend-sa-v2 replaces.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-sa-v2.md

## Q5
Three decisions rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback, reached through exp-302/303/305/306 and the v10 models and features built on it.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
cu-uplift-v3 is the note in force at the end of the line (cu-uplift-v1 → cu-uplift-v2 → cu-uplift-v3). It is built directly on cu-uplift-v2, exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only limit-decrease-policy/feat-cld-risk-band-v2 outside credit-line-increase builds directly on feat-cli-util-v2.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests directly on feat-app-thin-file, bsm-app-gbm-v10a and feat-bsm-score-map-v2. Its dataset notes, direct or through those, are ds-app-applications-2024, ds-bsm-app-dev-2024, ds-bsm-dual-pull-sample, ds-bsm-v10-cohorts-2026 and ds-bsm-v8-history.
Notes: bureau-score-migration/bsm-app-gbm-v10b.md, application-scorecard/ds-app-applications-2024.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-v8-history.md

## Q9
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fsm-spend-lgbm-v2.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is still current, with no supersession marker, and builds directly on feat-cli-util-v1, which feat-cli-util-v2 replaced. No other current credit-line-increase model builds on a replaced feature or dataset.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md