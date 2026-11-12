## Q1
The line runs cld-gbm-v1 → cld-gbm-v2 → cld-gbm-v3, and cld-gbm-v3 is the model in force now (AUC 0.81 on cld-test-2026q1). It is built on cld-gbm-v2 (now replaced) and feat-cld-payment-shock.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/feat-cld-payment-shock.md

## Q2
cc-ft-v1 rests on three dataset notes: ds-cc-qa-labels and ds-cc-taxonomy-v3 directly, and ds-cc-tickets-raw through ds-cc-qa-labels and feat-cc-embed-v1.
Notes: complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/ds-cc-tickets-raw.md

## Q3
Two decisions rest on feat-xs-balance-proxy. dec-xs-top-decile-offer rests on it through xs-gbm-v2 and exp-405-top-decile. dec-xs-retrain-quarterly rests on it through xs-gbm-v2, exp-407-oot-2026h1 and find-xs-drift-2026. xs-gbm-v2 itself traces back to the proxy through xs-gbm-v1 and feat-xs-payroll-flag-v2.
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md

## Q4
The line runs mrisk-gbm-v1 → mrisk-gbm-v2 → mrisk-gbm-v3, and mrisk-gbm-v3 is in force now. It is built on exp-507, feat-mrisk-dispute-ratio and mrisk-gbm-v2 (now replaced).
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/exp-507.md, merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/mrisk-gbm-v2.md

## Q5
cli-logreg-baseline rests on two dataset notes. ds-cli-eligible-pop comes in through feat-cli-pay-behaviour, feat-cli-util-v1 and q-cli-utilization-trigger. ds-cli-outcome-90d comes in through feat-cli-spend-velocity, and it is itself built on ds-cli-eligible-pop.
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decisions rest on ds-clv-holdout-2021h1. dec-clv-ship-ml-v1 (now replaced) rests on it through exp-501, clv-bgnbd-v1, clv-ml-v1 and fnd-clv-bgnbd-bias. dec-clv-ship-ml-v2, the current one, rests on it through clv-ml-v2 and dec-clv-ship-ml-v1.
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
The line runs pbs-kmeans-v1 → pbs-gmm-v2 → pbs-gmm-v3, and pbs-gmm-v3 is in force now. It is built on exp-403, feat-pbs-timing-v2 and pbs-gmm-v2 (now replaced).
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md, payment-behavior-segments/pbs-gmm-v2.md

## Q8
xs-call-uplift-v1 rests on two dataset notes. ds-xs-callcentre comes in through exp-403-callcentre-naive, feat-xs-call-recent and find-xs-call-overstated. ds-xs-offer-log comes in because ds-xs-callcentre is built on it.
Notes: cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decisions rest on ds-disp-analyst-labels. dec-disp-labels-two-analyst uses it directly. dec-disp-autoresolve-090 (now replaced) and dec-disp-autoresolve-095 rest on it through ds-disp-oot, exp-304 and exp-305, and also through the exp-301→303 line and disp-lgbm-v2. dec-disp-fraud-score-in rests on it through exp-306 and exp-307.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
The line runs rs-xgb-v1 → rs-xgb-v2 → rs-xgb-v3, and rs-xgb-v3 is in force now. It is built on exp-308 and rs-xgb-v2 (now replaced).
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/exp-308.md, recovery-scoring/rs-xgb-v2.md