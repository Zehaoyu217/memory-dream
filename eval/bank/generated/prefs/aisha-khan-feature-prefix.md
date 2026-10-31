---
updated: 2026-01-13
---
# Aisha Khan wants every feature name prefixed with its domain code (`cli_`, `fraud_`, `col_`)
- Feature names carry their domain prefix: `cli_` for credit-line, `fraud_` for fraud, `col_` for collections.
- Names are snake_case and include the window, e.g. `cli_spend_30d_sum`.
- Reason: the registry had two `spend_30d` features from different domains with different definitions in 2025.
