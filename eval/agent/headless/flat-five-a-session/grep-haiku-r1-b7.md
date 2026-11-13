## Q1
The chain rests on one dataset root, `ds-cb-sessions`. It reaches that root directly through `ds-cb-escalation-labels` and through `feat-cb-prior-calls-v1` → `ds-cb-call-linkage`.

Notes: work/cb-escalate-v1.md, work/ds-cb-escalation-labels.md, work/feat-cb-prior-calls-v1.md, work/ds-cb-call-linkage.md, work/ds-cb-sessions.md

## Q2
`nps-gbm-v1` and `nps-gbm-v2` both build directly on three features: the complaint call flag (`feat-nps-complaint-flag-v1`), the theme share feature (`feat-nps-theme-share-v1`) and the transaction frequency feature (`feat-nps-txn-freq-v1`). `nps-gbm-v2` also adds `feat-nps-fee-shock-v2`, which `v1` does not use.

Notes: work/nps-gbm-v1.md, work/nps-gbm-v2.md, work/feat-nps-complaint-flag-v1.md, work/feat-nps-theme-share-v1.md, work/feat-nps-txn-freq-v1.md

## Q3
Two decision notes rest on `feat-c25-util-v2`. `dec-c25-drop-app-sessions` gets there through `exp-104-churn-2025` → `exp-105-churn-2025`. `dec-c25-ship-gbm-v2` gets there through `churn-gbm-2025-v2`. The same model also feeds `exp-106`, `exp-107` and the `ror-uplift-v1` chain, but those are experiments and downstream uses, not decisions.

Notes: work/feat-c25-util-v2.md, work/exp-104-churn-2025.md, work/exp-105-churn-2025.md, work/dec-c25-drop-app-sessions.md, work/churn-gbm-2025-v2.md, work/dec-c25-ship-gbm-v2.md

## Q4
The line ends at `fraud26-gbm-v3`, which is in force. `dec-f26-promote-v3` put it live from 2026-08-26, replacing `v2`. It builds on `exp-207-fraud-2026`, `feat-f26-amt-zscore`, `feat-f26-geo-mismatch` and `fraud26-gbm-v2`. I found no later promotion note, so it is still the current model as of 2026-11-12.

Notes: work/fraud25-gbm-v1.md, work/dec-f25-champion-v2.md, work/dec-f26-replace-f25.md, work/fraud26-gbm-v1.md, work/fraud26-gbm-v2.md, work/dec-f26-promote-v2.md, work/fraud26-gbm-v3.md, work/dec-f26-promote-v3.md, work/exp-207-fraud-2026.md, work/feat-f26-amt-zscore.md, work/feat-f26-geo-mismatch.md

## Q5
Following `churn-gbm-2025-v2` back, the verified dataset roots are `ds-c25-accounts-snapshot` (via `feat-c25-util-v2`, `feat-c25-payment-behaviour` and `feat-c25-txn-recency`) and `ds-c25-app-engagement` (via `feat-c25-app-sessions`, which the dropped-app-sessions decision rests on). I did not find `ds-c25-churn-labels` or `ds-c25-oot-2024h1` in the builds-on chain I checked. The label note `dec-c25-label-60d` and the holdout note `ds-c25-oot-2024h1` are linked to the churn work, but not as ancestors of `churn-gbm-2025-v2`. The walk through `fnd-c25-recency-dominates` is also unchecked.

Notes: work/churn-gbm-2025-v2.md, work/dec-c25-drop-app-sessions.md, work/exp-105-churn-2025.md, work/exp-104-churn-2025.md, work/feat-c25-util-v2.md, work/exp-106-churn-2025.md, work/feat-c25-payment-behaviour.md, work/feat-c25-txn-recency.md, work/feat-c25-app-sessions.md, work/ds-c25-accounts-snapshot.md, work/ds-c25-app-engagement.md