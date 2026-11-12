## Q1
Only one note in another project was built directly on find-cu-sms-cost: collections-channel-mix/find-ch-sms-call-gap, the finding that SMS captures 53% of the call's promise-to-pay lift on 8-29 DPD. The memory map lists no other cross-project user.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline was built on ds-bt-bureau-join and feat-bt-util-3m (since replaced). feat-bt-util-3m was built on ds-bt-bureau-join and ds-bt-offer-log, and ds-bt-bureau-join on ds-bt-offer-log, which goes back to the question q-bt-who-accepts. So it rests on two datasets: ds-bt-bureau-join and ds-bt-offer-log.
Notes: balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both models build directly on three feature notes: feat-cli-pay-behaviour, feat-cli-spend-velocity and feat-cli-util-v1. feat-cli-util-v1 has since been replaced by feat-cli-util-v2.
Notes: credit-line-increase/feat-cli-pay-behaviour.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base is the only one. It is still current and builds directly on feat-csb-spend-raw, which was replaced by feat-csb-spend-sa-v2. The other current model, csb-xgb-v2, builds only on current features.
Notes: churn-small-business/csb-lr-base.md

## Q5
Three decisions rest on ds-bsm-v10-cohorts-2026, all through other notes. dec-bsm-isotonic-map comes through exp-303 and find-bsm-psi-after-map. dec-bsm-cutover-2026q3 comes through feat-bsm-v10-band, bsm-cutoff-logit, exp-305 and find-bsm-ks-parity. dec-bsm-keep-v8-fallback comes through feat-bsm-thin-file-flag, find-bsm-thin-file-gap and exp-307.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
The line runs cu-uplift-v1 → cu-uplift-v2 → cu-uplift-v3, and cu-uplift-v3 is in force now. It is built on cu-uplift-v2 (replaced), exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only one note in another project was built directly on feat-cli-util-v2: limit-decrease-policy/feat-cld-risk-band-v2.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b goes back through v10a, v8, both score maps, the missing-score impute feature and the thin-file flag. Along the way it rests on four datasets: ds-bsm-app-dev-2024, ds-bsm-v8-history, ds-bsm-dual-pull-sample and ds-bsm-v10-cohorts-2026.
Notes: bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v8-history.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md

## Q9
Both models build directly on two feature notes: feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is the only one. It is still current and builds directly on feat-cli-util-v1, which was replaced by feat-cli-util-v2. The other current model, cli-xgb-v3, builds only on experiments and a finding.
Notes: credit-line-increase/cli-logreg-baseline.md