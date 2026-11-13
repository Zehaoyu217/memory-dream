# EDGES — relation types between entities, read "X <type> Y". Constrained open: the dreamer uses these types and
# their aliases (~ = read in reverse); any other link it finds keeps its own label and is shown as other/<label>.
# A label becomes a type only over the bar below, through the review, within the budget; a type marked
# (proposed <date>) is demoted back to a label if it is still under the bar after the probation. Edit freely: a
# hand-written line is permanent and relabels everything at the next merge (0 calls). Optional: pack: software, research, ops.
# Note-to-note links (from:, supersedes:, refs) are lineage, not relations.
# `walk:` lists the words of a question that make `ask` follow that type from a thing the question names: `*` stands
# for any letters, `(a/b)` for either, and a word marked `~` asks for the link read the other way ("what uses X").
# `hops: 2` marks a type whose links chain: an input of an input is an input. A line without them takes the seed's.
promote: 5 uses, 5 notes, 2 areas
budget: 24
probation: 60 days
- uses: X needs Y as an input (model uses feature; feature uses table) | walk: use, uses, using, used by, depend*, input, inputs, feed, feeds, read, reads, built on, built from, based on, source, sources, feature, features, ~(what/which/who) (use/uses/depend/depends/read/reads/consume/consumes/feed/feeds/relies), ~used by, ~downstream, ~dependent, ~dependents | hops: 2 | aka: depends-on, consumes, built-on, built-from, derived-from, based-on, sourced-from, requires, reads, reads-from, joined-to, ~feeds, ~input-to, ~used-by, ~used-for, ~used-in, basis
- produces: X creates or writes Y (job produces table; model produces scores) | walk: produce, produces, output, outputs, write, writes, generat* | aka: writes, writes-to, creates, outputs, generates, ~generated-by, ~produced-by, ~output-of
- part-of: X is a component of Y (column part-of table; feature part-of feature-set) | walk: part of, component, components, member, members, column, columns, contain, contains | hops: 2 | aka: member-of, column-of, subset-of, stored-in, ~contains, ~has, ~includes
- trained-on: model X was fit on dataset Y | walk: train*, fit on, fitted on | hops: 2 | aka: fit-on, fitted-on, trained-with | shape: model → dataset
- evaluated-on: X was measured on dataset or segment Y | walk: evaluat*, tested on, validat*, holdout, holdouts, backtest*, scored on | aka: tested-on, validated-on, measured-on, scored-on, backtested-on | shape: * → dataset
- measured-by: X is judged by metric Y | walk: metric, metrics, measured by, auc, recall, precision, mape, f1, score, scores, scored | aka: reports, reports-metric, has-metric, measures, measured-in, scored-by, optimizes, optimises, targets, ~metric-of | shape: * → metric
- replaces: X is the newer version of Y | walk: replac*, supersed*, version, versions, predecessor, successor, newer, older, retire, retired | aka: supersedes, retires, ~replaced-by, ~superseded-by | shape: same
- owned-by: X is maintained or decided by person or team Y | walk: own, owns, owner*, owned, maintain*, responsible, team, teams | aka: maintained-by, managed-by, run-by, approved-by, decided-by, set-by, signed-off-by, agreed-by, ~owns, ~maintains | shape: * → party
- compared-with (proposed 2026-11-12): a link where one result is measured against a baseline or rival result on the same question; differs from evaluated-on (names the dataset) and replaces (names a newer version)
- shows (proposed 2026-11-12): X presents a result, figure or fact about Y to a reader, as a dashboard or note does; differs from measured-by (X is judged by metric Y) and produces (X writes Y), since shows only displays Y
drop: related-to, associated-with, about, mentions, relates-to, answers, answered-by, basis-for, evidence-for, led-to, leads-to, motivates, motivated-by, informs, follows, confirms, explains, supports, overturned-by, see
