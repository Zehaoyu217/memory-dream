## Q1
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 and ds-app-reject-sample. It gets there through app-gbm-v1, app-scorecard-v3, the thin-file, application-velocity and external-utilisation features, find-app-reject-inference-gain, exp-501 and q-app-reject-inference.
Notes: work/ds-app-applications-2024.md, work/ds-app-reject-sample.md

## Q2
Both models build directly on feat-csb-spend-raw and feat-csb-tenure-band. csb-lr-base names the tenure feature only as "the tenure bands feature".
Notes: work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q3
Five decision notes rest on ds-bt-offer-log: the three BT decisions (drop post-offer features, train on margin, mail the top 30%) and two promo-APR decisions. The promo-APR ones get there through find-pa-margin-corrected → pa-margin-v2 → pa-bal-forecast-v1 → bt-xgb-v3. dec-pa-glide-exit does not rest on it.
Notes: work/dec-bt-drop-post-offer-features.md, work/dec-bt-margin-label.md, work/dec-bt-cut-mailer-top30.md, work/dec-pa-6m-default.md, work/dec-pa-no-12m-subprime.md

## Q4
dec-cb-adopt-banded-tiers replaced dec-cb-extend-flat-pilot and was then replaced by dec-cb-threshold-2500, which is the structure of record now. That note is built on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: work/dec-cb-threshold-2500.md, work/dec-cb-adopt-banded-tiers.md, work/exp-206-breakeven-sim.md, work/find-cb-breakeven-lift.md

## Q5
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join directly, and ds-bt-offer-log both through the bureau join and through feat-bt-util-3m. The offer log itself builds only on a question note.
Notes: work/ds-bt-bureau-join.md, work/ds-bt-offer-log.md

## Q6
Both models build directly on three feature notes: feat-cli-pay-behaviour (cited as "the full-pay versus minimum-pay feature"), feat-cli-spend-velocity and feat-cli-util-v1.
Notes: work/feat-cli-pay-behaviour.md, work/feat-cli-spend-velocity.md, work/feat-cli-util-v1.md

## Q7
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map (via exp-303), dec-bsm-cutover-2026q3 (via bsm-cutoff-logit, exp-305 and find-bsm-ks-parity), and dec-bsm-keep-v8-fallback (via exp-307 and find-bsm-thin-file-gap). dec-bsm-linear-map rests only on the dual-pull sample, not on the cohorts.
Notes: work/dec-bsm-isotonic-map.md, work/dec-bsm-cutover-2026q3.md, work/dec-bsm-keep-v8-fallback.md

## Q8
cu-uplift-v2 replaced cu-uplift-v1 and was then replaced by cu-uplift-v3, which is the one in force now. cu-uplift-v3 is built on cu-uplift-v2, exp-106-collections-uplift and feat-cu-bureau-delta.
Notes: work/cu-uplift-v3.md, work/cu-uplift-v2.md, work/exp-106-collections-uplift.md, work/feat-cu-bureau-delta.md

## Q9
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-app-dev-2024 (via v10a and v8), ds-bsm-v8-history, ds-bsm-dual-pull-sample (via the score maps and the cohorts) and ds-bsm-v10-cohorts-2026 (via the thin-file flag and the missing-score imputation).
Notes: work/ds-bsm-app-dev-2024.md, work/ds-bsm-v8-history.md, work/ds-bsm-dual-pull-sample.md, work/ds-bsm-v10-cohorts-2026.md

## Q10
Both models build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: work/feat-fsm-payment-lag-v2.md, work/feat-fsm-spend-cv-30d.md