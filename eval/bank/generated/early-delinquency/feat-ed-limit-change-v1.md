---
from: [ds-ed-current-base]
updated: 2025-05-19
---
# feat-ed-limit-change-v1 is the credit-limit change over 90 days from cards.limits_history, with decreases flagged
Feature: percentage change in credit limit over the 90 days before the snapshot, plus a flag for any decrease.
Source: `cards.limits_history` (credit-data), joined at snapshot date.
On its face the feature is the strongest single signal tested so far. Its status is under review; see q-ed-limit-feature-usable.
