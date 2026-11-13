## Q1
`fsm-churn-xgb-v2` rests on the two feature-store-migration dataset notes, `ds-fsm-legacy-features` and `ds-fsm-parity-sample`, directly or through its feature and experiment inputs.

Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/ds-fsm-legacy-features.md, feature-store-migration/ds-fsm-parity-sample.md

## Q2
Only `retention-offers-roi/ror-uplift-v1` is a current model built directly on a replaced feature, `feat-ror-value-band-v1`. The other replaced inputs I found were models (`fraud25-gbm-v2`, `fraud26-gbm-v2`, `disp-lgbm-v2`, `sfc-lgbm-v2`), not feature or dataset notes.

Notes: retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/feat-ror-value-band-v1.md

## Q3
Six notes outside fraud-2025 rest on it directly: `fraud-2026/dec-f26-replace-f25`, `feat-f26-amt-zscore`, `feat-f26-device-age`, `feat-f26-velocity-v2`, `fraud26-gbm-v1` and `q-f26-travel-rule`. Through those, the fraud-2026 experiments, promote decisions, findings and `fraud26-gbm-v2`/`v3` depend on it too, and so do `dispute-triage/feat-disp-fraud-score`, `disp-lgbm-v3` and their dependents.

Notes: fraud-2026/dec-f26-replace-f25.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-device-age.md, fraud-2026/feat-f26-velocity-v2.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/fraud26-gbm-v3.md, fraud-2026/q-f26-travel-rule.md, fraud-2026/exp-201.md, fraud-2026/exp-203.md, fraud-2026/exp-204.md, fraud-2026/exp-205.md, fraud-2026/exp-206.md, fraud-2026/exp-207.md, fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-promote-v3.md, fraud-2026/fraud26-find-label-bias.md, fraud-2026/fraud26-find-geo-drift.md, fraud-2026/fraud26-find-velocity-leak.md, dispute-triage/feat-disp-fraud-score.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/exp-307.md, dispute-triage/disp-lgbm-v3.md, dispute-triage/exp-308.md

## Q4
Four notes outside churn-2025 rest on it. `retention-offers-roi/feat-ror-churn-score` uses `churn-gbm-2025-v2` directly. `exp-403`, `ror-uplift-v1` and `ror-roi-v1` depend on it transitively.

Notes: retention-offers-roi/feat-ror-churn-score.md, retention-offers-roi/exp-403.md, retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/ror-roi-v1.md

## Q5
Eight notes outside spend-forecasting rest on it. `revenue-forecast-2026/ds-rev26-spend-volume` and `rev26-combined-v1` use `sfc-hier-v3` directly. The rest are downstream of those two.

Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md, revenue-forecast-2026/feat-rev26-volume-lag.md, revenue-forecast-2026/exp-301.md, revenue-forecast-2026/exp-305.md, revenue-forecast-2026/exp-307.md, revenue-forecast-2026/dec-rev26-p10-p90-bands.md, revenue-forecast-2026/dec-rev26-v2-for-board.md

## Q6
Only one decision chain qualifies: `dec-cb-extend-flat-pilot` was replaced by `dec-cb-adopt-banded-tiers`, which was itself replaced by `dec-cb-threshold-2500`. The `dec-f26-promote-v2` → `v3` chain stops at `v3`, which has not been replaced.

Notes: cashback-redesign/dec-cb-extend-flat-pilot.md

## Q7
Four model chains qualify, and I've listed each chain's first note: `fraud25-gbm-v1` (through `v2`, `fraud26-gbm-v1`, `v2`, `v3`), `txc-logreg-v1` (through `txc-gbm-v2`, `v3`), `sfc-ets-v1` (through `sfc-lgbm-v2`, `sfc-hier-v3`) and `disp-lgbm-v1` (through `v2`, `v3`). `ror-roi-v1` is excluded because its replacement, `ror-roi-v2`, has not itself been replaced.

Notes: fraud-2025/fraud25-gbm-v1.md, txn-categorization/txc-logreg-v1.md, spend-forecasting/sfc-ets-v1.md, dispute-triage/disp-lgbm-v1.md

## Q8
Seven current notes have a direct link to a note in another project. `dispute-triage/feat-disp-fraud-score` is built on `fraud-2026/fraud26-gbm-v3`. The other six are fraud-2026 notes built on fraud-2025 notes: `dec-f26-replace-f25`, `feat-f26-amt-zscore`, `feat-f26-device-age`, `feat-f26-velocity-v2`, `fraud26-gbm-v1` and `q-f26-travel-rule`.

Notes: dispute-triage/feat-disp-fraud-score.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-device-age.md, fraud-2026/feat-f26-velocity-v2.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/q-f26-travel-rule.md

---

**Disclosure:** I created a scratch file at `<path>` earlier and have now deleted it. Some large tool outputs were also saved under `<path>`, outside the memory folder. I did not read those files, but they are still on disk, and I can delete them if you want. No notes were written, and I did not run `dream` or `log`.