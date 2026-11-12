## Q1
cld-gbm-v3 is the one in force; it replaced cld-gbm-v2, which had replaced cld-gbm-v1. cld-gbm-v3 is built on cld-gbm-v2 and feat-cld-payment-shock.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/feat-cld-payment-shock.md

## Q2
cc-ft-v1 rests on ds-cc-qa-labels and ds-cc-taxonomy-v3 directly, and on ds-cc-tickets-raw through ds-cc-qa-labels and feat-cc-embed-v1.
Notes: complaint-classification/cc-ft-v1.md, complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/feat-cc-embed-v1.md, complaint-classification/ds-cc-tickets-raw.md

## Q3
dec-xs-top-decile-offer rests on feat-xs-balance-proxy through xs-gbm-v2 and xs-gbm-v1, and dec-xs-retrain-quarterly rests on it through exp-407 and xs-gbm-v2. dec-xs-call-low-deciles does not, because its call-uplift chain never touches the balance proxy.
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md, cross-sell-savings/feat-xs-balance-proxy.md, cross-sell-savings/xs-gbm-v1.md, cross-sell-savings/xs-gbm-v2.md, cross-sell-savings/feat-xs-payroll-flag-v2.md, cross-sell-savings/exp-407-oot-2026h1.md

## Q4
mrisk-gbm-v3 is the one in force; it replaced mrisk-gbm-v2, which had replaced mrisk-gbm-v1. mrisk-gbm-v3 is built on mrisk-gbm-v2, feat-mrisk-dispute-ratio and exp-507.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/mrisk-gbm-v2.md, merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/exp-507.md

## Q5
cli-logreg-baseline rests on ds-cli-eligible-pop directly and on ds-cli-outcome-90d through feat-cli-spend-velocity. Its other inputs, feat-cli-pay-behaviour and feat-cli-util-v1, also trace back to ds-cli-eligible-pop.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-pay-behaviour.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/ds-cli-outcome-90d.md, credit-line-increase/ds-cli-eligible-pop.md

## Q6
dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2 both rest on ds-clv-holdout-2021h1, through exp-501, clv-bgnbd-v1, clv-ml-v1 and clv-ml-v2. No other decision note in the folder traces back to it.
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md, customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/exp-501.md, customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/clv-ml-v1.md, customer-lifetime-value/clv-ml-v2.md

## Q7
pbs-gmm-v3 is the one in force; it replaced pbs-gmm-v2, which had replaced pbs-kmeans-v1. pbs-gmm-v3 is built on exp-403, feat-pbs-timing-v2 and pbs-gmm-v2.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md, payment-behavior-segments/pbs-gmm-v2.md

## Q8
xs-call-uplift-v1 rests on ds-xs-callcentre directly, through its call-effect inputs and feat-xs-call-recent, and on ds-xs-offer-log through ds-xs-callcentre.
Notes: cross-sell-savings/xs-call-uplift-v1.md, cross-sell-savings/exp-403-callcentre-naive.md, cross-sell-savings/feat-xs-call-recent.md, cross-sell-savings/find-xs-call-overstated.md, cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through the disp-lgbm-v1/v2 and exp-306/307 chain.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/ds-disp-analyst-labels.md, dispute-triage/disp-lgbm-v1.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/disp-find-autoresolve-96.md, dispute-triage/exp-306.md, dispute-triage/exp-307.md

## Q10
rs-xgb-v3 is the one in force; it replaced rs-xgb-v2, which had replaced rs-xgb-v1. rs-xgb-v3 is built on exp-308 and rs-xgb-v2.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/exp-308.md, recovery-scoring/rs-xgb-v2.md