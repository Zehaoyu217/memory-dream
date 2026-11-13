## Q1
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (through xs-gbm-v1 → xs-gbm-v2 → exp-405) and dec-xs-retrain-quarterly (through exp-407-oot-2026h1 and find-xs-drift-2026). Both chains are declared in the notes' own "builds on" lines.
Notes: work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md

## Q2
mrisk-gbm-v1 was replaced by mrisk-gbm-v2, which was replaced by mrisk-gbm-v3. mrisk-gbm-v3 is the one in force, and it is built on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: work/mrisk-gbm-v3.md, work/exp-507-merchant-risk.md, work/feat-mrisk-dispute-ratio.md, work/mrisk-gbm-v2.md

## Q3
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop (through feat-cli-util-v1 and feat-cli-pay-behaviour) and ds-cli-outcome-90d (through feat-cli-spend-velocity). The memory tool's chain lines printed for this query were for churn-lr-base-2025, so I used the references in the notes themselves. Chasing ds-cli-eligible-pop leads to the glossary term "churn", which is superseded by the churn-includes-dormant correction, and to an unmatched reference to cards.limits_history.
Notes: work/ds-cli-eligible-pop.md, work/ds-cli-outcome-90d.md

## Q4
No decision notes rest on ds-clv-holdout-2021h1. Only exp-501-customer-lifetime-value builds on it, and nothing builds on that experiment in turn. clv-ml-v2 and exp-505 name the holdout in their text, but neither declares a link to it.
Notes: work/ds-clv-holdout-2021h1.md, work/exp-501-customer-lifetime-value.md

## Q5
pbs-kmeans-v1 was replaced by pbs-gmm-v2, then pbs-gmm-v3, and the line ends at dec-pbs-gmm-v3-current, which is the segment table of record in force since 26 Jan 2026. That decision is built on fnd-pbs-five-segments and pbs-gmm-v3.
Notes: work/dec-pbs-gmm-v3-current.md, work/fnd-pbs-five-segments.md, work/pbs-gmm-v3.md