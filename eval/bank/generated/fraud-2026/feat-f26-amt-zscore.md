---
from: [fraud-2025/feat-f25-amt-ratio, ds-f26-cnp-txn]
updated: 2026-06-30
---
# feat-f26-amt-zscore: amount z-score against the card's 90-day history
Z-score of the CNP amount against the card's trailing 90-day mean and standard deviation.
Replaces the 2025 median ratio (feat-f25-amt-ratio) in v3; floor of 1.0 on the std.
Shipped in fraud26-gbm-v3 with geo-mismatch.
