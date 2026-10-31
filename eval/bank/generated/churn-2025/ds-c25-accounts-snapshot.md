---
from: []
updated: 2025-01-07
---
# Churn-2025 base population: 1.18M account-months from cards.accounts_monthly
Month-end snapshots of open consumer accounts from `cards.accounts_monthly`, 2023-07 to 2024-01 for training.
- Rows: 1,184,206 account-months across 412,955 accounts. Charged-off and deceased flags excluded.
- Fields used: statement balance, credit limit, months on book, segment code.
- Limit changes come from `cards.limits_history`, joined for util-v2.
