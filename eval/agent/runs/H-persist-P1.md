## Q1
feat-rs-region-rate is the out-of-fold recovery rate by postcode region, used in rs-xgb-v1. It lifted Gini from 0.42 to 0.44 on recovery-scoring-holdout-2023h2 (exp-303), but it proxies neighbourhood demographics, so it was flagged by compliance and dropped from all recovery-scoring models (dec-rs-drop-region, 2025-05-22). The current model rs-xgb-v3 does not use it.
Sources: memory/recovery-scoring/feat-rs-region-rate.md, memory/recovery-scoring/exp-303.md, memory/recovery-scoring/exp-304.md, memory/recovery-scoring/find-rs-region-proxy.md, memory/recovery-scoring/dec-rs-drop-region.md

## Q2
exp-403-callcentre-naive found a naive +1.8 point open-rate lift from a call in the prior 90 days (4.9% against 3.1%). After matching on propensity and tenure the effect fell to +0.6 points, not significant, so the naive effect was mostly selection (find-xs-call-overstated). Call outreach was then restricted to deciles 1-2 only, where exp-406 and xs-call-uplift-v1 show about +1.2 points (dec-xs-call-low-deciles).
Sources: memory/cross-sell-savings/exp-403-callcentre-naive.md, memory/cross-sell-savings/find-xs-call-overstated.md, memory/cross-sell-savings/xs-call-uplift-v1.md, memory/cross-sell-savings/dec-xs-call-low-deciles.md, memory/cross-sell-savings/exp-406-call-uplift.md

## Q3
sfc-hier-v3 is built from sfc-lgbm-v2 (now superseded) with the feat-sfc-active-accounts regressor added, and its Q4 bias was fixed by MinT reconciliation (exp-207, fnd-sfc-q4-reconciled, which gave Q4 bias of -0.4%). It also uses feat-sfc-cpi-lag6, and it is the spend volume input for revenue-forecast-2026 (downstream, not a dependency). It is evaluated on sfc-oot-2025h2 with total MAPE 2.3%.
Sources: memory/spend-forecasting/sfc-hier-v3.md, memory/spend-forecasting/feat-sfc-active-accounts.md, memory/spend-forecasting/exp-207.md, memory/spend-forecasting/fnd-sfc-q4-reconciled.md, memory/spend-forecasting/feat-sfc-cpi-lag6.md, memory/spend-forecasting/dec-sfc-ship-hier-v3.md

## Q4
The fraud-2026 model now uses an alert threshold of 0.66. fraud26-gbm-v3 was promoted on 2026-08-26 with that threshold, replacing v2's 0.62 (dec-f26-promote-v3). The basis was exp-208: 21.5% precision at a 0.6% alert rate, recall 0.61.
Sources: memory/fraud-2026/dec-f26-promote-v3.md, memory/fraud-2026/fraud26-gbm-v3.md, memory/fraud-2026/exp-208.md, memory/fraud-2026/dec-f26-promote-v2.md

## Q5
mrisk-gbm-v2 reached AUC 0.86 and precision@100 0.43 on mrisk-oot-2026h1 (exp-505, 2026-07-06), and exp-507 repeats these same figures as its reference. It was later superseded by mrisk-gbm-v3, which reached AUC 0.91 and precision@100 0.58.
Sources: memory/merchant-risk/mrisk-gbm-v2.md, memory/merchant-risk/exp-505.md, memory/merchant-risk/exp-507.md

## Q6
The new-account scorecard was rebuilt as v4 (dec-app-rebuild-v4) because v3's Gini fell from 0.41 to 0.33 on the 2026-Q1 holdout as bureau scores drifted (find-app-gini-v3-drift). The rebuild moves to v10 bands, reject-inference weights and the income estimate, and reaches out-of-time Gini 0.42 against 0.35 for v3 (exp-507).
Sources: memory/application-scorecard/dec-app-rebuild-v4.md, memory/application-scorecard/find-app-gini-v3-drift.md, memory/application-scorecard/exp-507.md, memory/application-scorecard/app-scorecard-v4.md, memory/application-scorecard/q-app-gini-target.md

## Q7
feat-txc-normalise-v2 (created 2025-09-22 from the descriptor sample) strips store numbers, hash codes and city suffixes from transaction descriptors. Adding it lifted txc-gbm-v2 macro-F1 from 0.78 to 0.81 (exp-104). It is an input to txc-gbm-v3, the current model at macro-F1 0.83, and the rule list is versioned in the repo, so new suffixes are added by pull request.
Sources: memory/txn-categorization/feat-txc-normalise-v2.md, memory/txn-categorization/exp-104.md, memory/txn-categorization/txc-gbm-v3.md, memory/txn-categorization/feat-txc-descriptor-tokens-v2.md

## Q8
exp-205 added the payment-to-minimum ratio (feat-ed-minpay-v2) to ed-gbm-v1 and lifted AUC from 0.781 to 0.803 on early-delinquency-holdout-2024q4, with no limit-change feature (Gini 0.606, KS 0.44). That signal went into ed-gbm-v2 (find-ed-minpay calls it the real second signal, with no leakage). ed-gbm-v3 is the current model.
Sources: memory/early-delinquency/exp-205.md, memory/early-delinquency/find-ed-minpay.md, memory/early-delinquency/ed-gbm-v2.md, memory/early-delinquency/ed-gbm-v3.md

## Q9
fsm-churn-xgb-v2 reads 41 feature-store features. These are the 40 v1 features, with feat-fsm-payment-lag-v2 (UTC) and feat-fsm-util-ratio read from the store, plus feat-fsm-spend-cv-30d. It uses the same trees and hyperparameters as v1, and holdout AUC is 0.791 against 0.782 for v1 (exp-105).
Sources: memory/feature-store-migration/fsm-churn-xgb-v2.md, memory/feature-store-migration/exp-105.md, memory/feature-store-migration/feat-fsm-payment-lag-v2.md, memory/feature-store-migration/feat-fsm-util-ratio.md, memory/feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
The current approval cutoff for application decisions on the v10 scale is 652. It took effect 2026-09-01 and replaced the v8 cutoff of 640, with the same 58% approval rate and 4.1% bad rate (exp-305). The grep of bureau-score-migration found no later decision that changes it, and the v8 fallback stays in place.
Sources: memory/bureau-score-migration/dec-bsm-cutover-2026q3.md, memory/bureau-score-migration/bsm-cutoff-logit.md, memory/bureau-score-migration/exp-305.md