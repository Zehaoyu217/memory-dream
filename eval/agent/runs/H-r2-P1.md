## Q1
feat-rs-region-rate is the out-of-fold recovery rate by postcode region, target-encoded and smoothed toward the book mean. It lifted Gini from 0.41 to 0.44 (exp-303), but the 2.9x recovery spread across region deciles at equal balance and payment history showed it was a proxy for neighbourhood demographics, so it was dropped from all recovery-scoring models (dec-rs-drop-region); rs-xgb-v2 (Gini 0.47) has no region feature.
Sources: memory/recovery-scoring/feat-rs-region-rate.md, memory/recovery-scoring/find-rs-region-proxy.md, memory/recovery-scoring/dec-rs-drop-region.md, memory/recovery-scoring/exp-304.md

## Q2
The naive comparison showed +1.8 points of open rate (4.9% with a call against 3.1% without). After matching on propensity and tenure the effect fell to +0.6 points, not significant, so the naive result was mostly selection (find-xs-call-overstated). The later causal forest (xs-call-uplift-v1) and exp-406 led to limiting call-centre outreach to deciles 1-2, where a call adds about 1.2 points.
Sources: memory/cross-sell-savings/exp-403-callcentre-naive.md, memory/cross-sell-savings/find-xs-call-overstated.md, memory/cross-sell-savings/dec-xs-call-low-deciles.md

## Q3
sfc-hier-v3 is built from sfc-lgbm-v2 (its base, which it supersedes), feat-sfc-active-accounts (added as a regressor), fnd-sfc-q4-reconciled (the Q4 bias finding) and exp-207 (the MinT reconciliation experiment). It reaches total MAPE 2.3% on sfc-oot-2025h2 and was adopted for finance FY26 volume.
Sources: memory/spend-forecasting/sfc-hier-v3.md, memory/spend-forecasting/dec-sfc-ship-hier-v3.md

## Q4
The alert threshold is 0.66. fraud26-gbm-v3 replaced v2 (threshold 0.62) from 2026-08-26 with no travel-specific uplift (dec-f26-promote-v3). At 0.66 exp-208 gives 21.5% precision at a 0.6% alert rate.
Sources: memory/fraud-2026/dec-f26-promote-v3.md, memory/fraud-2026/exp-208.md, memory/fraud-2026/fraud26-gbm-v3.md

## Q5
mrisk-gbm-v2 reached AUC 0.86 and precision@100 of 0.43 on mrisk-oot-2026h1 (exp-505, 2026-07-06). It has since been superseded by mrisk-gbm-v3, which reached AUC 0.91 and precision@100 0.58 on the same holdout (exp-507).
Sources: memory/merchant-risk/exp-505.md, memory/merchant-risk/mrisk-gbm-v2.md, memory/merchant-risk/exp-507.md

## Q6
The v3 scorecard's Gini fell from 0.41 to 0.33 on the 2026-Q1 holdout as bureau scores drifted (find-app-gini-v3-drift), so the team decided to rebuild on v10 bands, reject inference and the income estimate (dec-app-rebuild-v4). On the out-of-time set v4 reached Gini 0.42 against 0.35 for v3 (exp-507), and its approval cutoff is 592 on the v4 points scale from 2026-11-01.
Sources: memory/application-scorecard/dec-app-rebuild-v4.md, memory/application-scorecard/find-app-gini-v3-drift.md, memory/application-scorecard/exp-507.md, memory/application-scorecard/app-scorecard-v4.md, memory/application-scorecard/dec-app-cutoff-v4.md

## Q7
feat-txc-normalise-v2 strips store numbers, hash codes and city suffixes from merchant descriptors before tokenising, and its rule list is versioned in the repo. It lifted txc-gbm-v2 macro-F1 from 0.78 to 0.81 (exp-104) and is an input to txc-gbm-v3, the current model with macro-F1 0.83 on txc-oot-2026h1.
Sources: memory/txn-categorization/feat-txc-normalise-v2.md, memory/txn-categorization/exp-104.md, memory/txn-categorization/txc-gbm-v3.md

## Q8
exp-205 added the payment-to-minimum ratio (feat-ed-minpay-v2) to ed-gbm-v1 without the limit feature, lifting AUC from 0.781 to 0.803 on early-delinquency-holdout-2024q4 (+0.022, no leakage per find-ed-minpay). The signal became part of ed-gbm-v2, which ed-gbm-v3 later superseded.
Sources: memory/early-delinquency/exp-205.md, memory/early-delinquency/find-ed-minpay.md, memory/early-delinquency/ed-gbm-v2.md

## Q9
fsm-churn-xgb-v2 reads 41 store features: v1's 40 legacy features, with feat-fsm-payment-lag-v2 and feat-fsm-util-ratio taken from the feature store, plus feat-fsm-spend-cv-30d. Its holdout AUC is 0.791 against 0.782 for v1 (exp-105), and it cut over on 2026-03-02 behind the parity gate (dec-fsm-cutover).
Sources: memory/feature-store-migration/fsm-churn-xgb-v2.md, memory/feature-store-migration/exp-105.md, memory/feature-store-migration/dec-fsm-cutover.md, memory/feature-store-migration/feat-fsm-payment-lag-v2.md, memory/feature-store-migration/feat-fsm-util-ratio.md

## Q10
The approval cutoff is 652 on the v10 scale, replacing the v8 cutoff of 640 for application decisions from 2026-09-01 (dec-bsm-cutover-2026q3). exp-305 showed it holds the same 58% approval rate and 4.1% bad rate.
Sources: memory/bureau-score-migration/dec-bsm-cutover-2026q3.md, memory/bureau-score-migration/exp-305.md, memory/bureau-score-migration/bsm-cutoff-logit.md