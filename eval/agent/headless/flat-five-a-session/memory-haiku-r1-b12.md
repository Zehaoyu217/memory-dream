## Q1
xs-call-uplift-v1 rests on the dataset notes ds-xs-callcentre (`callcenter.calls` joined to offers) and ds-xs-offer-log, reached through exp-403-callcentre-naive, feat-xs-call-recent and find-xs-call-overstated. The chain also passes through the question q-xs-propensity.
Notes: work/xs-call-uplift-v1.md, work/exp-403-callcentre-naive.md, work/feat-xs-call-recent.md, work/find-xs-call-overstated.md, work/ds-xs-callcentre.md, work/ds-xs-offer-log.md

## Q2
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through the models and experiments built on it.
Notes: work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md

## Q3
The note in force at the end of the rs-xgb-v1 line is rs-xgb-v3, which replaces rs-xgb-v2 and is built on exp-308-recovery-scoring and rs-xgb-v2 directly.
Notes: work/rs-xgb-v3.md, work/exp-308-recovery-scoring.md, work/rs-xgb-v2.md

## Q4
clv-bgnbd-v1 rests on ds-clv-cohort-panel and ds-clv-revenue-monthly, through feat-clv-arpu-v1 and feat-clv-tenure. Its phrase "the bg/nbd versus gbm accuracy test" matches exp-501-customer-lifetime-value (inferred from the index, not a note link), which adds ds-clv-holdout-2021h1, itself built on ds-clv-cohort-panel.
Notes: work/clv-bgnbd-v1.md, work/feat-clv-arpu-v1.md, work/feat-clv-tenure.md, work/ds-clv-cohort-panel.md, work/ds-clv-revenue-monthly.md, work/exp-501-customer-lifetime-value.md, work/ds-clv-holdout-2021h1.md

## Q5
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3, through ed-gbm-v3, exp-207-early-delinquency and find-ed-bureau-slope, and dec-ed-gbm-for-watchlist, through find-ed-gbm-vs-logit and exp-201-early-delinquency.
Notes: work/dec-ed-promote-v3.md, work/dec-ed-gbm-for-watchlist.md