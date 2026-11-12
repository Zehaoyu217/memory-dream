## Q1
Only one note from another project was built directly on find-cu-sms-cost: find-ch-sms-call-gap in collections-channel-mix, which supersedes find-ch-sms-matches-call.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
Two dataset notes: ds-bt-bureau-join is a direct input, and ds-bt-offer-log is reached through it and feat-bt-util-3m. The chain also runs through feat-bt-util-3m and q-bt-who-accepts.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/ds-bt-offer-log.md, balance-transfer-propensity/q-bt-who-accepts.md

## Q3
Both models build directly on feat-cli-spend-velocity and feat-cli-util-v1. cli-logreg-baseline also uses feat-cli-pay-behaviour, and cli-xgb-v1 also uses ds-cli-holdout-2025q4.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/cli-xgb-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
Only csb-lr-base is a current model built directly on a replaced feature. It uses feat-csb-spend-raw, which feat-csb-spend-sa-v2 replaced. The other current model, csb-xgb-v2, uses only non-replaced features.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md

## Q5
Three decisions rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback. The 19 notes that depend on it include these three, reached directly or through the models and findings built on it.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
cu-uplift-v3 is the note in force at the end of the line (cu-uplift-v1 → cu-uplift-v2 → cu-uplift-v3). It is built directly on cu-uplift-v2, exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only feat-cld-risk-band-v2 in limit-decrease-policy was built directly on feat-cli-util-v2.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
Five dataset notes: ds-app-applications-2024, ds-bsm-dual-pull-sample, ds-bsm-app-dev-2024, ds-bsm-v10-cohorts-2026 and ds-bsm-v8-history. Three are direct inputs or reached through the intermediate notes, and the rest sit further back in the chain.
Notes: application-scorecard/ds-app-applications-2024.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-v8-history.md

## Q9
Both models build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d. fsm-churn-xgb-v2 also uses feat-fsm-util-ratio.
Notes: feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md, feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fsm-spend-lgbm-v2.md

## Q10
cli-logreg-baseline is the only current model that builds directly on a replaced feature: feat-cli-util-v1, which feat-cli-util-v2 replaced. cli-xgb-v3, the other current model, uses no replaced feature or dataset directly.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md