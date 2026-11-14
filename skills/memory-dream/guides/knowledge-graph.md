# The knowledge-graph page, for a memory or for any graph

Read this when someone wants to see the things and links of a memory, or of any other data, as one page that
opens offline.

- A memory: `memory.py viz` writes `memory/_dream/knowledge-graph.html`, and every dream that read links refreshes it.
  It needs a memory dreamed with a model command, because the things and links are what its keepers read.
  `--theme paper|star|gala|moon|fanfare|noir` picks the look it opens in; a switch in its header changes it.
- Any other graph: `python3 <this skill>/scripts/graph_page.py graph.json out.html [--title "…"] [--theme …]
  [--colour COLUMN]`, or `graph_page.py nodes.csv links.csv out.html`. The script's own help states the whole contract.
  The page holds 20,000 things and 45,000 links.

## The contract: the least it works with
- A **thing** needs an `id`. `label` is the name shown (the id when absent); `group` puts it on an island (without
  groups, the islands are the link communities).
- A **link** needs a `source` and a `target`. `type` says what it is (links-to when absent); `direction` is `->`
  (the default), `<-`, or `o-o` (none: equal, related, the same either way); `text` is the line that says so.
- **Every other field is a tag**, and nothing is declared. A tag is one column, and a row has a value, several (a
  list, or `;` between them) or none (absent, empty, n/a, none, unknown). The values tell its sort:
  - **category**: values that repeat (type, team, status), or paths whose levels are split by `/` (dataset/table).
  - **time**: ISO dates or moments, read as year / month / day.
  - **number**: every value a number. A thing's `size` sizes its dot, and a link's `weight` its line and how hard
    it pulls its ends together.
  - **text**: long or mostly unique values (a definition, a citation), shown whole and searched.
- Weight, time and provenance are tags like any other. Provenance is whichever tags say where a link comes from: a
  category (the system that found it), a time (when), a text (the citation).
- Optional entries only rename or overrule what the values say: `columns` (`name`, `parents` for a hierarchy over
  flat values, `names`, `colours`, `sort`, `use`), `link_columns`, and `link_types` (how a type reads forwards and
  back, and its direction).

## The fewest fields for the goal
Add a column only for a question people will ask of the picture.

| they want to see | give |
|---|---|
| what is linked to what | ids, and links with their two ends: nothing more |
| what kind of link each is | the link's `type`; `direction` only where it is not source to target |
| which things belong together | `group`, or nothing (the communities of the links) |
| things coloured by one property | one category column (`--colour` picks it; `type` is first by default) |
| a hierarchy | values written as paths (`dataset/table/daily`), or `parents` in `columns` |
| when | one ISO time column |
| how much, or how sure | one number column; `size` for things, `weight` for links |
| why a link is there | the link's `text`, plus a tag for its source |
| what a thing is | one text column (a definition) |

Leave out ids written again as tags, columns with one value everywhere (the legend shows no chip for them), and
anything a reader cannot act on. A memory's page already carries type (family/type), project, tag (TAGS.md, its
`family:` as levels), when last noted and About for each thing, and for each link the kind of the note that states
it, when, and whether that note was replaced.
