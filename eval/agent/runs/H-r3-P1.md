## Q1
feat-rs-region-rate is the out-of-fold recovery rate by postcode region (target-encoded, smoothed to the book mean). It lifted Gini from 0.41 to 0.44 (exp-303), but exp-304 showed a 2.9x recovery spread across region deciles at equal balance and payment history, so it was read as a proxy for neighbourhood demographics and dropped from all recovery-scoring models (dec-rs-drop-region, 2025-05-22).
Sources: memory/recovery-scoring/feat-rs-region-rate.md, memory/recovery-scoring/exp-303.md, memory/recovery-scoring/exp-304.md, memory/recovery-scoring/find-rs-region-proxy.md, memory/recovery-scoring/dec-rs-drop-region.md

## Q2
exp-403 found a raw call-centre effect of +1.8 points of open rate (4.9% with a call vs 3.1% without), but after matching on propensity and tenure the effect was +0.6 points and not significant, so the naive effect was mostly selection (find-xs-call-overstated). The causal forest in xs-call-uplift-v1 and exp-406 then found a call adds about 1.2 points in deciles 1-2, and the decision (dec-xs-call-low-deciles, 2025-11-10) limits call-centre outreach to deciles 1-2.
Sources: memory/cross-sell-savings/exp-403-callcentre-naive.md, memory/cross-sell-savings/find-xs-call-overstated.md, memory/cross-sell-savings/xs-call-uplift-v1.md, memory/cross-sell-savings/exp-406-call-uplift.md, memory/cross-sell-savings/dec-xs-call-low-deciles.md

## Q3
sfc-hier-v3 is built from sfc-lgbm-v2 (which it supersedes) with feat-sfc-active-accounts added as a regressor per segment, and its basis is exp-207 (MinT reconciliation, total MAPE 2.9% to 2.3% on sfc-oot-2025h2) and fnd-sfc-q4-reconciled (Q4 bias -0.4%). Its downstream dependant is revenue-forecast-2026, which uses it as the spend-volume input for interchange.
Sources: memory/spend-forecasting/sfc-hier-v3.md, memory/spend-forecasting/dec-sfc-ship-hier-v3.md, memory/spend-forecasting/exp-207.md, memory/spend-forecasting/feat-sfc-active-accounts.md, memory/spend-forecasting/fnd-sfc-q4-reconciled.md

## Q4
The current fraud-2026 alert threshold is 0.66, set with fraud26-gbm-v3 from 2026-08-26 (dec-f26-promote-v3), replacing 0.62 under v2. The basis was exp-208: at 0.66 the v3 candidate gives a 0.6% alert rate, 21.5% precision and 0.61 recall.
Sources: memory/fraud-2026/dec-f26-promote-v3.md, memory/fraud-2026/exp-208.md, memory/fraud-2026/fraud26-gbm-v3.md, memory/fraud-2026/dec-f26-promote-v2.md

## Q5
mrisk-gbm-v2 reached AUC 0.86 and precision@100 0.43 on mrisk-oot-2026h1 (exp-505, 2026-07-06). It was later superseded by mrisk-gbm-v3, which reached AUC 0.91 and precision@100 0.58 on the same holdout (exp-507).
Sources: memory/merchant-risk/exp-505.md, memory/merchant-risk/mrisk-gbm-v2.md, memory/merchant-risk/exp-507.md, memory/merchant-risk/mrisk-gbm-v3.md

## Q6
Gini for app-scorecard-v3 drifted from 0.41 to 0.33 on the 2026-Q1 holdout as bureau scores drifted (find-app-gini-v3-drift). The rebuild (dec-app-rebuild-v4, 2026-06-26) kept the points-based form and added v10 bureau bands, an income estimate and reject-inference weights. On the out-of-time set v4 reached Gini 0.42 against 0.35 for v3 (exp-507), and the goal was to reach 0.42 without manual overrides.
Sources: memory/application-scorecard/find-app-gini-v3-drift.md, memory/application-scorecard/dec-app-rebuild-v4.md, memory/application-scorecard/app-scorecard-v4.md, memory/application-scorecard/exp-507.md, memory/application-scorecard/q-app-gini-target.md

## Q7
feat-txc-normalise-v2 strips store numbers, hash codes and city suffixes from transaction descriptors, and its rule list is versioned in the repo so new suffixes come in by pull request. It lifted txc-gbm-v2 macro-F1 from 0.78 to 0.81 (exp-104). It is an input to txc-gbm-v3, the current model (macro-F1 0.83 on txc-oot-2026h1), shipped 2026-03-10 with the v2 token set.
Sources: memory/txn-categorization/feat-txc-normalise-v2.md, memory/txn-categorization/exp-104.md, memory/txn-categorization/txc-gbm-v3.md, memory/txn-categorization/dec-txc-ship-gbm-v3.md

## Q8
exp-205 added the payment-to-minimum ratio (feat-ed-minpay-v2) to ed-gbm-v1 and lifted AUC from 0.781 to 0.803 on early-delinquency-holdout-2024q4 (+0.022, no leakage), without the limit-change feature. The feature went into ed-gbm-v2 (2025-09-10), and ed-gbm-v3 later reached AUC 0.809 on early-delinquency-oot-2026h1.
Sources: memory/early-delinquency/exp-205.md, memory/early-delinquency/find-ed-minpay.md, memory/early-delinquency/ed-gbm-v2.md, memory/early-delinquency/ed-gbm-v3.md

## Q9
fsm-churn-xgb-v2 reads 41 store features: v1's 40 features, with feat-fsm-payment-lag-v2 (UTC timestamps) and feat-fsm-util-ratio taken from the store, plus feat-fsm-spend-cv-30d. It was trained on the same trees and hyperparameters and reached holdout AUC 0.791 on holdout-2025q2.
Sources: memory/feature-store-migration/fsm-churn-xgb-v2.md, memory/feature-store-migration/exp-105.md, memory/feature-store-migration/feat-fsm-payment-lag-v2.md, memory/feature-store-migration/feat-fsm-util-ratio.md, memory/feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
The current approval cutoff on the v10 scale is 652, in force from the 2026-09-01 cutover (dec-bsm-cutover-2026q3). It matches the v8 cutoff of 640 at a 58% approval rate and a 4.1% bad rate (exp-305), and the v8 fallback stays in place.
Sources: memory/bureau-score-migration/dec-bsm-cutover-2026q3.md, memory/bureau-score-migration/exp-305.md, memory/bureau-score-migration/bsm-cutoff-logit.md, memory/bureau-score-migration/dec-bsm-keep-v8-fallback.md