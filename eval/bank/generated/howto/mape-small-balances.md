---
updated: 2025-09-30
---
# MAPE is not reported for balances under $500; use WAPE for balance models
MAPE blows up when actual balances are near zero. Accounts under $50 drove 48% MAPE in the August 2025 monthly review. Use WAPE, which is the sum of absolute error divided by the sum of actual, and which was 12% on the same run.
MAPE is reported only for the segment above $500. Ben Carter's finance team reads WAPE as the headline.
