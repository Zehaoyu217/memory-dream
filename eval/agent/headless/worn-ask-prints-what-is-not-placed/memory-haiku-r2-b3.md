## Q1
The only note of another project built directly on find-cu-sms-cost is collections-channel-mix/find-ch-sms-call-gap, which lists it alongside exp-504 and find-ch-sms-matches-call.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests directly on the dataset ds-bt-bureau-join and on the feature feat-bt-util-3m. Through them it also rests on the dataset ds-bt-offer-log, which sits behind the question q-bt-who-accepts. So the dataset notes are ds-bt-bureau-join and ds-bt-offer-log.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both cli-logreg-baseline and cli-xgb-v1 build directly on feat-cli-spend-velocity and feat-cli-util-v1. cli-logreg-baseline also uses feat-cli-pay-behaviour, and cli-xgb-v1 also uses the dataset ds-cli-holdout-2025q4.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/cli-xgb-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base is still current (no SUPERSEDED marker) and builds directly on feat-csb-spend-raw, which was replaced by feat-csb-spend-sa-v2. The other current model, csb-xgb-v2, rests only on current features and datasets.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-spend-sa-v2.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map (via exp-303), dec-bsm-cutover-2026q3 (via bsm-cutoff-logit and exp-305), and dec-bsm-keep-v8-fallback (via exp-307 and bsm-app-gbm-v10b). The chain for dec-bsm-cutover-2026q3 holds only because the pointer to its own words was resolved by reading the note.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
cu-uplift-v3 is in force: cu-uplift-v1 was superseded by cu-uplift-v2, which was superseded by cu-uplift-v3. cu-uplift-v3 is built directly on cu-uplift-v2, exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v1.md, collections-uplift/cu-uplift-v2.md, collections-uplift/cu-uplift-v3.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only one note of another project builds directly on feat-cli-util-v2: feat-cld-risk-band-v2 in limit-decrease-policy.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on five dataset notes: ds-app-applications-2024 (via feat-app-thin-file), ds-bsm-app-dev-2024 (via bsm-app-gbm-v8), ds-bsm-dual-pull-sample, ds-bsm-v10-cohorts-2026 and ds-bsm-v8-history. The first two are in application-scorecard and the others are in bureau-score-migration.
Notes: bureau-score-migration/bsm-app-gbm-v10b.md, application-scorecard/feat-app-thin-file.md, application-scorecard/ds-app-applications-2024.md, bureau-score-migration/bsm-app-gbm-v8.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-v8-history.md

## Q9
Both fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d. fsm-churn-xgb-v2 also uses feat-fsm-util-ratio, which the spend model does not.
Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fsm-spend-lgbm-v2.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is still current (no SUPERSEDED marker) and builds directly on feat-cli-util-v1, which was replaced by feat-cli-util-v2. The other current model, cli-xgb-v3, rests only on exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-util-v2.md