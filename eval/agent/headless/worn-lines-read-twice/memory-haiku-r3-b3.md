## Q1
The only note in another project built directly on find-cu-sms-cost is `collections-channel-mix/find-ch-sms-call-gap`, which lists it as a source and says it builds on `collections-uplift/find-cu-sms-cost`.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests on two dataset notes directly: `ds-bt-bureau-join`, and `ds-bt-offer-log` through `feat-bt-util-3m`. The chain runs back to the question note `q-bt-who-accepts`.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/ds-bt-offer-log.md, balance-transfer-propensity/q-bt-who-accepts.md

## Q3
Both cli-logreg-baseline and cli-xgb-v1 build directly on the same three feature notes: `feat-cli-pay-behaviour`, `feat-cli-spend-velocity` and `feat-cli-util-v1`.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/cli-xgb-v1.md, credit-line-increase/feat-cli-pay-behaviour.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
`csb-lr-base` is the current model that builds directly on a replaced feature: it uses `feat-csb-spend-raw`, which was superseded by `feat-csb-spend-sa-v2`. This is inferred from the absence of a SUPERSEDED tag on `csb-lr-base`, since no note supersedes it. The current `csb-xgb-v2` uses only current features.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-spend-sa-v2.md

## Q5
Three decision notes rest on `ds-bsm-v10-cohorts-2026`: `dec-bsm-isotonic-map` (via exp-303), `dec-bsm-cutover-2026q3` (via bsm-app-gbm-v10b and bsm-cutoff-logit) and `dec-bsm-keep-v8-fallback` (via exp-307 and bsm-app-gbm-v10b).
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
The line ends at `cu-uplift-v3`, which is in force now. It is built directly on `cu-uplift-v2` (replaced), `exp-106` and `feat-cu-bureau-delta`.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only one note in another project is built directly on `feat-cli-util-v2`: `limit-decrease-policy/feat-cld-risk-band-v2`.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on four dataset notes: `ds-bsm-dual-pull-sample` and `ds-bsm-v10-cohorts-2026` directly or nearly so, plus `ds-bsm-app-dev-2024` (via bsm-app-gbm-v8) and `ds-bsm-v8-history` at the root of the chain.
Notes: bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v8-history.md

## Q9
Both models build directly on `feat-fsm-payment-lag-v2` and `feat-fsm-spend-cv-30d`. `fsm-churn-xgb-v2` also uses `feat-fsm-util-ratio`, which the spend model does not.
Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fsm-spend-lgbm-v2.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
`cli-logreg-baseline` is the current model built directly on a replaced feature, `feat-cli-util-v1` (superseded by `feat-cli-util-v2`). This is inferred from the absence of a SUPERSEDED tag on it, and `cli-xgb-v3` uses no replaced inputs.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-util-v2.md