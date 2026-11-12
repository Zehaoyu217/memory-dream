## Q1
The only other-project note built directly on `collections-uplift/find-cu-sms-cost` is `collections-channel-mix/find-ch-sms-call-gap`. Its `from:` list names it alongside `exp-504` and `find-ch-sms-matches-call`.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
`bt-logit-baseline` rests on two dataset notes: `ds-bt-bureau-join` directly, and `ds-bt-offer-log` through `ds-bt-bureau-join` and `feat-bt-util-3m`. The chain runs through `feat-bt-util-3m` and `q-bt-who-accepts`, which has no further sources.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both `cli-logreg-baseline` and `cli-xgb-v1` build directly on `feat-cli-util-v1`, `feat-cli-spend-velocity` and `feat-cli-pay-behaviour`. `cli-xgb-v1` also lists `ds-cli-holdout-2025q4`, which is a dataset note, not a feature.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/cli-xgb-v1.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-pay-behaviour.md

## Q4
`csb-lr-base` is still current and builds directly on `feat-csb-spend-raw`, which `feat-csb-spend-sa-v2` has since superseded. The other current model, `csb-xgb-v2`, does not build on any replaced feature or dataset note.
Notes: churn-small-business/csb-lr-base.md

## Q5
Three decision notes rest on `ds-bsm-v10-cohorts-2026`. `dec-bsm-isotonic-map` comes through `find-bsm-psi-after-map` and `exp-303`. `dec-bsm-cutover-2026q3` comes through `exp-305`, `bsm-cutoff-logit`, and `find-bsm-ks-parity`. `dec-bsm-keep-v8-fallback` comes through `find-bsm-thin-file-gap` and `exp-307`.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
The line runs cu-uplift-v1, then cu-uplift-v2, then cu-uplift-v3. `cu-uplift-v3` is in force, and it is built on `cu-uplift-v2`, `feat-cu-bureau-delta` and `exp-106`.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/feat-cu-bureau-delta.md, collections-uplift/exp-106.md

## Q7
Only one note in another project builds directly on `credit-line-increase/feat-cli-util-v2`: `feat-cld-risk-band-v2` in limit-decrease-policy.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
`bsm-app-gbm-v10b` rests on four dataset notes. `ds-bsm-v10-cohorts-2026` comes via `feat-bsm-thin-file-flag`, `ds-bsm-dual-pull-sample` via `feat-bsm-score-map-v2`, `ds-bsm-app-dev-2024` via `bsm-app-gbm-v8` and `bsm-app-gbm-v10a`, and `ds-bsm-v8-history` sits at the start of every line.
Notes: bureau-score-migration/bsm-app-gbm-v10b.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v8-history.md

## Q9
Both models build directly on `feat-fsm-payment-lag-v2` and `feat-fsm-spend-cv-30d`. `fsm-churn-xgb-v2` also uses `feat-fsm-util-ratio`.
Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fsm-spend-lgbm-v2.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
`cli-logreg-baseline` is the only current model that builds directly on a replaced feature note: `feat-cli-util-v1`, which `feat-cli-util-v2` supersedes. `cli-xgb-v3` is current but does not build on any feature or dataset note.
Notes: credit-line-increase/cli-logreg-baseline.md