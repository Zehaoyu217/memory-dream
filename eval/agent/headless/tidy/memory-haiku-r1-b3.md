## Q1
Only one note outside collections-uplift was built directly on find-cu-sms-cost: find-ch-sms-call-gap in collections-channel-mix, which lists it among its sources alongside exp-504 and find-ch-sms-matches-call.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests directly on the dataset ds-bt-bureau-join and on the feature feat-bt-util-3m. Through feat-bt-util-3m and the other notes it builds on, it also reaches the dataset ds-bt-offer-log.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both models build directly on feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour. Note that feat-cli-util-v1 has since been replaced by feat-cli-util-v2.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/cli-xgb-v1.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-pay-behaviour.md

## Q4
csb-lr-base is the only model in churn-small-business that is not marked superseded and builds directly on a replaced feature: it uses feat-csb-spend-raw, which was replaced by feat-csb-spend-sa-v2. The other current model, csb-xgb-v2, uses only features and datasets that are still current.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026, either directly or through the notes built on it: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
The line ends at cu-uplift-v3, which is the note in force now. It is built directly on cu-uplift-v2, feat-cu-bureau-delta and exp-106.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/feat-cu-bureau-delta.md, collections-uplift/exp-106.md

## Q7
Only one note outside credit-line-increase was built directly on feat-cli-util-v2: feat-cld-risk-band-v2 in limit-decrease-policy, which uses the utilisation slope from it.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-dual-pull-sample, ds-bsm-v10-cohorts-2026, ds-bsm-app-dev-2024 and ds-bsm-v8-history. The first two are reached directly or through its direct inputs, and the last two through the earlier notes in its chain.
Notes: bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v8-history.md

## Q9
Both models build directly on the features feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d. fsm-churn-xgb-v2 also uses feat-fsm-util-ratio, which fsm-spend-lgbm-v2 does not.
Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fsm-spend-lgbm-v2.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is the only model in credit-line-increase that is not marked superseded and builds directly on a replaced feature. It uses feat-cli-util-v1, which was replaced by feat-cli-util-v2. Its 2025 cutoff was replaced by dec-cli-cutoff-2025's successor, but the model note itself carries no supersession marker.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md