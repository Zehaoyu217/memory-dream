---
from: [fraud25-gbm-v2, ds-f25-travel-tags]
updated: 2025-09-08
---
# Why do travel-MCC alerts take about 31% of the fraud-2025 queue?
Travel merchants are about 11% of card-not-present volume but about 31% of alerts from fraud25-gbm-v2 in the Jul-Sep 2025 replay (exp-106, `fraud25_alerts_log`).
Open: is the travel flag driving the score, or are travel tickets larger and more often in the holdout? Split alert precision by MCC group before changing the threshold.
