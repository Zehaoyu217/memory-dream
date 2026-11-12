## Q1
Only one note from another project was built directly on find-cu-sms-cost: the collections-channel-mix finding on the 8-29 DPD SMS-versus-call gap, which replaces an earlier finding.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join directly, and ds-bt-offer-log through feat-bt-util-3m and ds-bt-bureau-join.
Notes: balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both cli-logreg-baseline and cli-xgb-v1 build directly on feat-cli-spend-velocity and feat-cli-util-v1.
Notes: credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base is the only current model that builds directly on a replaced feature: it uses feat-csb-spend-raw, which feat-csb-spend-sa-v2 replaces. csb-xgb-v2 (current) builds only on current features and notes.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026, directly or through models and experiments: the isotonic map decision, the 2026-Q3 cutover decision, and the keep-v8-fallback decision.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
cu-uplift-v3 is the note in force now, and it is built directly on cu-uplift-v2, exp-106 and feat-cu-bureau-delta. Its chain reaches back through cu-uplift-v2 to cu-uplift-v1.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only one note from another project was built directly on feat-cli-util-v2: the limit-decrease-policy risk-band feature feat-cld-risk-band-v2.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on five dataset notes: ds-app-applications-2024 and ds-bsm-app-dev-2024 at the start, plus ds-bsm-dual-pull-sample, ds-bsm-v8-history and ds-bsm-v10-cohorts-2026. The first two are reached through bsm-app-gbm-v8 and the v8 feeds, and the last three through the score maps and v10 cohort chain.
Notes: application-scorecard/ds-app-applications-2024.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v8-history.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md

## Q9
Both models build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is the only current model that builds directly on a replaced feature: it uses feat-cli-util-v1, which feat-cli-util-v2 replaces.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md