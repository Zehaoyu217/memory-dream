---
updated: 2026-01-30
---
# Sam Lee requires every reported number to rebuild from one `make report` target
- Every number in a deck or model card is produced by `make report`; no figure is copied by hand from a notebook.
- Each run writes a manifest with the git SHA, seed `20260` and the input table snapshot date.
- A figure that cannot be rebuilt from the manifest is removed from the deck, not footnoted.
