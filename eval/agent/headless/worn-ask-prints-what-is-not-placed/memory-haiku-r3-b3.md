## Q1
The only note of another project built directly on find-cu-sms-cost is collections-channel-mix/find-ch-sms-call-gap, which lists it among its sources.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests directly on the bureau join and the utilisation feature feat-bt-util-3m. Through those it reaches the offer log. The two dataset notes are ds-bt-bureau-join (direct) and ds-bt-offer-log (via feat-bt-util-3m).
Notes: balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both cli-logreg-baseline and cli-xgb-v1 build directly on feat-cli-spend-velocity and feat-cli-util-v1. The first is still used by logreg, and the second has since been replaced by feat-cli-util-v2.
Notes: credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
Only csb-lr-base is a current model that builds directly on a replaced feature, namely feat-csb-spend-raw, which feat-csb-spend-sa-v2 replaced. csb-xgb-v2, the other current model, builds only on live features and findings.
Notes: churn-small-business/csb-lr-base.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026. dec-bsm-isotonic-map and dec-bsm-keep-v8-fallback reach it through exp-303 and exp-307/find-bsm-thin-file-gap. dec-bsm-cutover-2026q3 reaches it through bsm-cutoff-logit and find-bsm-ks-parity. dec-bsm-linear-map does not, since it rests only on the dual-pull sample.
Notes: bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
cu-uplift-v3 is in force now; it replaced cu-uplift-v2, which had replaced cu-uplift-v1. cu-uplift-v3 is built on cu-uplift-v2, exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md

## Q7
Only limit-decrease-policy/feat-cld-risk-band-v2 is built directly on feat-cli-util-v2 from another project. It reuses the utilisation slope in its bands.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on five datasets: ds-app-applications-2024 (via feat-app-thin-file), ds-bsm-dual-pull-sample, ds-bsm-app-dev-2024 (via bsm-app-gbm-v8), ds-bsm-v10-cohorts-2026, and ds-bsm-v8-history.
Notes: application-scorecard/ds-app-applications-2024.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-v8-history.md

## Q9
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
Only cli-logreg-baseline is a current model that builds directly on a replaced feature, feat-cli-util-v1, which feat-cli-util-v2 replaced. cli-xgb-v3 builds only on live findings and experiments.
Notes: credit-line-increase/cli-logreg-baseline.md