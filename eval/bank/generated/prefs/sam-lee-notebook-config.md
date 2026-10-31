---
updated: 2025-10-14
---
# Sam Lee wants every notebook to open with a config cell and seed 20260
- The first code cell holds all paths, table names and the seed (`SEED = 20260`); no hard-coded paths appear below it.
- Print statements are replaced by a small `log()` helper that writes to the run log.
- Outputs are cleared before commit with `nbstripout`, so diffs show code only.
