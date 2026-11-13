## Q1
xs-call-uplift-v1 rests on two dataset notes: `ds-xs-callcentre` (the `callcenter.calls` join, via the recent-call feature and the naive-comparison experiment) and `ds-xs-offer-log` (the `sav.offer_log` table that `ds-xs-callcentre` is built on). That chain ends at the question note `q-xs-propensity`, which has no earlier basis.
Notes: work/xs-call-uplift-v1.md, work/exp-403-callcentre-naive.md, work/find-xs-call-overstated.md, work/feat-xs-call-recent.md, work/ds-xs-callcentre.md, work/ds-xs-offer-log.md, work/q-xs-propensity.md

## Q2
Four decisions rest on ds-disp-analyst-labels. `dec-disp-labels-two-analyst` builds on it directly. `dec-disp-autoresolve-090` and `dec-disp-autoresolve-095` reach it through disp-lgbm-v2, disp-lgbm-v1, exp-301/303/304 and disp-find-precision-real. `dec-disp-fraud-score-in` reaches it through exp-307, exp-306 and disp-find-autoresolve-96.
Notes: work/ds-disp-analyst-labels.md, work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md

## Q3
The note in force at the end of the rs-xgb-v1 → rs-xgb-v2 → rs-xgb-v3 line is `rs-xgb-v3`, which is not superseded by any later note. It is built on `exp-308-recovery-scoring` and `rs-xgb-v2`.
Notes: work/rs-xgb-v3.md, work/exp-308-recovery-scoring.md, work/rs-xgb-v2.md

## Q4
clv-bgnbd-v1 rests on three dataset notes: `ds-clv-cohort-panel` (the base panel), `ds-clv-revenue-monthly` (via the six-month revenue feature) and `ds-clv-holdout-2021h1` (the test set used in the accuracy experiment). The cohort panel is the start of that chain.
Notes: work/clv-bgnbd-v1.md, work/exp-501-customer-lifetime-value.md, work/feat-clv-arpu-v1.md, work/feat-clv-tenure.md, work/ds-clv-cohort-panel.md, work/ds-clv-revenue-monthly.md, work/ds-clv-holdout-2021h1.md

## Q5
Only `dec-ed-promote-v3` rests on ds-ed-bureau-join, through feat-ed-bureau-slope-v1, exp-207-early-delinquency, find-ed-bureau-slope and ed-gbm-v3. `ed-logit-v1` is also built on the join, but no decision names it as a basis.
Notes: work/dec-ed-promote-v3.md, work/ed-gbm-v3.md, work/exp-207-early-delinquency.md, work/find-ed-bureau-slope.md, work/feat-ed-bureau-slope-v1.md, work/ds-ed-bureau-join.md