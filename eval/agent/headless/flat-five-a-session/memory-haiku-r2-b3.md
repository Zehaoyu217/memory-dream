## Q1
app-gbm-v2 rests on two datasets: `ds-app-applications-2024`, which feeds the v3 scorecard and the thin-file and velocity features, and `ds-app-reject-sample`, which feeds the reject-inference experiment exp-501.
Notes: work/ds-app-applications-2024.md, work/ds-app-reject-sample.md

## Q2
Both models build directly on the spend feature `feat-csb-spend-raw` (since superseded by `feat-csb-spend-sa-v2`) and the tenure-band feature `feat-csb-tenure-band`.
Notes: work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q3
Five decision notes rest on `ds-bt-offer-log`: `dec-bt-cut-mailer-top30`, `dec-bt-drop-post-offer-features` and `dec-bt-margin-label` through the bt model chain, and `dec-pa-6m-default` and `dec-pa-no-12m-subprime` through `find-pa-margin-corrected`. About 90 other notes in `work/` have unresolved links, so a few more decisions could rest on it, but nothing in memory confirms that.
Notes: work/dec-bt-cut-mailer-top30.md, work/dec-bt-drop-post-offer-features.md, work/dec-bt-margin-label.md, work/dec-pa-6m-default.md, work/dec-pa-no-12m-subprime.md

## Q4
The line ends at `dec-cb-threshold-2500`, which is in force: it replaces `dec-cb-adopt-banded-tiers`, which replaced `dec-cb-extend-flat-pilot`. It is built directly on `dec-cb-adopt-banded-tiers`, `exp-206-breakeven-sim` and `find-cb-breakeven-lift`.
Notes: work/dec-cb-threshold-2500.md, work/dec-cb-adopt-banded-tiers.md, work/exp-206-breakeven-sim.md, work/find-cb-breakeven-lift.md

## Q5
bt-logit-baseline rests on two datasets: `ds-bt-bureau-join` directly, and `ds-bt-offer-log` through `feat-bt-util-3m` and `ds-bt-bureau-join`.
Notes: work/ds-bt-bureau-join.md, work/ds-bt-offer-log.md