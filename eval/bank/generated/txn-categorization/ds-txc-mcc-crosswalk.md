---
from: []
updated: 2025-05-12
---
# MCC-to-category crosswalk: 412 codes mapped to 23 categories
The crosswalk maps 412 merchant category codes to the same 23 categories used by the labels. Owner is data-eng-cards (Tomás Rivera).
14 codes are ambiguous (for example 5812 and 5814 split between 'Restaurants' and 'Food delivery') and are left to the model.
Source column is the MCC in `cards.merchants`; the crosswalk is versioned in the repo, not in the warehouse.
Source for feat-txc-mcc-prior.
