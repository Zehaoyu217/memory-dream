---
updated: 2026-01-20
supersedes: [howto/gbm-early-stopping-on-test]
---
# Early stopping uses a validation slice from the training window, never the OOT set
Stop on log-loss of a validation slice cut from the most recent three months of the training window, with patience of 50 rounds. The OOT set is scored once, after the round count is fixed. Sam Lee's pipeline enforces this through the `early_stop_split` parameter in the run config.
Re-runs under this rule come in lower on OOT than the old numbers did. That lower figure is the honest one.
