# EDGES — relation types between entities, read "X <type> Y". Constrained open: the dreamer uses these types and
# their aliases (~ = read in reverse); any other link it finds keeps its own label and is shown as other/<label>.
# A label becomes a type only over the bar below, through the review, within the budget; a type marked
# (proposed <date>) is demoted back to a label if it is still under the bar after the probation. Edit freely: a
# hand-written line is permanent and relabels everything at the next merge (0 calls). Optional: pack: software, research, ops.
# Note-to-note links (from:, supersedes:, refs) are lineage, not relations.
promote: 5 uses, 5 notes, 2 areas
budget: 24
probation: 60 days
- uses: X needs Y as an input (model uses feature; feature uses table) | aka: depends-on, consumes, built-on, built-from, derived-from, based-on, sourced-from, requires, reads, reads-from, joined-to, ~feeds, ~input-to, ~used-by, ~used-for, ~used-in, from
- produces: X creates or writes Y (job produces table; model produces scores) | aka: writes, writes-to, creates, outputs, generates, ~generated-by, ~produced-by, ~output-of
- part-of: X is a component of Y (column part-of table; feature part-of feature-set) | aka: member-of, column-of, subset-of, stored-in, ~contains, ~has, ~includes
- trained-on: model X was fit on dataset Y | aka: fit-on, fitted-on, trained-with | shape: model → dataset
- evaluated-on: X was measured on dataset or segment Y | aka: tested-on, validated-on, measured-on, scored-on, backtested-on | shape: * → dataset
- measured-by: X is judged by metric Y | aka: reports, reports-metric, has-metric, measures, measured-in, scored-by, optimizes, optimises, targets, ~metric-of | shape: * → metric
- replaces: X is the newer version of Y | aka: supersedes, retires, ~replaced-by, ~superseded-by | shape: same
- owned-by: X is maintained or decided by person or team Y | aka: maintained-by, managed-by, run-by, approved-by, decided-by, set-by, signed-off-by, agreed-by, ~owns, ~maintains | shape: * → party
- beats (proposed 2026-11-02): X outperforms Y on the same metric in one evaluation; directional, unlike compared-with, which states no winner
- compared-with (proposed 2026-11-02): X is set side by side with Y on the same evaluation, with no winner stated; neutral, unlike beats
- compared-against (proposed 2026-11-02): X is set side by side with Y on the same evaluation, with no winner stated; neutral, unlike beats
- lifts (proposed 2026-11-02): X raises metric Y over a baseline when added or applied; a causal improvement, unlike measured-by, which only names the metric
- removed-from (proposed 2026-11-02): X is dropped from Y (a model, feature store or feature set); the negation of part-of, used when an item is taken out
- excluded-from (proposed 2026-11-02): X is held out of Y from the start (a model or training set); same meaning as removed-from
drop: related-to, associated-with, about, mentions, relates-to, answers, answered-by, basis-for, evidence-for, led-to, leads-to, motivates, motivated-by, informs, follows, confirms, explains, supports, overturned-by
