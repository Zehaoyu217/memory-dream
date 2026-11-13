## Q1
xs-call-uplift-v1 rests on two dataset notes: the call-centre table (ds-xs-callcentre) through the recent-call feature and the naive call-effect study (exp-403), and the offer log (ds-xs-offer-log), which its propensity covariates come from and which ds-xs-callcentre builds on.
Notes: work/xs-call-uplift-v1.md, work/feat-xs-call-recent.md, work/exp-403-callcentre-naive.md, work/find-xs-call-overstated.md, work/ds-xs-callcentre.md, work/ds-xs-offer-log.md

## Q2
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090 and dec-disp-autoresolve-095 through disp-lgbm-v1/v2 (and exp-304 via ds-disp-oot). dec-disp-fraud-score-in rests on it through exp-307, exp-306 and disp-find-autoresolve-96.
Notes: work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md

## Q3
The note in force at the end of the rs-xgb-v1 line is rs-xgb-v3, the current placement model per dec-rs-promote-v3. It is built on exp-308-recovery-scoring and rs-xgb-v2.
Notes: work/rs-xgb-v3.md, work/exp-308-recovery-scoring.md, work/rs-xgb-v2.md

## Q4
clv-bgnbd-v1 rests on three dataset notes: the origination cohort panel (ds-clv-cohort-panel), the 2021 H1 holdout (ds-clv-holdout-2021h1), and the monthly revenue table (ds-clv-revenue-monthly), the last via the six-month revenue feature. The first two also reach it through the accuracy test (exp-501) and the tenure feature.
Notes: work/clv-bgnbd-v1.md, work/exp-501-customer-lifetime-value.md, work/feat-clv-arpu-v1.md, work/feat-clv-tenure.md, work/ds-clv-holdout-2021h1.md, work/ds-clv-cohort-panel.md, work/ds-clv-revenue-monthly.md

## Q5
Only dec-ed-promote-v3 rests on ds-ed-bureau-join, through ed-gbm-v3 and feat-ed-bureau-slope-v1. dec-ed-gbm-for-watchlist is not counted because its listed basis (ed-gbm-v2, find-ed-gbm-vs-logit) does not build on the bureau join.
Notes: work/dec-ed-promote-v3.md, work/ed-gbm-v3.md, work/feat-ed-bureau-slope-v1.md, work/find-ed-bureau-slope.md, work/ds-ed-bureau-join.md