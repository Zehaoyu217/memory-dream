## Q1
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer and dec-xs-retrain-quarterly, both through xs-gbm-v1 and xs-gbm-v2 (which build on the balance proxy directly or through feat-xs-payroll-flag-v2).
Notes: work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md

## Q2
mrisk-gbm-v1 was superseded by mrisk-gbm-v2, which was superseded by mrisk-gbm-v3, the note in force now. mrisk-gbm-v3 is built on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: work/mrisk-gbm-v3.md, work/exp-507-merchant-risk.md, work/feat-mrisk-dispute-ratio.md, work/mrisk-gbm-v2.md

## Q3
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop (through feat-cli-util-v1 and feat-cli-pay-behaviour) and ds-cli-outcome-90d (through feat-cli-spend-velocity). The tool's chain output printed a different note's chain, so I traced these from the per-note lines.
Notes: work/cli-logreg-baseline.md, work/feat-cli-util-v1.md, work/feat-cli-pay-behaviour.md, work/feat-cli-spend-velocity.md, work/ds-cli-eligible-pop.md, work/ds-cli-outcome-90d.md

## Q4
No decision note rests on ds-clv-holdout-2021h1. The only note that does is exp-501-customer-lifetime-value, an experiment, and no decision cites it.
Notes: work/ds-clv-holdout-2021h1.md, work/exp-501-customer-lifetime-value.md

## Q5
pbs-kmeans-v1 was superseded by pbs-gmm-v2, then pbs-gmm-v3, which is now replaced by the decision dec-pbs-gmm-v3-current, the note in force. That decision is built on fnd-pbs-five-segments and pbs-gmm-v3.
Notes: work/dec-pbs-gmm-v3-current.md, work/fnd-pbs-five-segments.md, work/pbs-gmm-v3.md

## Q6
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre (through exp-403-callcentre-naive and feat-xs-call-recent) and ds-xs-offer-log (through q-xs-propensity).
Notes: work/xs-call-uplift-v1.md, work/ds-xs-callcentre.md, work/ds-xs-offer-log.md

## Q7
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through the dispute-triage models and experiments.
Notes: work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md

## Q8
rs-xgb-v1 was superseded by rs-xgb-v2, then rs-xgb-v3, which is in force now. rs-xgb-v3 is built on exp-308-recovery-scoring and rs-xgb-v2.
Notes: work/rs-xgb-v3.md, work/exp-308-recovery-scoring.md, work/rs-xgb-v2.md

## Q9
clv-bgnbd-v1 rests on two dataset notes: ds-clv-cohort-panel and ds-clv-revenue-monthly, both reached through its feature notes. Its "bg/nbd versus gbm accuracy test" has no note of its own, so I did not trace it.
Notes: work/clv-bgnbd-v1.md, work/ds-clv-cohort-panel.md, work/ds-clv-revenue-monthly.md

## Q10
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3 and dec-ed-gbm-for-watchlist, both through the ed-gbm and bureau-slope chain.
Notes: work/dec-ed-promote-v3.md, work/dec-ed-gbm-for-watchlist.md