## Q1
cld-gbm-v3 is in force at the end of the cld-gbm-v1 line (v1 was replaced by v2, then v2 by v3). It builds on cld-gbm-v2 and feat-cld-payment-shock.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/feat-cld-payment-shock.md

## Q2
cc-ft-v1 rests on three dataset notes: ds-cc-qa-labels and ds-cc-taxonomy-v3 directly, and ds-cc-tickets-raw through ds-cc-qa-labels and feat-cc-embed-v1.
Notes: complaint-classification/cc-ft-v1.md, complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/feat-cc-embed-v1.md, complaint-classification/ds-cc-tickets-raw.md

## Q3
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (via xs-gbm-v2, which builds on feat-xs-payroll-flag-v2, which replaces the balance proxy) and dec-xs-retrain-quarterly (via exp-407, which builds on xs-gbm-v2). dec-xs-call-low-deciles does not rest on it.
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md, cross-sell-savings/feat-xs-balance-proxy.md, cross-sell-savings/feat-xs-payroll-flag-v2.md, cross-sell-savings/xs-gbm-v2.md, cross-sell-savings/exp-407-oot-2026h1.md

## Q4
mrisk-gbm-v3 is in force at the end of the mrisk-gbm-v1 line. It builds on exp-507, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/exp-507.md, merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/mrisk-gbm-v2.md

## Q5
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop (directly, and through the pay-behaviour and utilisation features) and ds-cli-outcome-90d (through feat-cli-spend-velocity).
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-pay-behaviour.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 (via exp-501, clv-bgnbd-v1 and clv-ml-v1) and dec-clv-ship-ml-v2 (which builds on dec-clv-ship-ml-v1).
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md, customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/exp-501.md, customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/clv-ml-v1.md

## Q7
pbs-gmm-v3 is in force at the end of the pbs-kmeans-v1 line (v1 was replaced by pbs-gmm-v2, then pbs-gmm-v2 by pbs-gmm-v3). It builds on exp-403, feat-pbs-timing-v2 and pbs-gmm-v2.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md, payment-behavior-segments/pbs-gmm-v2.md

## Q8
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre directly, and ds-xs-offer-log through ds-xs-callcentre.
Notes: cross-sell-savings/xs-call-uplift-v1.md, cross-sell-savings/exp-403-callcentre-naive.md, cross-sell-savings/feat-xs-call-recent.md, cross-sell-savings/find-xs-call-overstated.md, cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through the disp-lgbm-v2, exp-304 and exp-306 chain.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/ds-disp-analyst-labels.md

## Q10
rs-xgb-v3 is in force at the end of the rs-xgb-v1 line (v1 was replaced by v2, then v2 by v3). It builds on exp-308 and rs-xgb-v2.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/exp-308.md, recovery-scoring/rs-xgb-v2.md