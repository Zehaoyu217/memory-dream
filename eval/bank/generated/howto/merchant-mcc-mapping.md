---
updated: 2025-11-11
---
# Map merchants to a category with the four-digit MCC, not the merchant name
`cards.merchants` carries `mcc` as a four-digit string. Category comes from the MCC table, and MCC 5812 and 5814 both map to restaurants. Grouping by merchant name split one chain into 14 groups in the 2025 spend model, so name grouping was dropped.
