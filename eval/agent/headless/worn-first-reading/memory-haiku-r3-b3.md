## Q1
The only note in another project built directly on find-cu-sms-cost is collections-channel-mix/find-ch-sms-call-gap, which uses it alongside exp-504 and find-ch-sms-matches-call.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests directly on ds-bt-bureau-join and feat-bt-util-3m. Through those it reaches ds-bt-offer-log, so its dataset notes are ds-bt-bureau-join (direct) and ds-bt-offer-log (indirect).
Notes: balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both cli-logreg-baseline and cli-xgb-v1 build directly on feat-cli-spend-velocity and feat-cli-util-v1.
Notes: credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base is still current and builds directly on feat-csb-spend-raw, which was replaced by feat-csb-spend-sa-v2 from January 2026. csb-xgb-v2 is also current but is built on the replacement, so it does not qualify.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-spend-sa-v2.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026, either directly or through notes built on it: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
The line is cu-uplift-v1 → cu-uplift-v2 → cu-uplift-v3, and cu-uplift-v3 is the one in force. It builds directly on cu-uplift-v2, exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only limit-decrease-policy/feat-cld-risk-band-v2 was built directly on feat-cli-util-v2 from another project; the rest of its dependents are in credit-line-increase.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on five dataset notes: ds-app-applications-2024 (via feat-app-thin-file), ds-bsm-app-dev-2024 (via bsm-app-gbm-v8), ds-bsm-dual-pull-sample, ds-bsm-v8-history and ds-bsm-v10-cohorts-2026.
Notes: application-scorecard/ds-app-applications-2024.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v8-history.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md

## Q9
Both fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is still current and builds directly on feat-cli-util-v1, which was replaced by feat-cli-util-v2. The other current model, cli-xgb-v3, does not build on any feature note.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md