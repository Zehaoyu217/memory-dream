## Q1
One note in another project builds directly on find-cu-sms-cost: find-ch-sms-call-gap in collections-channel-mix.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline builds on ds-bt-bureau-join and feat-bt-util-3m, and feat-bt-util-3m builds on the bureau join and ds-bt-offer-log. ds-bt-bureau-join itself rests on ds-bt-offer-log, which goes back to q-bt-who-accepts. So it rests on two dataset notes: ds-bt-bureau-join and ds-bt-offer-log.
Notes: balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both models build directly on the same three feature notes: feat-cli-pay-behaviour (the "full-pay versus minimum-pay feature"), feat-cli-spend-velocity and feat-cli-util-v1.
Notes: credit-line-increase/feat-cli-pay-behaviour.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base is still current (it stays on as the monitoring challenger) and builds directly on feat-csb-spend-raw, which feat-csb-spend-sa-v2 has replaced. The other current model, csb-xgb-v2, builds only on feature notes that have not been replaced.
Notes: churn-small-business/csb-lr-base.md

## Q5
Three decision notes rest on it. dec-bsm-isotonic-map comes through exp-303. dec-bsm-cutover-2026q3 comes through exp-303, feat-bsm-v10-band, bsm-cutoff-logit and exp-305, and also through v10a, v10b, exp-306 and find-bsm-ks-parity. dec-bsm-keep-v8-fallback comes through v10b and exp-307, and through feat-bsm-thin-file-flag, exp-304 and find-bsm-thin-file-gap.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
The line runs cu-uplift-v1, then cu-uplift-v2, then cu-uplift-v3, and cu-uplift-v3 is the note in force now. It builds on cu-uplift-v2 (the "calibrated uplift model used for routing"), exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
One note in another project builds directly on feat-cli-util-v2: feat-cld-risk-band-v2 in limit-decrease-policy.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b builds on v10a, score-map-v2 and the thin-file flag. Following those back through v8, score-map-v1, exp-301 and missing-impute, it rests on four dataset notes: ds-bsm-app-dev-2024, ds-bsm-v8-history, ds-bsm-dual-pull-sample and ds-bsm-v10-cohorts-2026.
Notes: bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v8-history.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md

## Q9
Both models build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is the one: no note replaces it, and it builds directly on feat-cli-util-v1, which feat-cli-util-v2 has replaced. The other current model, cli-xgb-v3, builds directly only on experiment and finding notes, and cli-xgb-v1 and v2 have both been replaced.
Notes: credit-line-increase/cli-logreg-baseline.md