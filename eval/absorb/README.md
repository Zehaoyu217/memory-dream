# eval/absorb — a graph another system's model wrote

`policy-kb/` is a small made-up knowledge base in the shape model-written graphs usually have: one card per entity
(`entities/<id>.md` with `type`, `id`, `title`, `entity_type`, `aliases`, `sources`), one `relations.jsonl`
(`{from, relation, label, to, evidence[]}`) and the three source texts the relations cite. Its evidence is a file
name, with no line and no quote.

It is about model governance at the bank of the test world, so four of its eleven things (`fraud26-gbm-v3`,
`fraud25-gbm-v2`, `lightgbm`, `auc`) are things the bank's memory already names. Three of its twelve relations are
planted errors: they name a thing that the source they cite never mentions.

`eval/contract_probe.py` (experiment 4) turns it into notes and readings, takes it into a memory through the
file-mode socket, asks a question across the two, and drops it again. RESULTS phase K has the numbers.
