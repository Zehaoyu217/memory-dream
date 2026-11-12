## Q1
cld-gbm-v3 is the one in force at the end of the cld-gbm-v1 line. It builds on cld-gbm-v2 and feat-cld-payment-shock.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/feat-cld-payment-shock.md

## Q2
cc-ft-v1 rests on three dataset notes: ds-cc-qa-labels and ds-cc-tickets-raw (through ds-cc-qa-labels and feat-cc-embed-v1), and ds-cc-taxonomy-v3 directly.
Notes: complaint-classification/cc-ft-v1.md, complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-tickets-raw.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/feat-cc-embed-v1.md

## Q3
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (via exp-405 and xs-gbm-v2, which builds on xs-gbm-v1) and dec-xs-retrain-quarterly (via exp-407 and the payroll-flag boosting model xs-gbm-v2).
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md

## Q4
mrisk-gbm-v3 is in force. It builds on mrisk-gbm-v2, exp-507 and feat-mrisk-dispute-ratio (borrowed from dispute-triage).
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/mrisk-gbm-v2.md, merchant-risk/exp-507.md, merchant-risk/feat-mrisk-dispute-ratio.md

## Q5
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop directly, and ds-cli-outcome-90d (which itself builds on ds-cli-eligible-pop).
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 (via exp-501, clv-bgnbd-v1, clv-ml-v1) and dec-clv-ship-ml-v2 (via clv-ml-v2, which builds on clv-ml-v1).
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
pbs-gmm-v3 is in force. It builds on pbs-gmm-v2, exp-403 and feat-pbs-timing-v2.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/pbs-gmm-v2.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md

## Q8
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre (directly and via feat-xs-call-recent and exp-403) and ds-xs-offer-log (via ds-xs-callcentre).
Notes: cross-sell-savings/xs-call-uplift-v1.md, cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through the model and experiment chains.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
rs-xgb-v3 is in force. It builds on rs-xgb-v2 and exp-308.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/rs-xgb-v2.md, recovery-scoring/exp-308.md