## Q1
Only one note from another project builds directly on `find-cu-sms-cost`: `find-ch-sms-call-gap` in collections-channel-mix, which lists it in its "Builds on" line. The other reference in dec-cu-promote-v3 is within the same project.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
`bt-logit-baseline` rests on two dataset notes: `ds-bt-offer-log` (directly, and through `ds-bt-bureau-join`) and `ds-bt-bureau-join` (directly). It also builds on `feat-bt-util-3m`, which is built on the bureau join and the offer log. Both trace back to `q-bt-who-accepts`.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/ds-bt-offer-log.md, balance-transfer-propensity/q-bt-who-accepts.md

## Q3
Both `cli-logreg-baseline` and `cli-xgb-v1` build directly on `feat-cli-util-v1`, `feat-cli-spend-velocity` and `feat-cli-pay-behaviour` (the full-pay versus minimum-pay feature).
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/cli-xgb-v1.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-pay-behaviour.md

## Q4
`csb-lr-base` is still current (it is the monitoring challenger) and builds directly on `feat-csb-spend-raw`, which was replaced by `feat-csb-spend-sa-v2` from January 2026. `csb-xgb-v2` is the other current model, but its feature inputs are all still current.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md

## Q5
Three decision notes rest on `ds-bsm-v10-cohorts-2026`: `dec-bsm-cutover-2026q3` (via `exp-305` and `find-bsm-ks-parity`), `dec-bsm-isotonic-map` (via `exp-303`), and `dec-bsm-keep-v8-fallback` (via `find-bsm-thin-file-gap` and `exp-304`). `dec-bsm-linear-map` rests only on the dual-pull sample, so it is excluded.
Notes: bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md, bureau-score-migration/exp-303.md, bureau-score-migration/exp-304.md, bureau-score-migration/exp-305.md, bureau-score-migration/exp-306.md, bureau-score-migration/find-bsm-ks-parity.md, bureau-score-migration/find-bsm-thin-file-gap.md, bureau-score-migration/bsm-app-gbm-v10a.md, bureau-score-migration/bsm-cutoff-logit.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md

## Q6
`cu-uplift-v3` is in force at the end of the line (cu-uplift-v1 → cu-uplift-v2 → cu-uplift-v3), and nothing replaces it. It builds on the calibrated uplift model used for routing (cu-uplift-v2), `exp-106` and `feat-cu-bureau-delta`.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only `feat-cld-risk-band-v2` in limit-decrease-policy builds directly on `credit-line-increase/feat-cli-util-v2`. The similarly named notes in churn-2025 are built on that project's own `feat-c25-util-v2`.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
`bsm-app-gbm-v10b` rests on two dataset notes, `ds-bsm-v10-cohorts-2026` and `ds-bsm-dual-pull-sample`, both directly or through `bsm-app-gbm-v10a` and `feat-bsm-score-map-v2`. It also rests on `ds-bsm-app-dev-2024` and `ds-bsm-v8-history` through `bsm-app-gbm-v8`, which is a parent of v10a.
Notes: bureau-score-migration/bsm-app-gbm-v10b.md, bureau-score-migration/bsm-app-gbm-v10a.md, bureau-score-migration/bsm-app-gbm-v8.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v8-history.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/feat-bsm-score-map-v2.md, bureau-score-migration/feat-bsm-score-map-v1.md

## Q9
Both `fsm-churn-xgb-v2` and `fsm-spend-lgbm-v2` build directly on `feat-fsm-payment-lag-v2` and `feat-fsm-spend-cv-30d`.
Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fsm-spend-lgbm-v2.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
`cli-logreg-baseline` is still current (it is not marked replaced) and builds directly on `feat-cli-util-v1`, which was replaced by `feat-cli-util-v2` in October 2025. `cli-xgb-v3`, the other current model, builds on the v2 feature set and so is not affected.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-util-v2.md