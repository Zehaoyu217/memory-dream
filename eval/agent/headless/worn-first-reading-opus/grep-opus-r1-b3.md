## Q1
Only one note in another project builds directly on find-cu-sms-cost: find-ch-sms-call-gap in collections-channel-mix. It cites `collections-uplift/find-cu-sms-cost` by name in its "Builds on" line.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline builds on ds-bt-bureau-join and feat-bt-util-3m. feat-bt-util-3m builds on the bureau join and ds-bt-offer-log, and the bureau join itself builds on the offer log, which goes back to the question q-bt-who-accepts. So it rests on two dataset notes: ds-bt-bureau-join and ds-bt-offer-log.
Notes: balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both build directly on the same three feature notes: feat-cli-pay-behaviour (the full-pay versus minimum-pay feature), feat-cli-spend-velocity and feat-cli-util-v1.
Notes: credit-line-increase/feat-cli-pay-behaviour.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
The only replaced feature or dataset note is feat-csb-spend-raw, replaced by feat-csb-spend-sa-v2. The one current model still built directly on it is csb-lr-base, which is kept as the monitoring challenger. csb-xgb-v1 also used it but has been superseded.
Notes: churn-small-business/csb-lr-base.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026. dec-bsm-isotonic-map gets there through exp-303. dec-bsm-cutover-2026q3 gets there through bsm-cutoff-logit, exp-305 and find-bsm-ks-parity. dec-bsm-keep-v8-fallback gets there through exp-307 and find-bsm-thin-file-gap.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
cu-uplift-v3 is the note in force now: cu-uplift-v1 was replaced by v2, and v2 by v3, which was promoted on 2026-03-25. It builds on cu-uplift-v2, exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only one note in another project builds directly on feat-cli-util-v2: feat-cld-risk-band-v2 in limit-decrease-policy.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b goes back through v10a, bsm-app-gbm-v8, both score maps, exp-301, the missing-score impute and the thin-file flag. Along that chain it rests on four dataset notes: ds-bsm-v10-cohorts-2026, ds-bsm-dual-pull-sample, ds-bsm-app-dev-2024 and ds-bsm-v8-history.
Notes: bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v8-history.md

## Q9
Both list feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d in their "Builds on" lines. fsm-spend-lgbm-v2's text also mentions util ratio, but only fsm-churn-xgb-v2 lists feat-fsm-util-ratio as something it builds on.
Notes: feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
The only replaced feature or dataset note is feat-cli-util-v1, replaced by feat-cli-util-v2. The one current model built directly on it is cli-logreg-baseline. Its cutoff decision was superseded, but no note replaces the model itself. cli-xgb-v1 also used it but has been replaced.
Notes: credit-line-increase/cli-logreg-baseline.md