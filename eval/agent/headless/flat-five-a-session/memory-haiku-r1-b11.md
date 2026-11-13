## Q1
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (directly via xs-gbm-v2, through exp-405 and xs-gbm-v2) and dec-xs-retrain-quarterly (through find-xs-drift-2026 and exp-407). The feature was replaced by feat-xs-payroll-flag-v2, so these decisions also depend on the replaced chain.
Notes: work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md

## Q2
mrisk-gbm-v3 is the model in force at the end of the line (mrisk-gbm-v1 → mrisk-gbm-v2 → mrisk-gbm-v3). It is built on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: work/mrisk-gbm-v3.md, work/exp-507-merchant-risk.md, work/feat-mrisk-dispute-ratio.md, work/mrisk-gbm-v2.md

## Q3
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop, directly through feat-cli-util-v1 and feat-cli-pay-behaviour, and ds-cli-outcome-90d, through feat-cli-spend-velocity. ds-cli-outcome-90d itself builds on ds-cli-eligible-pop, so that is the root of the chain.
Notes: work/cli-logreg-baseline.md, work/ds-cli-eligible-pop.md, work/ds-cli-outcome-90d.md

## Q4
No decision note rests on ds-clv-holdout-2021h1. Its only dependent is the experiment exp-501-customer-lifetime-value, and no decision note is recorded downstream of that experiment.
Notes: work/ds-clv-holdout-2021h1.md, work/exp-501-customer-lifetime-value.md

## Q5
dec-pbs-gmm-v3-current is the note in force at the end of the line (pbs-kmeans-v1 → pbs-gmm-v2 → pbs-gmm-v3 → dec-pbs-gmm-v3-current). It is built on fnd-pbs-five-segments and pbs-gmm-v3.
Notes: work/dec-pbs-gmm-v3-current.md, work/fnd-pbs-five-segments.md, work/pbs-gmm-v3.md