**Q1: dec-xs-top-decile-offer and dec-xs-retrain-quarterly** both rest on feat-xs-balance-proxy, through xs-gbm-v2 and xs-gbm-v1. dec-xs-call-low-deciles does not.

**Q2: mrisk-gbm-v1 → mrisk-gbm-v2 → mrisk-gbm-v3.** mrisk-gbm-v3 is the current model. It is built on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2.

**Q3: cli-logreg-baseline** is built on feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour.
- feat-cli-util-v1 and feat-cli-pay-behaviour both build on ds-cli-eligible-pop.
- feat-cli-spend-velocity builds on ds-cli-outcome-90d, which builds on ds-cli-eligible-pop.
- So the dataset lineage is ds-cli-eligible-pop and ds-cli-outcome-90d.
- feat-cli-util-v1 is superseded by feat-cli-util-v2 (2025-10-14), but the baseline still uses v1.

**Q4: ds-clv-holdout-2021h1** is linked directly only to exp-501-customer-lifetime-value. That experiment feeds clv-bgnbd-v1 (the baseline) and q-clv-model-choice.
- Its note says it is the test set for every CLV model, so clv-ml-v1 and clv-ml-v2 depend on it by that statement. Neither note links to it directly.
- dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2 depend on it only through clv-ml-v1 and clv-ml-v2. Their own links are to clv-ml-v*, exp-503/exp-505 and the fnd-clv notes.
- dec-clv-include-losses does not depend on it. It builds on exp-502, fnd-clv-gross-overstates and q-clv-loss-treatment.
- dec-clv-discount-rate does not depend on it. It builds only on dec-clv-include-losses.

So for Q4, the decisions that rest on the holdout are dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2, but only indirectly. Neither of the other two does.

**Q5: pbs-kmeans-v1 → pbs-gmm-v2 → pbs-gmm-v3.** pbs-gmm-v3 is the current segment table. It is built on exp-403-payment-behavior-segments, feat-pbs-timing-v2 and pbs-gmm-v2.

Nothing was written or edited. Everything here came from reading the notes.