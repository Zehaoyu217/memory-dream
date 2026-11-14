#!/usr/bin/env python3
"""memory-dream v0.4: notes are the truth; answering is grep plus a thin layer of lineage and names.

  memory.py ask "q1" "q2" ... [-p P]     grep with memory: every question in one call
  memory.py dream [--cmd C] [-j N] [--review] [--all]   index entities and relations (optional), write the viewer
  memory.py viz [--out F]                 the HTML viewer: overview, explorer, health
  memory.py check                         warnings in full
  memory.py log "text" [-p P]             append to today's log
  memory.py export --to DIR               the graph as CSV + Cypher for a graph database
  MEMORY_STORE=postgres|neo4j             publish the graph to a hosted store after dream; ask reads it (stores.py, ADR-001)

Stdlib only. Every verb rescans first; only `dream` calls the model or writes derived files.
Contract: .specs/memory-dream/CONTRACT.md · runbook: .specs/memory-dream/RUNBOOK.md · origin: build-spec.md (v0.4 as first
specified; `where`, `trace`, `--gists` and INDEX.md from it were replaced by `ask`, lineage headers and the viewer).
"""
import argparse
import bisect
import contextlib
import datetime as dt
import functools
import hashlib
import html
import io
import json
import math
import os
import posixpath
import re
import shutil
import signal
import sqlite3
import subprocess
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

V = "0.4"
SCHEMA = 1  # the graph contract (.specs/memory-dream/CONTRACT.md): bumped when a field changes meaning
CODE = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:12]  # a changed script rebuilds the graph once, 0 calls
NOTE_MAX_LINES = 40  # SKILL.md's own rule; over it is C11
SKIP = {"INDEX.md", "EDGES.md", "ALIASES.md", "CONFLICTS.md", "KINDS.md", "TYPES.md", "TAGS.md", "SETUP.md", "README.md",
        "DIGEST.md", "ORIGIN.md"}
# An origin is a top folder with an ORIGIN.md in it: another base's notes, taken in as data (PLAN §9). They answer
# questions; they do not instruct, their entities are not the host's until a line in ALIASES.md says so, and their
# next folder level is the area. {folder: {"trust": words of its `trust:` line}}, read by load_domain().
ORIGINS = {}


def load_origins(root):
    out = {}
    try:
        names = sorted(os.listdir(root))
    except OSError:
        names = []
    for d in names:
        f = Path(root) / d / "ORIGIN.md"
        if not d.startswith(("_", ".")) and f.is_file():
            m = re.search(r"^trust\s*:\s*(.+)$", f.read_text(encoding="utf-8", errors="replace"), flags=re.M | re.I)
            out[d] = {"trust": {w for w in re.split(r"[,\s]+", m.group(1).lower()) if w} if m else set()}
    return out


def origin_of(p):
    """The origin a note belongs to; "" for the host's own notes."""
    s = p.split("/", 1)[0]
    return s if ORIGINS and "/" in p and s in ORIGINS else ""


def area_of(p):
    """A note's area: its first folder; under an origin, the origin and its next folder (`policy-kb/entities`)."""
    s = p.split("/")
    if ORIGINS and len(s) > 2 and s[0] in ORIGINS:
        return s[0] + "/" + s[1]
    return s[0] if len(s) > 1 else ""


def in_scope(p, scope):
    """Is this note inside one of these areas (lowercase)? An origin's name takes all of its areas."""
    return area_of(p).lower() in scope or (ORIGINS and origin_of(p).lower() in scope)
CC_KIND = {"user": "preference", "feedback": "rule", "project": "note", "reference": "note"}  # Claude Code's auto-memory types
DIGEST_MAX_LINES, DIGEST_HEADS = 40, 10  # memory/DIGEST.md: ≤ 40 lines so it can sit in context every session
# The domain — kinds of note (prefixes, areas, roles, the class tree), types of thing (with families) and the usual
# shapes of relations — lives in three files at the memory root, KINDS.md, TYPES.md and EDGES.md, seeded below and
# read by load_domain(); these module names are set from them: PREFIX_KIND, AREA_KIND, KINDS, KIND_PARENT, GENERAL,
# WORK, CONFLICT_KINDS, DIGEST_KINDS, ROLE_OF, KIND_ORDER, TYPE_PARENT, SHAPES. Nothing about data science is fixed
# in the code; the seeds cover data, software and finance, and a hand-written line in any of the files is permanent.


def family(k, tree=None):
    """A kind's or type's parent in the class tree, or itself."""
    return (KIND_PARENT if tree is None else tree).get(k, k)


def successors(notes, path, hops=4):
    """The chain after `path`'s first successor: v2 → v3 → … to the live end (phase H: 11% of the bank's history
    notes had a successor that was itself superseded, so the header sent the agent on a second hop)."""
    out, p, seen = [], path, {path}
    while len(out) < hops:
        nxt = (notes.get(p) or {}).get("superseded_by") or []
        if not nxt or nxt[0] in seen or nxt[0] not in notes:
            break
        p = nxt[0]
        seen.add(p)
        out.append(p)
    return out


def chain_mark(notes, n):
    """` · SUPERSEDED → v2 → v3`: every direct successor, then the first one's chain to the live end."""
    if not n["superseded_by"]:
        return ""
    return " · SUPERSEDED → " + ", ".join(notes[q]["id"] for q in n["superseded_by"] if q in notes) \
        + "".join(" → " + notes[q]["id"] for q in successors(notes, n["superseded_by"][0]))


def shape_checks(ents, rels, shapes=None, tparent=None):
    """C12 (phase H): a relation whose entity families are unusual for its type (the `shape:` of its EDGES.md line) —
    a `term` trained-on a `term` is probably a mistyped model and dataset; the review or a person retypes or drops it.
    Bank: 35 of 1,071 (3%)."""
    out, shapes, tparent = [], SHAPES if shapes is None else shapes, TYPE_PARENT if tparent is None else tparent
    for (s, T, o), rec in rels.items():
        exp = shapes.get(T)
        if not exp or s not in ents or o not in ents:
            continue
        fs, fo = family(ents[s]["type"], tparent), family(ents[o]["type"], tparent)
        es, eo = exp
        bad = (fs != fo) if es == "same" else ((es and fs != es) or (eo and fo != eo))
        if bad:
            out.append(("C12", f"{s} ({ents[s]['type']}) {T} {o} ({ents[o]['type']}): usually "
                        f"{'the same family on both sides' if es == 'same' else (es or '*') + ' → ' + eo}; retype or drop · "
                        f"{(rec.get('evidence') or ['?'])[0]}"))
    return out
TIMEOUT = int(os.environ.get("MEMORY_TIMEOUT", "300"))
KEEP_DAYS = 30
# Constrained open vocabulary (REVIEW.md §10): a link outside EDGES.md keeps its label (other/<label>); a label may
# become a type only over this bar, through the review, within the budget; a proposed type is demoted after the probation.
PROMOTE, BUDGET, PROBATION_DAYS = (5, 5, 2), 24, 60  # uses, notes, areas · types · days — EDGES.md can override
# Conflicts (REVIEW.md phase C): two live notes of one kind in one area, unlinked, sharing a rare title word, are
# queued for the review; decisions persist in memory/CONFLICTS.md; notes are never edited.
# Conflict kinds come from KINDS.md (`conflicts: yes`; a child kind counts as its family — phase H). Rules and
# preferences are distinct by nature: not queued (bank: 157 false pairs)
CONFLICT_MAX = 20  # pairs per review
CONFLICT_STOP = set("decision model finding current holdout threshold rule note with from that this using when what".split())
CONFLICTS_HEAD = ("# CONFLICTS — decisions about pairs of live notes that looked contradictory. `- a > b`: a supersedes b "
                  "(lineage from then on; the notes are untouched). `compatible: a / b`: both stand. `- a ? b`: the reviewer "
                  "was unsure; a person decides. Edit freely.\n")
WIDE = int(os.environ.get("MEMORY_WIDE", "10000"))  # above this many notes, ask greps only where a question points

EDGES_SEED = """# EDGES — relation types between entities, read "X <type> Y". Constrained open: the dreamer uses these types and
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
- uses: X needs Y as an input (model uses feature; feature uses table) | walk: use, uses, using, used by, depend*, input, inputs, feed, feeds, read, reads, built on, built from, based on, source, sources, feature, features, ~(what/which/who) (use/uses/depend/depends/read/reads/consume/consumes/feed/feeds/relies), ~used by, ~downstream, ~dependent, ~dependents | hops: 2 | aka: depends-on, consumes, built-on, built-from, derived-from, based-on, sourced-from, requires, reads, reads-from, joined-to, ~feeds, ~input-to, ~used-by, ~used-for, ~used-in
- produces: X creates or writes Y (job produces table; model produces scores) | walk: produce, produces, output, outputs, write, writes, generat* | aka: writes, writes-to, creates, outputs, generates, ~generated-by, ~produced-by, ~output-of
- part-of: X is a component of Y (column part-of table; feature part-of feature-set) | walk: part of, component, components, member, members, column, columns, contain, contains | hops: 2 | aka: member-of, column-of, subset-of, stored-in, ~contains, ~has, ~includes
- trained-on: model X was fit on dataset Y | walk: train*, fit on, fitted on | hops: 2 | aka: fit-on, fitted-on, trained-with | shape: model → dataset
- evaluated-on: X was measured on dataset or segment Y | walk: evaluat*, tested on, validat*, holdout, holdouts, backtest*, scored on | aka: tested-on, validated-on, measured-on, scored-on, backtested-on | shape: * → dataset
- measured-by: X is judged by metric Y | walk: metric, metrics, measured by, auc, recall, precision, mape, f1, score, scores, scored | aka: reports, reports-metric, has-metric, measures, measured-in, scored-by, optimizes, optimises, targets, ~metric-of | shape: * → metric
- replaces: X is the newer version of Y | walk: replac*, supersed*, version, versions, predecessor, successor, newer, older, retire, retired | aka: supersedes, retires, ~replaced-by, ~superseded-by | shape: same
- owned-by: X is maintained or decided by person or team Y | walk: own, owns, owner*, owned, maintain*, responsible, team, teams | aka: maintained-by, managed-by, run-by, approved-by, decided-by, set-by, signed-off-by, agreed-by, ~owns, ~maintains | shape: * → party
drop: related-to, associated-with, about, mentions, relates-to, answers, answered-by, basis-for, evidence-for, led-to, leads-to, motivates, motivated-by, informs, follows, confirms, explains, supports, overturned-by
"""
PACKS = {  # seed vocabularies for other domains: `pack: software` in EDGES.md adds these lines (they count in the budget)
    "software": """- calls: X invokes Y (service calls API; function calls function) | aka: invokes, requests, queries, ~called-by, ~serves
- implements: X realises Y (module implements interface; service implements spec) | aka: realises, realizes, satisfies, ~implemented-by, ~specified-by
- deployed-to: X runs in Y (service deployed-to cluster) | aka: runs-on, runs-in, hosted-on, ~hosts
- configures: X sets Y's behaviour (flag configures service; file configures job) | aka: sets, parameterises, parameterizes, ~configured-by
- tested-by: X is checked by Y (module tested-by suite) | aka: covered-by, verified-by, ~tests, ~covers, ~verifies
- blocked-by: X waits on Y (release blocked-by bug) | aka: waits-on, ~blocks""",
    "research": """- cites: X refers to Y as a source (paper cites paper; note cites report) | aka: references, quotes, ~cited-by
- extends: X builds on Y's method or result (model extends baseline) | aka: generalises, generalizes, refines, ~extended-by
- contradicts: X's result disagrees with Y's | aka: disagrees-with, refutes, ~contradicted-by
- reproduces: X repeats Y's result | aka: replicates, ~reproduced-by""",
    "ops": """- alerts-on: X raises an alert on Y (monitor alerts-on metric) | aka: monitors, watches, pages-on, ~monitored-by
- runs-after: X is scheduled after Y (job runs-after job) | aka: scheduled-after, ~runs-before, ~precedes
- escalates-to: X hands off to Y (queue escalates-to team) | aka: hands-off-to, ~escalated-from
- rolled-back-to: X reverted to Y (release rolled-back-to version) | aka: reverted-to, ~rolled-back-from""",
}
ALIASES_HEAD = ("# ALIASES — entity ids that name the same thing; the first id on a line is canonical. "
                "Edit freely.\n")

KINDS_SEED = """# KINDS — kinds of note. A note's kind is its frontmatter `type:`, else the kind of its area (`prefs/` → preference), else
# the kind whose prefix starts its filename (`exp-014` → experiment; `…-vN` is a model), else note. One line per
# kind: `- kind: definition | prefix: a, b | area: x, y | family: parent | role: R | digest: current | conflicts: yes
# | answers: yes | replaces: kinds | not: what it is not`. role ∈ question, evidence, state, rule, reference, log; project
# work is question, evidence and state. `answers: yes` kinds answer a question they are built on; `digest: current` kinds
# head the digest; `conflicts: yes` kinds are compared for disagreement (a child kind counts as its family). A note that
# a keeper reads as replacing another replaces one of its own family, or of a kind (or family) named after `replaces:`.
# `general:` names the areas that span projects. Constrained open, like EDGES.md: a keeper gives one of these kinds or
# an alias (`aka:`); a note that is none of them counts as note and keeps the keeper's word, and once the word is over
# the bar (`promote:`, by default 5 uses, 5 notes, 2 areas; `budget: 40`) the review may make it a kind, marked
# (proposed <date>), which takes its family's role. Edit freely: a hand-written line is permanent (0 model calls);
# `pack: research, ops` adds a domain's kinds.
# The seed covers data, analytics, software and finance work.
general: prefs, reporting, glossary, corrections, howto, qa, people, log
- question: something asked and not yet settled | prefix: q | role: question
- experiment: a run with a method and a measured result | prefix: exp | family: finding | role: evidence
- finding: a result or observation that holds until superseded | prefix: fnd, find, finding | role: evidence | conflicts: yes | answers: yes | not: a single run (experiment)
- incident: a failure, outage, loss or error, and what was learned | prefix: inc | family: finding | role: evidence
- decision: a choice made, with its reason | prefix: dec | role: state | digest: current | conflicts: yes | answers: yes
- plan: an intended course of action, with steps or dates | prefix: plan | role: state | digest: current
- requirement: a stated need or acceptance condition | prefix: req | role: state
- risk: a known exposure, its size and its owner | prefix: risk | role: state
- dataset: a table, file, feed or extract, and what it holds | prefix: ds | role: state
- feature: an input variable or feature set, and how it is built | prefix: feat | role: state
- model: a trained or rule-based model, scorecard or forecast, one version per note | prefix: model | role: state | digest: current | conflicts: yes
- metric: how something is measured | prefix: metric | family: term | role: state
- report: a recurring report, dashboard or deliverable, and its rules | prefix: rpt, report | role: reference
- component: a service, module, library or system and what it does, one per note | prefix: svc, mod, lib, sys | role: state
- design: an architecture or design decision, with the options weighed | prefix: adr, design | family: decision | role: state | digest: current | conflicts: yes | answers: yes
- bug: a defect observed, its cause and its fix | prefix: bug, fix | family: finding | role: evidence
- release: a shipped version or deployment, when and what changed | prefix: rel, release | role: state
- term: a defined word or concept | prefix: term | area: glossary | role: reference
- preference: how a named person wants things done | prefix: pref | area: prefs | family: rule | role: rule
- rule: a standing rule or procedure for the work | prefix: rule | area: reporting, howto | role: rule
- correction: a past mistake and the rule that prevents it | area: corrections | family: rule | role: rule | replaces: term
- log: a dated scratch line | area: log | role: log
- note: anything else | role: reference
"""
KIND_PACKS = {
    "research": """- hypothesis: a claim to test, and how | prefix: hyp | role: question
- paper: a paper or report read, and what it claims | prefix: paper | role: reference""",
    "ops": """- runbook: a procedure to run, check or fix something | prefix: rb | area: runbooks | role: rule
- change: a change made to a system, when and by whom | prefix: chg | role: state""",
}
TYPES_SEED = """# TYPES — kinds of thing the notes name, read "X is a <type>". Constrained open, like EDGES.md: the dreamer types each
# thing with one of these or an alias; a thing of any other type keeps the dreamer's word, shown as other/<word>; a word
# becomes a type only over the bar, through the review, within the budget; a (proposed <date>) type still under the bar
# after the probation goes back to a word. `family:` groups types for the viewer and the shape check (C12); `drop:`
# names words that are never things (grep finds files and numbers), `drop-names:` names that are never things whatever
# their type (`*` stands for anything; a base about code deletes what it wants kept). Edit freely: a hand-written line
# is permanent (0 model calls); `pack: research, ops` adds a domain's types. The seed covers data, analytics, software
# and finance.
promote: 5 uses, 5 notes, 2 areas
budget: 40
probation: 60 days
- person: a named individual | aka: people, user, analyst, engineer, manager, owner | family: party | not: a team or a company
- team: a named team or group of people | aka: group, squad, crew | family: party
- organisation: a company, client, vendor, regulator or other body | aka: organization, company, vendor, client, regulator, firm | family: party
- term: a defined word, concept or method | aka: concept, method, definition, technique | not: a measured quantity (metric)
- metric: a measured quantity used to judge something | aka: kpi, measure, statistic, score | not: a single value or threshold
- tool: software or a platform used to do the work | aka: library, platform, framework, package, software | family: system | not: a service the team runs (service)
- document: a report, deck, specification, policy document or paper named as a thing | aka: report, deck, spec, paper, memo, template
- dataset: a table, file, feed or extract of records | aka: table, data set, feed, extract, view, source | not: one column of it (feature), one subset of it (segment)
- segment: a defined subset of records, customers or accounts | aka: cohort, population, subset | family: dataset
- feature: an input variable or set of variables | aka: column, variable, field, feature set, attribute | not: the table it comes from (dataset)
- model: a trained or rule-based model, scorecard, forecast or one version of it | aka: scorecard, classifier, forecast model, algorithm
- pipeline: a job, pipeline or scheduled process that moves or transforms data | aka: job, dag, workflow, etl, process | family: system
- dashboard: a dashboard or report page people read regularly | aka: report page, bi report | family: document
- service: a running service, API or application | aka: api, app, application, endpoint, system | family: system
- module: a code module, package, repository or component | aka: repo, repository, component, class, function, script | family: system
- environment: a cluster, host, environment or deployment target | aka: cluster, host, prod, staging, region | family: system
- release: a named version or release of software | aka: version, build, tag | family: system
- instrument: a security, loan, contract or product that is traded, held or sold | aka: security, bond, loan, product, contract, derivative
- portfolio: a portfolio, book, fund or set of holdings | aka: book, fund, holdings
- account: a customer, ledger or trading account | aka: ledger, wallet
- counterparty: a client, issuer, borrower or counterparty in a transaction | aka: issuer, borrower, lender, obligor | family: party
- policy: a policy, limit, regulation or control that constrains the work | aka: regulation, limit, control, standard, mandate | family: rule
- scenario: a stress, forecast or planning scenario | aka: stress test, case, what-if
- desk: a trading desk, business unit or department | aka: business unit, department, division, unit | family: party
- flag: a feature flag, configuration setting or option | aka: feature flag, setting, config, option | family: system
- test: a test suite, test case or benchmark named as a thing | aka: suite, test case, benchmark | family: system
- issue: a ticket, issue or pull request named as a thing | aka: ticket, pr, pull request, bug report, merge request | family: document
drop: number, date, file, notebook, note, line, page, link
drop-names: *.py, *.sql, *.ipynb, *.csv, *.parquet, *.json, *.md, *notebook*, nb-*, *-script
"""
TYPE_PACKS = {
    "research": """- paper: a paper or published result | aka: article, preprint | family: document
- method: a named method or algorithm | aka: approach, procedure | family: term""",
    "ops": """- monitor: a monitor, alert rule or check that watches a system | aka: alert, probe, healthcheck | family: system
- queue: a queue, topic or channel that carries work | aka: topic, channel, stream | family: system""",
}


def parse_kinds(text):
    """KINDS.md -> {order, kinds: {kind: {def, aka, prefix, area, family, role, digest, conflicts, answers, replaces}},
    general, drop, bad}. The vocabulary grammar every vocabulary file shares (aka, family, the settings, `drop:`,
    `keep:`, a line marked (proposed <date>)); a kind given a family and no role takes its family's."""
    out = {"order": [], "kinds": {}, "general": set(), "drop": set(), "bad": []}
    roled = set()
    for i, ln in enumerate(expand_packs(text, KIND_PACKS).split("\n"), 1):
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        g = re.match(r"general\s*:(.*)$", s, re.I)
        dr = re.match(r"drop\s*:(.*)$", s, re.I)
        m = re.match(r"-\s*([^:|]+?)\s*:\s*(.*)$", s)
        if g:
            out["general"] |= {a.strip().lower() for a in g.group(1).split(",") if a.strip()}
        elif dr:
            out["drop"] |= {fold(x) for x in dr.group(1).split(",") if x.strip()}
        elif re.match(r"(pack|promote|budget|probation|keep)\s*:", s, re.I):
            continue
        elif m:
            k = fold(PROPOSED_RX.sub("", m.group(1)))
            segs = [x.strip() for x in m.group(2).split("|")]
            d = {"def": segs[0], "aka": [], "prefix": [], "area": [], "family": k, "role": "reference", "digest": False, "conflicts": False,
                 "answers": False, "replaces": [], "not": ""}
            for seg in segs[1:]:
                key, _, val = seg.partition(":")
                key, val = key.strip().lower(), val.strip()
                if key in ("prefix", "area", "replaces", "aka"):
                    d[key] = [fold(x) for x in val.split(",") if x.strip()]
                elif key == "family":
                    d["family"] = fold(val)
                elif key == "role":
                    d["role"] = fold(val)
                    roled.add(k)
                elif key == "digest":
                    d["digest"] = val.lower() in ("current", "yes", "true")
                elif key == "conflicts":
                    d["conflicts"] = val.lower() in ("yes", "true")
                elif key == "answers":
                    d["answers"] = val.lower() in ("yes", "true")
                elif key == "not":
                    d["not"] = val
            out["kinds"][k] = d
            out["order"].append(k)
        else:
            out["bad"].append((i, s))
    for k, d in out["kinds"].items():                    # a kind the review added: its family's role
        if k not in roled and d["family"] != k and d["family"] in out["kinds"]:
            d["role"] = out["kinds"][d["family"]]["role"]
    return out


def domain_texts(root):
    k, t = root / "KINDS.md", root / "TYPES.md"
    return (read(k) if k.exists() else KINDS_SEED), (read(t) if t.exists() else TYPES_SEED)


def name_drop(tt):
    """The `drop-names:` line of TYPES.md as one pattern: names that are never things whatever a keeper typed them
    (files and notebooks: grep finds them). A registry without the line takes the seed's, so a base made before the
    line existed keeps its things; a line with nothing after the colon keeps every name, for a base about code."""
    rx = r"^[ \t]*drop-names[ \t]*:(.*)$"
    m = re.search(rx, tt, re.M | re.I) or re.search(rx, TYPES_SEED, re.M | re.I)
    pats = [x.strip().lower() for x in m.group(1).split(",") if x.strip()]
    return re.compile("|".join("(?:" + re.escape(x).replace(r"\*", ".*") + ")" for x in pats)) if pats else None


def walk_rx(words):
    """Question words of a `walk:` field as one pattern: whole words, any case, runs of spaces alike; `*` stands for
    any letters and `(a/b)` for either (a `|` separates the fields of a registry line)."""
    alts = [re.escape(" ".join(w.split())).replace(r"\*", r"\w*").replace(r"\(", "(?:").replace(r"\)", ")").replace("/", "|")
            .replace(r"\ ", r"\s+") for w in words]
    return re.compile(r"\b(?:" + "|".join(alts) + r")\b", re.I) if alts else None


def walk_tables(etypes):
    """What `ask` walks, from the type lines of EDGES.md: RELCUE {type: the question words that point at it}, INWARD
    (the words that ask for a link read the other way) and INPUT_TYPES (the types whose links chain: `hops: 2`). A
    line without `walk:` or `hops:` takes the seed's line of the same type, so a registry written before the fields
    existed answers as it did."""
    cue, inward, chain = {}, [], set()
    for t, d in etypes.items():
        seed = SEED_EDGE_TYPES.get(t, {})
        walk = d.get("walk") if d.get("walk") is not None else seed.get("walk") or []
        hops = d.get("hops") if d.get("hops") is not None else seed.get("hops") or 1
        rx = walk_rx([w for w in walk if not w.startswith("~")])
        if rx:
            cue[t] = rx
        inward += [w[1:] for w in walk if w.startswith("~")]
        if hops >= 2:
            chain.add(t)
    return {"RELCUE": cue, "INWARD": walk_rx(inward) or re.compile(r"(?!)"), "INPUT_TYPES": chain}


def domain_from(kt, tt, et):
    """The module's domain tables from the three files' texts."""
    kc, tv, ev = parse_kinds(kt), parse_edges(tt, TYPE_PACKS), parse_edges(et)
    ks = kc["kinds"]
    return {"PREFIX_KIND": {p: k for k, d in ks.items() for p in d["prefix"]},
            "AREA_KIND": {a: k for k, d in ks.items() for a in d["area"]},
            "KINDS": set(ks), "KIND_ORDER": kc["order"],
            "KIND_ALIAS": {a: k for k, d in ks.items() for a in d.get("aka", [])}, "KIND_DROP": kc["drop"],
            "KIND_PARENT": {k: d["family"] for k, d in ks.items() if d["family"] != k},
            "GENERAL": kc["general"],
            "WORK": {k for k, d in ks.items() if d["role"] in ("question", "evidence", "state")},
            "CONFLICT_KINDS": {k for k, d in ks.items() if d["conflicts"]},
            "DIGEST_KINDS": {k for k, d in ks.items() if d["digest"]},
            "ANSWER_KINDS": {k for k, d in ks.items() if d["answers"]},
            "ROLE_OF": {k: d["role"] for k, d in ks.items()},
            "KIND_REPLACES": {k: set(d["replaces"]) for k, d in ks.items() if d["replaces"]},
            "TYPE_PARENT": tv[5]["family"], "SHAPES": {**SEED_SHAPES, **ev[5]["shape"]}, "NAME_DROP": name_drop(tt),
            **walk_tables(ev[0])}


def load_domain(root):
    """Read KINDS.md, TYPES.md and EDGES.md of this memory (seeds when absent) into the module's domain tables, and
    which of its top folders are origins."""
    globals().update(domain_from(*domain_texts(root), vocab_texts(root)[0]))
    globals()["ORIGINS"] = load_origins(root)


EXTRACT = """Index this memory note for retrieval. Reply with JSON only:
{"kind": "one of KINDS",
 "entities": [{"id": "...", "type": "a TYPES type or alias, or other", "label": "the note's own word for what it is, 1-2 words",
               "as": ["text copied verbatim from the note"]}],
 "relations": [{"s": "entity id", "type": "an EDGES type or alias, or other", "label": "the note's own verb, 1-3 words",
                "o": "entity id", "quote": "short text copied verbatim from the note that states it"}],
 "refs": ["ids or paths of other notes the text explicitly points to"],
 "built_on": [{"what": "its id", "quote": "words copied verbatim from the note that say so"}],
 "replaces": [{"what": "its id", "quote": "words copied verbatim from the note that say so"}]{tags_key}}
Entities are things someone would look up across notes; TYPES says which. Not numbers, dates, files,
notebooks or note ids (those go in refs). Type each with a TYPES type or one of its aliases; if none fits
a real thing, type is other and the label says what it is (a word that becomes common is offered as a type).
If an entity is in KNOWN, reuse its id. Otherwise id = its most specific name, lowercase, spaces to
hyphens; a table keeps its dots (cards.txn_daily).
Relations: only ones the note states, read "s <type> o". Use an EDGES type or one of its aliases
(aliases marked ~ read in reverse) and always give the label. If no type fits a real link between two
things, type is other: the label is kept and shown, and becomes a type once it is common.
built_on and replaces are about this note itself, the document. built_on: one item for each note or thing it says it
builds on, starts from, takes as an input or a basis, or follows from; a sentence that names three ("Builds on A, B
and the C dataset") gives three items with the same quote. replaces: only what this note, or the thing it is named
after, itself replaces or retires ("Replaces X."); that one thing replaced another ("v3 replaces v2", in a note that
is neither) is a relation and not this, and what replaced this note ("Superseded by X", "Replaced by X") is the
opposite of it: leave that out. `what` is the file name of the note meant, without .md, whenever FOLDER
lists it, however the text words it ("the dispositions dataset" is the note about that dataset); else its id in
KNOWN, or the id you gave it under entities; and when none of these names it, the words the note uses for it. An
item is never left out because the note it means cannot be named: a later reading places it.
{tags_rule}A note no kind fits: other: <word>.
KINDS: {kinds}
TYPES:
{types}
EDGES:
{edges}
{tags}KNOWN:
{known}
FOLDER (the notes of this folder, file name: first line):
{folder}
NOTE {path}:
{text}
"""
REVIEW = """You keep the vocabulary of a memory of work notes.
RELATION TYPES, read "X <type> Y" ({n} of {budget} slots used):
{edges}
LABELS the indexer used that fit no type, each over the bar of {u} uses in {nn} notes across {a} areas
(uses, notes, areas and which; up to 3 examples "X — Y: quote"):
{proposals}
ENTITY PAIRS that may name the same thing (each side: id, type, how the notes write it, what its own note says it is,
what it is linked to, a line that mentions it; then what the two are both linked to):
{pairs}
LIVE NOTES of one kind in one area that may disagree (path · "title" «first line»; neither supersedes the other):
{conflicts}
THING TYPES, read "X is a <type>" ({tn} of {tbudget} slots used):
{types}
TYPE WORDS the indexer used for things that fit no type, each over the bar (uses, notes, areas and which; up to 3 examples "id: as written"):
{etypes}
NOTE KINDS, what a note is ({kn} of {kbudget} slots used):
{kinds}
KIND WORDS the indexer gave notes that fit no kind, each over the bar (uses, notes, areas and which; up to 3 example notes):
{kwords}
TAGS, themes that notes share ({gn} of {gbudget} slots used):
{tags}
TAG WORDS that notes or their indexer used and no tag covers, each over the bar (uses, notes, areas and which; up to 3
example notes):
{gwords}
Reply with JSON only:
{"types": {"<label>": "alias T" | "alias ~T" | "new: <one line: what the link means and how it differs from the closest type>" | "label" | "drop"},
 "entities": {"<a> / <b>": "same" | "different"},
 "conflicts": {"<a> / <b>": "<a> supersedes <b>" | "<b> supersedes <a>" | "compatible" | "unsure"},
 "etypes": {"<word>": "alias T" | "new: <one line: what the thing is and how it differs from the closest type> | family: <a listed family or the word itself>" | "label" | "drop"},
 "kinds": {"<word>": "alias K" | "new: <one line: what such a note is and how it differs from the closest kind> | family: <a listed kind or the word itself>" | "label" | "drop"},
 "tags": {"<word>": "alias T" | "new: <one line: the theme, and how it differs from the closest tag> | family: <a listed tag or the word itself>" | "label" | "drop"}}
Every word, in every list, by the same rule: decide by what it means and how the examples use it, never by how it is spelled.
Map a label onto T when it names the same link as T, as a synonym ("alias T") or read in reverse
("alias ~T"). Answer "new: …" only for a link between two things that no listed type expresses and that
the notes will keep using; name the closest type and the difference. Answer "label" to keep it as a plain
label. Drop only what links notes rather than things (answers, led-to, basis-for) or is a conversation
(asked-by, raised-by). When unsure between alias and new, alias; when unsure between new and drop, label.
A type word: "alias T" when it is a kind of T; "new: …" only for a kind of thing people will keep looking up
across notes; "label" to keep the word; "drop" for what is not a thing (a number, a file, a date).
A kind word: "alias K" when such notes are K notes; "new: …" only for a kind of note people will keep writing;
"label" to keep the word; "drop" for what is not a kind of note (a topic, a status).
A tag word: "alias T" when it names the theme T names; "new: …" only for a theme that notes across the memory share
and that their folders, kinds and things do not already say; "label" to keep the word; "drop" for what is not a
theme (a status, a date, a person) or what the areas it is used in are about (a word for the subject of the one
folder it is used in says what the folder says).
Two entities are the same only when the evidence agrees: the same kind of thing, described alike, linked to the same
things by the same relations; a shared word in their names is not evidence. If unsure, answer different. Versions (v2,
v3) are different.
Two notes: the newer one supersedes the older when it decides or states the same thing differently (a new
threshold, a newer version as the current one); they are compatible when they are about different things or
one builds on the other; otherwise unsure. Never invent paths: copy them from the pair.
"""

# The curator (PLAN §7): identity by reading. It sees every thing a folder's notes name, each with how it is written
# and a line that mentions it, and says which are one thing under two names. Nothing here compares strings.
CURATE = """You keep the names of things in a memory of work notes. Below are the things that the notes of one folder name,
one per line: its id, what kind of thing it is, how the notes write it, in how many notes, what its own note says it is
(is:, when it has one), what the notes link it to (links:, → from it, ← to it), and one line that mentions it.
Some may be one thing written two ways: a short name and a full one, a plural, an abbreviation, a nickname. Find those
by the evidence, not by the names: one thing under two names is the same kind of thing, is described alike, and is
linked to the same things by the same relations. Two things whose links name each other are two things.
Not the same thing: two versions (v2 and v3), two periods or samples (2025 and 2026, h1 and h2), a thing and a part of
it, siblings that only share a pattern of name, a thing and a note or a person that describes it. When unsure, leave it out.
Reply with JSON only: {"same": [{"ids": ["<id>", "<id>"], "why": "<one short sentence: the words above that show it>"}]}
An empty list is a good answer.
FOLDER {area}:
{cards}
"""
CURATE_MAX = 60  # folders a dream has read by the curator; the rest wait for the next one
# The second reading (RESULTS phase S). The first reading finds the lines of a note that say what it builds on or
# replaces, and reads them among everything else it has to do: of the things such a line names by a phrase ("Builds on
# exp-303, the isotonic score map and the psi finding") it left one in ten out and said nothing, which was two thirds
# of the lineage the memory lacked on the worn bank. So each such line is read once more, by folder, with the folder's
# notes beside it and one thing asked: every member of the line, each with its own words and the note it means. That
# reading holds 99.2% of the bank's built-on links where the first held 96.3%, and its answer takes the first one's
# place on the lines it read.
PLACE = """Notes of a work memory say in their own words what they build on and what they replace. Below are such lines, copied
from notes of one folder. For each line, list every thing it says its note builds on (or, where that is what is
asked, replaces): each member of a list is one entry, in the order the line names them, none left out.
For each entry give the words the line uses for it, copied, and the note of the folder that is meant: its file name
without .md, however the line words it ("the dispositions dataset" is the note about that dataset, "the question of
which margin to target" is the note that asks it, "the first router run" is the note of that model). null when no
note of the folder is meant, or when two could be. A note of another folder, which a line names with its folder
(folder/name), is given as folder/name.
The note a line stands in is never an entry of its own line. Where replaces is asked: only what the note itself, or
the thing it is named after, replaces or retires; a line that says the note was replaced by something has no entry.
FOLDER {area} (file name: first line):
{folder}
LINES (number · the note it stands in · asked · the line):
{items}
Reply with JSON only, one key per line: {"1": [{"words": "<copied from the line>", "note": "<file name>"}, {"words": "...", "note": null}], "2": []}
"""
PLACE_LINES, PLACE_TEXT, PLACE_MAX = 45, 500, 400  # lines a call · characters of a line · calls a dream, the rest wait
# The third reading (RESULTS S8). Words two readings could not place ("the bg/nbd versus gbm accuracy test", whose note
# was on the second reading's list beside a look-alike): each is put once more with the few notes of its folder whose
# name and first lines share its rarest words, shown with those lines, and the keeper says which is meant or that none
# is. The script chooses what is shown; the keeper decides.
CHOOSE = """A note of a work memory says, in a line of its own, that it builds on or replaces something, and names it in a few
words. Two readings could not tell which note is meant. Under each item are the notes it could be, each with its
first lines. For each item, say which of those notes the words mean. null when none of them is meant, or when their
lines do not tell you.
ITEMS:
{items}
Reply with JSON only, one key per item: {"1": "<file name of one of its notes>", "2": null}
"""
CHOOSE_ITEMS, CHOOSE_SHOWN, CHOOSE_MAX = 8, 6, 60  # items a call · notes shown an item · calls a dream
# A folder with more notes than a prompt can list (the flat bank of RESULTS phase S: 1,224 in one). The keeper is then
# shown the notes near the lines it reads: those within four steps of a line's note by a name written in a note,
# either way, and beside them the eight notes whose first line and name share the rarest words with the line.
# Measured with no model on that bank: the note a phrase means is among them for 99.5% of 750 phrases, 33 notes at
# the median, where the steps alone hold 95.5% and the words alone under 90%. The two are shown apart and the keeper
# is told which is which: shown as one list, a look-alike from another project ("the logistic regression baseline"
# has one in every project) made it answer that two notes could be meant, for 30 phrases whose note was near. The
# script chooses what is shown and says how near it is; the keeper still decides.
FOLDER_SHOWN, NEAR_SHOWN, NEAR_STEPS, NEAR_WORDS = 200, 120, 4, 8
PLACE_NEAR = PLACE.replace("""FOLDER {area} (file name: first line):
{folder}
""", """FOLDER {area} has {count} notes, too many to list. NEAR are the notes that the notes of these lines name, or that
name them, within a few steps (file name: first line). A phrase nearly always means one of them:
{folder}
ELSEWHERE in the folder, notes whose first line shares rare words with a line. One of these is meant only when
nothing NEAR fits. When a NEAR note and one of these both fit, that is not "two could be": the NEAR one is meant.
{also}
""")
assert PLACE_NEAR != PLACE

# A packet (PLAN §4): the same reading asked for many notes in one call. The rules are EXTRACT's own, cut from it, so
# the two prompts cannot drift apart; a note is named by the first twelve characters of the hash of its text.
PACKET = """Index each memory note below for retrieval. Reply with one line of JSON per note, in the order given, and nothing else:
{"note": "the 12-character id on its NOTE line", "kind": "one of KINDS", "entities": [{"id": "...", "type": "a TYPES type or alias, or other", "label": "the note's own word for what it is, 1-2 words", "as": ["text copied verbatim from the note"]}], "relations": [{"s": "entity id", "type": "an EDGES type or alias, or other", "label": "the note's own verb, 1-3 words", "o": "entity id", "quote": "short text copied verbatim from the note that states it"}], "refs": ["ids or paths of other notes the text explicitly points to"], "built_on": [{"what": "its id", "quote": "words copied verbatim from the note that say so"}], "replaces": [{"what": "its id", "quote": "words copied verbatim from the note that say so"}]{tags_key}}
Read each note alone: its entities, its relations and every copied text come from that note's own lines, even when
another note here says more. Skip no note: one with nothing to index gets its line with empty lists. Index each note
as fully as if it were the only one: every dataset, table, feature, model, metric, experiment, decision and person
it names, and every use, evaluation, measurement, replacement and ownership it states.
One thing has one id in all your lines. When a note speaks of something that a note listed in FOLDER is about (by a
phrase, a short name, "the v2 model"), give it the id that note's file name gives it.
""" + EXTRACT[EXTRACT.index("Entities are things"):EXTRACT.index("NOTE {path}:")]


# ---------- small helpers ----------

@functools.lru_cache(maxsize=1 << 20)
def _fold(s):
    return re.sub(r"[\s_.-]+", "-", s.strip().lower())


def fold(s):
    """Identity key: case, spaces, `_`, `.` and `-` don't distinguish (cards.txn_daily = cards-txn-daily)."""
    return _fold(s if isinstance(s, str) else str(s))


def versions(a, b):
    """Ids that differ only in digits name different versions; never merged by rule or review."""
    return a != b and re.sub(r"\d+", "", a) == re.sub(r"\d+", "", b)


def qpat(q):
    """Verbatim match, case-insensitive, whitespace runs collapsed, backticks/asterisks ignored."""
    toks = [t.strip("`*") for t in str(q).split()]
    toks = [t for t in toks if t]
    return re.compile(r"[\s`*]+".join(map(re.escape, toks)), re.I) if toks else None


def line_at(text, i):
    return text.count("\n", 0, i) + 1


def fill(tpl, **kw):
    return re.sub(r"\{(\w+)\}", lambda m: str(kw[m.group(1)]) if m.group(1) in kw else m.group(0), tpl)


def parse_json(out):
    if not out:
        return None
    i, j = out.find("{"), out.rfind("}")
    if i < 0 or j <= i:
        return None
    try:
        obj = json.loads(out[i:j + 1])
    except ValueError:
        return None
    return obj if isinstance(obj, dict) else None


def read(p):
    return p.read_text(encoding="utf-8", errors="replace")


def rd(p, default=None):
    try:
        return json.loads(read(p))
    except (OSError, ValueError):
        return default


def wr(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_text(obj if isinstance(obj, str) else json.dumps(obj, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    tmp.replace(p)


def mmdd(d):
    return d[5:10] if d else "--"


def read_kind(x):
    """The kind a keeper read, through KINDS.md as it stands now: a word it gave that fitted no kind then counts as the
    kind a later alias or a new kind makes of it, with no new reading (the vocabulary resolves, the reading stays)."""
    if not x:
        return None
    k, w = x.get("kind"), fold(x.get("kind_word") or "")
    if k in (None, "", "note") and w:
        return w if w in KINDS else KIND_ALIAS.get(w, k)
    return k


def kind_of(rel, fm_type=None, x_kind=None):
    """A note's kind: frontmatter `type:` (Claude Code's user/feedback/project/reference map onto ours), else the
    kind of its area when the area has one (under an origin, by the area's last part), else a kind prefix in the
    first or second part of the filename (exp-, feat-, ds-, dec-, fnd-, q-, …), else model for `…-vN` (and `…-v10a`, a
    version with a letter), else the dreamer's reading, else note."""
    t = (fm_type or "").strip().lower()
    if t:
        return CC_KIND.get(t, t)
    stem_ = posixpath.basename(rel)[:-3].lower()
    area = area_of(rel).split("/")[-1].lower()  # under an origin, the kind of an area goes by its last part
    segs = stem_.split("-")
    # the name and the folder the writer chose come before the dreamer's reading (phase L: on the bank the reading had
    # relabelled 163 of the 886 notes named ds-, dec-, feat-, exp- or q-, and 61 of the 135 named …-vN; a dataset shown
    # as a "finding" cost an agent a right answer, and "every model" listed by kind found 8 of 15 lines)
    if area in AREA_KIND:  # a folder that has a kind says more than a first word: howto/model-card-fields is a rule
        return AREA_KIND[area]
    for pre in segs[:2]:  # exp-014, and project-prefixed ids such as aml-find-kyc-lift or mrisk-find-watchlist
        if len(segs) > 1 and pre in PREFIX_KIND:
            return PREFIX_KIND[pre]
    if re.search(r"-v\d+[a-z]?$", stem_):  # bsm-app-gbm-v10a was read as an experiment, and its successor's replacing it refused
        return "model"
    if x_kind and str(x_kind).lower() != "note":  # no name and no folder says what it is: the dreamer's reading does
        return str(x_kind).lower()
    return "note"


def general_areas(by_area, kind):
    """Areas that span projects (prefs, reporting, …): named, or mostly not project work by kind — judged on the notes
    that have a kind, since without an index many have none (REVIEW.md F6)."""
    out = set()
    for a, ps in by_area.items():
        ks = [kind(p) for p in ps]
        ks = [k for k in ks if k != "note"]
        if a.lower().split("/")[-1] in GENERAL or (ks and 2 * len(ks) >= len(ps) and 2 * sum(k in WORK for k in ks) < len(ks)):
            out.add(a)
    return out


def claude_code_memory(root):
    """Claude Code's auto-memory directory for this project, read only (REVIEW.md §8 R1): $MEMORY_CC_DIR; else
    `autoMemoryDirectory` from .claude/settings.local.json beside the project or ~/.claude/settings.json; else
    <config>/projects/<git root with non-alphanumerics as '-'>/memory. None when absent or switched off."""
    if os.environ.get("MEMORY_SOURCES", "").strip() == "notes" or os.environ.get("CLAUDE_CODE_DISABLE_AUTO_MEMORY") == "1":
        return None
    if os.environ.get("MEMORY_CC_DIR"):
        d = Path(os.environ["MEMORY_CC_DIR"]).expanduser()
        return d if d.is_dir() else None
    proj = root.parent
    try:
        r = subprocess.run(["git", "-C", str(proj), "rev-parse", "--show-toplevel"], capture_output=True, text=True, timeout=5)
        if r.returncode == 0 and r.stdout.strip():
            proj = Path(r.stdout.strip())
    except (OSError, subprocess.TimeoutExpired):
        pass
    cfg = Path(os.environ.get("CLAUDE_CONFIG_DIR") or "~/.claude").expanduser()
    for s in (proj / ".claude/settings.local.json", cfg / "settings.json"):  # not the checked-in project settings
        v = (rd(s, {}) or {}).get("autoMemoryDirectory")
        if isinstance(v, str) and v:
            d = Path(v).expanduser()
            return d if d.is_dir() else None
    d = cfg / "projects" / re.sub(r"[^a-zA-Z0-9]", "-", str(proj)) / "memory"
    return d if d.is_dir() else None


def claude_code_owned(root):
    """Why a root is Claude Code's own memory directory (which memory-dream never writes into), or ''."""
    if (root / "MEMORY.md").exists():
        return "it holds a MEMORY.md index"
    cfg = Path(os.environ.get("CLAUDE_CONFIG_DIR") or "~/.claude").expanduser().resolve()
    if root.name == "memory" and root.parent.parent.name == "projects" and root.parent.parent.parent == cfg:
        return f"it is {cfg}/projects/<project>/memory"
    return ""


def find_root(arg):
    if arg:
        return Path(arg).expanduser().resolve()
    if os.environ.get("MEMORY_DIR"):
        return Path(os.environ["MEMORY_DIR"]).expanduser().resolve()
    here = Path.cwd().resolve()
    for d in (here, *here.parents):
        if (d / "memory").is_dir():
            return d / "memory"
    return here / "memory"


# ---------- notes ----------

def scan(root, man):
    """Current notes {path: {sha, mtime, size}}, re-hashing only files whose stat changed; detect moves."""
    old, cur = man.get("files", {}), {}
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if not x.startswith(".") and x != "_dream"]  # an absorbed base may bring its own _dream/
        base = os.path.relpath(d, root).replace(os.sep, "/")
        for f in files:
            if not f.endswith(".md") or f in SKIP or f.startswith("."):
                continue
            rel = f if base == "." else f"{base}/{f}"
            st, o = os.stat(os.path.join(d, f)), old.get(rel)
            same = o and o.get("mtime") == st.st_mtime_ns and o.get("size") == st.st_size
            cur[rel] = {"sha": o["sha"] if same else hashlib.sha256((root / rel).read_bytes()).hexdigest(),
                        "mtime": st.st_mtime_ns, "size": st.st_size}
    oldf = man.get("former", {})
    former = {p: list(v) for p, v in oldf.items() if p in cur}
    arrived = defaultdict(list)
    for p in cur:
        if p not in old:
            arrived[cur[p]["sha"]].append(p)
    moved, deleted = [], []
    for p in (p for p in old if p not in cur):
        c = arrived.get(old[p]["sha"], [])
        if len(c) == 1:  # same content at exactly one new path: a move
            former[c[0]] = sorted(set(former.get(c[0], []) + [p] + oldf.get(p, [])))
            moved.append((p, c[0]))
        else:
            deleted.append(p)
    return cur, former, moved, deleted


def parse_note(text):
    """-> frontmatter dict, title, title line (1-based file line), body [[links]] outside code."""
    lines, fm, i0 = text.split("\n"), {}, 0
    if lines and lines[0].strip() == "---":
        for j in range(1, min(len(lines), 80)):
            if lines[j].strip() == "---":
                key = None
                for ln in lines[1:j]:
                    m = re.match(r"([A-Za-z_][\w-]*)\s*:\s*(.*)$", ln)
                    if m:
                        key = m.group(1).lower()
                        fm[key] = re.sub(r"\s+#.*$", "", m.group(2)).strip()
                    elif key and re.match(r"\s*-\s+", ln):
                        item = re.sub(r"\s+#.*$", "", ln.strip()[1:]).strip()
                        fm[key] = (fm[key] + ", " if fm[key] else "") + item
                i0 = j + 1
                break
    title, tline, fence, links = "", 0, False, []
    for k in range(i0, len(lines)):
        ln = lines[k]
        if ln.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        if not title and ln.startswith("# "):
            title, tline = ln[2:].strip(), k + 1
        links += re.findall(r"\[\[([^\]|#]+)", re.sub(r"`[^`]*`", "", ln))
    return fm, title, tline, links


SLUG = re.compile(r"(?<![\w/-])([a-z][a-z0-9]*(?:-[a-z0-9]+)+)(?![\w-])")


# A pointer into a file of the project, as agents write them: `memory.py#grep_lines`, `src/app.ts:120`, and
# `src/app.ts:120 "export function main"`. Measured on this repository's history (RESULTS K3): a bare line is right
# for 41% of definitions one version later and for none after five, its quoted words are found for 97%, a symbol for
# 100%. So the quote and the symbol are what a pointer is checked by, and a bare line is kept by the text it had.
POINTER = re.compile(r'(?<![\w/.:#-])((?:[\w.-]+/)*[\w.-]+\.[A-Za-z][A-Za-z0-9]{0,5})'
                     r'(?:#([A-Za-z_][\w.]*)|:(\d{1,6})\b(?:`?\s+"([^"\n]{3,160})")?)')


def pointers_in(text):
    """The places a note's text points at: [{to, symbol} | {to, line, quote}]. Whether `to` is a file of the project
    is decided where the project is known (pointer_states)."""
    out, seen = [], set()
    for m in POINTER.finditer(text):
        p = {"to": m.group(1), "symbol": m.group(2)} if m.group(2) else \
            {"to": m.group(1), "line": int(m.group(3)), "quote": m.group(4)}
        key = json.dumps(p, sort_keys=True)
        if key not in seen:
            seen.add(key)
            out.append(p)
    return out


FACTS_V = 2  # the shape of a cached row of note facts: rows of another shape are read again, once


def note_facts(text):
    """What the graph needs from a note's text: frontmatter lineage and dates, the `# ` line, links, body slugs, and
    its pointers into files."""
    fm, title, tline, links = parse_note(text)
    return {"fm": {k: fm[k] for k in ("from", "supersedes", "type", "updated", "modified", "tags") if k in fm}, "title": title, "v": FACTS_V,
            "line": tline, "links": links, "nul": "\x00" in text,  # binary-looking: C9
            "lines": text.count("\n") + (0 if text.endswith("\n") or not text else 1),  # over 40: C11
            "ids": sorted(set(SLUG.findall(text.lower().split("\n", tline)[-1]))) if tline else [],
            "pointers": pointers_in(text.split("\n", tline)[-1]) if tline else pointers_in(text)}


def fm_list(v):
    v = (v or "").strip()
    if v.startswith("[") and v.endswith("]") and not re.fullmatch(r"\[\[[^\]]*\]\]", v):
        v = v[1:-1]
    out = []
    for x in v.split(","):
        x = re.sub(r"^\[\[(.*)\]\]$", r"\1", x.strip().strip("'\"")).strip()
        if x:
            out.append(x)
    return out


POINTER_WALK = 20000  # files looked through to find a pointer written by file name alone (`memory.py:2440`)
# Where a symbol is defined, tried in this order; the first form found anywhere in the file decides, and a symbol is
# never found later by a weaker form than the one it was first seen in. A call is never a definition:
# `eval/pointer_probe.py --built` found 12 of 209 symbols of this file on the line of a call or of a local variable
# of the same name when one pattern took whichever came first.
DEFINES = (
    r"^\s*(?:(?:export|default|public|private|protected|static|async|pub|final|abstract|override)\s+)*"   # 0: a keyword
    r"(?:def|class|function\*?|fn|func(?:\s*\([^)]*\))?|struct|interface|type|enum|trait|impl|const|let|var|val|module|package)"
    r"\s+{s}\s*(?:[(:=<{\[;]|$|(?:extends|implements|where|for|struct|interface)\b)",
    r"^\s*(?:[\w<>\[\],.*&:~?]+\s+)*{s}\s*\([^;]*\{\s*$",   # 1: a block that opens: `render() {`, `static int parse(char *s) {`
    r"^\s*{s}\s*(?::=|=(?!=))",                               # 2: an assignment at the start of a line
    r"^\s*{s}\s*:(?!:)",                                      # 3: a key at the start of a line
)


def define_line(ls, symbol, weakest=None):
    """(the line where a symbol is defined, how many lines define that name, the form it was found by) in a file's
    lines; (None, 0, None) when none does. `Class.method` finds the class, then the method after it. `weakest`: the
    form the symbol was first seen in, when known."""
    at, n, k = 0, 0, None
    parts = symbol.split(".")
    for j, part in enumerate(parts):
        hits = []
        for k, form in enumerate(DEFINES[:len(DEFINES) if weakest is None or j < len(parts) - 1 else weakest + 1]):
            rx = re.compile(form.replace("{s}", re.escape(part)))
            hits = [i for i in range(at, len(ls)) if rx.search(ls[i])]
            if hits:
                break
        if not hits:
            return None, 0, None
        at, n = hits[0] + 1, len(hits)
    return at, n, k


def words_rx(q):
    """Quoted words as a pattern: found exactly, runs of spaces aside, and never inside a longer word (`STOP = set(`
    is not found in `CONFLICT_STOP = set(`)."""
    q = " ".join(q.split())
    edge = lambda c: c.isalnum() or c == "_"  # noqa: E731
    return re.compile((r"(?<!\w)" if edge(q[:1]) else "") + r"\s+".join(re.escape(w) for w in q.split(" "))
                      + (r"(?!\w)" if edge(q[-1:]) else ""))


def code_root(root):
    """Where the files that notes point into live: the repository around the memory (the nearest folder upward
    with a .git, at most four levels), else the folder the memory sits in. $MEMORY_CODE names another."""
    if os.environ.get("MEMORY_CODE"):
        return Path(os.environ["MEMORY_CODE"]).expanduser().resolve()
    r = Path(root).resolve()
    return next((p for p in [r.parent, *r.parent.parents][:4] if (p / ".git").exists()), r.parent)


def pointer_states(root, wanted, was):
    """Every pointer, looked up in the files as they are now. `wanted`: {note: its pointers as written}; `was`: what
    the last dream recorded for them, which holds the text a bare line pointed at when it was first seen.
    -> ({note: [{to, path, line, quote, symbol, text, state, now}]}, C16 checks). States: intact · moved (`now` is the
    line) · changed (the file is there, the words or the symbol are not) · gone (the file is not). A name that was
    never a file of the project is not a pointer and is left out."""
    base, mem = code_root(root), Path(root).resolve()
    cache, names = {}, None

    def lines_of(rel):
        if rel not in cache:
            f = base / rel
            ok = f.is_file() and mem not in f.resolve().parents and f.stat().st_size < 4_000_000
            cache[rel] = f.read_text(encoding="utf-8", errors="replace").split("\n") if ok else None
        return cache[rel]

    def find(to):
        """The file a pointer names: its path from the project's root, or the one file of that name."""
        nonlocal names
        if "/" in to or lines_of(to) is not None:
            return to if lines_of(to) is not None else None
        if names is None:  # by name alone: one walk, once
            names, n = defaultdict(list), 0
            for d, dirs, files in os.walk(base):
                dirs[:] = sorted(x for x in dirs if not x.startswith(".") and x not in ("node_modules", "_dream", "__pycache__")
                                 and Path(d, x).resolve() != mem)
                for f in files:
                    names[f].append(os.path.relpath(os.path.join(d, f), base).replace(os.sep, "/"))
                n += len(files)
                if n > POINTER_WALK:
                    break
        return names[to][0] if len(names.get(to, [])) == 1 else None

    out, checks, squash = {}, [], lambda s: " ".join(s.split())
    for note in sorted(wanted):
        old = {json.dumps({k: p.get(k) for k in ("to", "line", "quote", "symbol")}, sort_keys=True): p for p in was.get(note, [])}
        res = []
        for p in wanted[note]:
            prev = old.get(json.dumps({k: p.get(k) for k in ("to", "line", "quote", "symbol")}, sort_keys=True), {})
            path = prev.get("path") or find(p["to"])
            ls = lines_of(path) if path else None
            if ls is None and not prev:
                continue  # never a file here: a ratio, a host and its port, another base's path
            rec = {"to": p["to"], "path": path, "line": p.get("line"), "quote": p.get("quote"), "symbol": p.get("symbol"),
                   "text": prev.get("text"), "state": "gone", "now": None}
            if ls is not None and p.get("symbol"):
                rec["now"], rec["of"], form = define_line(ls, p["symbol"], prev.get("form"))
                rec["form"] = prev.get("form") if form is None else form
                rec["state"] = "intact" if rec["now"] else "changed"
            elif ls is not None:
                at = p["line"]
                if not p.get("quote") and rec["text"] is None:  # a bare line, first seen: keep the words it points at
                    rec["text"] = squash(ls[at - 1]) if 0 < at <= len(ls) else ""
                want = squash(p.get("quote") or rec["text"] or "")
                rx = words_rx(want) if want and p.get("quote") else None
                hits = [i for i, ln in enumerate(ls, 1) if want and (rx.search(ln) if rx else want == squash(ln))]
                # not on its own line any more and on several others: a line that begins with the words before one
                # that only mentions them, then the nearest; `ask` says that it is one of several
                lead = (lambda i: not rx.match(ls[i - 1].lstrip())) if rx else (lambda i: False)
                rec["now"] = at if at in hits else min(hits, key=lambda i: (lead(i), abs(i - at), i)) if hits else None
                rec["of"] = len(hits)
                rec["state"] = "intact" if rec["now"] == at else "moved" if rec["now"] else "changed"
            res.append(rec)
            if rec["state"] in ("changed", "gone"):
                where = f"#{p['symbol']}" if p.get("symbol") else f":{p['line']}"
                checks.append(("C16", f"{note}: points at {p['to']}{where}, which " + ("is gone" if rec["state"] == "gone" else
                               "changed: " + ("the symbol is not defined there" if p.get("symbol") else "the words it pointed at are not there"))))
        if res:
            out[note] = res
    return out, checks


def pointer_sig(root, ptr):
    """A signature of the files that pointers name: when one of them changes, a dream has pointers to look up again."""
    base, sig = code_root(root), []
    for path in sorted({p["path"] for ps in ptr.values() for p in ps if p.get("path")}):
        try:
            st = (base / path).stat()
            sig.append((path, st.st_mtime_ns, st.st_size))
        except OSError:
            sig.append((path, None, None))
    return hashlib.sha256(json.dumps(sig).encode()).hexdigest()[:12]


def ground(ans, text):
    """Keep only what the note supports: entities whose `as` text occurs in it, relations whose quote does."""
    dropped = {"entities": [], "relations": 0}
    ents, kept = [], {}
    for e in ans.get("entities") or []:
        if not isinstance(e, dict) or not str(e.get("id") or "").strip():
            continue
        ok = [a for a in (e.get("as") or []) if isinstance(a, str) and qpat(a) and qpat(a).search(text)]
        if not ok:
            dropped["entities"].append(str(e["id"]))
            continue
        lines = sorted({line_at(text, m.start()) for a in ok for m in qpat(a).finditer(text)})
        k = fold(e["id"])
        if k in kept:
            kept[k]["as"] = sorted(set(kept[k]["as"]) | set(ok))
            kept[k]["lines"] = sorted(set(kept[k]["lines"]) | set(lines))
            continue
        kept[k] = {"id": str(e["id"]).strip(), "type": str(e.get("type") or "other").strip().lower(),
                   "label": str(e.get("label") or "").strip().lower(), "as": ok, "lines": lines}
        ents.append(kept[k])
    rels = []
    for r in ans.get("relations") or []:
        if not isinstance(r, dict):
            continue
        q = str(r.get("quote") or "")
        m = qpat(q).search(text) if qpat(q) else None
        s, o, t = (str(r.get(k) or "").strip() for k in ("s", "o", "type"))
        if m and t and fold(s) in kept and fold(o) in kept:
            rels.append({"s": kept[fold(s)]["id"], "type": t, "label": str(r.get("label") or t).strip(),
                         "o": kept[fold(o)]["id"], "quote": q, "line": line_at(text, m.start())})
        else:
            dropped["relations"] += 1
    said, recheck = {}, set()
    for field in ("built_on", "replaces"):  # lineage the note states in its prose: kept with the words that state it
        said[field] = []
        for b in ans.get(field) or []:
            what, q = (str(b.get(k) or "").strip() for k in ("what", "quote")) if isinstance(b, dict) else ("", "")
            m = qpat(q).search(text) if what and qpat(q) else None
            if m:
                said[field].append({"what": what, "quote": q, "line": line_at(text, m.start())})
            elif what:
                dropped["relations"] += 1
                # the words were not copied as they stand ("Builds on aml-xgb-v3, …" for a line that says v2, and all four
                # of its members lost): the item is not kept, but the lines that write what it names are read again
                w = posixpath.basename(what[:-3] if what.endswith(".md") else what)
                if len(w) >= 3:
                    recheck |= {(field, line_at(text, mm.start())) for mm in re.finditer(r"(?<![\w/.-])" + re.escape(w) + r"(?![\w-])", text, re.I)}
    word = re.sub(r"^other\s*[:/]\s*", "", str(ans.get("kind") or "").strip().lower()).strip()
    kind = fold(word) if fold(word) in KINDS else KIND_ALIAS.get(fold(word), "note")
    tags = []                                            # tags as read: words kept as given, resolved at every merge
    for t in ans.get("tags") or []:
        if isinstance(t, str) and t.strip() and t.strip() not in tags and len(tags) < 5:
            tags.append(t.strip())
    return {"kind": kind, **({"kind_word": word} if kind == "note" and word and fold(word) not in ("note", "other") else {}),
            **({"tags": tags} if tags else {}), "entities": ents,
            "relations": rels, "refs": [str(x) for x in (ans.get("refs") or []) if isinstance(x, str)],
            **{k: v for k, v in said.items() if v}, **({"recheck": [{"field": f, "line": n} for f, n in sorted(recheck)]} if recheck else {}),
            "dropped": dropped}


# ---------- vocabularies ----------

PROPOSED_RX = re.compile(r"\s*\(proposed (\d{4}-\d\d-\d\d)\)\s*")


def expand_packs(text, packs=None):
    """A vocabulary file with its `pack: software, …` lines expanded into the packs' lines."""
    packs = PACKS if packs is None else packs
    names = [p.strip().lower() for ln in text.split("\n") for m in [re.match(r"\s*pack\s*:(.*)$", ln, re.I)] if m
             for p in m.group(1).split(",") if p.strip()]
    return text + "".join("\n" + packs[n] for n in names if n in packs)


def parse_shape(v):
    """`model → dataset`, `* → metric`, `same` -> (subject family or None, object family or None) or ("same", "same")."""
    v = v.strip()
    if fold(v) == "same":
        return ("same", "same")
    parts = re.split(r"\s*(?:→|->)\s*", v)
    if len(parts) != 2:
        return None
    return tuple(None if p.strip() in ("*", "") else fold(p) for p in parts)


def edges_cfg(text, defaults=None):
    """A vocabulary's constraints from its file (EDGES.md, TYPES.md, KINDS.md, TAGS.md: one grammar): promote (uses,
    notes, areas), budget, probation days, the proposed terms with their dates, the packs named, and the words the
    review chose to keep as plain words (`keep: word ×uses (date)`), each with how many uses it had then. `defaults`
    gives a vocabulary its own bar and budget when its file sets none."""
    cfg = {"promote": PROMOTE, "budget": BUDGET, "probation": PROBATION_DAYS, "proposed": {}, "packs": [], "kept": {},
           **(defaults or {})}
    for ln in text.split("\n"):
        s = ln.strip()
        m = re.match(r"keep\s*:(.*)$", s, re.I)
        if m:
            for w, u in re.findall(r"([^\s,×]+)\s*×\s*(\d+)", m.group(1)):
                cfg["kept"][fold(w)] = int(u)
        m = re.match(r"promote\s*:\s*(\d+)\D+(\d+)\D+(\d+)", s, re.I)
        if m:
            cfg["promote"] = tuple(int(x) for x in m.groups())
        m = re.match(r"budget\s*:\s*(\d+)", s, re.I)
        if m:
            cfg["budget"] = int(m.group(1))
        m = re.match(r"probation\s*:\s*(\d+)", s, re.I)
        if m:
            cfg["probation"] = int(m.group(1))
        m = re.match(r"pack\s*:(.*)$", s, re.I)
        if m:
            cfg["packs"] += [p.strip().lower() for p in m.group(1).split(",") if p.strip()]
        m = re.match(r"-\s*([^:|]+?)\s*:", s)
        if m and PROPOSED_RX.search(m.group(1)):
            cfg["proposed"][fold(PROPOSED_RX.sub("", m.group(1)))] = PROPOSED_RX.search(m.group(1)).group(1)
    return cfg


def parse_edges(text, packs=None):
    """A vocabulary file (EDGES.md, or TYPES.md with packs=TYPE_PACKS) -> types {T: {def, aka, family, shape}},
    alias {folded: (T, reversed)}, drop, raw type lines, bad lines, extra {family: {T: F}, shape: {T: (s, o)}}.
    A line is `- type: definition | aka: a, ~b | family: parent | shape: s → o`, the fields after the definition in any order."""
    types, alias, drop, tl, bad = {}, {}, set(), [], []
    extra = {"family": {}, "shape": {}}
    for i, ln in enumerate(expand_packs(text, packs).split("\n"), 1):
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        m = re.match(r"-\s*([^:|]+?)\s*:\s*(.*)$", s)
        d = re.match(r"drop\s*:(.*)$", s, re.I)
        if re.match(r"(mode|promote|budget|probation|pack|general|drop-names|keep)\s*:", s, re.I):  # settings: edges_cfg and name_drop read them
            continue
        if m:
            t = fold(PROPOSED_RX.sub("", m.group(1)))
            segs = [x.strip() for x in m.group(2).split("|")]
            aka, fam, shape, walk, hops = [], None, None, None, None
            for seg in segs[1:]:
                key, _, val = seg.partition(":")
                key = key.strip().lower()
                if key == "aka":
                    aka += [a.strip() for a in val.split(",") if a.strip()]
                elif key == "family":
                    fam = fold(val)
                elif key == "shape":
                    shape = parse_shape(val)
                elif key == "walk":
                    walk = [a.strip() for a in val.split(",") if a.strip()]
                elif key == "hops" and val.strip().isdigit():
                    hops = int(val)
            types[t] = {"def": segs[0], "aka": aka, "family": fam or t, "shape": shape, "walk": walk, "hops": hops}
            if fam and fam != t:
                extra["family"][t] = fam
            if shape:
                extra["shape"][t] = shape
            alias.setdefault(t, (t, False))
            for a in aka:
                alias.setdefault(fold(a.lstrip("~")), (t, a.startswith("~")))
            tl.append(s)
        elif d:
            drop |= {fold(x) for x in d.group(1).split(",") if x.strip()}
        else:
            bad.append((i, s))
    return types, alias, drop, tl, bad, extra


def split_pair(s):
    a, _, b = s.partition(" / ") if " / " in s else s.partition("/")
    return a.strip(), b.strip()


def parse_aliases(text):
    lines, nots, bad = [], set(), []
    for i, ln in enumerate(text.split("\n"), 1):
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        m = re.match(r"-\s*(.+?)\s*=\s*(.+)$", s)
        n = re.match(r"not\s*:(.+)$", s, re.I)
        if m:  # `- a = b, c | why: … | by: …`: what follows the first ` | ` is the reason and who decided, for people
            lines.append([m.group(1).strip()] + [x.strip() for x in m.group(2).split(" | ")[0].split(",") if x.strip()])
        elif n and "/" in n.group(1):
            a, b = split_pair(n.group(1).split(" | ")[0])
            nots.add(frozenset((fold(a), fold(b))))
        else:
            bad.append((i, s))
    return lines, nots, bad


def edit_edges(text, op, t, arg="", date=None):
    """Edits to a vocabulary file (EDGES.md, TYPES.md, KINDS.md, TAGS.md): alias (t onto arg's aka), drop (t onto the
    drop line), new (a line for t with the definition arg, marked proposed on date), demote (remove t's line), keep
    (t onto the keep line with arg, its uses now: the review kept it a plain word, and it is not asked again until its
    uses double)."""
    if op == "keep":
        lines = text.rstrip("\n").split("\n")
        k = next((i for i, ln in enumerate(lines) if re.match(r"\s*keep\s*:", ln, re.I)), -1)
        entry = f"{t} ×{arg} ({date})"
        if k < 0:
            lines.append(f"keep: {entry}")
        else:
            rest = [e.strip() for e in lines[k].split(":", 1)[1].split(",") if e.strip() and fold(e.split("×")[0]) != fold(t)]
            lines[k] = "keep: " + ", ".join(rest + [entry])
        return "\n".join(lines) + "\n"
    lines = text.rstrip("\n").split("\n")

    def find(T):
        for k, ln in enumerate(lines):
            m = re.match(r"\s*-\s*([^:|]+?)\s*:", ln)
            if m and fold(PROPOSED_RX.sub("", m.group(1))) == T:
                return k
        return -1

    def add_aka(k, a):  # into the aka field, before any field that follows it
        segs = lines[k].split("|")
        j = next((i for i, seg in enumerate(segs) if re.match(r"\s*aka\s*:", seg)), -1)
        if j >= 0:
            segs[j] = segs[j].rstrip() + ", " + a + " "
            lines[k] = "|".join(segs).rstrip()
        else:
            lines[k] = (segs[0].rstrip() + " | aka: " + a + (" | " + "|".join(segs[1:]).strip() if len(segs) > 1 else "")).rstrip()

    dk = next((k for k, ln in enumerate(lines) if re.match(r"\s*drop\s*:", ln, re.I)), -1)
    if op == "alias":
        add_aka(find(arg), t)
    elif op == "new":
        lines.insert(dk if dk >= 0 else len(lines), f"- {t} (proposed {date}): {arg}")
    elif op == "demote":
        k = find(t)
        if k >= 0:
            del lines[k]
    elif dk < 0:
        lines.append(f"drop: {t}")
    else:
        lines[dk] = lines[dk].rstrip() + ("" if lines[dk].rstrip().endswith(":") else ",") + " " + t
    return "\n".join(lines) + "\n"


def parse_conflicts(text):
    """memory/CONFLICTS.md -> supersessions [(a, b)], compatible pairs, unsure pairs, bad lines. Paths without .md accepted."""
    sup, compat, unsure, bad = [], set(), set(), []
    norm = lambda p: (p.strip() + ("" if p.strip().endswith(".md") else ".md"))  # noqa: E731
    for i, ln in enumerate(text.split("\n"), 1):
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        m = re.match(r"-\s*(\S+)\s*([>?])\s*(\S+)$", s)
        c = re.match(r"compatible\s*:\s*(\S+)\s*/\s*(\S+)$", s, re.I)
        if m and m.group(2) == ">":
            sup.append((norm(m.group(1)), norm(m.group(3))))
        elif m:
            unsure.add(frozenset((norm(m.group(1)), norm(m.group(3)))))
        elif c:
            compat.add(frozenset((norm(c.group(1)), norm(c.group(2)))))
        elif not DROPPED.match(s):  # a tombstone is read by parse_dropped
            bad.append((i, s))
    return sup, compat, unsure, bad


DROPPED = re.compile(r"dropped\s*:\s*(\S+)(?:\s+\((\d{4}-\d\d-\d\d)\))?(?:\s*>\s*(.+))?$", re.I)


def parse_dropped(text):
    """The tombstones of memory/CONFLICTS.md, written by `drop` and by nothing else:
    `dropped: <note.md | folder/> (YYYY-MM-DD) > <what it had replaced>, …` -> {path: {date, replaced: [paths]}}.
    A folder's key ends with "/". The build reads a tombstone as a pass-through in a line of replacements."""
    out = {}
    for ln in text.split("\n"):
        m = DROPPED.match(ln.strip())
        if m:
            p = m.group(1) if m.group(1).endswith(("/", ".md")) else m.group(1) + ".md"
            out[p] = {"date": m.group(2) or "", "replaced": [x.strip() + ("" if x.strip().endswith(".md") else ".md")
                                                              for x in (m.group(3) or "").split(",") if x.strip()]}
    return out


def tombstoned(tomb, p):
    """Is this path one `drop` recorded: a note's own line, or a folder's?"""
    return p in tomb or any(f.endswith("/") and p.startswith(f) for f in tomb)


SEED_SHAPES = parse_edges(EDGES_SEED)[5]["shape"]  # EDGES.md files written before `shape:` fields existed keep these
SEED_EDGE_TYPES = parse_edges(EDGES_SEED)[0]  # … and the seed's walk words and hops, type by type
globals().update(domain_from(KINDS_SEED, TYPES_SEED, EDGES_SEED))  # the module's defaults: the seeds


def title_tokens(title):
    return {t for t in re.findall(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", (title or "").lower())
            if len(t) >= 4 and t not in STOP and t not in CONFLICT_STOP}


def idlike(t):
    """A title token that names a thing rather than a word: a version, an id with digits, a long hyphenated name."""
    return bool(re.search(r"-v\d+$", t) or (re.search(r"[-.]", t) and re.search(r"\d", t)) or t.count("-") >= 2)


def conflict_candidates(notes, edges, decided):
    """Pairs of live notes in one area, not linked by lineage, that may disagree: two `…-vN` siblings (any kind), two
    notes with the same title, or two notes of a decision/model/finding kind sharing an id-like title token or two
    title words rare among that area's notes of the kind (bank: 282 → 38 with the token rule alone, both known true
    positives kept). `decided` pairs (unsure) are marked so the review is not asked again."""
    linked = {frozenset((e["src"], e["dst"])) for e in edges}
    live = [n for n in notes.values() if not n["superseded_by"] and n["project"] != "log"]
    out, seen = [], set()

    def add(a, b, shared):
        key = frozenset((a, b))
        if key in linked or key in seen:
            return
        seen.add(key)
        out.append({"a": min(a, b), "b": max(a, b), "shared": shared, "unsure": key in decided})

    by_ver = defaultdict(list)  # feat-x-v2 / feat-x-v3 both live and unlinked: almost always a missing supersedes:
    for n in live:
        if re.search(r"-v\d+$", n["id"]):
            by_ver[(n["project"], re.sub(r"-v\d+$", "", n["id"]))].append(n["path"])
    for ps in by_ver.values():
        for i, a in enumerate(sorted(ps)):
            for b in sorted(ps)[i + 1:]:
                add(a, b, ["version"])
    by_title = defaultdict(list)
    for n in live:
        if n["title"]:
            by_title[(n["project"], n["title"].strip().lower())].append(n["path"])
    for ps in by_title.values():
        for i, a in enumerate(sorted(ps)):
            for b in sorted(ps)[i + 1:]:
                add(a, b, ["same title"])
    by = defaultdict(list)
    for n in live:
        if family(n["kind"]) in CONFLICT_KINDS:
            by[(n["project"], family(n["kind"]))].append(n)
    for ns in by.values():
        toks = {n["path"]: title_tokens(n["title"]) for n in ns}
        freq = Counter(t for ts in toks.values() for t in ts)
        ps = sorted(toks)
        for i, a in enumerate(ps):
            for b in ps[i + 1:]:
                shared = sorted(t for t in toks[a] & toks[b] if freq[t] <= 3)
                if len(shared) >= 2 or any(idlike(t) for t in shared):
                    add(a, b, shared)
    out.sort(key=lambda c: (c["unsure"], c["shared"] not in (["version"], ["same title"]), -len(c["shared"]), c["a"], c["b"]))
    return out


def edit_aliases(text, a, b, same, lead=None, note=""):
    """One decision into ALIASES.md: `- lead = other` or `not: a / b`. `note` is appended to a new line
    (` | why: … | by: …`); names added to a line that exists go before its note. A line is extended only by the hand
    that signed it (`by: curator`, `by: review`, or nobody: a person): another's decision gets a line of its own, so
    that every line says who decided all of it."""
    lines = text.rstrip("\n").split("\n")
    if not same:
        lines.append(f"not: {a} / {b}{note}")
        return "\n".join(lines) + "\n"
    signer = lambda t: (re.search(r"\|\s*by:\s*(\S+)", " | " + t) or [None, ""])[1]  # noqa: E731
    for k, ln in enumerate(lines):
        core, sep, tail = ln.partition(" | ")
        m = re.match(r"\s*-\s*(.+?)\s*=\s*(.+)$", core)
        if m:
            have = {fold(x) for x in [m.group(1)] + m.group(2).split(",")}
            if (fold(a) in have or fold(b) in have) and signer(tail) == signer(note):
                lines[k] = core + "".join(", " + x for x in (a, b) if fold(x) not in have) + sep + tail
                return "\n".join(lines) + "\n"
    first = lead or a
    lines.append(f"- {first} = {b if first == a else a}{note}")
    return "\n".join(lines) + "\n"


def lead_aliases(text, lead):
    """The line of ALIASES.md that holds this id, rewritten so that the id leads it (the first id of a line is the
    thing's name)."""
    lines = text.rstrip("\n").split("\n")
    for k, ln in enumerate(lines):
        core, sep, tail = ln.partition(" | ")
        m = re.match(r"\s*-\s*(.+?)\s*=\s*(.+)$", core)
        ids = [m.group(1).strip()] + [x.strip() for x in m.group(2).split(",") if x.strip()] if m else []
        if fold(lead) in {fold(x) for x in ids} and fold(ids[0]) != fold(lead):
            rest = [x for x in ids if fold(x) != fold(lead)]
            lines[k] = f"- {lead} = {', '.join(rest)}" + sep + tail
    return "\n".join(lines) + "\n"


# ---------- merge ----------

def read_links(ends):
    """Pairs of ids that readings link, folded: two things, which no rule of the merge joins."""
    return {frozenset((fold(a), fold(b))) for a, b in ends if fold(a) != fold(b)}


def linked_pairs(g):
    """Pairs of things the graph links: every join is held to it (two things a note links are two things)."""
    return {frozenset((r["s"], r["o"])) for r in g["relations"]}


def merge_entities(occ, alines, nots, homes=None, stats=None, linked=frozenset()):
    """Entity groups as one union-find: ALIASES lines, folded-id equality, the surface-form rule. The rules never
    join two ids that a reading links to each other (`linked`, from read_links): a note that links two names says
    they are two things. Only a line of ALIASES.md can, and C19 reports it when a note links its names.
    An entity is kept when it has a home (a note whose slug is its id), is mentioned in >= 2 notes, or is
    named in ALIASES.md; a name on the `drop-names:` line of TYPES.md is not an entity (files and notebooks: grep finds them)."""
    homes, st = homes or {}, stats if stats is not None else Counter()
    par, mem, explicit = {}, {}, set()

    def find(x):
        par.setdefault(x, x)
        mem.setdefault(x, {x})
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    def join(a, b, force=False):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if not force:
            for x in mem[ra]:
                for y in mem[rb]:
                    p = frozenset((x, y))
                    if p in nots or p in linked or (versions(x, y) and p not in explicit):
                        st["refused_" + ("not_line" if p in nots else "linked" if p in linked else "versions")] += 1
                        return
        par[rb] = ra
        mem[ra] |= mem.pop(rb)

    def roots():
        return len({find(k) for k in raw})

    raw, surf, typ = defaultdict(Counter), defaultdict(Counter), defaultdict(Counter)
    ment = defaultdict(lambda: defaultdict(set))
    for path, e in occ:
        k = fold(e["id"])
        raw[k][e["id"]] += 1
        typ[k][e["type"]] += 1
        for a in e["as"]:
            surf[k][a] += 1
        ment[k][path] |= set(e["lines"])
    st["mentions"], st["ids_as_written"], st["after_folding"] = len(occ), sum(len(v) for v in raw.values()), len(raw)
    lead = {}
    for li, ids in enumerate(alines):
        fs = [fold(i) for i in ids]
        explicit |= {frozenset((x, y)) for x in fs for y in fs if x != y}
        for f in fs:
            lead.setdefault(f, (li, ids[0]))
            join(fs[0], f, force=True)
    if stats is not None:  # counting groups costs a pass over every id
        st["after_aliases_md"] = roots()
    sf_index = defaultdict(set)
    okeys = {fold(o) + ":" for o in ORIGINS}  # an origin's things carry its name; a surface form joins inside it only
    pre = lambda k: next((o for o in okeys if k.startswith(o)), "")  # noqa: E731
    for k in raw:
        find(k)
        for a in surf[k]:
            sf_index[pre(k) + fold(a)].add(k)
    for k in raw:  # exactly one other entity writes this id as a surface form → one entity
        users = sf_index.get(k, set())
        others = users - {k}
        if len(users) <= 3 and len(others) == 1:
            join(k, next(iter(others)))
    if stats is not None:
        st["after_surface_rule"] = roots()
    groups = defaultdict(list)
    for k in raw:
        groups[find(k)].append(k)
    ents, cmap, gkeys = {}, {}, {}
    for ks in groups.values():
        allk = set(ks) | {k for k in mem[find(ks[0])] if k in lead}
        led = sorted(lead[k] for k in allk if k in lead)
        cand, sc, exact = Counter(), Counter(), Counter()
        for k in ks:
            cand.update(raw[k])
        for k in ks:
            for a, n in surf[k].items():
                for rid in cand:
                    sc[rid] += n * (fold(a) == fold(rid))
                    exact[rid] += n * (a == rid)
        c = led[0][1] if led else min(cand, key=lambda r: (-(cand[r] + sc[r]), -exact[r], r.lower(), r))
        tc, names, mm = Counter(), Counter(), defaultdict(set)
        for k in ks:
            tc.update(typ[k])
            names.update(surf[k])
            for p, ls in ment[k].items():
                mm[p] |= ls
        projects = Counter(area_of(p) for p in mm)
        home = min((h for k in ks for h in homes.get(k, [])), default=None,
                   key=lambda h: (-projects[area_of(h)], h))
        if NAME_DROP and (NAME_DROP.fullmatch(c.lower()) or NAME_DROP.fullmatch(fold(c))):  # TYPES.md `drop-names:`
            st["dropped_file_like"] += 1
            continue
        if not (home or len(mm) >= 2 or led):
            st["dropped_one_note"] += 1
            continue
        st["kept_with_home" if home else "kept_in_2plus_notes" if len(mm) >= 2 else "kept_by_aliases_md"] += 1
        ents[c] = {"id": c, "type": min(tc, key=lambda t: (-tc[t], t)), "home": home,
                   "aka": sorted({r for k in ks for r in raw[k]} - {c}),
                   "names": [{"name": a, "n": n} for a, n in sorted(names.items(), key=lambda z: (-z[1], z[0]))],
                   "headline": None, "mentions": [{"path": p, "lines": sorted(mm[p])} for p in sorted(mm)]}
        gkeys[c] = set(ks)
        for k in ks:
            cmap[k] = c
    return ents, cmap, gkeys


def candidates(ents, new, gkeys, nots, linked=frozenset()):
    """Pairs for the review: two things of one type that some note writes with the same words. Nothing is proposed
    from how two names look: on the bank the string ratio that used to do it offered 46 pairs, 5 of them the same
    thing (all plurals) and 41 siblings such as aml-oot-2026h1 / cli-oot-2026h1 (RESULTS phase S). Two unlike names
    for one thing are found by the curator, which reads a folder's things together (Dream.run_curate)."""
    sfs = {c: {fold(n["name"]) for n in e["names"]} for c, e in ents.items()}
    cnt = Counter(s for v in sfs.values() for s in v)
    by_type = defaultdict(list)
    for c, e in ents.items():
        by_type[e["type"]].append(c)
    out = set()
    for a in new:
        fa = fold(a)
        mine = {s for s in sfs[a] if cnt[s] <= 3}
        for b in by_type[ents[a]["type"]]:
            if b == a or versions(fa, fold(b)):
                continue
            pair = tuple(sorted((a, b), key=fold))
            ha, hb = ents[a].get("home"), ents[b].get("home")
            if pair in out or (ha and hb and ha != hb) or frozenset(pair) in linked or decided(a, b, gkeys, nots):
                continue  # two home notes, or a note that links the two: two things
            if mine & sfs[b]:
                out.add(pair)
    return out


def thing_cards(g, root, ids, area=None):
    """What a thing is judged by, one card each -> {id: card}: its id and type, how the notes write it, in how many
    notes, what its own note says it is (is:), what the notes link it to (links:, the best attested first; → from it,
    ← to it), and a line that mentions it (in `area` when given). The curator reads a folder's cards, the review a
    pair's: who is the same is decided by what a thing is and what it is linked to, never by a name alone."""
    want = set(ids)
    ents = {e["id"]: e for e in g["entities"] if e["id"] in want}
    nmap = {n["path"]: n for n in g["notes"]}
    nb, texts, out = defaultdict(list), {}, {}
    for r in g["relations"]:
        if r["s"] in want:
            nb[r["s"]].append((-len(r["evidence"]), f"{r['type']} → {r['o']}"))
        if r["o"] in want:
            nb[r["o"]].append((-len(r["evidence"]), f"{r['type']} ← {r['s']}"))

    def line(m):
        if m["path"] not in texts:
            try:
                texts[m["path"]] = read(root / m["path"]).split("\n")
            except OSError:
                texts[m["path"]] = []
        ls, k = texts[m["path"]], (m["lines"] or [0])[0]
        return ls[k - 1].strip()[:140] if 0 < k <= len(ls) else ""
    for i in ids:
        e = ents.get(i)
        if not e:
            continue
        ms = [m for m in e["mentions"] if area is None or area_of(m["path"]) == area] or e["mentions"]
        ms = sorted(ms, key=lambda m: m["path"] == e.get("home"))  # its own note says what it is; the line is another's
        home = nmap.get(e.get("home") or "") or {}
        links = [x for _, x in sorted(nb[i])[:3]]
        out[i] = (f"{i} ({e['type']}) · written: " + "; ".join(f'"{x["name"]}"' for x in e["names"][:4]) + f" · in {len(e['mentions'])} notes"
                  + (f' · is: "{home["title"][:100]}"' if home.get("title") else "") + (f" · links: {'; '.join(links)}" if links else "")
                  + f" · «{line(ms[0]) if ms else ''}»")
    return out


def shared_links(g, a, b):
    """What two things are both linked to, by the same relation in the same direction: two names of one thing are
    linked alike; two things with nothing in common are likelier two."""
    def ends(i):
        return {(r["type"], "→", r["o"]) for r in g["relations"] if r["s"] == i} | {(r["type"], "←", r["s"]) for r in g["relations"] if r["o"] == i}
    return sorted(f"{t} {d} {x}" for t, d, x in ends(a) & ends(b))


def decided(a, b, gkeys, nots):
    return any(frozenset((x, y)) in nots for x in gkeys.get(a, {fold(a)}) for y in gkeys.get(b, {fold(b)}))


def notes_part(root, man, cur, former, xs=None, facts=None):
    """The half of the graph that the vocabulary does not touch: notes, lineage edges, note warnings."""
    load_domain(root)
    checks = []
    notes, aux, by_stem = {}, {}, defaultdict(list)
    for rel in sorted(cur):
        h = cur[rel]["sha"]
        f = facts[rel] if facts is not None and rel in facts else note_facts(read(root / rel))
        fm, title, tline, links = f["fm"], f["title"], f["line"], f["links"]
        x = xs.get(h[:12]) if xs is not None else rd(root / "_dream" / "notes" / f"{h[:12]}.json")
        up = fm.get("updated") or fm.get("modified") or ""  # modified: Claude Code's auto-memory timestamp
        stem_date = re.match(r"\d{4}-\d\d-\d\d$", posixpath.basename(rel)[:-3])  # log/YYYY-MM-DD.md
        up = up[:10] if re.match(r"\d{4}-\d\d-\d\d", up) else stem_date.group(0) if stem_date else \
            dt.date.fromtimestamp(cur[rel]["mtime"] / 1e9).isoformat()
        proj = area_of(rel)
        notes[rel] = {"path": rel, "id": posixpath.basename(rel)[:-3], "project": proj, "title": title,
                      "line": tline, "kind": kind_of(rel, fm.get("type"), read_kind(x)),
                      "superseded_by": [], "updated": up, "sha": h[:12], "indexed": bool(x)}
        aux[rel] = {"fm": fm, "links": links, "x": x, "ids": set(f["ids"]), "pointers": f.get("pointers") or []}
        by_stem[notes[rel]["id"]].append(rel)
        if not title:
            checks.append(("C6", f"{rel}: no '# ' line"))
        if f.get("nul"):
            checks.append(("C9", f"{rel}: contains NUL bytes (binary-looking); keep notes plain text"))
        if f.get("lines", 0) > NOTE_MAX_LINES and proj != "log":
            checks.append(("C11", f"{rel}: {f['lines']} lines, over the 40-line rule; split it, or move detail to a new note"))
        if not x:
            checks.append(("C3" if h[:12] in man.get("failed", {}) else "C5", f"{rel}: unindexed"))
        else:
            dr = x.get("dropped") or {}
            checks += [("C4", f"{rel}: entity {e} not in the note") for e in dr.get("entities", [])]
            checks += [("C4", f"{rel}: relation without its quote")] * dr.get("relations", 0)
    old2cur = {o: p for p, olds in former.items() for o in olds if p in notes}
    oldstem = defaultdict(list)
    for o, p in old2cur.items():
        oldstem[posixpath.basename(o)[:-3]].append(p)

    def resolve(v, src):
        v = re.sub(r"^\[\[|\]\]$", "", v.strip()).strip()
        v = v[:-3] if v.endswith(".md") else v
        so = origin_of(src)
        paths = [posixpath.normpath(posixpath.join(posixpath.dirname(src), v)) + ".md", posixpath.normpath(v) + ".md"] \
            + ([f"{so}/{posixpath.normpath(v)}.md"] if so else [])  # a path an absorbed base wrote from its own root
        for c in paths:
            if c in notes:
                return c, ""
        stem, c = posixpath.basename(v), by_stem.get(posixpath.basename(v), [])
        if ORIGINS:  # by name: inside the note's own origin, then the host; never guessed across origins
            c = [p for p in c if origin_of(p) == so] or ([p for p in c if not origin_of(p)] if so else [])
        if len(c) == 1:
            return c[0], ""
        if c:
            mine = [p for p in c if area_of(p) == area_of(src)]
            return sorted(mine or c)[0], "C1"
        for c in paths:
            if c in old2cur:
                return old2cur[c], ""
        return (sorted(oldstem[stem])[0], "") if oldstem.get(stem) else (None, "C2")

    cf = root / "CONFLICTS.md"  # decisions kept beside the notes: who replaced whom, and what was dropped
    ctext = read(cf) if cf.exists() else ""
    tomb = parse_dropped(ctext)
    for d in [d for d in tomb if d in notes]:  # the file is back: the note counts, the line is stale
        checks.append(("C8", f"CONFLICTS.md: dropped: {d} names a note that exists; delete the line"))
        del tomb[d]
    tstem = defaultdict(list)  # a bare id finds a dropped note as it finds a live one
    for d in tomb:
        if not d.endswith("/"):
            tstem[posixpath.basename(d)[:-3]].append(d)

    def was_dropped(v, src):
        """The dropped note a reference names, when no note answers to it."""
        v = re.sub(r"^\[\[|\]\]$", "", v.strip()).strip()
        v = v[:-3] if v.endswith(".md") else v
        for c in (posixpath.normpath(posixpath.join(posixpath.dirname(src), v)) + ".md", posixpath.normpath(v) + ".md"):
            if tombstoned(tomb, c):
                return c
        c = tstem.get(posixpath.basename(v), [])
        mine = [p for p in c if area_of(p) == area_of(src)]
        return sorted(mine or c)[0] if c else None

    def through(d, seen=frozenset()):
        """What a dropped note had replaced, followed to notes that exist: a tombstone passes a replacement on."""
        out = []
        for t in tomb.get(d, {}).get("replaced", []):
            if t in notes:
                out.append(t)
            elif t in tomb and t != d and t not in seen:
                out += through(t, seen | {d})
        return out

    edges, linked = [], set()
    built_on = defaultdict(list)  # dropped note → the notes whose from: line names it; they stay, and say so
    for rel in notes:
        for kind in ("from", "supersedes"):
            for v in fm_list(aux[rel]["fm"].get(kind)):
                dst, w = resolve(v, rel)
                gone = was_dropped(v, rel) if tomb and not dst else None
                if gone:  # C14, not C2: the note was dropped on purpose, and who replaced it now replaces what it had
                    if kind == "from":
                        built_on[gone].append(rel)
                    for t in (through(gone) if kind == "supersedes" else []):
                        if t != rel and (rel, t, kind) not in linked:
                            linked.add((rel, t, kind))
                            edges.append({"src": rel, "dst": t, "rel": kind, "by": "drop"})
                    continue
                if w:
                    checks.append((w, f"{rel}: {kind} {v} " + (f"is ambiguous, using {dst}" if dst else "not found")))
                if dst and dst != rel and (rel, dst, kind) not in linked:
                    linked.add((rel, dst, kind))
                    edges.append({"src": rel, "dst": dst, "rel": kind})
        x = aux[rel]["x"] or {}
        proj = area_of(rel)
        # a slug written in the body names a note of the same project (cross-project slugs measured nil for answers:
        # 67 links on the bank, gold 0.920 → 0.916, RESULTS phase F)
        mentioned = [i for i in aux[rel]["ids"] if any(area_of(p_) == proj for p_ in by_stem.get(i, []))]
        for v in aux[rel]["links"] + list(x.get("refs") or []) + sorted(mentioned):  # a slug written in the body points at that note
            dst = resolve(v, rel)[0]
            if dst and dst != rel and not any((rel, dst, k) in linked for k in ("from", "supersedes", "refs")):
                linked.add((rel, dst, "refs"))
                edges.append({"src": rel, "dst": dst, "rel": "refs"})
    # supersessions decided by the review or a person: lineage, with the notes untouched
    sup, _, _, bad_c = parse_conflicts(ctext)
    checks += [("C8", f"CONFLICTS.md:{i}: {s}") for i, s in bad_c]
    for o in ORIGINS:  # what an absorbed base had decided about its own notes holds inside it
        of = root / o / "CONFLICTS.md"
        osup, _, _, obad = parse_conflicts(read(of)) if of.exists() else ([], set(), set(), [])
        sup += [(f"{o}/{a}", f"{o}/{b}") for a, b in osup]
        checks += [("C8", f"{o}/CONFLICTS.md:{i}: {s}") for i, s in obad]
    for a, b in sup:
        for t in ([b] if b in notes else through(b) if b in tomb else []):
            if a in notes and a != t and (a, t, "supersedes") not in linked:
                linked.add((a, t, "supersedes"))
                edges.append({"src": a, "dst": t, "rel": "supersedes", "by": "review" if t == b else "drop"})
    for e in edges:
        if e["rel"] == "supersedes":
            notes[e["dst"]]["superseded_by"].append(e["src"])
    dropped = []  # what `drop` recorded, with what it means for the notes that are left (CONTRACT §1)
    for d in sorted(set(tomb) | set(built_on)):
        t = tomb.get(d) or next((tomb[f] for f in sorted(tomb) if f.endswith("/") and d.startswith(f)), {"date": "", "replaced": []})
        when = f" on {t['date']}" if t["date"] else ""
        by = sorted(set(built_on.get(d, [])))
        left = [y for y in t["replaced"] if y in notes and not notes[y]["superseded_by"]] if d in tomb else []
        dropped.append({"path": d, "date": t["date"], "replaced": list(t["replaced"]) if d in tomb else [],
                        "built_on_by": by, "left_newest": left})
        checks += [("C14", f"{r}: built on {d}, which was dropped{when}") for r in by]
        checks += [("C14", f"{y}: {d} had replaced it and was dropped{when}; it is the newest note left of that line") for y in left]
    return {"notes": notes, "aux": aux, "edges": edges, "checks": checks, "dropped": dropped}


def canon_occ(occ, talias, tdrop):
    """Entity occurrences with their type read through TYPES.md: a type or alias becomes the type; a word that fits
    none stays as other/<word> and is counted for the review; a dropped word (a file, a number) removes the occurrence.
    -> occurrences, {word: {type, uses, notes, areas, examples}}."""
    out, props = [], {}
    for rel, e in occ:
        raw, lbl = fold(e.get("type") or "other"), fold(e.get("label") or "")
        if raw in talias:
            T = talias[raw][0]
        elif lbl and lbl in talias:
            T = talias[lbl][0]
        elif raw in tdrop or (lbl and lbl in tdrop):
            continue
        elif raw in ("other", "") and not lbl:
            T = "other"
        else:
            w = lbl or raw
            T = f"other/{w}"
            p = props.setdefault(w, {"type": w, "uses": 0, "notes": set(), "areas": set(), "examples": []})
            p["uses"] += 1
            p["notes"].add(rel)
            p["areas"].add(area_of(rel))
            if len(p["examples"]) < 3:
                p["examples"].append(f"{e['id']}: {(e.get('as') or [e['id']])[0]}")
        out.append((rel, {**e, "type": T}))
    return out, props


def vocab_gate(props, cfg, n_types, usage, now, noun, shown):
    """The constrained-open gate, one for every vocabulary (relation labels, type words, kind words, tag words): ->
    (proposed over the bar while the budget has room, below the bar, proposed terms to demote after their probation,
    C7 checks). A word the review kept as a plain word is offered again only once its uses have doubled."""
    U, Nn, A = cfg["promote"]
    for p in props.values():
        if not isinstance(p["notes"], int):
            p["where"] = sorted(p["areas"])[:4]  # the review is told which areas, not only how many
            p["notes"], p["areas"] = len(p["notes"]), len(p["areas"])
    kept = cfg.get("kept") or {}
    over = [p for p in props.values() if p["uses"] >= U and p["notes"] >= Nn and p["areas"] >= A
            and p["uses"] >= 2 * kept.get(fold(p["type"]), 0)]
    below = sorted((p for p in props.values() if p not in over), key=lambda p: (-p["uses"], p["type"]))
    over.sort(key=lambda p: (-p["uses"], p["type"]))
    full = n_types >= cfg["budget"]
    proposed = [] if full else over  # a full budget offers nothing: a person merges or demotes a type first
    checks = [("C7", f"{noun} {p['type']} ×{p['uses']} ({p['notes']} notes, {p['areas']} areas) awaits review") for p in proposed]
    if full and over:
        checks.append(("C7", f"{'type ' if noun != 'label' else ''}vocabulary budget full ({n_types}/{cfg['budget']} types): "
                       + ", ".join(f"{p['type']} ×{p['uses']}" for p in over[:5]) + f" wait as {noun}s until a type is merged or demoted"))
    if below:
        checks.append(("C7", f"{len(below)} {noun}s below the review bar ({U} uses, {Nn} notes, {A} areas), shown as {shown}: "
                       + ", ".join(f"{p['type']} ×{p['uses']}" for p in below[:5]) + (" …" if len(below) > 5 else "")))
    demote = []
    for T, d in cfg["proposed"].items():
        try:
            age = (now.date() - dt.date.fromisoformat(d)).days
        except ValueError:
            continue
        u = usage.get(T, {"uses": 0, "notes": set(), "areas": set()})
        if age >= cfg["probation"] and not (u["uses"] >= U and len(u["notes"]) >= Nn and len(u["areas"]) >= A):
            demote.append(T)
    return proposed, below, demote, checks


def word_lines(ps):
    """The review's evidence for words over a bar, the same for every list: uses, notes, the areas by name, examples."""
    return "\n".join(f"- {p['type']}: {p['uses']} uses, {p['notes']} notes, {p['areas']} area{'s' * (p['areas'] != 1)}"
                     + (f" ({', '.join(a or '(root)' for a in p['where'])})" if p.get("where") else "") + "; "
                     + "; ".join(f'"{x}"' for x in p["examples"]) for p in ps) or "none"


def apply_terms(text, answers, offered, now, packs=None, reverse=False, stats=None, defaults=None):
    """A review's answers about one vocabulary's offered words, as the code admits them, the same for every
    vocabulary: `alias T` (or `alias ~T` where a link may read the other way) onto a known term; `new: <what it means,
    and how it differs from the closest term> | family: F` for a word that is not a term yet, within the budget,
    marked (proposed <date>); `label` keeps it a plain word, remembered with its uses so that it is not asked again
    until they double; `drop` for a word that is never a term. An answer about a word that was not offered changes
    nothing. -> the file's new text."""
    terms, alias_all = parse_edges(text, packs)[:2]
    budget = edges_cfg(text, defaults)["budget"]  # the list's own budget: the one its gate offered under
    offered = {fold(p["type"]): p for p in offered}
    stats = stats if stats is not None else Counter()
    for w, v in (answers or {}).items():
        w, v = fold(w), str(v).strip()
        low, day = v.lower(), now.date().isoformat()
        if w not in offered:
            continue
        tgt = v[5:].strip() if low.startswith("alias") else ""
        if tgt and fold(tgt.lstrip("~")) in terms:
            text = edit_edges(text, "alias", ("~" if reverse and tgt.startswith("~") else "") + w, fold(tgt.lstrip("~")))
            stats["mapped"] += 1
        elif low == "drop":
            text = edit_edges(text, "drop", w)
            stats["mapped"] += 1
        elif low.startswith("new"):                       # the code decides: a definition, not a known term, room
            definition = v.split(":", 1)[1].strip() if ":" in v else ""
            if definition and w not in terms and w not in alias_all and len(terms) < budget:
                text = edit_edges(text, "new", w, definition, date=day)
                terms[w] = {"def": definition, "aka": []}
                stats["new"] += 1
            else:
                stats["refused"] += 1
        elif low.startswith("label"):
            text = edit_edges(text, "keep", w, str(offered[w]["uses"]), date=day)
            stats["kept"] += 1
    return text


def lineage_as_read(root, notes, aux, edges, ents, cmap, own):
    """Lineage that a note states only in its prose, as its keeper read it: the `built_on` and `replaces` items of a
    reading, each with the note's own words. What an item names is looked up as a note (a path, or an id, in the
    note's own folder first), then through the things' names (the home note of the thing, or for a thing with no
    note of its own name the one note of the folder whose title names it). It becomes a `from` or
    `supersedes` edge marked `by: "reading"`; a line of frontmatter or of CONFLICTS.md that already says it, or says
    otherwise (`compatible: a / b`, the reverse replacement), wins. A replacement is not taken from a note older than
    the one it names, nor from a note of another family unless KINDS.md says that kind replaces it (`replaces:`), nor
    from a note of another kind when a note of the replaced note's own kind says it too. -> (notes, edges, counts); the inputs are not
    changed, because the note half of a graph is reused across rebuilds."""
    if not any((aux[rel]["x"] or {}).get(f) for rel in notes for f in ("built_on", "replaces")):
        return notes, edges, {}, []
    cf = Path(root) / "CONFLICTS.md"
    compat = parse_conflicts(read(cf))[1] if cf.exists() else set()
    notes, edges, st = dict(notes), list(edges), Counter()
    have = {(e["src"], e["dst"], e["rel"]) for e in edges}
    by_stem = defaultdict(list)
    for q, n in notes.items():
        by_stem[fold(n["id"])].append(q)

    def direct(what, src):
        w = what[:-3] if what.endswith(".md") else what
        for c in (posixpath.normpath(posixpath.join(posixpath.dirname(src), w)) + ".md", posixpath.normpath(w) + ".md"):
            if c in notes:
                return c
        c = by_stem.get(fold(posixpath.basename(w)), [])
        mine = [q for q in c if area_of(q) == area_of(src)]
        return (mine or c)[0] if len(mine) == 1 or len(c) == 1 else None

    def named(quote, src, taken):
        """An item no note answers to, whose own words name one note by its path or its id that no other item of the
        note took: that note ("Replaces glossary/brier.", which a keeper wrote down as the thing `glossary-brier`).
        Only a word that is written like a path or an id is looked up, never a plain word of the sentence."""
        c = set()
        for t in quote.split():
            t = t.strip("`'\"«»()[]{},;:.!?")
            if t and re.search(r"[/\d_-]", t):
                c.add(direct(t, src))
        c -= {None, src} | taken
        return next(iter(c)) if len(c) == 1 else None

    def note_of(what, src):
        c = direct(what, src)
        if c:
            return c
        e = cmap.get(fold(own(src, what)))
        if not e or e not in ents:
            return None
        if ents[e]["home"]:
            return ents[e]["home"]
        # a thing with no note of its own name (the table `callcenter.calls`, whose note is ds-cr-calls): the one
        # note of this folder that names it on its `# ` line is the note about it
        titled = [m_["path"] for m_ in ents[e]["mentions"] if area_of(m_["path"]) == area_of(src)
                  and m_["path"] in notes and notes[m_["path"]]["line"] in m_["lines"]]
        return titled[0] if len(titled) == 1 else None

    promoted, claims, left = set(), [], []
    for rel in sorted(notes):
        x = aux[rel]["x"] or {}
        for field, kind in (("built_on", "from"), ("replaces", "supersedes")):
            found = [note_of(b["what"], rel) for b in x.get(field) or []]
            for k, b in enumerate(x.get(field) or []):
                dst = found[k] = found[k] or named(b["quote"], rel, set(found))
                if not dst or dst == rel:
                    st["lineage_read_unplaced"] += 1
                    if not dst:
                        left.append({"note": rel, "field": field, "i": k, "what": b["what"], "quote": b["quote"], "asked": bool(b.get("asked"))})
                elif (rel, dst, kind) in have:
                    st["lineage_read_already_written"] += 1
                elif kind == "from":
                    have.add((rel, dst, kind))
                    promoted.add((rel, dst))
                    edges.append({"src": rel, "dst": dst, "rel": kind, "by": "reading"})
                    st["lineage_read"] += 1
                elif frozenset((rel, dst)) in compat or (dst, rel, "supersedes") in have:
                    pass  # a person's line, or a line of frontmatter, says otherwise
                elif notes[rel]["updated"] < notes[dst]["updated"]:
                    st["lineage_read_older"] += 1  # a note does not replace a newer one: "Superseded by X", read the wrong way round
                else:
                    claims.append((rel, dst))
    # Who replaces a note, when more than one note says it does. Measured on the worn bank (RESULTS phase S): a
    # decision that says "v3 replaces v2" is read as replacing the model v2, which the model v3 already says it does
    # (14 such, all wrong), while a correction that replaces a glossary term has no rival of the term's kind (34, all
    # right). So a note of the replaced note's own kind is believed before a note of another kind, and two notes that
    # each claim to replace the other are believed neither.
    fam = lambda q: family(notes[q]["kind"])  # noqa: E731

    def may_replace(src, dst):  # its own family, or a kind or family its KINDS.md line names under `replaces:`
        allow = KIND_REPLACES.get(notes[src]["kind"], set()) | KIND_REPLACES.get(fam(src), set())
        return fam(src) == fam(dst) or notes[dst]["kind"] in allow or fam(dst) in allow
    said = defaultdict(set)
    for s_, d, r in have:
        if r == "supersedes":
            said[d].add(s_)
    for src, dst in claims:
        said[dst].add(src)
    pairs = set(claims)
    for src, dst in sorted(claims):
        if (dst, src) in pairs:
            st["lineage_read_both_ways"] += 1
        elif not may_replace(src, dst):  # "pbs-gmm-v3 replaces the kmeans tables", in a decision: no decision replaces a model
            st["lineage_read_other_family"] += 1
        elif fam(src) != fam(dst) and any(fam(q) == fam(dst) for q in said[dst]):
            st["lineage_read_other_kind"] += 1
        else:
            have.add((src, dst, "supersedes"))
            promoted.add((src, dst))
            edges.append({"src": src, "dst": dst, "rel": "supersedes", "by": "reading"})
            st["lineage_read"] += 1
            notes[dst] = {**notes[dst], "superseded_by": notes[dst]["superseded_by"] + [src]}
    edges = [e for e in edges if not (e["rel"] == "refs" and (e["src"], e["dst"]) in promoted)]  # a mention that is lineage is said once
    return notes, edges, dict(st), left


def build(root, man, cur, former, et, at, xs=None, now=None, facts=None, base=None):
    """The graph = union of current notes' cached subgraphs, renamed by EDGES.md and ALIASES.md. `base` reuses the
    note half (notes_part) when only the vocabulary changed."""
    now = now or dt.datetime.now()
    load_domain(root)
    types, alias, drop, _, bad_e, e_extra = parse_edges(et)
    alines, nots, bad_a = parse_aliases(at)
    kt, tt = domain_texts(root)
    ttypes, talias, tdrop, _, bad_t, t_extra = parse_edges(tt, TYPE_PACKS)
    checks = [("C8", f"EDGES.md:{i}: {s}") for i, s in bad_e] + [("C8", f"ALIASES.md:{i}: {s}") for i, s in bad_a]
    checks += [("C8", f"TYPES.md:{i}: {s}") for i, s in bad_t] + [("C8", f"KINDS.md:{i}: {s}") for i, s in parse_kinds(kt)["bad"]]
    base = base or notes_part(root, man, cur, former, xs, facts)
    notes, aux, edges = base["notes"], base["aux"], base["edges"]
    checks += base["checks"]

    # an origin's things are its own: `policy-kb:auc` is not the host's `auc` until a line of ALIASES.md joins them
    own = lambda rel, i: f"{origin_of(rel)}:{i}" if origin_of(rel) else i  # noqa: E731
    occ, tprops = canon_occ(((rel, {**e, "id": own(rel, e["id"])} if origin_of(rel) else e) for rel in notes if aux[rel]["x"]
                             for e in aux[rel]["x"].get("entities", [])), talias, tdrop)
    homes = defaultdict(list)  # a note whose slug is an entity's id is that entity's home
    for rel, n in notes.items():
        if n["project"] != "log":
            homes[fold(own(rel, n["id"]))].append(rel)
    for o in ORIGINS:  # an origin's own ALIASES.md speaks of its own things
        af = root / o / "ALIASES.md"
        ol, on, _ = parse_aliases(read(af)) if af.exists() else ([], set(), [])
        alines = alines + [[f"{o}:{i}" for i in ids] for ids in ol]
        nots = nots | {frozenset(fold(f"{o}:{x}") for x in pair) for pair in on}
    linked = read_links((own(rel, r["s"]), own(rel, r["o"])) for rel in notes if aux[rel]["x"]
                        for r in aux[rel]["x"].get("relations", []))
    dedup = Counter()
    ents, cmap, gkeys = merge_entities(occ, alines, nots, homes, dedup, linked)
    notes, edges, read_stats, unplaced = lineage_as_read(root, notes, aux, edges, ents, cmap, own)
    dedup.update(read_stats)
    checks += [("C18", f"{u['note']}: says it {'builds on' if u['field'] == 'built_on' else 'replaces'} {u['what']!r} («{u['quote'][:70]}») and no "
                "note answers to that name; a `from:` or `supersedes:` line in the note settles it") for u in unplaced]
    tcfg = edges_cfg(tt)
    tusage = {}  # thing types in use, for the probation of proposed types
    for e in ents.values():
        u = tusage.setdefault(e["type"], {"uses": 0, "notes": set(), "areas": set()})
        u["uses"] += sum(len(m["lines"]) for m in e["mentions"])
        u["notes"] |= {m["path"] for m in e["mentions"]}
        u["areas"] |= {area_of(m["path"]) for m in e["mentions"]}
    proposed_t, tbelow, tdemote, tchecks = vocab_gate(tprops, tcfg, len(ttypes), tusage, now, "type word", "other/<word>")
    checks += tchecks
    cfg = edges_cfg(et)
    U, Nn, A = cfg["promote"]
    rels, props, selfl = {}, {}, defaultdict(dict)
    for rel in notes:
        for r in (aux[rel]["x"] or {}).get("relations", []):
            s, o = cmap.get(fold(own(rel, r["s"]))), cmap.get(fold(own(rel, r["o"])))
            if not s or not o:
                continue
            t = fold(r["type"]).lstrip("~")
            lbl = fold(r.get("label") or r["type"]).lstrip("~") or t  # extractions before labels: the type is the label
            key = t if t in alias else lbl if lbl in alias else None
            if key is None and (t in drop or lbl in drop):
                continue
            if key is not None:
                T, rev = alias[key]
            else:  # constrained open: a link outside the vocabulary keeps its label, shown as other/<label>
                T, rev = f"other/{lbl}", False
                p = props.setdefault(lbl, {"type": lbl, "uses": 0, "notes": set(), "areas": set(), "examples": []})
                p["uses"] += 1
                p["notes"].add(rel)
                p["areas"].add(area_of(rel))
                if len(p["examples"]) < 3:
                    p["examples"].append(f"{s} — {o}: {r['quote']}")
            s, o = (o, s) if rev else (s, o)
            if s == o:
                if frozenset((fold(own(rel, r["s"])), fold(own(rel, r["o"])))) in linked:  # two names one line joins
                    selfl[s].setdefault(tuple(sorted((r["s"], r["o"]), key=fold)), []).append(f"{rel}:{r['line']}")
                continue
            rec = rels.setdefault((s, T, o), {"s": s, "type": T, "o": o, "evidence": []})
            ev = f"{rel}:{r['line']}"
            if ev not in rec["evidence"]:
                rec["evidence"].append(ev)
    for e in ents.values():
        best = None
        for m in e["mentions"]:
            n = notes[m["path"]]
            if n["superseded_by"]:
                continue
            # equal notes: the first by path. Not the newest file: git keeps no modification times, so on two clones of
            # the same notes that picked 19 of the bank's 1,325 headlines differently (RESULTS phase J)
            key = (n["line"] in m["lines"], n["kind"] in ("finding", "decision"), n["updated"])
            if best is None or key > best[0] or (key == best[0] and m["path"] < best[1]):
                best = (key, m["path"])
        e["headline"] = best[1] if best else None
    for c, prs in sorted(selfl.items()):
        for (a, b), evs in sorted(prs.items()):
            checks.append(("C19", f"{evs[0]}{f' (+{len(evs) - 1})' if len(evs) > 1 else ''}: links {a!r} and {b!r}, which ALIASES.md "
                           f"joins as {c}; two things a note links are two things: if they are, take {b if fold(b) != fold(c) else a} "
                           f"off that line and add `not: {a} / {b}`"))
    clinked = {frozenset((s_, o_)) for s_, _, o_ in rels}
    seen = set(man.get("seen", []))
    pairs = candidates(ents, [c for c in ents if fold(c) not in seen], gkeys, nots, clinked)
    for a, b in man.get("queue", []):
        a, b = cmap.get(fold(a)), cmap.get(fold(b))
        if a and b and a != b and frozenset((a, b)) not in clinked and not decided(a, b, gkeys, nots):
            pairs.add(tuple(sorted((a, b), key=fold)))
    pairs = sorted(pairs, key=lambda p: (fold(p[0]), fold(p[1])))
    usage = {}  # probation: a proposed type still under the bar after its probation is demoted to a label (0 calls)
    for (s, T, o), rec in rels.items():
        u = usage.setdefault(T, {"uses": 0, "notes": set(), "areas": set()})
        u["uses"] += len(rec["evidence"])
        u["notes"] |= {ev.rsplit(":", 1)[0] for ev in rec["evidence"]}
        u["areas"] |= {area_of(ev) for ev in rec["evidence"]}
    proposed, below, demote, vchecks = vocab_gate(props, cfg, len(types), usage, now, "label", "other/<label>")
    checks += vchecks
    n_types = len(types)
    checks += [("C7", f"entities {a} / {b} await review") for a, b in pairs]
    checks += shape_checks(ents, rels, {**SEED_SHAPES, **e_extra["shape"]}, t_extra["family"])
    was = man.get("registry") or {}  # a type removed by hand is never lost: its readings stay as other/<word>; say so
    for name, had, have, als, used in (("EDGES.md", was.get("edges", []), types, alias, {k for (_, k, _) in rels} | {p for p in props}),
                                        ("TYPES.md", was.get("types", []), ttypes, talias, {e["type"] for e in ents.values()} | set(tprops))):
        for T in had:
            if T not in have and T not in als and (T in used or f"other/{T}" in used):
                checks.append(("C13", f"{name}: type {T} was removed while readings still use it; they now show as other/{T} — "
                               f"merge it instead (add {T} to another type's aka) or restore the line"))
    cf = root / "CONFLICTS.md"
    _, compat, unsure, _ = parse_conflicts(read(cf)) if cf.exists() else ([], set(), set(), [])
    conflicts = [c for c in conflict_candidates(notes, edges, unsure) if frozenset((c["a"], c["b"])) not in compat]
    wanted = {rel: aux[rel]["pointers"] for rel in notes if aux[rel].get("pointers")}  # pointers into the project's files
    ptr, pchecks = pointer_states(root, wanted, man.get("pointers") or {}) if wanted else ({}, [])
    checks += pchecks
    # tags and kinds through the same gate as relation labels and type words: one rule for every vocabulary
    tags, tchecks, gwords, gusage = note_tags(aux, root, notes)
    checks += tchecks
    gtext = tags_text(root)
    gcfg = edges_cfg(gtext, TAG_DEFAULTS)
    proposed_g, gbelow, gdemote, gchecks = vocab_gate(gwords, gcfg, len(parse_edges(gtext, {})[0]), gusage, now, "tag word", "a word")
    checks += gchecks
    kwords, kusage = {}, {}
    for rel, n in notes.items():
        u = kusage.setdefault(n["kind"], {"uses": 0, "notes": set(), "areas": set()})
        u["uses"] += 1
        u["notes"].add(rel)
        u["areas"].add(area_of(rel))
        w = fold((aux[rel]["x"] or {}).get("kind_word") or "")
        if n["kind"] == "note" and w and w not in KINDS and w not in KIND_ALIAS and w not in KIND_DROP:
            p = kwords.setdefault(w, {"type": w, "uses": 0, "notes": set(), "areas": set(), "examples": []})
            p["uses"] += 1
            p["notes"].add(rel)
            p["areas"].add(area_of(rel))
            if len(p["examples"]) < 3:
                p["examples"].append(f"{n['id']}: {(n['title'] or '')[:90]}")
    kcfg = edges_cfg(kt, KIND_DEFAULTS)
    proposed_k, kbelow, kdemote, kchecks = vocab_gate(kwords, kcfg, len(KINDS), kusage, now, "kind word", "note")
    checks += kchecks
    checks += [("C10", f"conflict pending: {c['a']} / {c['b']} — both live, share: {', '.join(c['shared'][:3])}"
                + (" · reviewer unsure, a person decides" if c["unsure"] else "")) for c in conflicts]
    return {"schema": SCHEMA, "v": V, "built": now.strftime("%Y-%m-%dT%H:%M"),
            "notes": [notes[p] for p in sorted(notes)],
            "entities": [ents[c] for c in sorted(ents, key=fold)],
            "relations": sorted(rels.values(), key=lambda r: (fold(r["s"]), r["type"], fold(r["o"]))),
            "edges": edges, "proposed": proposed, "review": [{"a": a, "b": b} for a, b in pairs], "conflicts": conflicts,
            "vocab": {"types": n_types, "budget": cfg["budget"], "promote": [U, Nn, A], "probation": cfg["probation"],
                      "labels": len(props), "below": len(below), "demote": sorted(demote)},
            "proposed_types": proposed_t,
            "tvocab": {"types": len(ttypes), "budget": tcfg["budget"], "promote": list(tcfg["promote"]), "probation": tcfg["probation"],
                       "labels": len(tprops), "below": len(tbelow), "demote": sorted(tdemote)},
            "proposed_kinds": proposed_k,
            "kvocab": {"types": len(KINDS), "budget": kcfg["budget"], "promote": list(kcfg["promote"]), "probation": kcfg["probation"],
                       "labels": len(kwords), "below": len(kbelow), "demote": sorted(kdemote)},
            "proposed_tags": proposed_g,
            "gvocab": {"types": len(parse_edges(gtext, {})[0]), "budget": gcfg["budget"], "promote": list(gcfg["promote"]),
                       "probation": gcfg["probation"], "labels": len(gwords), "below": len(gbelow), "demote": sorted(gdemote)},
            "dedup": dict(dedup), "dropped": base.get("dropped", []), "pointers": ptr, "tags": tags, "unplaced": unplaced,
            "checks": [{"code": c, "msg": m} for c, m in sorted(checks, key=lambda z: z[0])]}


def vocab_texts(root):
    e, a = root / "EDGES.md", root / "ALIASES.md"
    return (read(e) if e.exists() else EDGES_SEED), (read(a) if a.exists() else ALIASES_HEAD)


def validate(g, types=None):
    """The graph against CONTRACT.md §1 -> a list of problems (empty when it conforms). `types`: the vocabulary's
    type names, when known, to check relation types."""
    bad = []
    for k, t in (("schema", int), ("v", str), ("built", str), ("notes", list), ("entities", list), ("relations", list),
                 ("edges", list), ("proposed", list), ("review", list), ("conflicts", list), ("vocab", dict), ("checks", list)):
        if not isinstance(g.get(k), t):
            bad.append(f"{k}: missing or not {t.__name__}")
    if bad:
        return bad
    if g["schema"] != SCHEMA:
        bad.append(f"schema {g['schema']} is not {SCHEMA}")
    paths = {n["path"] for n in g["notes"]}
    for n in g["notes"]:
        for k in ("path", "id", "project", "title", "line", "kind", "updated", "superseded_by", "sha", "indexed"):
            if k not in n:
                bad.append(f"note {n.get('path')}: no {k}")
        if n.get("id") != posixpath.basename(n["path"])[:-3]:
            bad.append(f"note {n['path']}: id {n.get('id')!r} is not the filename")
        if n.get("project") != (area_of(n["path"])):
            bad.append(f"note {n['path']}: project {n.get('project')!r} is not the first path segment")
        if not re.fullmatch(r"\d{4}-\d\d-\d\d", str(n.get("updated", ""))):
            bad.append(f"note {n['path']}: updated {n.get('updated')!r} is not a date")
        if n.get("kind") != str(n.get("kind", "")).lower():
            bad.append(f"note {n['path']}: kind not lowercase")
        bad += [f"note {n['path']}: superseded_by {s} is not a note" for s in n.get("superseded_by", []) if s not in paths]
    sup_edges = {(e["src"], e["dst"]) for e in g["edges"] if e.get("rel") == "supersedes"}
    for n in g["notes"]:
        bad += [f"note {n['path']}: superseded_by {s} without a supersedes edge" for s in n.get("superseded_by", []) if (s, n["path"]) not in sup_edges]
    seen = set()
    for e in g["edges"]:
        key = (e.get("src"), e.get("dst"), e.get("rel"))
        if e.get("rel") not in ("from", "supersedes", "refs") or e.get("src") not in paths or e.get("dst") not in paths:
            bad.append(f"edge {key}: bad rel or unknown note")
        if key in seen:
            bad.append(f"edge {key}: duplicate")
        seen.add(key)
    eids = {e["id"] for e in g["entities"]}
    for e in g["entities"]:
        for k in ("id", "type", "home", "aka", "names", "headline", "mentions"):
            if k not in e:
                bad.append(f"entity {e.get('id')}: no {k}")
        for p in (e.get("home"), e.get("headline")):
            if p is not None and p not in paths:
                bad.append(f"entity {e['id']}: {p} is not a note")
        bad += [f"entity {e['id']}: mention {m.get('path')} is not a note" for m in e.get("mentions", []) if m.get("path") not in paths]
    for r in g["relations"]:
        if r.get("s") not in eids or r.get("o") not in eids:
            bad.append(f"relation {r.get('s')} {r.get('type')} {r.get('o')}: unknown entity")
        t = str(r.get("type", ""))
        if types is not None and not (t in types or t.startswith("other/")):
            bad.append(f"relation {r['s']} {t} {r['o']}: type is not in the vocabulary nor other/<label>")
        for ev in r.get("evidence", []):
            m = re.fullmatch(r"(.+):(\d+)", ev)
            if not m or m.group(1) not in paths or int(m.group(2)) < 1:
                bad.append(f"relation {r['s']} {t} {r['o']}: evidence {ev!r} is not path:line of a note")
    bad += [f"conflict {c.get('a')} / {c.get('b')}: unknown note" for c in g["conflicts"] if c.get("a") not in paths or c.get("b") not in paths]
    bad += [f"check {c.get('code')}: unknown code" for c in g["checks"] if not re.fullmatch(r"C(?:[1-9]|1[0-8])", str(c.get("code", "")))]
    bad += [f"pointers of {p}: not a note" for p in g.get("pointers", {}) if p not in paths]  # optional: pointers into files
    bad += [f"tag {t}: {p} is not a note" for t, ps in g.get("tags", {}).items() for p in ps if p not in paths]  # optional: tags
    bad += [f"unplaced {u.get('note')}: not a note" for u in g.get("unplaced", []) if u.get("note") not in paths]  # optional
    for d in g.get("dropped", []):  # optional: what `drop` recorded and what it means for the notes that are left
        if not isinstance(d.get("path"), str) or d["path"] in paths:
            bad.append(f"dropped {d.get('path')!r}: not a path, or a note that exists")
        bad += [f"dropped {d.get('path')}: {k} {x} is not a note" for k in ("built_on_by", "left_newest") for x in d.get(k, []) if x not in paths]
    if [c["code"] for c in g["checks"]] != sorted(c["code"] for c in g["checks"]):
        bad.append("checks are not sorted by code")
    return bad


def conflicts_text(root):
    cf = root / "CONFLICTS.md"
    return read(cf) if cf.exists() else ""


TAGS_HEAD = """# TAGS — themes that notes across the memory share and that their folder, kind and things do not already say. One
# line per tag: `- tag: what it means | aka: other words | family: parent`. Constrained open, like EDGES.md: a note's
# `tags:` and its keeper's reading use these tags or their aliases; any other word is kept as a word, and once it is
# over the bar the review answers alias, new (marked proposed: demoted after the probation if still under the bar),
# label (kept a word, asked again only once its uses double) or drop. Edit freely: a hand-written line is permanent.
promote: 3 uses, 3 notes, 1 area
budget: 30
probation: 60 days
"""
TAG_DEFAULTS = {"promote": (3, 3, 1), "budget": 30, "probation": 60}    # a tag is a theme: fewer notes, any one area
KIND_DEFAULTS = {"promote": (5, 5, 2), "budget": 40, "probation": 60}


def tags_text(root):
    """TAGS.md as it stands, or its head alone when the memory has none yet (no seed: a tag belongs to one base)."""
    f = Path(root) / "TAGS.md"
    return read(f) if f.exists() else TAGS_HEAD


def tags_registry(root):
    """TAGS.md: `- tag: what it means | aka: other spellings` -> ({tag: definition}, {folded spelling: tag}). A tag is
    a word of this file; there is no seed, because a tag belongs to one base."""
    f = Path(root) / "TAGS.md"
    types, alias = parse_edges(read(f), {})[:2] if f.exists() else ({}, {})
    return {t: d["def"] for t, d in types.items()}, {k: v[0] for k, v in alias.items()}


TAGS_RULE = ("Last, tags: [] for most notes; at most 3 themes that notes in other folders share and that the note's\n"
             "folder, kind and things do not say (a regulation, a risk), as a TAGS tag, or other: <word>. ")


def tag_fill(root):
    """What a reading prompt says about tags: nothing while TAGS.md lists no tag, else the rule, the list and a `tags`
    key last in the reply. On the fixture with Haiku, tags asked first in the reply cost a third of the links (66 and
    74 against 102 and 104); asked last the readings stayed within run-to-run noise (91 and 99; 89 to 104 for one
    prompt), and asked with an empty list they gave scattered one-off words. So a memory that lists no tag is not
    asked: its tags start from the `tags:` lines writers give, which the gate counts like any word."""
    lines = parse_edges(tags_text(root), {})[3]
    if not lines:
        return {"tags_key": "", "tags_rule": "", "tags": ""}
    return {"tags_key": ', "tags": []', "tags_rule": TAGS_RULE, "tags": "TAGS:\n" + "\n".join(lines) + "\n"}


def note_tags(aux, root, notes=None):
    """The notes of each tag -> ({tag: [paths]}, C17 checks, {word: its uses, for the gate}, {tag: its uses, for the
    probation}). Tags come two ways, both read through TAGS.md as it stands: written (a note's `tags:` line) and read
    (its keeper's reading). A written word that TAGS.md does not list is kept under its own spelling and reported
    (C17); every word outside TAGS.md, written or read, is counted, and the gate offers it to the review once it is
    common (the same gate as every vocabulary's)."""
    terms, alias, drop = parse_edges(tags_text(root), {})[:3]
    out, unlisted, words, usage = defaultdict(set), defaultdict(set), {}, {}
    for rel in sorted(aux):
        written = [fold(str(w).lstrip("#")) for w in fm_list(aux[rel]["fm"].get("tags"))]
        read_ = [fold(re.sub(r"^other\s*[:/]\s*", "", str(w)).lstrip("#")) for w in ((aux[rel]["x"] or {}).get("tags") or [])]
        for k, how in [(k, "written") for k in written] + [(k, "read") for k in read_]:
            if not k or k in drop:
                continue
            t = alias.get(k, (None,))[0]
            if t:
                out[t].add(rel)
                u = usage.setdefault(t, {"uses": 0, "notes": set(), "areas": set()})
                if rel not in u["notes"]:
                    u["uses"] += 1
                    u["notes"].add(rel)
                    u["areas"].add(area_of(rel))
                continue
            if how == "written":
                unlisted[k].add(rel)
            p = words.setdefault(k, {"type": k, "uses": 0, "notes": set(), "areas": set(), "examples": []})
            if rel not in p["notes"]:
                p["uses"] += 1
                p["notes"].add(rel)
                p["areas"].add(area_of(rel))
                if len(p["examples"]) < 3:
                    title = ((notes or {}).get(rel) or {}).get("title") or posixpath.basename(rel)[:-3]
                    p["examples"].append(f"{posixpath.basename(rel)[:-3]}: {title[:90]}")
    checks = [("C17", f"tag `{k}` on {len(ps)} note{'s' * (len(ps) != 1)} ({posixpath.basename(sorted(ps)[0])[:-3]}{', …' if len(ps) > 1 else ''}) "
               f"is not in TAGS.md: add `- {k}: what it means`, or name the tag it is another spelling of") for k, ps in sorted(unlisted.items())]
    return {t: sorted(ps) for t, ps in sorted({**unlisted, **out}.items())}, checks, words, usage


def shape_text(root):
    """CONFLICTS.md, and the files of each origin that shape the graph: a change to any of them is a change to dream."""
    out = conflicts_text(root)
    tf = Path(root) / "TAGS.md"
    out += f"\n<TAGS.md>\n{read(tf)}" if tf.exists() else ""
    for o in sorted(load_origins(root)):
        for name in ("ORIGIN.md", "CONFLICTS.md", "ALIASES.md"):
            f = root / o / name
            out += f"\n<{o}/{name}>\n{read(f)}" if f.exists() else ""
    return out


def vsig(et, at, ct="", kt="", tt=""):
    """Signature of the user-owned files that shape the graph without a model: EDGES.md, ALIASES.md, CONFLICTS.md,
    KINDS.md, TYPES.md."""
    return hashlib.sha256("\0".join((et, at, ct, kt, tt)).encode()).hexdigest()[:16]


def load(root):
    """Freshness: reuse graph.json when nothing changed since the last dream, else re-merge in memory."""
    man = rd(root / "_dream" / "manifest.json", {}) or {}
    cur, former, _, _ = scan(root, man)
    et, at = vocab_texts(root)
    same = {p: f["sha"] for p, f in cur.items()} == {p: f["sha"] for p, f in man.get("files", {}).items()}
    if same and man.get("vsig") == vsig(et, at, shape_text(root), *domain_texts(root)) and (man.get("code") == CODE or len(cur) > WIDE):
        g = rd(root / "_dream" / "graph.json") or read_index(root / "_dream")
        if g and g.get("v") == V:
            g.setdefault("dropped", man.get("dropped", []))  # index.db keeps rows; the manifest keeps what was dropped
            g.setdefault("pointers", man.get("pointers", {}))  # … and what the notes point at
            return g, former
    elif len(cur) > WIDE:  # rebuilding takes minutes here: patch the last graph for what changed since the dream
        g = rd(root / "_dream" / "graph.json") or read_index(root / "_dream")
        if g and g.get("v") == V:
            g.setdefault("dropped", man.get("dropped", []))
            g.setdefault("pointers", man.get("pointers", {}))
            return patch(root, g, man, cur), former
    return build(root, man, cur, former, et, at), former


def fresh_note(root, rel, cur, stems):
    """A note changed since the last dream: its record and its from:/supersedes: edges, from its text alone."""
    fm, title, tline, _ = parse_note(read(root / rel))
    up = fm.get("updated") or fm.get("modified") or ""
    proj = area_of(rel)
    n = {"path": rel, "id": posixpath.basename(rel)[:-3], "project": proj, "title": title, "line": tline,
         "kind": kind_of(rel, fm.get("type")), "superseded_by": [],
         "updated": up[:10] if re.match(r"\d{4}-\d\d-\d\d", up) else
         dt.date.fromtimestamp(cur[rel]["mtime"] / 1e9).isoformat(), "sha": cur[rel]["sha"][:12], "indexed": False}
    edges = []
    for kind in ("from", "supersedes"):
        for v in fm_list(fm.get(kind)):
            c = stems.get(posixpath.basename(re.sub(r"^\[\[|\]\]$|\.md$", "", v.strip())), [])
            mine = [x for x in c if area_of(x) == area_of(rel)]
            if (mine or c) and sorted(mine or c)[0] != rel:
                edges.append({"src": rel, "dst": sorted(mine or c)[0], "rel": kind})
    return n, edges


def patch(root, g, man, cur):
    """The last dream's graph with changed and new notes re-read (title, kind, date, from:/supersedes:) and
    deleted ones gone. Their entities wait for the next dream; grep reads their text as usual."""
    old = {p: f["sha"] for p, f in man.get("files", {}).items()}
    notes = {n["path"]: n for n in g["notes"] if n["path"] in cur}
    changed = [p for p in cur if old.get(p) != cur[p]["sha"]]
    stems = defaultdict(list)
    for p in cur:
        stems[posixpath.basename(p)[:-3]].append(p)
    ch = set(changed)
    edges = [e for e in g["edges"] if e["src"] not in ch and e["src"] in notes and e["dst"] in notes]
    for rel in changed:
        notes[rel], es = fresh_note(root, rel, cur, stems)
        edges += es
    for n in notes.values():
        n["superseded_by"] = []
    for e in edges:
        if e["rel"] == "supersedes":
            notes[e["dst"]]["superseded_by"].append(e["src"])
    if len(notes) < len(g["notes"]):  # something was deleted
        for e in g["entities"]:
            e["mentions"] = [m for m in e["mentions"] if m["path"] in notes]
    dropped = [{**d, **{k: [x for x in d.get(k, []) if x in notes] for k in ("built_on_by", "left_newest")}} for d in g.get("dropped", [])]
    return {**g, "notes": [notes[p] for p in sorted(notes)], "edges": edges, "dropped": dropped}


# ---------- dream caches and the index ----------

def extraction_files(dd):
    """{sha12: mtime_ns} of the extraction files in _dream/notes/."""
    if not (dd / "notes").is_dir():
        return {}
    with os.scandir(dd / "notes") as it:
        return {e.name[:-5]: e.stat().st_mtime_ns for e in it if e.name.endswith(".json")}


class Store:
    """dream's caches in _dream/store.db: parsed note facts by path, extractions by content hash (the files in
    _dream/notes/ stay the source; a row is used only while its file's mtime matches)."""
    def __init__(self, dd, keep=True):
        self.dd = dd
        self.db = sqlite3.connect(dd / "store.db" if keep else ":memory:")  # a dry run writes no cache
        self.db.executescript("CREATE TABLE IF NOT EXISTS facts(path TEXT PRIMARY KEY, sha TEXT, rec TEXT);"
                              "CREATE TABLE IF NOT EXISTS x(sha TEXT PRIMARY KEY, mt INTEGER, rec TEXT);")

    def facts(self, root, cur):
        have = {p: (h, r) for p, h, r in self.db.execute("SELECT path, sha, rec FROM facts")}
        out, new = {}, []
        for rel, f in cur.items():
            h, r = have.get(rel, (None, None))
            rec = json.loads(r) if h == f["sha"] else None
            if rec is not None and rec.get("v") == FACTS_V:  # rows of an older shape are re-read once
                out[rel] = rec
            else:
                out[rel] = note_facts(read(root / rel))
                new.append((rel, f["sha"], json.dumps(out[rel])))
        with self.db:
            self.db.executemany("INSERT OR REPLACE INTO facts VALUES (?,?,?)", new)
            self.db.executemany("DELETE FROM facts WHERE path=?", [(q,) for q in have if q not in cur])
        return out

    def extractions(self, shas):
        files = extraction_files(self.dd)
        have = {h: (mt, r) for h, mt, r in self.db.execute("SELECT sha, mt, rec FROM x")}
        xs, add = {}, []
        for h in shas:
            if h not in files:
                continue
            mt, r = have.get(h, (None, None))
            x = json.loads(r) if mt == files[h] else rd(self.dd / "notes" / f"{h}.json")
            if x:
                xs[h] = x
                if mt != files[h]:
                    add.append((h, files[h], json.dumps(x)))
        with self.db:
            self.db.executemany("INSERT OR REPLACE INTO x VALUES (?,?,?)", add)
            self.db.executemany("DELETE FROM x WHERE sha=?", [(h,) for h in have if h not in xs])
        return xs

    def put(self, h, x):
        with self.db:
            self.db.execute("INSERT OR REPLACE INTO x VALUES (?,?,?)",
                            (h, (self.dd / "notes" / f"{h}.json").stat().st_mtime_ns, json.dumps(x)))


def write_index(dd, g):
    """The graph as SQLite (_dream/index.db): `ask` on a big memory reads only the rows a question needs."""
    tmp = dd / "index.db.tmp"
    if tmp.exists():
        tmp.unlink()
    db = sqlite3.connect(tmp)
    db.executescript("""PRAGMA journal_mode=OFF; PRAGMA synchronous=OFF;
        CREATE TABLE meta(k TEXT PRIMARY KEY, v TEXT);
        CREATE TABLE notes(path TEXT PRIMARY KEY, id TEXT, area TEXT, title TEXT, line INT, kind TEXT, updated TEXT,
                           sha TEXT, indexed INT, sup TEXT);
        CREATE TABLE edges(src TEXT, dst TEXT, rel TEXT);
        CREATE TABLE ents(id TEXT PRIMARY KEY, type TEXT, home TEXT, headline TEXT, aka TEXT, names TEXT);
        CREATE TABLE ment(eid TEXT, path TEXT, lines TEXT);
        CREATE TABLE names(k TEXT, eid TEXT);
        CREATE TABLE rels(s TEXT, type TEXT, o TEXT, ev TEXT);
        CREATE TABLE checks(code TEXT, msg TEXT);""")
    with db:
        db.executemany("INSERT INTO meta VALUES (?,?)", [(k, json.dumps(g.get(k))) for k in ("schema", "v", "built", "proposed", "review", "dedup", "vocab", "conflicts", "proposed_types", "tvocab")])
        db.executemany("INSERT INTO notes VALUES (?,?,?,?,?,?,?,?,?,?)",
                       ((n["path"], n["id"], n["project"], n["title"], n["line"], n["kind"], n["updated"], n["sha"],
                         int(n["indexed"]), json.dumps(n["superseded_by"])) for n in g["notes"]))
        db.executemany("INSERT INTO edges VALUES (?,?,?)", ((e["src"], e["dst"], e["rel"]) for e in g["edges"]))
        db.executemany("INSERT INTO ents VALUES (?,?,?,?,?,?)", ((e["id"], e["type"], e["home"], e["headline"],
                                                                 json.dumps(e["aka"]), json.dumps(e["names"])) for e in g["entities"]))
        db.executemany("INSERT INTO ment VALUES (?,?,?)",
                       ((e["id"], m["path"], json.dumps(m["lines"])) for e in g["entities"] for m in e["mentions"]))
        db.executemany("INSERT INTO names VALUES (?,?)", ((k, e["id"]) for e in g["entities"] for k in  # sorted: one row order per graph
                                                          sorted({fold(x) for x in [e["id"], *e["aka"], *(n["name"] for n in e["names"])] if len(x) >= 3})))
        db.executemany("INSERT INTO rels VALUES (?,?,?,?)", ((r["s"], r["type"], r["o"], json.dumps(r["evidence"])) for r in g["relations"]))
        db.executemany("INSERT INTO checks VALUES (?,?)", ((c["code"], c["msg"]) for c in g["checks"]))
    db.executescript("CREATE INDEX e_src ON edges(src); CREATE INDEX e_dst ON edges(dst); CREATE INDEX m_eid ON ment(eid);"
                     "CREATE INDEX n_k ON names(k); CREATE INDEX r_s ON rels(s); CREATE INDEX r_o ON rels(o);")
    db.close()
    tmp.replace(dd / "index.db")


def index_db(dd):
    p = dd / "index.db"
    return sqlite3.connect(f"file:{p}?mode=ro", uri=True) if p.exists() else None


def old_lineage(dd, paths):
    """Where each of these notes stood at the last dream (graph.json, or index.db on a big memory): what it had
    replaced, what replaced it, what was built on it. -> {path: {replaced, replaced_by, built_on_by}}."""
    out = {p: {"replaced": [], "replaced_by": [], "built_on_by": []} for p in paths}
    g, db = rd(dd / "graph.json"), None
    if g:
        rows = [(e["src"], e["dst"], e["rel"]) for e in g.get("edges", []) if e["src"] in out or e["dst"] in out]
    else:
        db = index_db(dd)
        rows = [r for p in (paths if db else []) for r in db.execute("SELECT src, dst, rel FROM edges WHERE src=? OR dst=?", (p, p))]
    for s, d, rel in rows:
        if rel == "supersedes" and s in out:
            out[s]["replaced"].append(d)
        if rel == "supersedes" and d in out:
            out[d]["replaced_by"].append(s)
        if rel == "from" and d in out:
            out[d]["built_on_by"].append(s)
    return {p: {k: sorted(set(v)) for k, v in r.items()} for p, r in out.items()}


def read_index(dd):
    """The whole graph back from index.db (check, viz and tests on big memories; ask reads rows instead)."""
    db = index_db(dd)
    if not db:
        return None
    meta = {k: json.loads(v) for k, v in db.execute("SELECT k, v FROM meta")}
    ment = defaultdict(list)
    for eid, p, ls in db.execute("SELECT eid, path, lines FROM ment ORDER BY rowid"):
        ment[eid].append({"path": p, "lines": json.loads(ls)})
    g = {**meta,
         "notes": [{"path": p, "id": i, "project": a, "title": t, "line": ln, "kind": k, "superseded_by": json.loads(sup),
                    "updated": u, "sha": h, "indexed": bool(x)}
                   for p, i, a, t, ln, k, u, h, x, sup in db.execute("SELECT * FROM notes ORDER BY rowid")],
         "entities": [{"id": i, "type": t, "home": h, "aka": json.loads(a), "names": json.loads(nm), "headline": hl,
                       "mentions": ment[i]} for i, t, h, hl, a, nm in db.execute("SELECT * FROM ents ORDER BY rowid")],
         "relations": [{"s": s_, "type": t, "o": o, "evidence": json.loads(ev)} for s_, t, o, ev in db.execute("SELECT * FROM rels ORDER BY rowid")],
         "edges": [{"src": a, "dst": b, "rel": r} for a, b, r in db.execute("SELECT * FROM edges ORDER BY rowid")],
         "checks": [{"code": c, "msg": m} for c, m in db.execute("SELECT * FROM checks ORDER BY rowid")]}
    db.close()
    return g


# ---------- dream ----------

NOTE_CAP = 16000  # characters of note text per prompt: every call stays small (a note is 40 lines by rule)
# Packets: the reading as fewer, larger calls in place of one call a note. The instructions and the vocabulary travel
# once a packet, a helper agent that carries 35,000 tokens of its own in every request reads a dozen notes for the
# price of one, and a keeper that sees a folder's notes together names the note a phrase means more often than one
# that sees a single note. Two limits, and the first to bind closes the packet. The notes of a packet stay under
# PACKET_TEXT characters: about a dozen short notes. Measured on Haiku 5.5 (RESULTS phase S): at two dozen notes a
# call a reading held 0.60 of the things and 0.43 of the links of the same note read alone; at a dozen, with the
# prompt that asks for each note in full, it held as many things, 0.94 of the links and more of the lineage (97%
# against 93%), for 0.6 of the price. The prompt stays under PACKET_TOKENS by the script's own count of three
# characters a token: Haiku 5.5 costs five times as much over 100,000, and its tokenizer counts about 30% more than
# the old four characters; this limit binds only when notes are long.
# $MEMORY_PACKET="tokens,characters" sets both; $MEMORY_PRICE="in,out" the $ a million tokens of the dry run.
PACKET_TOKENS, PACKET_TEXT, KNOWN_ROOM = 60000, 6000, 8000
READING_RATIO = 3.2
OUT_PER_CHAR = 3.3  # output tokens a character of note, as Haiku 5.5 wrote them in phase S with its thinking counted
#   (2.2 in packets of 24, 3.3 one note a call, 4.1 in packets of 6): the dry run's estimate of the answer
PRICE = (0.10, 0.50)  # Haiku 5.5 under 100,000 tokens a prompt


def env_numbers(name, default):
    """A comma-separated environment setting as numbers; anything unreadable leaves the default."""
    try:
        got = [float(x) for x in os.environ.get(name, "").split(",") if x.strip()]
    except ValueError:
        got = []
    return tuple(got) if len(got) == len(default) else default


def parse_packet(out, wanted):
    """A packet's answer -> {note id: reading}: every JSON object in it that names one of the notes asked for, however
    the model laid them out (a line each, an array, one object keyed by id). An answer cut off at its end loses only
    the note it was cut in."""
    got, dec = {}, json.JSONDecoder()
    for m in re.finditer(r'\{\s*"note"\s*:', out or ""):
        try:
            obj = dec.raw_decode(out, m.start())[0]
        except ValueError:
            continue
        if isinstance(obj, dict) and str(obj.get("note")) in wanted:
            got.setdefault(str(obj["note"]), obj)
    if not got:
        whole = parse_json(out) or {}
        got = {k: v for k, v in whole.items() if k in wanted and isinstance(v, dict)}
    return got


def call_model(cmd, prompt, static=0, parse=parse_json):
    """One prompt on stdin, answer on stdout; retry once when unusable. -> (obj or None, calls).
    MEMORY_STATIC_PREFIX tells a cache-aware command how many leading characters are the same for every call of this
    project (template, EDGES, KNOWN): it can place them where the model caches (tests/haiku_cmd.py does)."""
    env = {**os.environ, "MEMORY_STATIC_PREFIX": str(static)}
    for n in (1, 2):
        out = run_command(cmd, prompt, env)
        obj = parse(out) if out is not None else None
        if obj or (obj is not None and parse is parse_json):  # for one note an empty object is an answer: nothing to index
            return obj, n
    return None, 2


def run_command(cmd, prompt, env):
    """One shell command with the prompt on stdin -> its stdout, or None when it failed or ran past MEMORY_TIMEOUT.
    It runs in a process group of its own and a timeout ends the whole group. Then the pipes are closed from this
    side and only the shell is waited for: `subprocess.run(timeout=…)` kills the shell alone and goes on reading, so
    a hung grandchild that holds the pipe keeps the dream waiting for good (seen with `claude -p` calls that never
    returned, RESULTS phase S)."""
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                         env=env, start_new_session=True)
    try:
        out, _ = p.communicate(prompt, timeout=TIMEOUT)
        return out if p.returncode == 0 else None
    except subprocess.TimeoutExpired:
        for kill in (lambda: os.killpg(p.pid, signal.SIGKILL), p.kill):  # the group; where that is not allowed, the shell
            try:
                kill()
            except (OSError, AttributeError):
                pass
        for f in (p.stdin, p.stdout, p.stderr):  # not communicate(): it would read on until every holder of the pipe is gone
            try:
                f.close()
            except (OSError, ValueError):
                pass
        try:
            p.wait(timeout=10)
        except subprocess.TimeoutExpired:
            pass
        return None


class Known:
    """Entities by mention count and each project's top ones: one sort serves every prompt of a wave."""
    def __init__(self, ents, local=80):
        self.local = local
        self.by_n = sorted(ents.values(), key=lambda e: (-len(e["mentions"]), fold(e["id"])))
        self.projs = [{area_of(m["path"]) for m in e["mentions"]} for e in self.by_n]
        self.top = defaultdict(list)
        for i, ps in enumerate(self.projs):
            for p in ps:
                if len(self.top[p]) < local:
                    self.top[p].append(i)


def known_lines(ents, project, local=80, shared=20):
    """KNOWN for a prompt: this project's entities, then the most-mentioned shared ones (small prompts)."""
    kn = ents if isinstance(ents, Known) and ents.local >= local else Known(ents if isinstance(ents, dict) else
                                                                              {e["id"]: e for e in ents.by_n}, local)
    rest = []
    for i, ps in enumerate(kn.projs):
        if len(rest) >= shared:
            break
        if project not in ps:
            rest.append(i)
    es = [kn.by_n[i] for i in kn.top.get(project, [])[:local] + rest]
    return "\n".join(f"{e['id']} ({e['type']}): " + "; ".join(n["name"] for n in e["names"][:4]) for e in es) or "(none)"


class Lock:
    """_dream/lock: one dream at a time (REVIEW.md F10). A lock older than LOCK_STALE_S is taken over."""
    def __init__(self, dd):
        self.p = dd / "lock"

    def __enter__(self):
        if self.p.exists() and time.time() - self.p.stat().st_mtime < LOCK_STALE_S:
            sys.stderr.write(f"memory.py: another dream is running ({self.p}, {int(time.time() - self.p.stat().st_mtime)} s "
                             "old); wait for it, or delete the lock if it died.\n")
            sys.exit(3)
        self.p.write_text(str(os.getpid()))
        return self

    def __exit__(self, *exc):
        self.p.unlink() if self.p.exists() else None


LOCK_STALE_S = 2 * 3600


def dream(args, root):
    if args.dry_run:  # no folder made, no lock taken, no cache written
        return Dream(args, root).run()
    root.mkdir(parents=True, exist_ok=True)
    dd = root / "_dream"
    (dd / "notes").mkdir(parents=True, exist_ok=True)
    with Lock(dd):
        dream_locked(args, root)


def dream_locked(args, root):
    Dream(args, root).run()


class Dream:
    """One dream, in stages: plan (scan, caches, what to index) → index (command or file mode) → graph → demote
    (probation over) → review (labels over the bar, entity pairs, conflicts: one call, or one prompt in file mode)
    → write (viewer, index.db, digest, pending list, manifest) → report. State lives on the instance."""

    def __init__(self, args, root):
        self.args, self.root = args, root
        for name, seed in (("EDGES.md", EDGES_SEED), ("ALIASES.md", ALIASES_HEAD), ("KINDS.md", KINDS_SEED), ("TYPES.md", TYPES_SEED)):
            if not (root / name).exists() and not args.dry_run:
                wr(root / name, seed)
        load_domain(root)
        self.dd, self.now = root / "_dream", dt.datetime.now()
        self.pend = self.dd / "pending"
        self.man = rd(self.dd / "manifest.json", {}) or {}
        self.cur, self.former, self.moved, self.deleted = scan(root, self.man)
        self.cmd = args.cmd or os.environ.get("MEMORY_LLM")
        self.st = Counter()
        self.review = {"pairs": 0, "types": 0, "calls": 0, "aliases": 0, "mapped": 0, "new": 0, "refused": 0,
                       "kept": 0, "demoted": 0, "conflicts": 0, "decided": 0, "kinds": Counter(), "tags": Counter()}
        self.curate = {"folders": 0, "calls": 0, "joined": 0, "refused": 0, "left": 0}
        self.placing = {"lines": 0, "members": 0, "links": 0, "calls": 0, "left": 0}
        self.choosing = {"items": 0, "placed": 0, "calls": 0}
        self.curated = dict(self.man.get("curated") or {})
        self.base = {}  # the note half of the graph, reused across rebuilds until a review changes lineage
        self.fresh = set()  # notes read in this dream: `--all` does not ask for them twice
        self.gone = {}  # notes that left without a `drop` (plan)

    def run(self):
        if self.nothing_new() and not self.args.dry_run:
            print(f"dream: {len(self.cur)} notes · 0 indexed (0 calls) · nothing new since {self.man.get('dreamed', '?')}"
                  + (f" · {store_publish(self.root, load(self.root)[0])}" if store_name() else ""))  # a store behind the index catches up
            return
        self.plan()
        if self.args.dry_run:
            return self.dry_run()
        self.index()
        g = self.demote(self.graph())
        g = self.run_place(g)
        g = self.run_choose(g)
        g = self.run_curate(g)
        g = self.run_review(g)
        self.report(g, self.write(g))

    def nothing_new(self):
        """Same hashes, vocabulary, conflicts and script; nothing unindexed, due or pending; every output present."""
        a, man, cur, dd, root = self.args, self.man, self.cur, self.dd, self.root
        return (not a.all and not a.review and man.get("v") == V and man.get("code") == CODE
                and man.get("unindexed") == 0 and not man.get("due")
                and man.get("psig", pointer_sig(root, {})) == pointer_sig(root, man.get("pointers") or {})  # a file a note points at changed
                and {p: f["sha"] for p, f in cur.items()} == {p: f["sha"] for p, f in man.get("files", {}).items()}
                and man.get("vsig") == vsig(*vocab_texts(root), shape_text(root), *domain_texts(root))
                and (dd / "index.db").exists() and (dd / "graph.html").exists() and (root / "DIGEST.md").exists()
                and not any(self.pend.glob("*.json"))
                and {f["sha"][:12] + ".json" for f in cur.values()} <= set(os.listdir(dd / "notes")))

    def plan(self):
        """Caches in, the list of notes to index (oldest first), the homes for entity dedup."""
        man, cur, root = self.man, self.cur, self.root
        self.failed, self.attempts = man.get("failed", {}), man.get("attempts", {})
        self.by_sha = {}
        for rel in sorted(cur):
            self.by_sha.setdefault(cur[rel]["sha"][:12], rel)
        self.store = Store(self.dd, keep=not self.args.dry_run)
        self.facts = self.store.facts(root, cur)
        self.xs = self.store.extractions(self.by_sha)
        et, at = vocab_texts(root)
        kt, tt = domain_texts(root)
        self.tlines = parse_edges(et)[3]
        self.ty_lines = parse_edges(tt, TYPE_PACKS)[3]
        self.kind_names = ", ".join(parse_kinds(kt)["order"])
        self.tag_fill = tag_fill(root)
        self.alines, self.nots, _ = parse_aliases(at)
        self.homes = defaultdict(list)
        for rel in cur:
            if not rel.startswith("log/"):
                self.homes[fold(posixpath.basename(rel)[:-3])].append(rel)
        # a file that is merely gone is not a drop (a branch switch, a rename with an edit): nothing is written or
        # deleted for it. It is remembered with what it had replaced, so `drop` can still record it, and C15 says so.
        tomb = parse_dropped(conflicts_text(root))
        self.gone = {p: r for p, r in (man.get("gone") or {}).items() if p not in cur and not tombstoned(tomb, p)}
        new = [p for p in self.deleted if p not in self.gone and not tombstoned(tomb, p)]
        if new:
            was = old_lineage(self.dd, new)
            for p in new:
                self.gone[p] = {"seen": self.now.date().isoformat(), **was[p]}

        def upd(rel):
            u = self.facts[rel]["fm"].get("updated", "")
            return u if re.match(r"\d{4}-\d\d-\d\d", u) else dt.date.fromtimestamp(cur[rel]["mtime"] / 1e9).isoformat()
        # by project, then date: a wave is one project, so its calls share one KNOWN and one cacheable prefix
        self.todo = sorted((h for h in self.by_sha if self.args.all or h not in self.xs),
                           key=lambda h: (area_of(self.by_sha[h]), upd(self.by_sha[h]), self.by_sha[h]))

    def entities_now(self):
        xs, cur = self.xs, self.cur
        _, talias, tdrop, _, _, _ = parse_edges(domain_texts(self.root)[1], TYPE_PACKS)
        occ, _ = canon_occ(((rel, e) for rel in cur if cur[rel]["sha"][:12] in xs for e in xs[cur[rel]["sha"][:12]]["entities"]), talias, tdrop)
        linked = read_links((r["s"], r["o"]) for rel in cur if cur[rel]["sha"][:12] in xs
                            for r in xs[cur[rel]["sha"][:12]].get("relations", []))
        return merge_entities(occ, self.alines, self.nots, self.homes, linked=linked)[0]

    def prompt_for(self, h, ents):
        """-> (prompt, static_len). The static part — template, EDGES, KNOWN — comes first and is byte-identical for
        every note of a project within a dream; the note follows, capped so no call is large."""
        rel = self.by_sha[h]
        text = read(self.root / rel)
        if len(text) > NOTE_CAP:
            text = text[:NOTE_CAP] + f"\n… [{len(text) - NOTE_CAP} more characters cut: the note is far over the 40-line rule]"
        pr = fill(EXTRACT, kinds=self.kind_names, types="\n".join(self.ty_lines), edges="\n".join(self.tlines), **self.tag_fill,
                  known=known_lines(ents, area_of(rel)), folder=self.folder_lines([area_of(rel)], text=text), path=rel, text=text)
        return pr, pr.index("\nNOTE ") + 1

    def folder_lines(self, areas, cap=80, text=""):
        """The notes of these folders as `file name: first line`: what lets a keeper name the note a phrase means
        ("the dispositions dataset") when the text does not give its id. At most `cap` a folder. A folder with more
        notes than that cannot be listed, and its first notes by name are no help: of such a folder only the notes
        that `text`, the notes about to be read, names by their file name are given."""
        if not hasattr(self, "by_area"):
            self.by_area, self.line_of = defaultdict(list), {}
            for q in sorted(self.cur):
                if self.facts[q]["title"] and area_of(q) != "log":
                    self.line_of[q] = f"{posixpath.basename(q)[:-3]}: {self.facts[q]['title'][:80]}"
                    self.by_area[area_of(q)].append(self.line_of[q])
        named = None
        out = []
        for a in areas:
            lines = self.by_area.get(a, [])
            if len(lines) > cap:
                named = named if named is not None else set(re.findall(r"[a-z0-9][\w.-]*[a-z0-9]", text.lower()))
                lines = [ln for ln in lines if ln.split(": ", 1)[0].lower() in named]
            out += lines[:cap]
        return "\n".join(out) or "(none)"

    def ingest(self, h, ans):
        rel = self.by_sha[h]
        rec = ground(ans, read(self.root / rel))
        rec.update(path=rel, sha=self.cur[rel]["sha"], model=self.cmd or "file",
                   indexed_at=self.now.isoformat(timespec="seconds"))
        wr(self.dd / "notes" / f"{h}.json", rec)
        self.store.put(h, rec)
        self.xs[h] = rec
        self.fresh.add(h)
        self.failed.pop(h, None)
        self.attempts.pop(h, None)
        self.st["indexed"] += 1

    def miss(self, h):
        """A note that was asked for and got no usable answer: once more, then it is recorded as failed (C3)."""
        if self.attempts.get(h, 0) >= 1:
            self.failed[h] = "unusable answer after one retry"
            self.attempts.pop(h, None)
            return True
        self.attempts[h] = self.attempts.get(h, 0) + 1
        return False

    def take_answers(self):
        """Answer files left in _dream/pending/, whoever wrote them: `<note id>.json` for one note, `packet-….json`
        for a packet. A reading that is on file is used, with a command set or without one (PLAN §6)."""
        pend, by_sha = self.pend, self.by_sha
        for pj in sorted(pend.glob("*.json")):
            k, pp = pj.name[:-5], pend / (pj.name[:-5] + ".prompt.md")
            if k.startswith("packet-"):
                got = parse_packet(read(pj), by_sha)
                asked = set(re.findall(r"^NOTE ([0-9a-f]{12}) ", read(pp), re.M)) if pp.exists() else set()
                pj.unlink()
                pp.unlink() if pp.exists() else None
                for h, obj in got.items():
                    self.ingest(h, obj)
                for h in sorted(asked - set(got)):
                    if h in by_sha and h not in self.xs:
                        self.miss(h)
            elif k in by_sha:
                obj = parse_json(read(pj))
                pj.unlink()
                if obj is not None:
                    self.ingest(k, obj)
                if (obj is not None or self.miss(k)) and pp.exists():
                    pp.unlink()

    def pack(self, todo):
        """The notes to read as packets, in their order (one project after another): [[note id, …]]. A packet closes
        when the next note would take its notes past PACKET_TEXT characters or its prompt past PACKET_TOKENS."""
        tokens, text = env_numbers("MEMORY_PACKET", (PACKET_TOKENS, PACKET_TEXT))
        head = len(fill(PACKET, kinds=self.kind_names, types="\n".join(self.ty_lines), edges="\n".join(self.tlines), **self.tag_fill, known="", folder="")) + KNOWN_ROOM
        out, size = [], 0
        for h in todo:
            n = min(self.cur[self.by_sha[h]]["size"], NOTE_CAP) + 80
            if not out or size + n > text or (head + size + n) / 3 > tokens:
                out.append([])
                size = 0
            out[-1].append(h)
            size += n
        return out

    def packet_prompt(self, hs, ents):
        """-> (prompt, static length) for one packet. The rules, the vocabulary and KNOWN for the packet's areas come
        first; each note follows under `NOTE <id> <path>:`."""
        areas = list(dict.fromkeys(area_of(self.by_sha[h]) for h in hs))
        known = list(dict.fromkeys(ln for a in areas for ln in known_lines(ents, a).split("\n")))[:120]
        body = ""
        for h in hs:
            rel = self.by_sha[h]
            text = read(self.root / rel)
            if len(text) > NOTE_CAP:
                text = text[:NOTE_CAP] + f"\n… [{len(text) - NOTE_CAP} more characters cut: the note is far over the 40-line rule]"
            body += f"NOTE {h} {rel}:\n{text.rstrip()}\n"
        pr = fill(PACKET, kinds=self.kind_names, types="\n".join(self.ty_lines), edges="\n".join(self.tlines), **self.tag_fill, known="\n".join(known),
                  folder=self.folder_lines(areas, text=body))
        return pr + body, len(pr)

    def index(self):
        """Answers left on file are taken first. Then, command mode: waves of -j parallel calls, a note each or with
        --packets a packet each, KNOWN refreshed between waves. File mode: prompts (--prompts) or packets (--packets)
        for what is still unread, written for a helper agent; the ones nobody needs any more are removed."""
        pend, by_sha, xs, args = self.pend, self.by_sha, self.xs, self.args
        pend.mkdir(parents=True, exist_ok=True)
        self.take_answers()
        todo = [h for h in self.todo if h not in xs or (args.all and h not in self.fresh)]
        if self.cmd and args.packets:
            self.index_packets(todo)
        elif self.cmd:
            j = max(1, args.j)
            with ThreadPoolExecutor(j) as ex:
                ents, proj, since = None, None, 0
                for w in range(0, len(todo), j):
                    wave = todo[w:w + j]
                    p0 = area_of(self.by_sha[wave[0]])
                    # KNOWN is refreshed when the project changes (big memories: at most every 10 waves, the merge is
                    # slow there), so every call of a project shares one prefix that the model can cache
                    if ents is None or (p0 != proj and (len(self.cur) <= WIDE or since >= 10)):
                        ents, proj, since = Known(self.entities_now()), p0, 0
                    since += 1
                    for h, (obj, n) in zip(wave, ex.map(lambda h: call_model(self.cmd, *self.prompt_for(h, ents)), wave)):
                        self.st["calls"] += n
                        if obj is None:
                            self.failed[h] = "unusable answer after one retry"
                        else:
                            self.ingest(h, obj)
        keep = set()
        if not self.cmd and todo and (args.prompts or args.packets):  # only when asked: a memory used without any model stays quiet (phase F)
            ents = Known(self.entities_now())
            if args.packets:
                for hs in self.pack(todo):
                    name = "packet-" + hashlib.sha256(" ".join(hs).encode()).hexdigest()[:8]
                    keep.add(name)
                    if not (pend / f"{name}.prompt.md").exists():  # the same notes: the same packet, left as a helper may be reading it
                        wr(pend / f"{name}.prompt.md", self.packet_prompt(hs, ents)[0])
            else:
                for h in todo:
                    keep.add(h)
                    wr(pend / f"{h}.prompt.md", self.prompt_for(h, ents)[0])
        for pp in pend.glob("*.prompt.md"):  # stale: the note changed or is gone, or nobody asked for prompts
            k = pp.name[:-len(".prompt.md")]
            if k not in keep and not ((k == "review" or k.startswith("curate-")) and (args.prompts or args.packets)):
                pp.unlink()

    def index_packets(self, todo):
        """Command mode with --packets: -j packets at a time. A note whose line is missing from an answer is packed
        once more with the others that were missed; after that it is recorded as failed (C3)."""
        j = max(1, self.args.j)
        for round_ in (1, 2):
            packs = self.pack(todo)
            with ThreadPoolExecutor(j) as ex:
                for w in range(0, len(packs), j):
                    wave = packs[w:w + j]
                    ents = Known(self.entities_now())
                    prompts = [self.packet_prompt(hs, ents) for hs in wave]
                    calls = ex.map(lambda q: call_model(self.cmd, q[0][0], q[0][1], parse=lambda out: parse_packet(out, set(q[1]))),
                                   list(zip(prompts, wave)))
                    for hs, (got, n) in zip(wave, calls):
                        self.st["calls"] += n
                        self.st["packets"] += 1
                        for h in hs:
                            if got and h in got:
                                self.ingest(h, got[h])
            todo = [h for h in todo if h not in self.fresh]
            if not todo:
                break
        for h in todo:
            self.failed[h] = "unusable answer after one retry"

    def dry_run(self):
        """What this dream would read and about what it would cost. No call is made, and no note, registry, reading or
        graph is written."""
        todo = [h for h in self.todo if h not in self.xs or self.args.all]
        pin, pout = env_numbers("MEMORY_PRICE", PRICE)
        if not todo:
            print(f"dream --dry-run: {len(self.cur)} notes · nothing to read: every note has its reading")
            return
        ents = Known(self.entities_now())
        if self.args.packets:
            packs = self.pack(todo)
            sizes = [len(self.packet_prompt(hs, ents)[0]) // 3 for hs in packs]
        else:
            packs, sizes = [[h] for h in todo], [len(self.prompt_for(h, ents)[0]) // 3 for h in todo]
        out = int(sum(min(self.cur[self.by_sha[h]]["size"], NOTE_CAP) for h in todo) * OUT_PER_CHAR)
        cost = sum(sizes) * pin / 1e6 + out * pout / 1e6
        what = ("packet" + "s" * (len(packs) != 1)) if self.args.packets else "calls, one a note (`--packets` reads many notes a call)"
        print(f"dream --dry-run: {len(self.cur)} notes · {len(todo)} to read in {len(packs)} {what} · about {sum(sizes):,} tokens in "
              f"and {out:,} out · about ${cost:.2f} at ${pin:.2f} and ${pout:.2f} a million tokens · the largest prompt about "
              f"{max(sizes):,} tokens" + (": OVER the 100,000 line, where a prompt costs five times as much" if max(sizes) > 100000 else "")
              + " · the answer is counted as Haiku 5.5 wrote it, thinking included · after it the lines that state what a note "
              f"builds on or replaces are read once more, a call for every {PLACE_LINES} such lines of a folder (on a bank of "
              "1,677 notes: 50 calls, a seventh of the first reading's cost) · nothing was called or written")
        if self.args.packets:
            for hs, n in list(zip(packs, sizes))[:40]:
                areas = list(dict.fromkeys(area_of(self.by_sha[h]) or "(root)" for h in hs))
                print(f"  {len(hs):>3} notes · about {n:>6,} tokens · {', '.join(areas[:4])}" + (f" and {len(areas) - 4} more" if len(areas) > 4 else ""))
            if len(packs) > 40:
                print(f"  … and {len(packs) - 40} more packets")

    def graph(self):
        """The graph now. The note half is reused across rebuilds in one dream unless a review changed lineage."""
        e2, a2 = vocab_texts(self.root)
        man = {**self.man, "failed": self.failed}
        self.base.update(self.base or notes_part(self.root, man, self.cur, self.former, self.xs, self.facts))
        g = build(self.root, man, self.cur, self.former, e2, a2, xs=self.xs, now=self.now, facts=self.facts, base=self.base)
        gone = [{"code": "C15", "msg": f"{p}: gone since {r['seen']} without a drop; `memory.py drop {p} --yes` records it "
                 "and keeps what it had replaced replaced, or put the file back"} for p, r in sorted(self.gone.items())]
        g["checks"] = sorted(g["checks"] + gone, key=lambda c: c["code"])
        return g

    def demote(self, g):
        """Probation over and still under the bar: the term goes back to a word, in whichever vocabulary (a label in
        EDGES.md, a word in TYPES.md, KINDS.md or TAGS.md), 0 calls."""
        root, done = self.root, 0
        into = {"KINDS.md": self.review["kinds"], "TAGS.md": self.review["tags"]}  # relation and thing types: the rest
        for key, name, text_of in (("vocab", "EDGES.md", lambda: vocab_texts(root)[0]), ("tvocab", "TYPES.md", lambda: domain_texts(root)[1]),
                                   ("kvocab", "KINDS.md", lambda: domain_texts(root)[0]), ("gvocab", "TAGS.md", lambda: tags_text(root))):
            gone = (g.get(key) or {}).get("demote") or []
            if gone:
                text = text_of()
                for T in gone:
                    text = edit_edges(text, "demote", T)
                wr(root / name, text)
                done += len(gone)
                if name in into:
                    into[name]["demoted"] += len(gone)
                if name == "KINDS.md":
                    self.base.clear()
        if not done:
            return g
        self.review["demoted"] = done - sum(c["demoted"] for c in into.values())
        return self.graph()

    def run_place(self, g):
        """The second reading. Every line of a note on which the first reading found lineage is put to the keeper once
        more, by folder: the line, the note it stands in, whether it says builds on or replaces, and the folder's
        notes by file name. The keeper lists every member of the line, each with its own words and the note meant;
        its answer takes the place of the first reading's items on that line, one item a member with the member's
        words as its quote, kept only when those words are in the line, and marked `asked`, so that a line is read
        twice and no more. A member no note is named for stays an item with its words, which the build lists (C18)
        and `ask` prints. Nothing is lost by silence: an answer that names no member for a line leaves the line as
        the first reading had it, and an item of the first reading whose name is written in the line as it stands
        ("Builds on ds-cc-tickets-raw.") stays whatever the answer left out. The lines read are those of the first
        reading's items, and the lines that write what an item names whose words grounding could not find (`recheck`).
        Command mode only."""
        if not self.cmd:
            return g
        todo = defaultdict(list)  # folder → [(note, field, line number, the line)]
        for rel in sorted(self.cur):
            x = self.xs.get(self.cur[rel]["sha"][:12]) or {}
            at = sorted({(f, b["line"]) for f in ("built_on", "replaces") for b in x.get(f) or [] if b.get("line") and not b.get("asked")}
                        | {(r["field"], r["line"]) for r in x.get("recheck") or [] if not r.get("asked")})
            if at:
                ls = read(self.root / rel).split("\n")
                todo[area_of(rel)] += [(rel, f, n, " ".join(ls[n - 1].split())[:PLACE_TEXT]) for f, n in at if n <= len(ls)]
        shown = int(env_numbers("MEMORY_FOLDER", (FOLDER_SHOWN,))[0])
        few = min(NEAR_SHOWN, shown)  # the notes one call shows of a folder too large to list
        self.folder_lines([])  # the lines by note, built once
        sizes = Counter(area_of(q) for q in self.line_of)
        adj, words, near = defaultdict(set), {}, {}
        for e in g["edges"] if any(sizes[a] > shown for a in todo) else []:
            if e["rel"] in ("refs", "from", "supersedes") and area_of(e["src"]) == area_of(e["dst"]):
                adj[e["src"]].add(e["dst"])
                adj[e["dst"]].add(e["src"])
        wrx = re.compile(r"[a-z][a-z0-9]{3,}")

        def steps(rel):  # {note of the folder: steps away, up to NEAR_STEPS} by a name written in a note, either way
            if rel not in near:
                seen, queue = {rel: 0}, [rel]
                while queue:
                    q = queue.pop(0)
                    if seen[q] < NEAR_STEPS:
                        for r in sorted(adj[q]):
                            if r not in seen:
                                seen[r] = seen[q] + 1
                                queue.append(r)
                near[rel] = seen
            return near[rel]

        def by_words(a, rel, text):  # the notes of the folder whose first line and name share the rarest words with the line
            if (rel, text) in words:
                return words[(rel, text)]
            if a not in words:
                ws = {q: set(wrx.findall((posixpath.basename(q)[:-3].replace("-", " ") + " " + self.facts[q]["title"]).lower()))
                      for q in self.line_of if area_of(q) == a}
                df, by = Counter(w for v in ws.values() for w in v), defaultdict(set)
                for q, v in ws.items():
                    for w in v:
                        by[w].add(q)
                words[a] = (len(ws), df, by)
            n, df, by = words[a]
            score = Counter()
            for w in set(wrx.findall(text.lower())):
                if w in by and df[w] <= n // 4:
                    for q in by[w]:
                        score[q] += math.log(n / df[w])
            score.pop(rel, None)
            words[(rel, text)] = [q for q, _ in sorted(score.items(), key=lambda kv: (-kv[1], kv[0]))[:NEAR_WORDS]]
            return words[(rel, text)]

        def nearby(a, part):  # {note of a large folder: how near} for the lines of one call; a note is not shown for its own line
            rank = {}
            for rel, f, n, text in part:
                for q, d in steps(rel).items():
                    if q != rel and q in self.line_of:
                        rank[q] = min(rank.get(q, 9), d)
                for q in by_words(a, rel, text):
                    rank.setdefault(q, 9)  # 9: not near, shown for its words
            return rank

        for a in [a for a in todo if sizes[a] > shown]:  # in a large folder, the lines of notes that name each other side by side
            have, order, seen = defaultdict(list), [], set()
            for e in todo[a]:
                have[e[0]].append(e)
            for start in sorted(have):
                queue = [] if start in seen else [start]
                seen.add(start)
                while queue:
                    q = queue.pop(0)
                    order += have.get(q, [])
                    for r in sorted(adj[q]):
                        if r not in seen:
                            seen.add(r)
                            queue.append(r)
            todo[a] = order
        parts = []
        for a in sorted(todo):
            if sizes[a] <= shown:
                parts += [(a, todo[a][k:k + PLACE_LINES]) for k in range(0, len(todo[a]), PLACE_LINES)]
                continue
            part = []
            for e in todo[a]:  # a call takes lines while the notes to show for them fit: none is cut for coming late in the alphabet
                if part and (len(part) == PLACE_LINES or len(nearby(a, part + [e])) > few):
                    parts.append((a, part))
                    part = []
                part.append(e)
            parts += [(a, part)] if part else []
        self.placing["left"] = sum(len(part) for _, part in parts[PLACE_MAX:])
        parts = parts[:PLACE_MAX]
        if not parts:
            return g

        def prompt(a, part):
            items = "\n".join(f"{k} · {posixpath.basename(rel)[:-3]} · {'builds on' if f == 'built_on' else 'replaces'} · {text}"
                              for k, (rel, f, n, text) in enumerate(part, 1))
            if sizes[a] <= shown:
                return fill(PLACE, area=a, folder=self.folder_lines([a], cap=shown), items=items)
            rank = nearby(a, part)
            pick = sorted(sorted(rank), key=lambda q: rank[q])[:few]
            return fill(PLACE_NEAR, area=a, count=sizes[a], items=items,
                        folder="\n".join(self.line_of[q] for q in sorted(pick) if rank[q] < 9) or "(none)",
                        also="\n".join(self.line_of[q] for q in sorted(pick) if rank[q] == 9) or "(none)")
        with ThreadPoolExecutor(max(1, self.args.j)) as ex:
            answers = list(ex.map(lambda part: call_model(self.cmd, prompt(*part)), parts))
        before = sum(e.get("by") == "reading" for e in g["edges"])
        changed = set()
        for (a, part), (obj, n) in zip(parts, answers):
            self.placing["calls"] += n
            if not isinstance(obj, dict):
                continue  # no answer: these lines stay as the first reading left them, and are asked again
            for k, (rel, f, ln, text) in enumerate(part, 1):
                h = self.cur[rel]["sha"][:12]
                x, ans = self.xs[h], obj.get(str(k))
                changed.add(h)
                self.placing["lines"] += 1
                first = [b for b in x.get(f) or [] if b.get("line") == ln]
                for b in first + [r for r in x.get("recheck") or [] if r["field"] == f and r["line"] == ln]:
                    b["asked"] = True
                new, low = [], text.lower()
                for e in ans if isinstance(ans, list) else []:
                    e = {"words": e, "note": e} if isinstance(e, str) else e  # a bare name: the words and the note at once
                    words = " ".join(str(e.get("words") or "").split()) if isinstance(e, dict) else ""
                    at = low.find(words.lower()) if words else -1
                    if at < 0:
                        continue  # kept only with words that are in the line
                    name = str(e.get("note") or "").strip()
                    name = name[:-3] if name.endswith(".md") else name
                    if name and name in (rel[:-3], posixpath.basename(rel)[:-3]):
                        continue  # the note itself
                    new.append({"what": name or text[at:at + len(words)], "quote": text[at:at + len(words)], "line": ln, "asked": True})
                if not new:
                    continue  # no member named, or the line passed over: it stays as the first reading had it, asked once
                took = {fold(posixpath.basename(b["what"])) for b in new}
                new += [b for b in first if fold(posixpath.basename(b["what"])) not in took and re.search(r"[/\d_-]", b["what"])
                        and re.search(r"(?<![\w/-])" + re.escape(b["what"]) + r"(?![\w/-])", text, re.I)]
                x[f] = sorted([b for b in x.get(f) or [] if b.get("line") != ln] + new, key=lambda b: b.get("line") or 0)
                self.placing["members"] += len(new)
        for h in changed:  # the reading on file is what the keepers read, the second reading included
            wr(self.dd / "notes" / f"{h}.json", self.xs[h])
            self.store.put(h, self.xs[h])
        if not changed:
            return g
        g = self.graph()
        self.placing["links"] = sum(e.get("by") == "reading" for e in g["edges"]) - before
        return g

    def run_choose(self, g):
        """The third reading, for the words two readings could not place (C18, items marked `asked`): each is shown
        with the few notes of its folder (CHOOSE_SHOWN) whose file name, first line and next two lines share the rarest
        of its words, those near its note first (within NEAR_STEPS by a name written in a note, as the second reading
        orders them), with those lines, and the keeper says which note is meant or that none is. An answer that names
        one of the notes shown becomes the item's `what`; every item asked is marked `looked` and not asked again.
        Command mode only. Ranked by the words alone, two common ones ("test", "versus") had put six notes of other
        projects before the one the words meant ("the bg/nbd versus gbm accuracy test": exp-501, one step away)."""
        if not self.cmd:
            return g
        todo = []
        for u in g.get("unplaced", []):
            h = self.cur[u["note"]]["sha"][:12] if u["note"] in self.cur else None
            items = (self.xs.get(h) or {}).get(u["field"]) or []
            if u["i"] < len(items) and items[u["i"]].get("asked") and not items[u["i"]].get("looked"):
                todo.append((u["note"], u["field"], items[u["i"]]))
        if not todo:
            return g
        tok = re.compile(r"[a-z0-9]+(?:[/.][a-z0-9]+)*")
        opening, index = {}, {}
        shown = int(env_numbers("MEMORY_FOLDER", (FOLDER_SHOWN,))[0])
        adj = defaultdict(set)
        for e in g["edges"]:
            if e["rel"] in ("refs", "from", "supersedes") and area_of(e["src"]) == area_of(e["dst"]):
                adj[e["src"]].add(e["dst"])
                adj[e["dst"]].add(e["src"])

        def near(rel):  # the notes within NEAR_STEPS of rel by a name written in a note, either way
            seen, queue = {rel: 0}, [rel]
            while queue:
                q = queue.pop(0)
                if seen[q] < NEAR_STEPS:
                    for r in sorted(adj[q]):
                        if r not in seen:
                            seen[r] = seen[q] + 1
                            queue.append(r)
            return set(seen)

        def first_lines(q):  # `name: first line | next | next`, and its words
            if q not in opening:
                ls = [" ".join(t.split()) for t in read(self.root / q).split("\n")]
                start, name, title = self.facts[q].get("line") or 1, posixpath.basename(q)[:-3], self.facts[q]["title"][:200]
                text = (title if title.lower().startswith(name.lower()) else f"{name}: {title}") + "".join(
                    f" | {t[:150]}" for t in [t for t in ls[start:] if t][:2])
                opening[q] = (text, {w for w in tok.findall(text.lower().replace("-", " ")) if w not in STOP and len(w) >= 2})
            return opening[q]

        def candidates(rel, words):
            a = area_of(rel)
            if a not in index:
                pool = [q for q in self.cur if area_of(q) == a and self.facts[q]["title"] and q.endswith(".md")]
                df = Counter(w for q in pool for w in first_lines(q)[1])
                index[a] = (pool, df)
            pool, df = index[a]
            close = near(rel) if len(pool) > shown else set(pool)  # a folder that is listed whole is all near
            want = {w for w in tok.findall(words.lower().replace("-", " ")) if w not in STOP and len(w) >= 2}
            score = {q: math.fsum(math.log(len(pool) / df[w]) for w in want & first_lines(q)[1]) for q in pool if q != rel}
            return [q for q in sorted(score, key=lambda q: (q not in close, -score[q], q)) if score[q] > 0][:CHOOSE_SHOWN]
        asks = []
        for rel, f, b in todo:
            cands = candidates(rel, f"{b['quote']} {b['what']}")
            if cands:
                ls = read(self.root / rel).split("\n")
                line = " ".join(ls[b["line"] - 1].split())[:PLACE_TEXT] if b.get("line") and b["line"] <= len(ls) else b["quote"]
                asks.append((rel, f, b, cands, line))
            else:
                b["looked"] = True  # nothing in its folder shares a word with it: there is nothing to choose from
        by_area = defaultdict(list)
        for x in asks:
            by_area[area_of(x[0])].append(x)
        parts = [xs[k:k + CHOOSE_ITEMS] for a in sorted(by_area) for xs in [by_area[a]] for k in range(0, len(xs), CHOOSE_ITEMS)][:CHOOSE_MAX]

        def prompt(part):
            out = []
            for k, (rel, f, b, cands, line) in enumerate(part, 1):
                out.append(f"{k} · {posixpath.basename(rel)[:-3]} {'builds on' if f == 'built_on' else 'replaces'} «{b['quote']}» · its line: «{line}»")
                out += [f"   - {first_lines(q)[0]}" for q in cands]
            return fill(CHOOSE, items="\n".join(out))
        with ThreadPoolExecutor(max(1, self.args.j)) as ex:
            answers = list(ex.map(lambda part: call_model(self.cmd, prompt(part)), parts))
        changed = {self.cur[rel]["sha"][:12] for rel, f, b in todo if b.get("looked")}
        for part, (obj, n) in zip(parts, answers):
            self.choosing["calls"] += n
            if not isinstance(obj, dict):
                continue  # no answer: asked again at the next dream
            for k, (rel, f, b, cands, line) in enumerate(part, 1):
                name = str(obj.get(str(k)) or "").strip()
                name = posixpath.basename(name[:-3] if name.endswith(".md") else name)
                pick = [q for q in cands if posixpath.basename(q)[:-3] == name]
                b["looked"] = True
                self.choosing["items"] += 1
                if pick:
                    b["said"], b["what"] = b["what"], name
                    self.choosing["placed"] += 1
                changed.add(self.cur[rel]["sha"][:12])
        for h in changed:
            wr(self.dd / "notes" / f"{h}.json", self.xs[h])
            self.store.put(h, self.xs[h])
        return self.graph() if changed else g

    def cards(self, g, area, cap=150, lines=True):
        """The things a folder's notes name, for the curator: -> (ids, one card each, from thing_cards). Most mentioned
        first. lines=False: the ids alone, which are what the folder's signature is made of."""
        rows = []
        for e in g["entities"]:
            n = sum(area_of(m["path"]) == area for m in e["mentions"])
            if n:
                rows.append((-n, fold(e["id"]), e["id"]))
        rows.sort()
        ids = [r[2] for r in rows[:cap]]
        if not lines:
            return ids, []
        cs = thing_cards(g, self.root, ids, area)
        return ids, [f"- {cs[i]}" for i in ids if i in cs]

    def run_curate(self, g):
        """Identity by reading (PLAN §7). For each folder whose things changed since the curator last read it: one
        prompt with all of them, and an answer that says which are one thing under two names, each with its reason.
        A join is one line of ALIASES.md, `- a = b | why: … | by: curator <date>`, which a person may delete or
        overrule with `not: a / b`. What the script holds, whatever the answer says: a join is between things on the
        folder's list; never between two versions, never against a `not:` line; the name that is joined to another
        is used in this folder alone (a short name that two folders use, "the response model", may be two things, and
        the first run on the bank joined two projects' models through one); a thing whose note is in another folder
        is not renamed here; and no line, with what it already holds, may come to join two things that each have a
        note, or two names in use beyond this folder; the one such name a line may hold leads it. With a command the folders are read `-j` at a time; without one the prompts are files, when asked
        for, like the review's, and their answers are taken at the next dream."""
        pend, args = self.pend, self.args
        ask_files = not self.cmd and (args.prompts or args.packets)
        sig = lambda ids: hashlib.sha256(" ".join(sorted(map(fold, ids))).encode()).hexdigest()[:12]  # noqa: E731
        slug = lambda a: "curate-" + a.replace("/", "--")  # noqa: E731
        areas = sorted({area_of(m["path"]) for e in g["entities"] for m in e["mentions"]} - {"log", ""})
        todo = []
        for a in areas:
            ids = self.cards(g, a, lines=False)[0]
            if len(ids) >= 2 and self.curated.get(a) != sig(ids):
                todo.append((a, ids, self.cards(g, a)[1]))
        self.curate["left"] = max(0, len(todo) - CURATE_MAX)
        todo = todo[:CURATE_MAX]
        answers = {}
        if self.cmd and todo:
            with ThreadPoolExecutor(max(1, args.j)) as ex:
                for (a, _, _), (obj, n) in zip(todo, ex.map(lambda t: call_model(self.cmd, fill(CURATE, area=t[0], cards="\n".join(t[2]))), todo)):
                    answers[a] = obj
                    self.curate["calls"] += n
        elif not self.cmd and pend.exists():
            for pj in sorted(pend.glob("curate-*.json")):  # what a helper agent left
                answers[pj.name[len("curate-"):-5].replace("--", "/")] = parse_json(read(pj))
                pj.unlink()
        ents = {e["id"]: e for e in g["entities"]}
        links = linked_pairs(g)
        a2 = vocab_texts(self.root)[1]
        nots = parse_aliases(a2)[1]
        stamp = f" | by: curator {self.now.date().isoformat()}"
        home = lambda i: ents[i]["home"] if i in ents else None  # noqa: E731
        local = lambda i, a: all(area_of(m["path"]) == a for m in ents[i]["mentions"])  # noqa: E731

        def line_of(text, i):
            """The ids already joined with this one in ALIASES.md."""
            return next((set(ln) for ln in parse_aliases(text)[0] if fold(i) in {fold(x) for x in ln}), {i})
        read_now = []
        for a, ids, _ in todo:
            if a not in answers:
                continue
            read_now.append(a)
            self.curate["folders"] += 1
            have = {fold(i): i for i in ids}
            for grp in ((answers[a] or {}).get("same") or []):
                if not isinstance(grp, dict):
                    continue
                gi = list(dict.fromkeys(have[fold(str(x))] for x in (grp.get("ids") or []) if fold(str(x)) in have))
                why = " ".join(str(grp.get("why") or "").split()).replace(" | ", " / ")[:160]
                if len(gi) < 2 or not why:
                    continue
                lead = min(gi, key=lambda i: (not ents[i]["home"], -len(ents[i]["mentions"]), fold(i)))
                for other in gi:
                    if other == lead or versions(fold(lead), fold(other)) or frozenset((fold(lead), fold(other))) in nots:
                        continue
                    if not local(other, a) or any(home(i) and area_of(home(i)) != a for i in (lead, other)):
                        self.curate["refused"] += 1  # a name other folders use too, or a thing that is another folder's
                        continue
                    if frozenset((lead, other)) in links:
                        self.curate["refused"] += 1  # two things a note links are two things
                        continue
                    line = line_of(a2, lead) | line_of(a2, other)  # what the line would hold, with what is joined already
                    wide = sorted(i for i in line if i in ents and not local(i, a))
                    if len({home(i) for i in line if home(i)}) > 1 or len(wide) > 1:
                        self.curate["refused"] += 1  # two things with a note each, or two names in use beyond this folder
                        continue
                    a2 = edit_aliases(a2, lead, other, True, lead, note=f" | why: {why}{stamp}")
                    if wide:  # the one name other folders use stays the thing's name: it leads its line
                        a2 = lead_aliases(a2, wide[0])
                    self.curate["joined"] += 1
        if a2 != vocab_texts(self.root)[1]:
            wr(self.root / "ALIASES.md", a2)
            g = self.graph()
        for a in read_now:  # what the folder holds after the joins: the same things are not read twice
            self.curated[a] = sig(self.cards(g, a, lines=False)[0])
            if (pend / f"{slug(a)}.prompt.md").exists():
                (pend / f"{slug(a)}.prompt.md").unlink()
        if ask_files:
            for a, ids, lines in todo:
                if a not in read_now:
                    wr(pend / f"{slug(a)}.prompt.md", fill(CURATE, area=a, cards="\n".join(lines)))
        return g

    def word_sections(self, g, kprops, gprops):
        """The review's kind and tag sections, in the shape of the type sections: the vocabulary with its definitions,
        then each word over the bar with its counts and example notes."""
        kinds = parse_kinds(domain_texts(self.root)[0])["kinds"]
        words = word_lines
        kv, gv = g.get("kvocab") or {}, g.get("gvocab") or {}
        return {"kinds": "\n".join(f"- {k}: {d['def']}" + (f" | family: {d['family']}" if d["family"] != k else "") for k, d in kinds.items()),
                "kn": kv.get("types", len(kinds)), "kbudget": kv.get("budget", KIND_DEFAULTS["budget"]), "kwords": words(kprops),
                "tags": "\n".join(parse_edges(tags_text(self.root), {})[3]) or "none yet",
                "gn": gv.get("types", 0), "gbudget": gv.get("budget", TAG_DEFAULTS["budget"]), "gwords": words(gprops)}

    def review_prompt(self, g):
        """-> (prompt or None, labels offered, entity pairs offered, conflicts offered)."""
        root = self.root
        props = g["proposed"][:40]
        tprops = g.get("proposed_types", [])[:40]
        kprops, gprops = g.get("proposed_kinds", [])[:40], g.get("proposed_tags", [])[:40]
        pairs = [(r["a"], r["b"]) for r in g["review"]][:30]
        conflicts = [c for c in g["conflicts"] if not c["unsure"]][:CONFLICT_MAX]
        if not props and not pairs and not conflicts and not tprops and not kprops and not gprops:
            return None, props, pairs, conflicts
        nmap = {n["path"]: n for n in g["notes"]}

        def first_line(p):
            n = nmap[p]
            ls = [x.strip() for x in read(root / p).split("\n")[(n["line"] or 1):] if x.strip() and not x.startswith("#")]
            return (ls[0] if ls else "")[:160]

        pc = thing_cards(g, root, sorted({x for p in pairs for x in p}))  # the curator's cards: one evidence for both

        def pair_line(a, b):
            both = shared_links(g, a, b)
            return f"- {a} / {b}: {pc.get(a, a)} | {pc.get(b, b)} · both: {'; '.join(both[:4]) if both else 'no link in common'}"
        vc, tv = g["vocab"], g["tvocab"]
        pr = fill(REVIEW, edges="\n".join(parse_edges(vocab_texts(root)[0])[3]), n=vc["types"], budget=vc["budget"],
                  u=vc["promote"][0], nn=vc["promote"][1], a=vc["promote"][2],
                  types="\n".join(parse_edges(domain_texts(root)[1], TYPE_PACKS)[3]), tn=tv["types"], tbudget=tv["budget"],
                  etypes=word_lines(tprops), proposals=word_lines(props),
                  pairs="\n".join(pair_line(a, b) for a, b in pairs) or "none",
                  conflicts="\n".join(f"- {c['a']} / {c['b']}: \"{nmap[c['a']]['title']}\" «{first_line(c['a'])}» | "
                                      f"\"{nmap[c['b']]['title']}\" «{first_line(c['b'])}»" for c in conflicts) or "none",
                  **self.word_sections(g, kprops, gprops))
        return pr, props, pairs, conflicts

    def apply_review(self, g, ans, props, pairs, conflicts=()):
        """Write what the review decided: CONFLICTS.md verdicts, EDGES.md aliases / drops / new types (within the
        budget), ALIASES.md pairs. The code decides what is admissible; the answer only proposes."""
        root, review, now = self.root, self.review, self.now
        e2, a2 = vocab_texts(root)
        cf = root / "CONFLICTS.md"
        c2 = read(cf) if cf.exists() else CONFLICTS_HEAD
        offered = {frozenset((c["a"], c["b"])): (c["a"], c["b"]) for c in conflicts}
        stem_ = lambda p: posixpath.basename(str(p).strip())[: -3 if str(p).strip().endswith(".md") else None]  # noqa: E731
        for k, v in (ans.get("conflicts") or {}).items():  # never invent: a verdict must name an offered pair
            ka, kb = split_pair(str(k))
            pair = next((ab for key, ab in offered.items() if {stem_(ka), stem_(kb)} == {stem_(x) for x in ab}), None)
            low = str(v).strip().lower()
            if not pair or not low:
                continue
            a, b = pair
            if "compatible" in low:
                c2 = c2.rstrip("\n") + f"\ncompatible: {a} / {b}\n"
            elif "supersedes" in low:
                left = low.split("supersedes", 1)[0]
                win = a if stem_(a) in left else b if stem_(b) in left else None
                if win:
                    c2 = c2.rstrip("\n") + f"\n- {win} > {a if win == b else b}\n"
            elif "unsure" in low:
                c2 = c2.rstrip("\n") + f"\n- {a} ? {b}\n"
            else:
                continue
            review["decided"] += "unsure" not in low
            offered.pop(frozenset(pair), None)
        if conflicts and c2 != (read(cf) if cf.exists() else CONFLICTS_HEAD):
            wr(cf, c2)
            self.base.clear()  # a supersession changes the note half: rebuild it, not only the vocabulary half
        mentions = {e["id"]: len(e["mentions"]) for e in g["entities"]}
        links = linked_pairs(g)
        # every vocabulary by the same rule (apply_terms): relation labels into EDGES.md here, type words, kind words and
        # tag words into their files below
        e2 = apply_terms(e2, ans.get("types"), props, now, reverse=True, stats=review)
        asked = {frozenset((fold(a), fold(b))): (a, b) for a, b in pairs}
        for k, v in (ans.get("entities") or {}).items():
            a, b = split_pair(str(k))
            ab = asked.get(frozenset((fold(a), fold(b))))
            v = str(v).strip().lower()
            if ab and v in ("same", "different"):
                a, b = ab
                if v == "same" and frozenset((a, b)) in links:
                    continue  # two things a note links are two things, whatever the answer
                lead = a if mentions.get(a, 0) >= mentions.get(b, 0) else b
                a2 = edit_aliases(a2, a, b, v == "same", lead, note=f" | by: review {now.date().isoformat()}")
                review["aliases"] += v == "same"
        if e2 != vocab_texts(root)[0]:
            wr(root / "EDGES.md", e2)
        if a2 != vocab_texts(root)[1]:
            wr(root / "ALIASES.md", a2)
        for key, name, now_text, packs, offered, dflt, st in (
                ("etypes", "TYPES.md", lambda: domain_texts(root)[1], TYPE_PACKS, g.get("proposed_types", []), None, review),
                ("kinds", "KINDS.md", lambda: domain_texts(root)[0], KIND_PACKS, g.get("proposed_kinds", []), KIND_DEFAULTS, review["kinds"]),
                ("tags", "TAGS.md", lambda: tags_text(root), None, g.get("proposed_tags", []), TAG_DEFAULTS, review["tags"])):
            was = now_text()
            text = apply_terms(was, ans.get(key), offered, now, packs, stats=st, defaults=dflt)
            if text != was:
                wr(root / name, text)
                if name == "KINDS.md":
                    self.base.clear()                     # a note's kind is in the note half: rebuild it

    def run_review(self, g):
        """Command mode: one call when something is due. File mode: ingest review.json if the helper agent left one,
        then write review.prompt.md for what is still due."""
        pend, cmd, args = self.pend, self.cmd, self.args
        open_ = lambda g_: [c for c in g_["conflicts"] if not c["unsure"]]  # noqa: E731
        due = lambda g_: (g_["proposed"] or g_.get("proposed_types") or g_.get("proposed_kinds") or g_.get("proposed_tags")  # noqa: E731
                          or g_["review"] or open_(g_))   # anything over a bar, a pair, a conflict: the same review for all
        if cmd and (args.review or due(g)):
            pr, props, pairs, conflicts = self.review_prompt(g)
            if pr:
                obj, n = call_model(cmd, pr)
                self.review.update(pairs=len(pairs), types=len(props), calls=n, conflicts=len(conflicts))
                if obj is not None:
                    self.apply_review(g, obj, props, pairs, conflicts)
                    g = self.graph()
        elif not cmd:
            rj = pend / "review.json"
            if rj.exists():
                obj = parse_json(read(rj))
                props, pairs, conflicts = g["proposed"], [(r["a"], r["b"]) for r in g["review"]], open_(g)[:CONFLICT_MAX]
                self.review.update(pairs=len(pairs), types=len(props), conflicts=len(conflicts))
                if obj is not None:
                    self.apply_review(g, obj, props, pairs, conflicts)
                    g = self.graph()
                rj.unlink()
                (pend / "review.prompt.md").unlink() if (pend / "review.prompt.md").exists() else None
            pr = self.review_prompt(g)[0] if (args.prompts or args.packets) and (args.review or due(g)) else None
            if pr:
                wr(pend / "review.prompt.md", pr)
            elif (pend / "review.prompt.md").exists():
                (pend / "review.prompt.md").unlink()
        return g

    def write(self, g):
        """Cache upkeep, the viewer, index.db, the digest, the pending list, the manifest. -> pending prompts."""
        root, dd, pend, now, cur, man = self.root, self.dd, self.pend, self.now, self.cur, self.man
        refs = man.get("refs", {})  # keep extractions referenced in the last KEEP_DAYS: edit reverts reuse them
        today = now.date().isoformat()
        for h in self.by_sha:
            refs[h] = today
        cutoff = (now.date() - dt.timedelta(days=KEEP_DAYS)).isoformat()
        for f in (dd / "notes").glob("*.json"):
            h = f.name[:-5]
            last = refs.get(h) or dt.date.fromtimestamp(f.stat().st_mtime).isoformat()
            if h not in self.by_sha and last < cutoff:
                f.unlink()
                refs.pop(h, None)
        e2, a2 = vocab_texts(root)
        if len(cur) > WIDE:  # big: no 380 MB graph.json; an overview page and one page per area
            (dd / "graph.json").unlink() if (dd / "graph.json").exists() else None
            write_viz_big(root, g, dd)
        else:
            wr(dd / "graph.json", g)
            write_viz(root, g, dd / "graph.html")
        write_kg(root, g, dd / "knowledge-graph.html")
        write_index(dd, g)
        self.published = store_publish(root, g)  # MEMORY_STORE: the hosted store, as a diff (stores.py)
        write_digest(root, g, now)
        todo_list = sorted(p for p in pend.glob("*.prompt.md")) if pend.exists() else []
        todo_list = [p for p in todo_list if not (pend / (p.name[:-len(".prompt.md")] + ".json")).exists()]
        if todo_list:  # the helper agent may have no way to list files: name them
            wr(pend / "TODO.md", "# pending prompts: answer each with <same name>.json\n"
               + "".join(f"{p.resolve()}\n" for p in todo_list))
        elif (pend / "TODO.md").exists():
            (pend / "TODO.md").unlink()
        wr(dd / "manifest.json", {"v": V, "code": CODE, "files": cur, "former": self.former,
                                  "vsig": vsig(e2, a2, shape_text(root), *domain_texts(root)),
                                  "seen": sorted(fold(e["id"]) for e in g["entities"]),
                                  "registry": {"edges": sorted(parse_edges(e2)[0]), "types": sorted(parse_edges(domain_texts(root)[1], TYPE_PACKS)[0])},
                                  "queue": [[r["a"], r["b"]] for r in g["review"]],
                                  "failed": self.failed, "attempts": self.attempts, "refs": refs,
                                  "dropped": g.get("dropped", []), "gone": self.gone,
                                  "pointers": g.get("pointers", {}), "psig": pointer_sig(root, g.get("pointers", {})),
                                  "tags": g.get("tags", {}), "unplaced": g.get("unplaced", []),
                                  "dreamed": now.isoformat(timespec="seconds"),
                                  "unindexed": sum(1 for n in g["notes"] if not n["indexed"]),
                                  "curated": self.curated,
                                  "due": bool(self.cmd and (g["proposed"] or g.get("proposed_types") or g["review"] or self.curate["left"]
                                                            or [c for c in g["conflicts"] if not c["unsure"]]))})
        return len(todo_list)

    def report(self, g, pending):
        st, review, cmd = self.st, self.review, self.cmd
        codes = Counter(c["code"] for c in g["checks"] if c["code"] != "C5")
        pl = lambda n, w: f"{n} {w}" + ("s" if n != 1 else "")  # noqa: E731
        out = f"dream: {len(self.cur)} notes · {st['indexed']} indexed ({st['calls']} calls" + (f", {st['packets']} packets)" if st["packets"] else ")")
        if review["pairs"] or review["types"] or review["conflicts"]:
            out += f" · review: {pl(review['pairs'], 'pair')}, {pl(review['types'], 'label')}, {pl(review['conflicts'], 'conflict')} " + \
                (f"({pl(review['calls'], 'call')})" if cmd else "(file mode)")
        pc, ch = self.placing, self.choosing
        if pc["calls"] or pc["left"]:  # calls with no line read are a command that did not answer: said, not hidden
            out += (f" · second reading: {pl(pc['lines'], 'line')} read once more, {pc['links']:+d} {'link' if abs(pc['links']) == 1 else 'links'} "
                    f"({pl(pc['calls'], 'call')})" + (f", {pl(pc['left'], 'line')} left for the next dream" if pc["left"] else ""))
        if ch["calls"]:
            out += f" · third reading: {ch['placed']} of {ch['items']} words placed ({pl(ch['calls'], 'call')})"
        cu = self.curate
        if cu["folders"]:
            out += (f" · curator: {pl(cu['folders'], 'folder')}, {pl(cu['joined'], 'name')} joined"
                    + (f", {cu['refused']} refused" if cu["refused"] else "")
                    + (f" ({pl(cu['calls'], 'call')})" if cmd else " (file mode)") + (f", {cu['left']} folders left" if cu["left"] else ""))
        out += f" · {review['decided']} conflicts decided" if review["decided"] else ""
        out += f" · +{review['aliases']} aliases" if review["aliases"] else ""
        for noun, c in (("type", review), ("kind", review["kinds"]), ("tag", review["tags"])):  # one line per list
            out += f" · {pl(c['mapped'], noun)} mapped" if c.get("mapped") else ""
            out += f" · {pl(c['new'], 'new ' + noun)}" if c.get("new") else ""
            out += f" · {pl(c['kept'], noun + ' word')} kept as words" if c.get("kept") else ""
            out += f" · {c['refused']} new {noun}s refused (the list is full, or no definition)" if c.get("refused") else ""
            out += f" · {pl(c['demoted'], noun)} demoted" if c.get("demoted") else ""
        out += f" · {len(self.moved)} moved" if self.moved else ""
        out += f" · {len(self.deleted)} deleted" if self.deleted else ""
        unindexed = sum(1 for n in g["notes"] if not n["indexed"])
        if cmd:
            out += f" · {unindexed} pending"
        elif self.args.prompts or self.args.packets:
            out += f" · {pending} pending"
        elif unindexed:
            out += f" · {unindexed} without entities (no model; `dream --packets` writes them as packets for a helper agent)"
        out += (" · " + " ".join(f"{c}×{n}" for c, n in sorted(codes.items()))) if codes else ""
        out += f" · {self.published}" if getattr(self, "published", "") else ""
        print(out)
        if pending:
            print(f"{pending} prompts listed in {self.pend / 'TODO.md'}: run the memory-dreamer subagent, "
                  "then memory.py dream again")


def write_digest(root, g, now):
    """memory/DIGEST.md (REVIEW.md §8 R3): ≤ 40 lines that can sit in an agent's context every session — Claude Code
    loads it when CLAUDE.md imports it with `@memory/DIGEST.md`. How to ask, the user's own preferences, the newest
    live decisions and models. Deterministic, 0 calls, nothing from anyone else's memory: the digest is read as
    instruction every session, so an origin's notes are not in it."""
    load_domain(root)
    notes = [n for n in g["notes"] if n["project"] != "log" and not origin_of(n["path"])]
    areas = sorted({n["project"] for n in notes if n["project"]})
    me = [n for n in notes if n["project"] == "prefs" and n["id"].startswith("me-") and not n["superseded_by"]]
    load_domain(root)
    heads = sorted(DIGEST_KINDS) or ["decision", "model"]
    live = sorted((n for n in notes if not n["superseded_by"] and n["project"].lower() not in GENERAL
                   and n["kind"] in DIGEST_KINDS), key=lambda n: (n["updated"], n["path"]), reverse=True)
    role = lambda k: ROLE_OF.get(k, ROLE_OF.get(family(k), "reference"))  # noqa: E731
    by_path = {n["path"]: n for n in g["notes"]}
    answered = {e["dst"] for e in g["edges"] if e["rel"] in ("from", "refs")  # an answering kind (finding, decision) built on it
                and by_path[e["src"]]["kind"] in ANSWER_KINDS}
    open_q = sorted((n for n in notes if role(n["kind"]) == "question" and not n["superseded_by"] and n["path"] not in answered),
                    key=lambda n: (n["updated"], n["path"]), reverse=True)
    plural = lambda k: k + ("s" if not k.endswith("s") else "")  # noqa: E731
    head_names = ", ".join(plural(k) for k in heads[:-1]) + (" and " if len(heads) > 1 else "") + plural(heads[-1])
    lines = ["<!-- written by memory.py dream; edit nothing here. To keep it in context every session, import it from "
             "CLAUDE.md with the line: @memory/DIGEST.md -->",
             f"# memory digest · {now.date().isoformat()} · {len(notes)} notes in {len(areas)} areas",
             f"The project's memory is the notes in `memory/<area>/`. Ask it everything in ONE call, tasks included: "
             f"`python3 {Path(__file__).resolve()} ask \"q1\" \"q2\" …`. Write a short note per new fact or decision; "
             "run `dream` at the end of a session."]
    if me:
        lines += ["", "## your own preferences"] + [f"- {n['title'][:140]}" for n in me[:10]]
    if live:
        lines += ["", f"## current: the newest live {head_names}"] + \
                 [f"- {n['updated']} {n['project']}: {n['title'][:120]}" for n in live[:DIGEST_HEADS]]
    if open_q:  # free from kinds and lineage: what is asked and not yet answered
        lines += ["", f"## open questions ({len(open_q)}): nothing has been built on them yet"] + \
                 [f"- {n['updated']} {n['project']}: {n['title'][:120]}" for n in open_q[:8]]
    wr(root / "DIGEST.md", "\n".join(lines[:DIGEST_MAX_LINES]) + "\n")


# ---------- retrieval ----------

class Lazy(dict):
    """A dict that fills a missing key from a function and keeps it."""
    def __init__(self, fn):
        super().__init__()
        self.fn = fn

    def __missing__(self, k):
        v = self[k] = self.fn(k)
        return v


class View:
    """The graph in memory, for ask on small memories."""
    def __init__(self, g):
        self.g = g
        self._names = None
        self.dropped, self.pointers, self.tags = g.get("dropped", []), g.get("pointers", {}), g.get("tags", {})
        self.unplaced = g.get("unplaced", [])
        self.notes = {n["path"]: n for n in g["notes"]}
        self.ents = {e["id"]: e for e in g["entities"]}
        self.out_r, self.in_r = defaultdict(list), defaultdict(list)
        for r in g["relations"]:
            self.out_r[r["s"]].append(r)
            self.in_r[r["o"]].append(r)
        self.frm, self.down = defaultdict(list), defaultdict(list)
        for e in g["edges"]:
            self.frm[e["src"]].append(e)
            self.down[e["dst"]].append(e)

    def name_map(self):
        if self._names is None:
            self._names = defaultdict(set)  # folded name → entity ids, for alias expansion
            for e in self.g["entities"]:
                for x in [e["id"], *e["aka"], *(n["name"] for n in e["names"])]:
                    if len(x) >= 3:
                        self._names[fold(x)].add(e["id"])
        return self._names

    def names_of(self, k):
        return self.name_map().get(k, set())

    def multi_names(self, low):
        """Entity names of 2-3 words that the question spells out."""
        lw = " " + low.replace("-", " ") + " "
        return [(nm, ids) for nm, ids in self.name_map().items()
                if 2 <= len(nm.replace("-", " ").split()) <= 3 and f" {nm.replace('-', ' ')} " in lw]


class SqliteRows:
    """Rows of _dream/index.db for DbView: the seven calls a store answers (stores.py answers the same seven for
    PostgreSQL and Neo4j): notes(), edges_from(p), edges_to(p), rels_out(i), rels_in(i), entity(i), names(k)."""
    def __init__(self, db):
        self.db = db

    def notes(self):
        for p, i, a, t, ln, k, u, sup in self.db.execute("SELECT path, id, area, title, line, kind, updated, sup FROM notes"):
            yield p, i, a, t, ln, k, u, json.loads(sup)

    def edges_from(self, p):
        return self.db.execute("SELECT src, dst, rel FROM edges WHERE src=?", (p,)).fetchall()

    def edges_to(self, p):
        return self.db.execute("SELECT src, dst, rel FROM edges WHERE dst=?", (p,)).fetchall()

    def rels_out(self, i):
        return [(s, t, o, json.loads(ev)) for s, t, o, ev in self.db.execute("SELECT s, type, o, ev FROM rels WHERE s=?", (i,))]

    def rels_in(self, i):
        return [(s, t, o, json.loads(ev)) for s, t, o, ev in self.db.execute("SELECT s, type, o, ev FROM rels WHERE o=?", (i,))]

    def entity(self, i):
        row = self.db.execute("SELECT id, type, home, headline, aka, names FROM ents WHERE id=?", (i,)).fetchone()
        if not row:
            return None
        ms = [(p, json.loads(ls)) for p, ls in self.db.execute("SELECT path, lines FROM ment WHERE eid=?", (i,))]
        return {"id": row[0], "type": row[1], "home": row[2], "headline": row[3], "aka": json.loads(row[4]), "names": json.loads(row[5])}, ms

    def names(self, k):
        return {i for (i,) in self.db.execute("SELECT eid FROM names WHERE k=?", (k,))}


class DbView:
    """Rows on demand, for ask on big memories (index.db) and on a hosted store (stores.py): every note's row, everything
    else read when a question needs it. Notes changed since the dream are read from their text (lineage now; entities
    at the next dream)."""
    def __init__(self, rows, root, man, cur):
        self.rows = rows
        self.notes = {p: {"path": p, "id": i, "project": a, "title": t, "line": ln, "kind": k, "updated": u,
                          "superseded_by": list(sup or [])} for p, i, a, t, ln, k, u, sup in rows.notes()}
        self.dropped, self.pointers, self.tags = man.get("dropped", []), man.get("pointers", {}), man.get("tags", {})
        self.unplaced = man.get("unplaced", [])
        old = {p: f["sha"] for p, f in man.get("files", {}).items()}
        changed = {p for p in cur if old.get(p) != cur[p]["sha"]}
        gone = {p for p in self.notes if p not in cur}
        for p in gone:
            del self.notes[p]
        for n in self.notes.values() if gone else []:  # a note that is gone replaces nothing: naming it here sent ask
            if gone.intersection(n["superseded_by"]):  # to read a file that does not exist (RESULTS phase K)
                n["superseded_by"] = [x for x in n["superseded_by"] if x not in gone]
        mine, added = {}, defaultdict(list)
        if changed:
            stems = defaultdict(list)
            for p in cur:
                stems[posixpath.basename(p)[:-3]].append(p)
            for rel in changed:
                self.notes[rel], mine[rel] = fresh_note(root, rel, cur, stems)
                for e in mine[rel]:
                    added[e["dst"]].append(e)
            for n in self.notes.values():
                if changed.intersection(n["superseded_by"]):
                    n["superseded_by"] = [x for x in n["superseded_by"] if x not in changed]
            for rel, es in mine.items():
                for e in es:
                    if e["rel"] == "supersedes" and e["dst"] in self.notes:
                        self.notes[e["dst"]]["superseded_by"].append(rel)
        skip = changed | gone
        E = lambda rs: [{"src": a, "dst": b, "rel": r} for a, b, r in rs]  # noqa: E731
        self.frm = Lazy(lambda p: mine[p] if p in mine else [e for e in E(rows.edges_from(p)) if e["dst"] in self.notes and p not in skip])
        self.down = Lazy(lambda p: [e for e in E(rows.edges_to(p)) if e["src"] not in skip] + added[p])
        R = lambda rs: [{"s": a, "type": t, "o": b, "evidence": list(ev)} for a, t, b, ev in rs]  # noqa: E731
        self.out_r = Lazy(lambda i: R(rows.rels_out(i)))
        self.in_r = Lazy(lambda i: R(rows.rels_in(i)))
        self.ents = Lazy(self._ent)
        self._names = Lazy(lambda k: set(rows.names(k)))

    def _ent(self, i):
        got = self.rows.entity(i)
        if not got:
            raise KeyError(i)
        e, ms = got
        return {**e, "mentions": [{"path": p, "lines": list(ls)} for p, ls in ms if p in self.notes]}

    def names_of(self, k):
        return self._names[k]

    def multi_names(self, low):
        ws, out = low.replace("-", " ").split(), []
        for n in (2, 3):
            for i in range(len(ws) - n + 1):
                k = fold(" ".join(ws[i:i + n]))
                if self._names[k]:
                    out.append((k, self._names[k]))
        return out


def store_name():
    """The hosted store `MEMORY_STORE` names (ADR-001: postgres, neo4j), or "" for the local index."""
    s = os.environ.get("MEMORY_STORE", "").strip().lower()
    return "" if s in ("", "sqlite", "local", "files") else s


def stores_module():
    """stores.py beside this script: the PostgreSQL and Neo4j backends and the CSV export; imported only when used, so
    the script itself stays standard-library only."""
    import importlib.util
    p = Path(__file__).resolve().parent / "stores.py"
    spec = importlib.util.spec_from_file_location("memory_stores", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def store_rows(root):
    """Rows from the hosted store for ask, or None: no store named, or one that cannot answer (ask says so on stderr and
    reads the local index, so an answer never depends on a database being up)."""
    name = store_name()
    if not name:
        return None
    try:
        return stores_module().rows(name, root)
    except Exception as e:  # noqa: BLE001
        sys.stderr.write(f"memory.py: store {name} unavailable ({type(e).__name__}: {e}); reading the local index\n")
        return None


def store_publish(root, g):
    """After a dream: the graph into the hosted store as a diff (stores.py). -> one report fragment, or ""."""
    name = store_name()
    if not name:
        return ""
    try:
        return stores_module().publish(name, root, g, fold)
    except Exception as e:  # noqa: BLE001
        sys.stderr.write(f"memory.py: store {name}: publish failed ({type(e).__name__}: {e}); the local index is complete\n")
        return f"store {name}: publish failed"


def open_view(root):
    """What ask reads: the hosted store's rows when MEMORY_STORE names one, index.db rows on demand for big memories,
    else the graph in memory."""
    man = rd(root / "_dream" / "manifest.json", {}) or {}
    rows = store_rows(root)
    if rows is not None:
        return DbView(rows, root, man, scan(root, man)[0])
    if len(man.get("files", {})) > WIDE and (root / "_dream" / "index.db").exists():
        cur = scan(root, man)[0]
        if len(cur) > WIDE:
            return DbView(SqliteRows(index_db(root / "_dream")), root, man, cur)
    return View(load(root)[0])


def rebuild(root):
    """The graph again from what is on disk, with no model: the dream's plan, graph and write stages. For the commands
    that change which notes exist (drop, absorb); reading new notes and the review stay with `dream`."""
    dm = Dream(argparse.Namespace(cmd=None, j=1, review=False, all=False, prompts=False, packets=False, dry_run=False), root)
    dm.plan()
    g = dm.demote(dm.graph())
    dm.report(g, dm.write(g))
    return g


def named_in(text, name):
    """Is this name written in the text, as a word of its own? Exact, case aside."""
    return re.search(r"(?<!\w)" + re.escape(name) + r"(?!\w)", text, re.I) is not None


def absorb_read(src):
    """What a folder offers: {note path: text} (a note with no `# ` line gets one from its file name), the registries
    it brings for its own notes, the files not taken with the reason, and the paths whose title was given."""
    take, regs, skip, titled = {}, {}, [], []
    for d, dirs, files in os.walk(src):
        dirs[:] = sorted(x for x in dirs if not x.startswith(".") and x not in ("_dream", "_readings"))
        base = os.path.relpath(d, src).replace(os.sep, "/")
        for f in sorted(x for x in files if not x.startswith(".")):
            rel = f if base == "." else f"{base}/{f}"
            if base == "." and f in ("ALIASES.md", "CONFLICTS.md"):
                regs[f] = read(Path(d) / f)  # what that base decided about its own notes holds inside it
            elif base == "." and f in ("KINDS.md", "TYPES.md", "EDGES.md", "ORIGIN.md", "DIGEST.md", "relations.jsonl", "entities.jsonl"):
                continue  # its words are read through this memory's registries; its graph is read below
            elif not f.endswith(".md"):
                skip.append((rel, "not a .md file"))
            elif f in SKIP:
                skip.append((rel, "a registry or a README is not a note here; rename it to take it"))
            else:
                text = read(Path(d) / f)
                if not text.strip():
                    skip.append((rel, "empty"))
                    continue
                if not parse_note(text)[1]:  # no claim line: the file's name is the best one there is
                    ls = text.split("\n")
                    at = next((j + 1 for j in range(1, min(len(ls), 80)) if ls[j].strip() == "---"), 0) if ls[0].strip() == "---" else 0
                    text = "\n".join(ls[:at] + ["# " + re.sub(r"[-_]+", " ", f[:-3]).strip()] + ls[at:])
                    titled.append(rel)
                take[rel] = text
    return take, regs, skip, titled


def absorb_readings(src, take, titled):
    """The readings that come with the folder, each checked against its note by ground(), the gate every reading
    passes: an entity is kept if its words are in the note, a link if its quote is and both ends are named there.
    Two sources: a memory-dream base's own readings (`_dream/notes/<sha12>.json`), and a graph written by someone
    else's model, `relations.jsonl` (`{from, relation, to, evidence: [note paths]}`) with entity cards (notes whose
    frontmatter has `id:`, and may have `entity_type:` and `aliases:`). A graph with no notes at all becomes one note
    per entity whose lines state its links. -> {note path: reading}, [refused records with the reason]."""
    readings, refused = {}, []
    for cand in (src / "_dream" / "notes", src / "_readings"):
        for rel in (sorted(take) if cand.is_dir() else []):
            raw = (src / rel).read_bytes() if rel not in titled and (src / rel).is_file() else b""
            x = rd(cand / (hashlib.sha256(raw).hexdigest()[:12] + ".json")) if raw else None
            if x and raw == take[rel].encode("utf-8"):
                readings[rel] = ground(x, take[rel])
    rj = src / "relations.jsonl"
    if not rj.is_file():
        return readings, refused
    rels = []
    for i, ln in enumerate(read(rj).splitlines(), 1):
        try:
            r = json.loads(ln) if ln.strip() else None
        except ValueError:
            r = None
            refused.append({"line": i, "why": "relations.jsonl: not JSON"})
        if isinstance(r, dict):
            s, o, t = (str(r.get(a) or r.get(b) or "").strip() for a, b in (("from", "s"), ("to", "o"), ("relation", "type")))
            ev = r.get("evidence") or r.get("sources") or []
            rels.append({"s": s, "o": o, "type": t, "label": str(r.get("label") or t), "evidence": [ev] if isinstance(ev, str) else list(ev)})
    cards = {}
    for rel, text in take.items():  # an entity card: the note that says which entity it is about
        fm = parse_note(text)[0]
        if fm.get("id"):
            names = [fm["id"], fm.get("title", "")] + fm_list(fm.get("aliases"))
            cards[fm["id"]] = {"type": (fm.get("entity_type") or "other").lower(), "names": sorted({n for n in names if n})}
    if not take:  # a graph with no text: one note per entity, a line per link it takes part in
        for i in sorted(({r["s"] for r in rels} | {r["o"] for r in rels}) - {""}):
            mine = [f"{r['s']} {r['label']} {r['o']}." for r in rels if i in (r["s"], r["o"])]
            take[f"entities/{i}.md"] = f"---\ntype: entity\n---\n# {i}\n" + "\n".join(mine) + "\n"
        for r in rels:  # each link is stated on the note of the thing it starts from
            r["evidence"] = [f"entities/{r['s']}.md"]
    names = {i: [i] for r in rels for i in (r["s"], r["o"]) if i}
    names.update({i: c["names"] for i, c in cards.items()})
    cited = defaultdict(list)
    for r in rels:
        got = [e[:-3] + ".md" if e.endswith(".md") else e + ".md" for e in r["evidence"]]
        got = [e for e in got if e in take]
        if not (r["s"] and r["o"] and r["type"]):
            refused.append({**r, "why": "a link needs two things and a word for it"})
        elif not got:
            refused.append({**r, "why": "it cites no note that was taken"})
        for e in got:
            cited[e].append(r)
    for rel, text in take.items():
        if rel in readings:
            continue
        found = {i: [n for n in ns if named_in(text, n)] for i, ns in names.items()}
        found = {i: ns for i, ns in found.items() if ns}
        lines, out = text.split("\n"), []
        for r in cited.get(rel, []):
            if r["s"] not in found or r["o"] not in found:
                refused.append({**r, "why": f"{rel} does not name {r['s'] if r['s'] not in found else r['o']}"})
                continue
            both = [ln for ln in lines if any(named_in(ln, n) for n in found[r["s"]]) and any(named_in(ln, n) for n in found[r["o"]])]
            q = (both or [ln for ln in lines if any(named_in(ln, n) for n in found[r["o"]])])[0].strip()
            out.append({"s": r["s"], "type": r["type"], "label": r["label"], "o": r["o"], "quote": q})
        if found:
            ty = lambda i: cards.get(i, {}).get("type", "other")  # noqa: E731
            readings[rel] = ground({"kind": "note", "entities": [{"id": i, "type": ty(i), "label": ty(i), "as": ns} for i, ns in sorted(found.items())],
                                    "relations": out, "refs": []}, text)
    return readings, refused


def absorb(args, root):
    """`absorb <folder> --as <origin> [--trust preferences] [--yes]`: another base's notes, taken in as an origin.
    Without --yes it reads the folder and prints what it would take and what it would not, and changes nothing. With
    it: the notes go under `<origin>/`, an `ORIGIN.md` says where they came from and what they are trusted for, their
    readings come along checked, and the graph is rebuilt with no model. The origin stays apart: its things are not
    the host's until a line of ALIASES.md joins them, its preferences are not served unless trusted, and `ask` lists
    its notes after the host's own. Absorbing the same origin again replaces it; `drop <origin>` takes it out."""
    src, origin = Path(args.folder).expanduser().resolve(), (args.origin or "").strip().strip("/")
    dd, dst, me = root / "_dream", root / origin, root.resolve()
    why = (f"{args.folder} is not a folder" if not src.is_dir() else
           f"{origin!r} is not a name for a folder" if not re.fullmatch(r"[A-Za-z0-9][\w.-]*", origin) or origin + ".md" in SKIP else
           "the folder and the memory must lie apart" if src == me or me in src.parents or src in me.parents else
           f"{origin}/ exists here and is not an origin: choose another name with --as" if dst.exists() and not (dst / "ORIGIN.md").is_file() else "")
    if why:
        print(f"absorb: {why}")
        sys.exit(2)
    take, regs, skip, titled = absorb_read(src)
    readings, refused = absorb_readings(src, take, titled)
    if not take:
        print(f"absorb: no note in {args.folder}: it takes .md files, or a relations.jsonl" + "".join(f"\n    {rel}: {w}" for rel, w in skip[:10]))
        sys.exit(2)
    g = load(root)[0]
    here = defaultdict(set)  # a name the host uses → where: its things and its notes
    title = {n["path"]: n["title"] for n in g["notes"]}
    for e in g["entities"]:
        if e["mentions"] and not origin_of(e["mentions"][0]["path"]):
            for x in [e["id"], *e["aka"]]:
                here[fold(x)].add(e.get("home") or e.get("headline") or e["mentions"][0]["path"])
    for n in g["notes"]:
        if not origin_of(n["path"]) and n["project"] != "log":
            here[fold(n["id"])].add(n["path"])
    there = defaultdict(set)  # a name the folder uses → its notes that use it
    for rel in take:
        there[fold(posixpath.basename(rel)[:-3])].add(rel)
    for rel, x in readings.items():
        for e in x["entities"]:
            there[fold(e["id"])].add(rel)
    both = sorted(k for k in there if k in here)
    _, alias, drop_, _, _, _ = parse_edges(vocab_texts(root)[0])
    _, talias, tdrop, _, _, _ = parse_edges(domain_texts(root)[1], TYPE_PACKS)
    new_t = Counter(fold(e["type"]) for x in readings.values() for e in x["entities"]
                    if fold(e["type"]) not in talias and fold(e["type"]) not in tdrop and fold(e["type"]) != "other")
    new_r = Counter(fold(r["type"]).lstrip("~") for x in readings.values() for r in x["relations"]
                    if not {fold(r["type"]).lstrip("~"), fold(r.get("label") or "").lstrip("~")} & (set(alias) | set(drop_)))
    areas = Counter(rel.split("/")[0] if "/" in rel else "(its top folder)" for rel in take)
    first = lambda text: next((ln.strip()[:90] for ln in text.split("\n") if ln.startswith("# ")), "")  # noqa: E731
    print(f"absorb {args.folder} as {origin}/ — {len(take)} notes in {len(areas)} areas: "
          + ", ".join(f"{a} {n}" for a, n in sorted(areas.items())[:10]) + (" …" if len(areas) > 10 else ""))
    if titled:
        print(f"  given a title from the file name: {len(titled)} — {', '.join(titled[:6])}" + (" …" if len(titled) > 6 else ""))
    print(f"  not taken: {len(skip)}" + ("".join(f"\n    {rel}: {w}" for rel, w in skip[:10]) + (f"\n    … and {len(skip) - 10} more" if len(skip) > 10 else "")))
    kept = sum(len(x["entities"]) for x in readings.values()), sum(len(x["relations"]) for x in readings.values())
    lost = sum(len(x["dropped"]["entities"]) for x in readings.values()), sum(x["dropped"]["relations"] for x in readings.values())
    print(f"  readings that come with it: {len(readings)} of {len(take)} notes — {kept[0]} things and {kept[1]} links kept; refused "
          f"{lost[0]} things and {lost[1] + len(refused)} links" + ("".join(f"\n    {r.get('s', '')} {r.get('type', '')} {r.get('o', '')}: {r['why']}" for r in refused[:6])))
    print(f"  names both sides use: {len(both)} — they stay two things until a line of ALIASES.md joins them (`- name = {origin}:name`)"
          + "".join(f"\n    {k} — here: {(title.get(sorted(here[k])[0]) or sorted(here[k])[0])[:90]} · there: {first(take[sorted(there[k])[0]])[2:]}" for k in both[:8])
          + (f"\n    … and {len(both) - 8} more" if len(both) > 8 else ""))
    if new_t or new_r:
        print("  words the registries do not know (kept as other/<word>; add a line to TYPES.md or EDGES.md to read them): "
              + ", ".join(f"{w} ×{n}" for w, n in (new_t + new_r).most_common(12)))
    if dst.exists():
        print(f"  {origin}/ is an origin here already: its {sum(1 for _ in dst.rglob('*.md')) - 1} files are replaced")
    if not args.yes:
        print("  nothing is changed yet: run it again with --yes")
        return
    trust = sorted({"answers"} | {w for w in re.split(r"[,\s]+", (args.trust or "").lower()) if w})
    now = dt.datetime.now()
    (dd / "notes").mkdir(parents=True, exist_ok=True)
    with Lock(dd):
        shutil.rmtree(dst) if dst.exists() else None
        for rel, text in take.items():
            wr(dst / rel, text)
        for name, text in regs.items():
            wr(dst / name, text)
        wr(dst / "ORIGIN.md", f"# ORIGIN — {origin}: notes of another base, taken in as data\nfrom: {args.folder}\nabsorbed: {now.date().isoformat()}\n"
                              f"notes: {len(take)}\ntrust: {', '.join(trust)}\n")
        for rel, x in readings.items():
            sha = hashlib.sha256(take[rel].encode("utf-8")).hexdigest()
            wr(dd / "notes" / f"{sha[:12]}.json", {**x, "path": f"{origin}/{rel}", "sha": sha, "model": f"absorb:{origin}",
                                                   "indexed_at": now.isoformat(timespec="seconds")})
        wr(dd / f"absorb-{origin}.json", {"origin": origin, "from": args.folder, "at": now.isoformat(timespec="seconds"), "notes": len(take),
                                           "titled": titled, "not_taken": [{"path": p, "why": w} for p, w in skip], "refused": refused,
                                           "names_both_sides": both, "unknown_words": dict(new_t + new_r)})
        rebuild(root)
    print(f"absorbed {len(take)} notes as {origin}/ (trust: {', '.join(trust)}). What was refused and why: _dream/absorb-{origin}.json. "
          f"`memory.py drop {origin} --yes` takes it out again.")


def drop(args, root):
    """`drop <note | folder> [--yes]`: the one way a note leaves the memory. Without --yes it prints what goes with the
    note and changes nothing. With it: the file and its reading are deleted, one line `dropped: <path> (date) > <what
    it had replaced>` goes to CONFLICTS.md, and the graph is rebuilt with no model. Who had replaced the dropped note
    now replaces what it had replaced; a note made from it alone (`source:`) goes with it; a note built on it
    (`from:`) stays and says so. A file deleted by hand is not a drop: `dream` reports it (C15) and names this command."""
    dd = root / "_dream"
    man = rd(dd / "manifest.json", {}) or {}
    cur, gone = scan(root, man)[0], man.get("gone") or {}
    t = args.target.strip().replace("\\", "/")
    t = (t[2:] if t.startswith("./") else t).rstrip("/")
    paths = sorted(p for p in cur if p.startswith(t + "/"))
    folder = t + "/" if paths else ""
    if not paths:
        c = t if t.endswith(".md") else t + ".md"
        same = sorted(p for p in cur if "/" not in t and posixpath.basename(p) == c)
        paths = [c] if c in cur or c in gone or c in man.get("files", {}) else same if len(same) == 1 else []
        if not paths:
            print(f"drop: no note or folder {args.target!r}" + (f": {', '.join(same)} share that name, give the path" if same else ""))
            sys.exit(2)
    g, S, srcs = load(root)[0], set(paths), {}
    for p in cur:  # what each other note says it was made from: frontmatter, at the top of the file
        text = read(root / p) if p not in S else ""
        if "source:" in text[:1500]:
            made_of = [x if posixpath.splitext(x)[1] else x + ".md" for x in fm_list(parse_note(text)[0].get("source"))]
            if made_of:
                srcs[p] = made_of
    more = True
    while more:  # made from dropped notes and from nothing else: it goes with them
        more = [p for p, s in srcs.items() if p not in S and all(x in S for x in s)]
        S.update(more)
    sup_of, sup_by, built = defaultdict(list), defaultdict(list), defaultdict(list)
    for e in g["edges"]:
        if e["rel"] == "supersedes":
            sup_of[e["src"]].append(e["dst"])
            sup_by[e["dst"]].append(e["src"])
        elif e["rel"] == "from" and e["dst"] in S and e["src"] not in S:
            built[e["dst"]].append(e["src"])
    for p in (p for p in paths if p not in cur):  # already gone: where it stood, by the dream that noticed or the last one
        was = gone.get(p) or old_lineage(dd, [p])[p]
        sup_of[p], sup_by[p] = list(was.get("replaced", [])), [x for x in was.get("replaced_by", []) if x in cur]
        built[p] = [x for x in was.get("built_on_by", []) if x in cur]

    def left(p, seen=frozenset()):
        """What p had replaced, followed through the notes that go with it to the notes that stay."""
        out = []
        for y in sup_of.get(p, []):
            out += [y] if y not in S else left(y, seen | {p}) if y not in seen else []
        return sorted(set(out))

    title = {n["path"]: n["title"] for n in g["notes"]}
    stays = sorted({r for p in S for r in built.get(p, [])})
    print(f"drop {folder or paths[0]}" + (f" — {len(paths)} notes" if folder else f" — {title.get(paths[0], '(the file is already gone)')[:100]}"))
    made = sorted(S - set(paths))
    if made:
        print(f"  made from {'them' if folder else 'it'} alone, dropped as well: {len(made)} — {', '.join(made[:8])}" + (" …" if len(made) > 8 else ""))
    for p in sorted(S):
        old, took = left(p), [x for x in sup_by.get(p, []) if x not in S]
        if old and took:
            print(f"  {p} had replaced {', '.join(old)}; {', '.join(took)} replaced it and will replace "
                  f"{'that' if len(old) == 1 else 'those'} directly")
        elif old:
            print(f"  {p} had replaced {', '.join(old)}, which will be the newest left of its line")
        elif took:
            print(f"  {p} was replaced by {', '.join(took)}")
    if stays:
        print(f"  built on {'them' if len(S) > 1 else 'it'}, kept and marked: {len(stays)} — {', '.join(stays[:8])}" + (" …" if len(stays) > 8 else ""))
    if not args.yes:
        print("  nothing is changed yet: run it again with --yes")
        return
    today = dt.date.today().isoformat()
    mark = lambda p: f"dropped: {p} ({today})" + (f" > {', '.join(left(p))}" if left(p) else "")  # noqa: E731
    lines = [f"dropped: {folder} ({today})"] if folder else []
    lines += [mark(p) for p in sorted(S) if not (folder and p.startswith(folder))
              or left(p) or built.get(p) or any(x not in S for x in sup_by.get(p, []))]  # in a folder: only notes others name
    (dd / "notes").mkdir(parents=True, exist_ok=True)
    with Lock(dd):
        cf = root / "CONFLICTS.md"
        wr(cf, (read(cf) if cf.exists() else CONFLICTS_HEAD).rstrip("\n") + "\n" + "\n".join(lines) + "\n")
        keep = {cur[p]["sha"][:12] for p in cur if p not in S}
        for p in sorted(S):
            (root / p).unlink() if (root / p).exists() else None
            h = cur.get(p, {}).get("sha", "")[:12]
            if h and h not in keep and (dd / "notes" / f"{h}.json").exists():
                (dd / "notes" / f"{h}.json").unlink()  # its reading goes with it
        if folder and folder[:-1] in ORIGINS:  # an origin goes with the files that made it one
            for name in ("ORIGIN.md", "ALIASES.md", "CONFLICTS.md"):
                (root / folder / name).unlink() if (root / folder / name).exists() else None
            (dd / f"absorb-{folder[:-1]}.json").unlink() if (dd / f"absorb-{folder[:-1]}.json").exists() else None
        if folder:  # the folder too, when nothing but its notes was in it
            for d_, _, _ in sorted(os.walk(root / folder), reverse=True):
                os.rmdir(d_) if not os.listdir(d_) else None
            if (root / folder).exists():
                print(f"  {folder} still holds files that are not notes; they are left alone")
        rebuild(root)
    print(f"dropped {len(S)} note{'s' if len(S) != 1 else ''}: {len(lines)} line{'s' if len(lines) != 1 else ''} in CONFLICTS.md. "
          "To undo, restore the file from git and delete its line.")


PROOF = re.compile(r"^\s*-\s*(.+?\?)\s*(?:->|→)\s*(\S+)\s*$")


def proof(root):
    """A memory's own test, kept in memory/SETUP.md as lines `- a question? -> area/note.md`: each question is put to
    `ask` alone and must be answered by a section headed by that note. -> [(question, note, held)]."""
    f = Path(root) / "SETUP.md"
    out = []
    for q, note in ([m.groups() for m in map(PROOF.match, read(f).split("\n")) if m] if f.exists() else []):
        want, buf = note if note.endswith(".md") else note + ".md", io.StringIO()
        with contextlib.redirect_stdout(buf):
            ask(argparse.Namespace(questions=[q], file=None, p=None, budget=None, list=False, kind=None, all=False, tag=None), root)
        heads = [ln[2:].split(" · ")[0] for ln in buf.getvalue().split("\n") if ln.startswith("▸ ")]
        out.append((q, want, any(h == want or h.endswith("/" + want) for h in heads)))
    return out


def check(args, root):
    g, _ = load(root)
    d = g.get("dedup") or {}
    if d:
        print(f"dedup: {d.get('mentions', 0)} entity mentions · {d.get('ids_as_written', 0)} ids as written → "
              f"{d.get('after_folding', 0)} after folding → {d.get('after_aliases_md', 0)} after ALIASES.md → "
              f"{d.get('after_surface_rule', 0)} after the surface rule · kept {len(g['entities'])} "
              f"({d.get('kept_with_home', 0)} with a home note, {d.get('kept_in_2plus_notes', 0)} in 2+ notes, "
              f"{d.get('kept_by_aliases_md', 0)} by ALIASES.md) · dropped {d.get('dropped_one_note', 0)} one-note, "
              f"{d.get('dropped_file_like', 0)} file-like · refused {d.get('refused_versions', 0)} version merges, "
              f"{d.get('refused_not_line', 0)} by not: lines")
    problems = validate(g, set(parse_edges(vocab_texts(root)[0])[0]))
    print(f"contract: schema {g.get('schema')} " + ("ok" if not problems else f"{len(problems)} problems: " + "; ".join(problems[:5])))
    if store_name():
        try:
            print(stores_module().status(store_name(), root))
        except Exception as e:  # noqa: BLE001
            print(f"store {store_name()}: unavailable ({type(e).__name__}: {e})")
    deg = Counter()  # lineage connectivity: "why" and "what came of" can only walk links that were written (phase G)
    for e in g["edges"]:
        if e["rel"] in ("from", "supersedes"):
            deg[e["src"]] += 1
            deg[e["dst"]] += 1
    proj = [n["path"] for n in g["notes"] if not n["superseded_by"] and n["project"] not in GENERAL and n["project"] != "log"]
    loose = [p for p in proj if not deg[p]]
    if proj:
        print(f"lineage: {sum(deg.values()) // 2} from/supersedes links over {len(proj)} live project notes "
              f"({sum(deg.values()) / 2 / len(proj):.1f} per note) · {len(loose)} link to nothing"
              + (": " + ", ".join(loose[:5]) + (" …" if len(loose) > 5 else "") if loose else ""))
    asked = proof(root)
    if asked:
        missed = [(q, n) for q, n, held in asked if not held]
        print(f"proof: {len(asked) - len(missed)} of {len(asked)} questions of SETUP.md are answered by their note"
              + "".join(f"\n  not by {n}: {q}" for q, n in missed))
    by = defaultdict(list)
    for c in g["checks"]:
        by[c["code"]].append(c["msg"])
    if not by:
        print("check: no warnings")
    for code in sorted(by):
        if code == "C5":  # one line, not one per note: a memory used without a model is not a problem
            print(f"C5 ×{len(by[code])}: notes without entities (no model has indexed them; answering is unaffected). "
                  "To add entities and relations: dream with $MEMORY_LLM, or `dream --packets` and memory-dreamer agents.")
            continue
        print(f"{code} ×{len(by[code])}")
        for m in by[code]:
            print(f"  {m}")


def log(args, root):
    now = dt.datetime.now()
    f = root / "log" / f"{now.date().isoformat()}.md"
    f.parent.mkdir(parents=True, exist_ok=True)
    if not f.exists():
        f.write_text(f"# log {now.date().isoformat()}\n\n", encoding="utf-8")
    with f.open("a", encoding="utf-8") as fh:
        fh.write(f"- {now.strftime('%H:%M')} " + (f"[{args.p}] " if args.p else "") + args.text.strip() + "\n")
    print(f"{f.relative_to(root).as_posix()}: logged")


# ---------- ask: grep with memory ----------
# A thin layer on grep: the graph expands each question into grep patterns (aliases, ids), one grep -F
# pass finds the lines, and the graph orders the notes (current first, lineage) and heads them.

STOP = set("""a an and are as at be been being but by can could did do does doing done for from had has have
how i if in into is it its of on or our should so than that the their them then there these they this those
to us was were what when where which while who whom whose why will with would you your about any all also
each more most other some such only same too very just know known tell me give list show say said get make
made much many one we came come happened led lead ended end up""".split())
SYN = {"own": ["owner", "owned by", "maintain"], "owns": ["owner", "owned by", "maintain"],
       "depend": ["uses", "built on", "feeds", "reads"], "train": ["trained on", "fit on"],
       "defin": ["means", "definition"], "prefer": ["wants", "likes"]}
INTENT = {"current": re.compile(r"\b(current|currently|now|latest|today|still|valid|in force|production|live)\b", re.I),
          "down": re.compile(r"\b(came of|come of|became of|outcome|result\w*|happened|follow.?up)\b", re.I),
          "up": re.compile(r"\b(led to|lead to|what led|based on|rests? on|built on|evidence|came from|origin\w*)\b", re.I),
          "why": re.compile(r"\bwhy\b|\breason\b|\bcaused?\b", re.I),
          "dep": re.compile(r"\b(depend\w*|uses?|used by|feeds?|inputs?|downstream|trained on)\b", re.I),
          # a task, not a question: someone's taste and the house rules should shape what gets made
          "task": re.compile(r"^\s*(please\s+)?(make|build|draft|write|prepare|create|put together|set up|design|plot|"
                             r"format|produce|update|add|summari[sz]e|sketch|lay out|turn)\b|\bhow (should|do|would|can) "
                             r"(i|we) (present|show|report|format|chart|plot|write|name|round|label|lay out|display)\b", re.I)}
ART = re.compile(r"\b(chart|plot|graph|table|deck|slide|email|notebook|query|sql|model card|alert|report|page|dashboard|"
                 r"memo|summary|readout|title|label|column|axis|axes|colou?r)s?\b", re.I)
WORD = re.compile(r"[\w@%$][\w.@%/+$-]*")  # \w: words in any script count (REVIEW.md F13)
# A question about a set across the whole memory ("across every project, which model notes …"): `ask` prints its best
# matches, which are not the set, and the map of every note of a big memory is larger than a reader's context (RESULTS
# S7: a session that read it whole under a 100,000-token window was compacted and got 2 of 8). It says which map to grep.
SET_WIDE = re.compile(r"\b(across (every|all|the whole|the memory)|every project|all projects|whole memory|other projects)\b", re.I)
SET_KIND = re.compile(r"\b(?:which|every|all|how many|list)\s+(?:of the\s+)?(?:current\s+|live\s+)?([a-z]+?)s?\s+notes?\b", re.I)
# Read-path constants, each with the measurement that set it (.specs/memory-dream/REVIEW.md F1, F4, F7).
COMPLETE_MAX_NOTES = 200  # only this small a memory is considered for printing whole (reading every note is cheap)
COMPLETE_RATIO = 1.2  # print the whole memory when it costs <= this x the surgical output; then nothing is missed
WEAK_SHARE = 0.5  # weak match: a question word found nowhere, and the best note covers <= this share of the words
# Phase L: an agent answers from what one call shows and takes its silence for absence, so the call has to be complete.
AREA_WHOLE = 16000  # characters: a project folder this small is printed whole when most of a call points at it (on the
#   bank the churn-2026 batch printed 25,322 characters of excerpts and missed gold notes for six of ten questions;
#   the folder is 8,579 characters)
CLOSURE_MAX = 40  # notes named per direction when a question asks what a note rests on, or what rests on it
WHOLE_KEEP = 5  # pointers into a folder printed whole that a question keeps; its other notes are in the folder below.
#   Everything outside the folder stays as it would be alone, so a question loses nothing by the company it keeps
TASTE_MAX, TASTE_FLOOR = 12, 0.15  # taste notes printed (were 6, 0.25): house-rule recall 0.39 -> 0.42, +25% chars
W = {  # the tuned numbers of rank() and route(), in one place (REVIEW.md F9); set in RESULTS rounds 2-4 and phase A
    "entity_named": 0.25,  # boost per mention of an entity the question names by id, as a share of the top score (F4
    #   sweep on a real index: 0.15–0.30 tie; 0.35 and 0.50 lose; a weaker boost for phrase-matched entities and a
    #   ×1.5 for findings and decisions measured nil and were removed)
    "successor_current": 1.1, "successor": 0.85,   # a superseded note lifts its successor, above itself when "current" is asked
    "superseded_current": 0.85,                    # the replaced note stays, below its successor
    "why_parent": 0.6, "down_intent": 0.7, "down_named": 0.5, "up_hop": 0.6,  # lineage walks: why / what came of / based on
    "seeds": 6, "picks": 8, "pick_floor": 0.2, "lines_top": 4, "lines_rest": 2,  # notes considered, printed, lines each
    "route_common": 50, "route_near": 0.9, "route_areas": 8, "route_floor": 0.6,  # big memories: where a question points
    "lineage_lines": 4,  # relatives of the picked notes shown as header + # line (F1: 4 beats 0 and 8; F9: for every question)
    "other_notes": 3,  # notes of other bases (origins) listed after the host's own, two lines each
    "other_floor": 0.8,  # … when one names what the question names, or scores this share of the host's best text match
    "relation_lines": 8, "relation_mode": "inputs", "relation_hops": 2,  # typed-link one-liners (phase I, typed_links()): the
    #   notes of the things a named thing is linked to; "cue" = only over the relation types the question's words point at,
    #   "inputs" = only questions about inputs or users, "always" = any type; input questions walk two hops (inputs of
    #   inputs, the predecessor's inputs).
    #   MEMORY_RELATION_LINES, MEMORY_RELATION_MODE and MEMORY_RELATION_HOPS override them for measurement. Real index,
    #   326 questions (RESULTS I3): inputs · 2 hops · 8 lines takes gold 0.933 → 0.941, complete answers 270 → 274 and
    #   dependency questions 0.853 → 0.920 for +4.6% characters; one hop +1 answer, any-type cues +10% characters for the
    #   same gain, 12 lines +1 more answer for +1% more; nothing else moves.
}
# RELCUE (question words → the relation types worth one hop, phase I), INWARD and INPUT_TYPES are read from the
# `walk:` and `hops:` fields of EDGES.md by walk_tables(); the seed's lines carry the words that used to stand here.


def stem(t):
    for suf in ("ings", "ing", "ies", "ed", "es", "s"):
        if t.isalpha() and t.endswith(suf) and len(t) - len(suf) >= 4:
            return t[:-len(suf)]
    return t


def qterms(q):
    """Question → {grep pattern: weight}: ids strong, numbers kept, words stemmed to prefixes, word pairs."""
    pats, words = {}, []
    for raw in WORD.findall(q):
        t = raw.lower().rstrip(".,;:?!)'\"").strip("-/")
        if len(t) < 2 or t in STOP:
            words.append(None)
            continue
        if re.fullmatch(r"[\d.,]+%?", t):
            pats[t] = max(pats.get(t, 0), 1.5)
        elif re.search(r"[._/@-]", t) or (re.search(r"\d", t) and re.search(r"[a-z]", t)):
            pats[t] = 3.0 if len(t) > 3 else 1.5
            if "-" in t and not re.search(r"\d", t):  # a hyphenated phrase ("call-routing") also searches as its words
                for part in t.split("-"):  # bank: gold 0.888 -> 0.894, numbers 0.969 -> 0.976, +4% chars
                    if len(part) >= 3 and part not in STOP:
                        pats.setdefault(stem(part), 1.0)
        elif len(t) >= 3:
            s = stem(t)
            pats[s] = max(pats.get(s, 0), 1.0)
            for x in SYN.get(s, []):
                pats.setdefault(x, 0.5)
        words.append(t)
    for a, b in zip(words, words[1:]):
        if a and b and a.isalpha() and b.isalpha():
            pats.setdefault(f"{a} {stem(b)}", 1.5)
    return pats


def boundary(p):
    return re.compile(r"(?<![a-z0-9])" + re.escape(p))


def grep_lines(root, pats, areas=None):
    """One `grep -F` pass over the notes (or only these top-level areas) for every pattern → {path: [(line, text)]}.
    Python if grep is missing."""
    hits = defaultdict(list)
    where = [str(root)] if areas is None else [str(root / a) for a in areas if a and (root / a).is_dir()]
    if not pats or not where:
        return hits
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".pat", delete=False, encoding="utf-8") as f:
        f.write("\n".join(sorted(pats)) + "\n")
    out = None
    try:
        r = subprocess.run(["grep", "-rniaF", "--include=*.md", "--exclude-dir=_dream", "-f", f.name, *where],  # -a: a NUL byte must not hide a note
                           capture_output=True, text=True, errors="replace")
        out = r.stdout if r.returncode in (0, 1) else None
    except OSError:
        pass
    finally:
        os.unlink(f.name)
    if out is None:
        for p in (q for w in where for q in Path(w).rglob("*.md")):
            rel = p.relative_to(root).as_posix()
            if rel.startswith("_dream/") or p.name in SKIP:  # the registries are not notes, with grep or without
                continue
            for i, ln in enumerate(read(p).split("\n"), 1):
                if any(x in ln.lower() for x in pats):
                    hits[rel].append((i, ln))
        return hits
    pre = str(root).rstrip("/") + "/"
    for ln in out.splitlines():
        m = re.match(r"(.*?):(\d+):(.*)$", ln)
        if m:
            rel = m.group(1)[len(pre):] if m.group(1).startswith(pre) else Path(m.group(1)).resolve().relative_to(root).as_posix()
            if posixpath.basename(rel) not in SKIP:
                hits[rel].append((int(m.group(2)), m.group(3)))
    return hits


def catalog(v, other=False):
    """Every note's id and `# ` line in one lowercase string, for routing questions to areas: the host's notes, or with
    `other` those of the origins, which are routed apart so that another base never takes a host area's place."""
    paths = sorted(p for p in v.notes if bool(origin_of(p)) == other)
    lines = [(v.notes[p]["id"] + " " + (v.notes[p]["title"] or "")).lower().replace("\n", " ") for p in paths]
    starts, k = [], 0
    for ln in lines:
        starts.append(k)
        k += len(ln) + 1
    return paths, "\n".join(lines), starts


def route(pats, cat):
    """Areas whose note ids and titles match the question best (idf-weighted, each pattern once per area).
    → (areas, hint): at most 8 areas; a hint when many match about equally."""
    paths, text, starts = cat
    terms = defaultdict(list)
    for t, w in pats.items():
        if len(t) < 3 or text.count(t) > max(W["route_common"], len(paths) // 50):  # too common to say where to look
            continue
        hit, i = set(), text.find(t)
        while i >= 0:
            k = bisect.bisect_right(starts, i) - 1
            if i == 0 or not text[i - 1].isalnum():
                hit.add(k)
            i = text.find(t, i + 1)
        idf = math.log(1 + len(paths) / max(1, len(hit)))
        for a in {area_of(paths[k]) for k in hit}:
            terms[a].append(w * idf)
    if not terms:
        return None, ""
    # the same answer every run and on every machine (see rank()): exact sums, and equal areas in name order
    order = sorted(((a, math.fsum(ts)) for a, ts in terms.items()), key=lambda z: (-z[1], z[0]))
    best = order[0][1]
    near = [a for a, s_ in order if s_ >= W["route_near"] * best]
    hint = f"{len(near)} areas match about equally ({', '.join(sorted(near)[:4])}, …): name the project" if len(near) > W["route_areas"] else ""
    return [a for a, s_ in order[:W["route_areas"]] if s_ >= W["route_floor"] * best], hint


LIST_MAX = 150  # lines of `ask --list` before it says how many more there are


def loose_ends(v):
    """What notes name, in their own words, that no note was placed for (C18): {note: [(verb, the words)]}. `ask`
    prints them wherever it prints the note, and says so on a chain that runs through one: a link the memory does not
    hold must not read as a link that is not there (the worn bank, RESULTS phase S)."""
    out = defaultdict(list)
    for u in getattr(v, "unplaced", None) or []:
        out[u["note"]].append(("builds on" if u["field"] == "built_on" else "replaces", " ".join(str(u["quote"]).split())[:120]))
    return out


def drop_marks(v):
    """What `drop` left on the notes that stayed: {note: [dropped notes it was built on]} and {note: [dropped notes
    that had replaced it]}, by id. A header says both, so a reader sees that a chain was cut on purpose."""
    built, newest = defaultdict(list), defaultdict(list)
    for d in getattr(v, "dropped", None) or []:
        i = posixpath.basename(d["path"])[:-3]
        for r in d.get("built_on_by", []):
            built[r].append(i)
        for r in d.get("left_newest", []):
            newest[r].append(i)
    return built, newest


def list_notes(args, v, root=None):
    """`ask --list [-p folder] [--kind K] [--tag T]`: the map, one line per note — path, kind, date, its tags, what it was built on (marked
    when that note has since been replaced), what it replaced, whether it was replaced, and its `# ` line. A question
    whose answer is a set, or a relationship across a folder, is answered by reading these lines; `ask` does not guess
    a list from a question's wording (phase L)."""
    kind = (getattr(args, "kind", None) or "").lower()
    area = lambda p: area_of(p)  # noqa: E731
    here = (lambda p: in_scope(p, {args.p.lower().rstrip("/")})) if args.p else (lambda p: True)  # -p takes an origin whole
    tagged, by_tag = None, getattr(v, "tags", None) or {}
    of_note = defaultdict(list)
    for t, ps in by_tag.items():
        for q in ps:
            of_note[q].append(t)
    tag = fold((getattr(args, "tag", None) or "").lstrip("#"))
    if tag:
        defs, alias = tags_registry(root) if root else ({}, {})
        tag = alias.get(tag, tag)
        if tag not in by_tag:
            print(f"## no note carries the tag {tag}" + (" · tags in use: " + ", ".join(f"{t} ({len(ps)})" for t, ps in sorted(by_tag.items())) if by_tag
                                                             else " · no note has a `tags:` line"))
            return
        tagged = set(by_tag[tag])
    rows = [p for p in sorted(v.notes) if here(p) and (tagged is None or p in tagged)
            and (not kind or kind in (v.notes[p]["kind"], family(v.notes[p]["kind"])))]
    cap = len(rows) if getattr(args, "all", False) else LIST_MAX
    built, newest = drop_marks(v)
    loose = loose_ends(v)
    print(f"## {len(rows)} notes" + (f" of {args.p}/" if args.p else "") + (f" of kind {kind}" if kind else "")
          + (f" tagged {tag}" + (f" ({defs[tag]})" if defs.get(tag) else " (not in TAGS.md: no definition)") if tag else "")
          + " — one line each: built on (a note of another folder with its folder) · replaces · replaced by · used in other folders")
    if args.p:  # what the folder as a whole rests on, and what rests on it, outside itself: first, so that a cut or a
        # compacted read keeps it (RESULTS S8: one session that read four maps cut to 8,000 characters answered from the rest)
        for mark, edges, far, text in (("⇡", v.frm, "dst", f"{args.p}/ rests on {{n}} notes of other folders"),
                                       ("⇣", v.down, "src", f"{{n}} notes of other folders rest on {args.p}/")):
            seen, todo = set(), [p for p in sorted(v.notes) if here(p)]
            start = set(todo)
            while todo:
                for q in sorted(e[far] for e in edges[todo.pop(0)] if e["rel"] == "from"):
                    if q not in seen and q not in start and q in v.notes:
                        seen.add(q)
                        todo.append(q)
            ext = sorted(q for q in seen if not here(q))
            if ext:
                print(f"  {mark} {text.format(n=len(ext))}, directly or through other notes: "
                      + " · ".join(f"{q[:-3]} ({v.notes[q]['kind']})" for q in ext[:CLOSURE_MAX * 2])
                      + (f" · and {len(ext) - CLOSURE_MAX * 2} more" if len(ext) > CLOSURE_MAX * 2 else ""))
    for p in rows[:cap]:
        n = v.notes[p]
        name = lambda q: v.notes[q]["id"] if area(q) == area(p) else q[:-3]  # noqa: E731
        frm = [name(e["dst"]) + (" (replaced)" if v.notes[e["dst"]]["superseded_by"] else "")
               for e in v.frm[p] if e["rel"] == "from" and e["dst"] in v.notes] + [f"{i} (dropped)" for i in built.get(p, [])]
        sup = [name(e["dst"]) for e in v.frm[p] if e["rel"] == "supersedes" and e["dst"] in v.notes]
        out = sorted(e["src"][:-3] for e in v.down[p] if e["rel"] == "from" and e["src"] in v.notes and area(e["src"]) != area(p))
        print(f"▸ {p} · {n['kind']}" + (f" of {origin_of(p)}, another base" if origin_of(p) else "") + f" · {n['updated']}"
              + "".join(f" #{t}" for t in sorted(of_note.get(p, [])))
              + (f" · from {', '.join(frm)}" if frm else "")
              + (f" · supersedes {', '.join(sup)}" if sup else "") + chain_mark(v.notes, n)
              + (f" · its replacement {', '.join(newest[p])} was dropped" if p in newest else "")
              + (f" · used in {', '.join(out)}" if out else "")
              + "".join(f" · {verb} «{words}», no note placed" for verb, words in loose.get(p, []))
              + f" — {n['title'][:110]}")
    if len(rows) > cap:
        print(f"  ({len(rows) - cap} more: narrow it with -p <folder>, --kind <kind> or --tag <tag>, or print them all with --all)")


def ask(args, root):
    v = open_view(root)
    if getattr(args, "list", False):
        return list_notes(args, v, root)
    built, newest = drop_marks(v)
    loose = loose_ends(v)
    ptr_now = {}

    def pointers_of(path):
        """A note's pointers into the project's files, looked up now: the dream found them, the files may have moved on."""
        recs = (getattr(v, "pointers", None) or {}).get(path)
        if recs and path not in ptr_now:
            ptr_now[path] = pointer_states(root, {path: recs}, {path: recs})[0].get(path, [])
        return ptr_now.get(path, [])

    def pointer_lines(path):
        out = [f"  ? it {verb} «{words}», in its own words: no note was placed for that, so it is in no chain here; grep "
               "the folder for it" for verb, words in loose.get(path, [])]
        for r in pointers_of(path)[:4]:
            loc = f"#{r['symbol']}" if r.get("symbol") else f":{r['line']}" + (f' "{r["quote"]}"' if r.get("quote") else "")
            bare = not r.get("symbol") and not r.get("quote")  # held only by the words found there when first seen
            several = (r.get("of") or 0) > 1  # the name is defined, or the words stand, in more than one place
            now = {"intact": (f"at line {r['now']}" + (f", the first of {r['of']} definitions of that name" if several else "")
                              if r.get("symbol") else "still there" + (" (a bare line: weak)" if bare else "")),
                   "moved": f"now at line {r['now']}" + (f", one of {r['of']} lines with those words" if several else ""),
                   "changed": "the symbol is not defined there now" if r.get("symbol") else "those words are not there now",
                   "gone": "the file is gone"}[r["state"]]
            out.append(f"  → {r.get('path') or r['to']}{loc} · {now}")
        return out
    qs = [q.strip() for q in (args.questions or []) for q in q.split("\n") if q.strip()]
    if args.file:
        qs += [q.strip() for q in read(Path(args.file)).split("\n") if q.strip()]
    if not qs:
        print("ask: give one or more questions")
        return
    stems = defaultdict(list)
    for p, n in v.notes.items():
        stems[n["id"].lower()].append(p)
    folders = {area_of(p).lower() for p in v.notes if area_of(p)}  # an origin is named in full: policy-kb/entities
    big, by_area, cat, cat_o = len(v.notes) > WIDE, defaultdict(list), None, None
    for p in v.notes:
        by_area[area_of(p)].append(p)
    general = general_areas(by_area, lambda p: v.notes[p]["kind"])  # by name, or mostly not project work
    # preferences and house rules instruct: an origin's are served only when its ORIGIN.md says `trust: preferences`,
    # and a `me-` note of another base never is
    taste_pool = {p for a in general for p in by_area[a] if not origin_of(p)
                  or ("preferences" in ORIGINS[origin_of(p)]["trust"] and not posixpath.basename(p).startswith("me-"))}
    cc = claude_code_memory(root)  # Claude Code's own memory beside ours: read in the same call, never written
    per_q = []
    for q in qs:
        pats = qterms(q)
        own = list(pats)
        raw = {t.lower().rstrip(".,;:?!)'\"").strip("-/") for t in WORD.findall(q)}  # unstemmed: folder names
        intent = {k for k, rx in INTENT.items() if rx.search(q)}
        low = " " + " ".join(WORD.findall(q.lower())) + " "  # punctuation off: "…about intent model v2?" still names it
        # the index only adds aliases of things the question names: a token that is an entity's id ("churn"), an id-like
        # token that is a recorded name (a digit or separator in it, 4+ chars: "exp-102" — never "model" or "v2", which
        # the dreamer records as names of one model: F9), or a name of 2-3 words spelt out; loose names never become
        # patterns (MEMORY_NO_INDEX=1 switches this off: RESULTS phases D–F)
        # a name the host and another base both use is two things (PLAN §9): unless the question is put to that base,
        # only the host's thing lends its other names, so an absorbed base changes nothing in the host's own answers
        there = bool(ORIGINS) and any(s.split("/")[0] in {o.lower() for o in ORIGINS}
                                       for s in ({args.p.lower()} if args.p else {t for t in raw if t in folders}))
        ours = (lambda ids: {i for i in ids if not (":" in i and i.split(":", 1)[0] in ORIGINS)}) if ORIGINS and not there else (lambda ids: ids)
        by_id = {i for t in pats if " " not in t and 0 < len(ours(v.names_of(fold(t)))) <= 2 for i in ours(v.names_of(fold(t)))
                 if fold(i) == fold(t) or (len(t) >= 4 and pats[t] >= 1.5)} \
            if not os.environ.get("MEMORY_NO_INDEX") else set()
        hit_ents = by_id | ({i for nm, ids in v.multi_names(low) if 0 < len(ours(ids)) <= 2 for i in ours(ids)}
                            if not os.environ.get("MEMORY_NO_INDEX") else set())
        for eid in sorted(hit_ents):
            e = v.ents[eid]
            for x in [e["id"], *e["aka"], *(n["name"] for n in e["names"][:4])]:
                if 3 <= len(x) <= 30 and len(x.split()) <= 3 and len(ours(v.names_of(fold(x)))) <= 2 \
                        and (x == e["id"] or " " in x or re.search(r"[\d._/@-]", x)):  # a plain word is not an alias
                    pats.setdefault(x.lower(), 1.5)
        # "in the aml-alerts project": matched on the question's own words, since the stemmer turns pricing into pric;
        # general areas are not scopes by word ("… in reporting" asks about reporting, -p reporting scopes to it)
        scope = {args.p.lower()} if args.p else {t for t in raw | set(pats) if t in folders and t not in GENERAL}
        scoped_pats = scope | {stem(s) for s in scope} | \
            {stem(p) for s in scope for p in s.split("-") if len(p) >= 3}  # the folder's name is a scope, not a pattern
        named = {p for t in pats for p in stems.get(t, [])} | \
                {p for t in pats for p in ([t] if t in v.notes else [t + ".md"] if t + ".md" in v.notes else [])}
        if scope:
            named = {p for p in named if in_scope(p, scope)}
        areas, hint = None, ""  # None: grep everything (memories up to WIDE notes)
        if big:
            areas = sorted({a for a in by_area if a.lower() in scope or ("/" in a and origin_of(a + "/").lower() in scope)}) if scope else None
            if not scope:  # where to look: titles that match, notes it names, areas that mention the ids it names
                cat = cat or catalog(v)
                areas, hint = route(pats, cat)
                ids = [t for t in own if len(t) >= 4 and re.search(r"[0-9._@-]", t)]
                named = {p for p in named if len(stems.get(v.notes[p]["id"].lower(), ())) <= 3}  # a name used everywhere names nothing
                near = {area_of(p) for p in named if "/" in p}
                for t in ids:  # each id points at the areas that mention it, unless it is mentioned everywhere
                    at = {area_of(m["path"]) for e in ours(v.names_of(fold(t))) for m in v.ents[e]["mentions"]}
                    near |= at if len(at) <= 12 else set()
                near = near if len(near) <= 12 else set()
                near |= {a for a in general if not near}  # no project in sight: the general areas too
                if not areas and not near and ids:  # ids the index does not know: grep everything for them alone
                    near = {area_of(p) for p in grep_lines(root, ids) if "/" in p}
                    near = near if len(near) <= 12 else set()
                areas = sorted(set(areas or []) | near) if areas or near else None
                if ORIGINS and areas is not None:  # and the two areas of other bases that match best, beside the host's
                    cat_o = cat_o or catalog(v, True)
                    areas = sorted(set(areas) | set((route(pats, cat_o)[0] or [])[:2]))
            if "task" in intent and areas is not None:
                areas = sorted(set(areas) | general)
        if not scope and SET_WIDE.search(q):
            km = SET_KIND.search(q)
            k = fold(km.group(1)) if km and fold(km.group(1)) in KINDS else ""
            hint = (f"a set across the whole memory, not these matches: `memory.py ask --list --kind {k} --all` lists every {k} note, "
                    "one line each; pipe it through grep" if k else
                    f"a set across the whole memory, not these matches: `memory.py ask --list --all` lists all {len(v.notes)} notes, one "
                    "line each, more than to read: pipe it through grep, or narrow it with --kind")
        pool = v.notes if areas is None else [p for a in areas for p in by_area[a]]
        paths = {p: [t for t in pats if len(t) >= 4 and t not in scoped_pats and t in p.lower()] for p in pool
                 if not scope or in_scope(p, scope)}
        per_q.append({"q": q, "pats": {t: w for t, w in pats.items() if t not in scoped_pats}, "intent": intent, "hint": hint,
                      "own": set(own), "ents": hit_ents, "by_id": by_id, "named": named, "scope": scope, "areas": areas,
                      "paths": {p: ts for p, ts in paths.items() if ts}})
    groups = defaultdict(list)  # questions that grep the same areas share one grep
    for x in per_q:
        groups[None if x["areas"] is None else tuple(x["areas"])].append(x)
    for areas, xs in groups.items():
        allpats = {p for x in xs for p in x["pats"]}
        hits = grep_lines(root, allpats, areas)
        if args.p:
            hits = {p: h for p, h in hits.items() if in_scope(p, {args.p.lower()})}
        rx = {p: boundary(p) for p in allpats}
        line_pats = {}  # (path, line) → patterns that really match there (word start)
        df, df_host = Counter(), Counter()
        for path, rows in hits.items():
            seen = set()
            for no, text in rows:
                lowt = text.lower()
                ms = {p for p in allpats if p in lowt and rx[p].search(lowt)}
                if ms:
                    line_pats[(path, no)] = (ms, text)
                    seen |= ms
            df.update(seen)
            df_host.update(seen) if ORIGINS and not origin_of(path) else None
        N = max(len(v.notes) if areas is None else sum(len(by_area[a]) for a in areas), 1)
        idf = {p: math.log(1 + N / df[p]) for p in df}
        idf_host = None
        if ORIGINS:  # the host's own notes are ranked as if no other base were there (rank())
            Nh = max(sum(not origin_of(p) for p in (v.notes if areas is None else [p for a in areas for p in by_area[a]])), 1)
            idf_host = {p: math.log(1 + Nh / df_host[p]) for p in df_host}
        by_file = defaultdict(list)
        for (path, no), (ms, text) in line_pats.items():
            by_file[path].append((no, ms, text))
        for x in xs:
            x["ranked"] = rank(x, by_file, idf, v, idf_host)
            x["taste"] = taste(x, by_file, v, taste_pool) if "task" in x["intent"] else []
    cc_search(cc, per_q) if cc else None
    budget = args.budget or 900 * len(qs) + 1500

    # where the call points (phase L): questions asked together are usually about one piece of work. When at least half
    # of them, and two, have a note of one project folder among their first three notes, and the folder is small, it is
    # printed whole once and listed as pointers under each question. A memory small enough to be printed whole is.
    whole = []
    if len(v.notes) > COMPLETE_MAX_NOTES and not args.budget:
        votes = Counter()
        for x in per_q:
            x["tops"] = {area_of(p) for p, _ in x["ranked"][:3]} | {area_of(p) for p in x.get("mine", x["named"])}
            votes.update(x["tops"] - set(general) - {""})
        need = max(2, (len(per_q) + 1) // 2)
        whole = [a for a in sorted(votes) if votes[a] >= need
                 and sum(os.path.getsize(root / p) for p in by_area[a] if (root / p).exists()) <= AREA_WHOLE]

    def closure(start, edges, far):
        """Everything reached from a note through `from:` lines, nearest first: {path: steps}."""
        seen, todo = {}, [(start, 0)]
        while todo:
            p, d = todo.pop(0)
            for q in sorted(e[far] for e in edges[p] if e["rel"] == "from"):
                if q not in seen and q != start and q in v.notes:
                    seen[q] = d + 1
                    todo.append((q, d + 1))
        return seen

    def chain_lines(x):
        """For a question that names a note and asks what it was built on or what came of it: the whole chain each way,
        one line, so no hop is left to a second call (phase L: the first eight were shown, and the rest was missed).
        The notes one step away are named apart from those reached through them: "depends on" is asked both ways."""
        out = []
        if not x["intent"] & {"up", "down", "dep"} or not hasattr(v, "down"):
            return out
        for p in sorted(x.get("mine", x["named"]))[:2]:
            here, nid = area_of(p), v.notes[p]["id"]
            name = lambda q: (v.notes[q]["id"] if area_of(q) == here else q[:-3]) + f" ({v.notes[q]['kind']})"  # noqa: E731
            for mark, got, text in (("⇡", closure(p, v.frm, "dst"), f"{nid} rests on {{n}} notes"),
                                    ("⇣", closure(p, v.down, "src"), f"{{n}} notes rest on {nid}")):
                # a chain is as whole as its notes' links: a note on it that names something no note was placed for
                # may rest on more than is listed, and saying nothing would read as "nothing more"
                gaps = sorted(v.notes[q]["id"] for q in [p, *got] if any(verb == "builds on" for verb, _ in loose.get(q, []))) if mark == "⇡" else []
                if got:
                    ids = sorted(got, key=lambda q: (got[q], q))
                    near = [name(q) for q in ids[:CLOSURE_MAX] if got[q] == 1]
                    far = [name(q) for q in ids[:CLOSURE_MAX] if got[q] > 1]
                    out.append(f"  {mark} {text.format(n=len(ids))} — directly: " + " · ".join(near)
                               + (" — through them: " + " · ".join(far) if far else "")
                               + (f" · and {len(ids) - CLOSURE_MAX} more" if len(ids) > CLOSURE_MAX else ""))
                if gaps:
                    out.append(f"    not the whole chain: {', '.join(gaps[:8])}" + (f" and {len(gaps) - 8} more" if len(gaps) > 8 else "")
                               + " also build" + ("s" if len(gaps) == 1 else "") + " on something named only in words, for which no note "
                               "was placed: " + " · ".join(f"{v.notes[q]['id']} «{words}»" for q in [p, *got] for verb, words in loose.get(q, [])
                                                           if verb == "builds on")[:400] + " — find those with grep")
                if mark == "⇣":
                    there = sorted(v.notes[q]["id"] for q in loose if area_of(q) == here and q != p)
                    if there:
                        out.append(f"    {len(there)} other notes of {here}/ build on something no note was placed for, and it may be {nid}: "
                                   + ", ".join(there[:10]) + (" …" if len(there) > 10 else "") + f" (`ask --list -p {here}` shows their words)")
        return out

    def header(path):
        n = v.notes.get(path)
        if not n:
            return f"▸ {path}"
        s = f"▸ {path} · {n['kind']}" + (f" of {origin_of(path)}, another base" if origin_of(path) else "") + f" · {n['updated']}"
        f = [v.notes[e["dst"]]["id"] for e in v.frm[path] if e["rel"] == "from"] + [f"{i} (dropped)" for i in built.get(path, [])]
        sup = [v.notes[e["dst"]]["id"] for e in v.frm[path] if e["rel"] == "supersedes"]
        s += f" · from {', '.join(f)}" if f else ""
        s += f" · supersedes {', '.join(sup)}" if sup else ""
        stale = sum(r["state"] in ("changed", "gone") for r in pointers_of(path))
        return s + chain_mark(v.notes, n) + (f" · its replacement {', '.join(newest[path])} was dropped" if path in newest else "") \
            + (f" · STALE: {stale} of its pointers no longer hold" if stale else "")

    def body(path):
        """Compact note: title and body lines, no frontmatter, no blanks. A file gone since the dream has none."""
        try:
            ls, n = read(root / path).split("\n"), v.notes.get(path, {})
        except OSError:
            return []
        start = (n.get("line") or 1) - 1
        return [(i + 1, ln) for i, ln in enumerate(ls) if i >= start and ln.strip()]

    picked = {p for x in per_q for p, _ in x["ranked"]}
    full = sum(sum(len(t) + 6 for _, t in body(p)) for p in picked) <= budget

    def render(complete):
        """complete=False: the answering lines under each question. complete=True: each question points at its
        notes, then the whole memory follows once, by area — for small memories, where that costs about the same."""
        printed, out = {}, []
        for x in per_q:
            out.append(f"## {x['q']}")
            if x["hint"]:
                out.append(f"  ({x['hint']})")
            if x.get("weak"):
                out.append(f"  ({x['weak']} — try other words, or grep memory/)")
            for eid in sorted(x["ents"])[:2] if "dep" in x["intent"] else []:
                out.append(entity_line(v, eid))
            out += chain_lines(x)
            here = [a for a in whole if a in x.get("tops", ())] if not complete else []
            if here:
                out.append(f"  ({', '.join(a + '/' for a in here)} is printed whole below: nothing else is recorded there)")
            # the other case said as plainly: a section about a folder the question names, which is not printed whole,
            # holds its best matches and not the set (one agent of phase L read ten notes of 23 and answered "none")
            for a in sorted(a for a in by_area if a.lower() in x["scope"] and a not in here) if not complete else []:
                out.append(f"  (the best matches among the {len(by_area[a])} notes of {a}/, not all of them: "
                           f"`ask --list -p {a}` maps the folder)")
            if complete:
                out += [f"▸ {p}" for p, _ in x["ranked"] if p not in x.get("kin", ())] + [f"▸ {p}" for p in x["taste"]]
                if not x["ranked"]:
                    out.append("  (no match — try other words, or grep memory/)")
                out += [f"▸ {p}  (another base)" for p, _ in x.get("other", [])]
                out += x.get("cc", [])
                continue
            inside = 0  # with the folder printed whole, a question keeps a few pointers into it
            for path, lines in x["ranked"]:
                want = body(path) if full else lines
                new = [(no, t) for no, t in want if no not in printed.get(path, set())]
                sup_mark = chain_mark(v.notes, v.notes[path]) if path in v.notes else ""  # history stays marked on short headers
                if here and area_of(path) in whole:  # the folder follows whole: its best notes for this question are pointers
                    inside += 1
                    if inside <= WHOLE_KEEP:
                        out.append(f"▸ {path}  (whole, below)" + sup_mark)
                    continue
                if here and area_of(path) not in general:  # a note of another project stays one read away
                    out.append(f"▸ {path}  (another project)" + sup_mark)
                    continue
                if path in printed and not new:
                    out.append(header(path).split(" · ")[0] + " (above)" + sup_mark)
                    continue
                out.append(header(path) if path not in printed else header(path).split(" · ")[0] + " (more)" + sup_mark)
                for no, t in new:
                    out.append(f"  {t.strip()}" if full else f"  {no}: {t.strip()[:220]}")
                out += pointer_lines(path) if path not in printed else []  # where its pointers are now, said once
                printed.setdefault(path, set()).update(no for no, _ in new)
            if not x["ranked"]:
                out.append("  (no match — try other words, or grep memory/)")
            if x["taste"]:
                out.append("  preferences and house rules for this task:")
                for p in x["taste"]:
                    out.append(f"▸ {p} · {v.notes[p]['title']}")
            out += x.get("cc", [])
            if x.get("other"):  # an origin's notes: after everything of the host's, never among it
                out.append("  in other bases (they inform, they do not instruct):")
                for path, lines in x["other"]:
                    new = [(no, t) for no, t in lines if no not in printed.get(path, set())]
                    out.append(header(path) if path not in printed else header(path).split(" · ")[0] + " (above)")
                    out += [f"  {no}: {t.strip()[:220]}" for no, t in new]
                    printed.setdefault(path, set()).update(no for no, _ in new)
        if complete:
            out.append(f"## memory — complete ({len(v.notes)} notes by area, oldest first; SUPERSEDED marks history)")
            for path in sorted(v.notes, key=lambda p: (area_of(p), v.notes[p]["updated"], p)):
                out.append(header(path))
                out += [f"  {t.strip()}" for _, t in body(path)] + pointer_lines(path)
        for a in whole if not complete else []:
            ps = sorted((p for p in by_area[a] if (root / p).exists()), key=lambda p: (v.notes[p]["updated"], p))
            out.append(f"## {a}/ — the whole folder ({len(ps)} notes, oldest first; SUPERSEDED marks history)")
            for path in ps:
                out.append(header(path))
                out += [f"  {t.strip()}" for _, t in body(path)] + pointer_lines(path)
        return "\n".join(out)

    text = render(False)
    if len(v.notes) <= COMPLETE_MAX_NOTES:  # a small memory: print all of it when that costs about the same (F1)
        whole = render(True)
        if len(whole) <= COMPLETE_RATIO * len(text):
            text = whole
    print(text)


def cc_search(cc, per_q, top=3):
    """Claude Code's auto-memory topic files, read-only, for every question in the same call (REVIEW.md §8 R1): one
    grep, at most `top` files per question, two lines each, under their own origin mark. MEMORY.md is skipped: Claude
    Code already loads it. Sets x["cc"] (printable lines) on each question."""
    allpats = {t for x in per_q for t in x["pats"]}
    if not allpats:
        return
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".pat", delete=False, encoding="utf-8") as f:
        f.write("\n".join(sorted(allpats)) + "\n")
    try:
        r = subprocess.run(["grep", "-rniaF", "--include=*.md", "--exclude=MEMORY.md", "-f", f.name, str(cc)],
                           capture_output=True, text=True, errors="replace")
        out = r.stdout if r.returncode in (0, 1) else ""
    except OSError:
        out = ""
    finally:
        os.unlink(f.name)
    hits = defaultdict(list)
    for ln in out.splitlines():
        m = re.match(r"(.*?):(\d+):(.*)$", ln)
        if m:
            hits[os.path.relpath(m.group(1), cc)].append((int(m.group(2)), m.group(3)))
    if not hits:
        return
    rx = {p: boundary(p) for p in allpats}
    meta = {}
    for f_ in hits:
        fm, _, _, _ = parse_note(read(cc / f_))
        up = (fm.get("modified") or fm.get("updated") or "")[:10]
        meta[f_] = (fm.get("type", "memory"), up if re.match(r"\d{4}-\d\d-\d\d", up) else
                    dt.date.fromtimestamp((cc / f_).stat().st_mtime).isoformat())
    for x in per_q:
        score, best = {}, {}
        for f_, rows in hits.items():
            lines = []
            for no, text in rows:
                ms = {p for p in x["pats"] if p in text.lower() and rx[p].search(text.lower())}
                if ms:
                    w = sum(x["pats"][p] for p in ms)
                    lines.append((w, no, text))
            if lines:
                score[f_] = sum(w for w, _, _ in lines) + max(w for w, _, _ in lines)
                best[f_] = sorted(lines, key=lambda z: (-z[0], z[1]))[:2]
        picks = sorted(score.items(), key=lambda z: (-z[1], z[0]))[:top]
        picks = [(f_, s) for f_, s in picks if s >= 0.3 * picks[0][1]] if picks else []
        if picks:
            x["cc"] = ["  also in Claude Code's memory:"]
            for f_, _ in picks:
                x["cc"].append(f"▸ claude-code: {f_} · {meta[f_][0]} · {meta[f_][1]}")
                x["cc"] += [f"  {no}: {t.strip()[:220]}" for _, no, t in sorted(best[f_], key=lambda z: z[1])]


def taste(x, by_file, v, pool):
    """A task ("make the chart for Chloe's readout") → the preferences and house rules that should shape it. Scored
    inside the general areas only, so project notes that share a word cannot crowd them out. A person (or a family of
    rules) named in the task, or matched through their meetings and reports, brings all their notes; rules about the
    artifact asked for (chart, table, deck …) come along."""
    pats, n = x["pats"], max(len(pool), 1)
    cand = {p: rows for p, rows in by_file.items() if p in pool and p in v.notes}
    df = Counter(t for rows in cand.values() for t in {t for _, ms, _ in rows for t in ms})
    score = {}
    for p, rows in cand.items():
        got = Counter()
        for no, ms, _ in rows:
            for t in ms:
                if t in pats:
                    got[t] += 2 if no == v.notes[p]["line"] else 1
        s_ = math.fsum(pats[t] * math.log(1 + n / df[t]) * (2 if " " in t else 1) for t in got)  # exact: see rank()
        if s_:
            score[p] = s_
    fam = defaultdict(list)  # a family = notes sharing the first two words of their id: prefs/<first>-<last>-* is one
    # person, reporting/chart-style-* one family of rules. Each rule below was measured (RESULTS phase F): dropping the
    # family-word rule costs 7 pts of house rules, the context rule 6 pts of implicit prefs, the artifact rule 4 pts
    for p in pool:
        parts = v.notes[p]["id"].lower().split("-")
        if len(parts) >= 3 and parts[0].isalpha() and parts[1].isalpha():
            fam[f"{parts[0]}-{parts[1]}"].append(p)
    fam = {k: ps for k, ps in fam.items() if len(ps) >= 2}
    words = re.findall(r"[a-z]+", re.sub(r"'s\b", "", x["q"].lower()))
    firsts = defaultdict(set)
    for k in fam:
        firsts[k.split("-")[0]].add(k)
    named = {k for k in fam if k in {f"{a}-{b}" for a, b in zip(words, words[1:])}}
    named |= {next(iter(ks)) for f, ks in firsts.items() if len(ks) == 1 and f in words}  # "chart" → chart-style-*; "maya" → maya-ortiz-*
    for p, _s in sorted(score.items(), key=lambda z: (-z[1], z[0]))[:3]:  # two hops: a person named in a matched house note
        for _no, _ms, txt in cand.get(p, []):  # (the roster of their meeting, their report) is the audience
            if not any(t in pats for t in _ms):  # a line only another question of this call matched is not this task's
                continue
            low_t = txt.lower()
            for k in fam:
                if k not in named and re.search(r"\b" + k.replace("-", "[ -]") + r"\b", low_t):
                    named.add(k)
    top = max(score.values(), default=0) or 1.0
    for k in named:
        for p in fam[k]:
            score[p] = score.get(p, 0) + top + 1
    for k, ps in fam.items():  # matched through context (their meeting, their report): the whole person comes along
        got = math.fsum(score.get(p, 0) for p in ps)
        if k not in named and got >= 0.5 * top:
            for p in ps:
                score[p] = max(score.get(p, 0), 0.6 * got)
    arts = {stem(m.group(1).lower()) for m in ART.finditer(x["q"])}
    for p in pool:
        t = (v.notes[p]["title"] or "").lower()
        if arts and any(re.search(r"\b" + re.escape(a), t) for a in arts):
            score[p] = score.get(p, 0) + 0.5 * top
        if v.notes[p]["id"].lower().startswith("me-"):  # your own taste applies to every task
            score[p] = score.get(p, 0) + 0.5 * top
    shown = {p for p, _ in x["ranked"]}
    ranked = sorted(((p, s_) for p, s_ in score.items() if p not in shown), key=lambda z: (-z[1], z[0]))
    return [p for p, s_ in ranked[:TASTE_MAX] if s_ >= TASTE_FLOOR * ranked[0][1]] if ranked else []


def rank(x, by_file, idf, v, idf_host=None):
    """Score notes by the patterns they contain (idf-weighted, title lines count double), then apply the
    graph: named notes first, successors of superseded notes, children for lineage, parents for why.
    Greedy pick that discounts patterns already covered. → [(path, [(line, text)])]

    The same question gets the same notes on every run and every machine: scores are exact sums (math.fsum: adding
    the same terms in another order cannot move a score by a last bit) and every sort ends on the path or the line
    number, so equal scores never fall back on the order grep listed the files in or on Python's per-process hash
    seed. Before this, of 1,149 questions on the bank 9-14 printed differently under another hash seed and 4 with
    the files listed in another order (RESULTS phase J; tests/acceptance.py A42)."""
    pats, intent = x["pats"], x["intent"]
    # Another base's notes (an origin) are data beside the host's, not among them: unless the question names the
    # origin, the host's notes are ranked exactly as if it were not there, and its best notes are listed after them.
    apart = bool(ORIGINS) and not any(s.split("/")[0] in {o.lower() for o in ORIGINS} for s in x["scope"])
    theirs, idf_all, named = {}, idf, x["named"]
    if apart:
        theirs = {p: rows for p, rows in by_file.items() if origin_of(p)}
        by_file = {p: rows for p, rows in by_file.items() if not origin_of(p)}
        idf = idf_host if idf_host is not None else idf
        named = {p for p in named if not origin_of(p)}
    x["mine"] = named  # the notes the question names that the answer is about: the host's, unless it names an origin

    def matched(path, rows):
        """The patterns a note contains, its `# ` line counting double."""
        n = v.notes.get(path)
        tl, got = (n["line"] if n else 0), Counter()
        for no, ms, _ in rows:
            for p in ms:
                if p in pats:
                    got[p] += 2 if no == tl else 1
        return got
    base = {}
    for path, rows in by_file.items():
        got = matched(path, rows)
        if got:
            base[path] = got
    score = {p: math.fsum(pats[t] * idf[t] * (1 + math.log(c)) for t, c in got.items()) for p, got in base.items()}
    for p, ts in x["paths"].items():  # the slug names the thing: count it like a title hit
        if not (apart and origin_of(p)):
            score[p] = score.get(p, 0) + math.fsum(pats.get(t, 1) * idf.get(t, 1) for t in ts)
    if x["scope"]:
        score = {p: s_ for p, s_ in score.items() if in_scope(p, x["scope"])}
    top = max(score.values(), default=0) or 1.0
    for p in named:
        score[p] = score.get(p, 0) + top + 1
    inside = {a.lower() for a in (x["scope"] or x.get("areas") or ())}
    for eid in x["by_id"]:  # notes that mention an entity the question names by id (phrase matches only add aliases)
        for m in v.ents[eid]["mentions"]:
            if (inside and not in_scope(m["path"], inside)) or (apart and origin_of(m["path"])):
                continue
            score[m["path"]] = score.get(m["path"], 0) + W["entity_named"] * top
    up = intent & {"up", "why", "dep"}
    seeds = sorted(score.items(), key=lambda z: (-z[1], z[0]))[:W["seeds"]]
    best_live = next((p for p, _ in seeds if v.notes.get(p) and not v.notes[p]["superseded_by"]), None)
    for p, s in seeds:
        n = v.notes.get(p)
        if not n:
            continue
        for succ in n["superseded_by"]:
            for q in [succ] + successors(v.notes, succ):  # the whole chain to the live end (phase H)
                score[q] = max(score.get(q, 0), s * (W["successor_current"] if "current" in intent else W["successor"]))
            if "why" in intent:  # why it was replaced: what the successor built on
                for e in v.frm[succ]:
                    if e["rel"] in ("from", "refs") and e["dst"] != p:
                        score[e["dst"]] = max(score.get(e["dst"], 0), s * W["why_parent"])
        if "current" in intent and n["superseded_by"]:
            score[p] = s * W["superseded_current"]  # still shown (answers cite what was replaced), below its successor
        if "down" in intent or (p in named and not up and len(named) == 1) or \
                ("current" in intent and p == best_live):
            for e in v.down[p]:
                if e["rel"] in ("from", "refs"):
                    score[e["src"]] = max(score.get(e["src"], 0), s * (W["down_intent"] if "down" in intent else W["down_named"]))
        if up:  # ancestors, two hops
            frontier = [(p, s)]
            for _ in range(2):
                nxt = []
                for q_, sq in frontier:
                    for e in v.frm[q_]:
                        if e["rel"] in ("from", "refs"):
                            w = sq * W["up_hop"]
                            score[e["dst"]] = max(score.get(e["dst"], 0), w)
                            nxt.append((e["dst"], w))
                frontier = nxt
    for p in list(score):  # a superseded note never outranks its live successor; it stays right below it (phase E:
        n = v.notes.get(p)  # on 104 stale-vs-current questions the successor came first in 70% → 95%, gold −0.003)
        for succ in (n["superseded_by"] if n else []):
            end = ([succ] + successors(v.notes, succ))[-1]  # the live end of the chain (phase H)
            if v.notes.get(end) and not v.notes[end]["superseded_by"]:
                score[end] = max(score.get(end, 0), score[p] * 1.001)
    ranked = sorted(score.items(), key=lambda z: (-z[1], z[0]))
    picks = [(p, sc) for p, sc in ranked[:W["picks"]] if sc >= W["pick_floor"] * ranked[0][1]] if ranked else []
    # weak match (F4): a word of the question occurs nowhere in the memory and the best note covers at most half of
    # the question's words — say so instead of heading an unrelated note like a hit
    content = {t for t in x["own"] if pats.get(t, 0) >= 1 and " " not in t  # the question's own words, not aliases;
               and not ("-" in t and not re.search(r"\d", t))}  # a hyphenated phrase is judged by its words
    missing = sorted(t for t in content if t not in idf)
    hit = set(base.get(picks[0][0], {})) if picks else set()
    strong = any(pats.get(t, 0) >= 1.5 for t in hit if t in x["own"])  # an id, number or word pair of the question matched
    ids_missing = [t for t in missing if re.search(r"\d|[._/@]", t)]  # an id, version or number the question names and
    x["weak"] = ""  # no note mentions: always said, even when its neighbours match (phase G absence set: 97% flagged)
    if picks and (ids_missing or (missing and not strong and content and len(hit & content) <= WEAK_SHARE * len(content))):
        said = (ids_missing or missing)[:3]
        x["weak"] = "weak match: " + ", ".join(f"'{t}'" for t in said) + \
            (" found only in another base, below" if apart and all(t in idf_all for t in said) else " found nowhere in memory")
    # The other bases' best notes for this question, by the words alone. One is listed when it speaks of what the
    # question names (the note itself, or an id the question wrote: letters with a digit or a separator, four
    # characters or more), or matches as well as the host's own best. A common word, a year or `v2` shared with
    # another base is no reason to quote it, and a question put to one of the host's projects is not put to it.
    x["other"] = []
    said = {t for t in x["own"] if len(t) >= 4 and re.search(r"[a-z]", t) and re.search(r"[0-9._@-]", t)}
    osc = {}
    for p, rows in ({} if x["scope"] else theirs).items():
        got = matched(p, rows)
        s_ = math.fsum(pats[t] * idf_all[t] * (1 + math.log(c)) for t, c in got.items())
        if p in x["named"] or said & set(got) or (s_ and s_ >= float(os.environ.get("MEMORY_OTHER_FLOOR", W["other_floor"])) * top):
            osc[p] = (s_, p in x["named"])
    for p in sorted(osc, key=lambda p: (not osc[p][1], -osc[p][0], p))[:W["other_notes"]]:
        n = v.notes.get(p)
        rows = sorted((r for r in theirs[p] if not n or r[0] >= n["line"]),
                      key=lambda r: (-math.fsum(pats.get(t, 0) * idf_all.get(t, 0) for t in r[1]), r[0]))
        lines = {(no, t) for no, _, t in rows[:W["lines_rest"]]}
        if n and n["line"]:
            lines.add((n["line"], "# " + n["title"]))
        x["other"].append((p, sorted(lines)))
    if os.environ.get("MEMORY_DEBUG"):
        sys.stderr.write(f"Q {x['q']} intent={sorted(intent)} named={sorted(x['named'])}\n  pats={pats}\n")
        for p, s in sorted(score.items(), key=lambda z: (-z[1], z[0]))[:12]:
            sys.stderr.write(f"  {s:7.2f} {p}{' PICK' if p in dict(picks) else ''}\n")
    res = []
    for k, (p, _) in enumerate(picks):
        n = v.notes.get(p)
        rows = sorted((r for r in by_file.get(p, []) if not n or r[0] >= n["line"]),  # body lines; the header has the lineage
                      key=lambda r: (-math.fsum(pats.get(t, 0) * idf.get(t, 0) for t in r[1]), r[0]))
        keep = rows[:W["lines_top"] if k < 2 else W["lines_rest"]]
        lines = {(no, t) for no, _, t in keep}
        if n and n["line"]:
            lines.add((n["line"], "# " + n["title"]))
        res.append((p, sorted(lines)))
    # lineage one-liners (phase F): the picked notes' nearest relatives — parents, successors, and children for "what
    # came of" — come along as a header plus their # line. For every question: a trigger (lineage intents or 2+ ids
    # named) measured −7 complete answers on the real index for −3% characters (F9)
    if W["lineage_lines"]:
        have, extra = {p for p, _ in res}, []
        for p, _ in res:
            kin = [e["dst"] for e in v.frm[p] if e["rel"] in ("from", "supersedes")] + \
                  [e["src"] for e in v.down[p] if e["rel"] == "supersedes"] + \
                  ([e["src"] for e in v.down[p] if e["rel"] == "from"] if "down" in intent else [])
            for q_ in kin:
                n = v.notes.get(q_)
                if n and q_ not in have and n["line"]:
                    have.add(q_)
                    extra.append((q_, [(n["line"], "# " + n["title"])]))
                if len(extra) >= W["lineage_lines"]:
                    break
            if len(extra) >= W["lineage_lines"]:
                break
        x["kin"] = {q_ for q_, _ in extra}  # the complete print lists them with the memory, not as pointers
        res += extra
    # typed-link one-liners (phase I): the notes of the things the index links a named thing to (typed_links)
    n_rel = int(os.environ.get("MEMORY_RELATION_LINES", W["relation_lines"]))
    if n_rel:
        extra, cued = typed_links(x, v, {p for p, _ in res}, n_rel, int(os.environ.get("MEMORY_RELATION_HOPS", W["relation_hops"])),
                                  os.environ.get("MEMORY_RELATION_MODE", W["relation_mode"]))
        x["kin"] = set(x.get("kin", set())) | {q_ for q_, _ in extra}
        res += extra
        if os.environ.get("MEMORY_DEBUG"):
            sys.stderr.write(f"  typed links: cued={sorted(cued)} by_id={sorted(x['by_id'])} added={[q_ for q_, _ in extra]}\n")
    return res


# INPUT_TYPES: the input relations (`hops: 2` in EDGES.md): the two-hop walk follows these and `from:` lineage.


def typed_links(x, v, have, n_rel, hops, mode):
    """Phase I: for a thing the question names by id, the notes of the things the index links it to. One hop over the
    relation types the question's words point at (RELCUE: inputs → uses, trained-on; owner → owned-by; holdout →
    evaluated-on; …), or any type in "always" mode. For input questions a second hop: the inputs of the inputs and the
    inputs of the thing's predecessor (a version inherits what it did not replace), through typed relations and `from:`
    lineage alike; "what uses X" walks the other way, to the users. Each linked thing comes as its own note, or its
    headline note, at the live end. -> ([(note, [(line, "# title")])] in depth order, at most n_rel; the cued types)."""
    cued = {t for t, rx in RELCUE.items() if rx.search(x["q"])}
    if mode == "inputs":  # only questions about what a thing is built from, or what is built on it
        cued &= INPUT_TYPES
    if not x["by_id"] or not (cued or mode == "always"):
        return [], cued
    inward, input_q = bool(INWARD.search(x["q"])), bool(cued & INPUT_TYPES)

    def ent(i):
        try:
            return v.ents[i]
        except KeyError:
            return None

    def note_of(e):
        home = e["home"] or e["headline"]
        if not home or home not in v.notes:
            return None
        chain = successors(v.notes, home)
        return chain[-1] if chain else home

    def step(eid, depth):
        """One step from a thing: (note, linked thing or None, relation type, its entity) for each link worth a line."""
        out, types = [], (cued or None) if depth == 1 else (cued & INPUT_TYPES)
        rels = (v.in_r[eid] if inward else v.out_r[eid]) if input_q else v.in_r[eid] + v.out_r[eid]
        for r in rels:
            if types is not None and r["type"] not in types:
                continue
            other = r["o"] if r["s"] == eid else r["s"]
            oe = ent(other) if other != eid else None
            q_ = note_of(oe) if oe else None
            if q_:
                out.append((q_, other, r["type"], oe))
        if input_q:  # lineage is the same walk without the index: the parents (inputs) or children (users) of its note
            e = ent(eid)
            home = e["home"] if e else None
            if home and home in v.notes:
                kin = [e_["src"] for e_ in v.down[home] if e_["rel"] == "from"] if inward else \
                      [e_["dst"] for e_ in v.frm[home] if e_["rel"] == "from"]
                out += [(q_, None, "from", None) for q_ in kin if q_ in v.notes]
        return out

    cands, seen, frontier = [], set(x["by_id"]), [(i, 1) for i in sorted(x["by_id"])]
    if input_q and hops >= 2 and not inward:  # the predecessor's inputs
        for i in sorted(x["by_id"]):
            e = ent(i)
            home = e["home"] if e else None
            for e_ in (v.frm[home] if home and home in v.notes else []):
                if e_["rel"] == "supersedes":
                    pid = v.notes[e_["dst"]]["id"]
                    if ent(pid) and pid not in seen:
                        seen.add(pid)
                        frontier.append((pid, 2))
    while frontier:
        nxt = []
        for eid, depth in frontier:
            for q_, other, t, oe in step(eid, depth):
                cands.append(((depth, 0 if t in cued or t == "from" else 1, t.startswith("other/"), -(len(oe["mentions"]) if oe else 0), q_), q_))
                if other and other not in seen and depth < hops and input_q:
                    seen.add(other)
                    nxt.append((other, depth + 1))
        frontier = nxt
    extra, got = [], set(have)
    for _, q_ in sorted(cands):
        n = v.notes.get(q_)
        if q_ in got or not n or not n["line"]:
            continue
        got.add(q_)
        extra.append((q_, [(n["line"], "# " + n["title"])]))
        if len(extra) >= n_rel:
            break
    return extra, cued


def entity_line(v, eid):
    e = v.ents[eid]
    parts = []
    for arrow, rs, end in (("←", v.in_r[eid], "s"), ("→", v.out_r[eid], "o")):
        grp = defaultdict(list)
        for r in rs:
            grp[r["type"]].append(r[end])
        parts += [f"{arrow} {t}: {', '.join(sorted(set(xs))[:8])}" for t, xs in sorted(grp.items())]
    return f"= {eid} ({e['type']}" + (f"; aka {', '.join(e['aka'][:3])}" if e["aka"] else "") + ") " + " · ".join(parts[:6])


def export(args, root):
    """The graph as CSV + Cypher for a graph database (neo4j-admin database import, or LOAD CSV); no driver needed."""
    g, _ = load(root)
    print(stores_module().export_csv(root, g, Path(args.to), fold))


def viz(args, root):
    """Write the HTML viewer (default memory/_dream/graph.html; `dream` refreshes it too) and the knowledge-graph page."""
    g, _ = load(root)
    if len(g["notes"]) > WIDE and not args.out:
        n = write_viz_big(root, g, root / "_dream", force=True)
        print(f"{root / '_dream' / 'graph.html'}: overview of {len(g['notes'])} notes; {n} area pages in "
              f"{root / '_dream' / 'viz'} — open it in a browser")
    else:
        out = Path(args.out).expanduser() if args.out else root / "_dream" / "graph.html"
        write_viz(root, g, out)
        print(f"{out}: {len(g['notes'])} notes, {len(g['entities'])} entities — open it in a browser")
    if args.out:
        return
    kg = root / "_dream" / "knowledge-graph.html"
    print(f"{kg}: the things and their links alone, to show people" if write_kg(root, g, kg, args.theme)
          else "no knowledge-graph page: no two things are linked yet (a dream with a model command reads the links)")


def viz_template():
    return read(Path(__file__).resolve().parent.parent / "assets" / "viz.html")


def render_viz(data, out, tpl=None):
    tpl = tpl or viz_template()
    island = "{\n" + ",\n".join(f'"{k}": ' + ("[\n" + ",\n".join(json.dumps(r, ensure_ascii=False) for r in v) + "\n]"
                                             if isinstance(v, list) else json.dumps(v)) for k, v in data.items()) + "\n}\n"
    a = tpl.index('id="data-graph"')
    a = tpl.index("\n", a) + 1
    wr(out, tpl[:a] + island.replace("</", "<\\/") + tpl[tpl.index("</script>", a):])


def note_text(root, n):
    try:
        ls = read(root / n["path"]).split("\n")
    except OSError:
        ls = []
    return [x for x in ls[(n["line"] or 1) - 1:] if x.strip()][:60]  # the whole note (40 lines by rule): the viewer reads it


def write_viz(root, g, out):
    """A self-contained HTML viewer of the graph: map, overview, explorer, health."""
    render_viz({"schema": g.get("schema", SCHEMA), "built": g["built"], "families": {"kinds": KIND_PARENT, "types": TYPE_PARENT},
                "tags": g.get("tags", {}), "tag_defs": tags_registry(root)[0], "origins": sorted(ORIGINS),  # the page's filters
                "notes": [{**n, "text": note_text(root, n)} for n in g["notes"]],
                "entities": g["entities"], "relations": g["relations"], "edges": g["edges"], "checks": g["checks"],
                "review": g["review"], "proposed": g["proposed"], "conflicts": g.get("conflicts", [])}, out)


def write_viz_big(root, g, dd, force=False):
    """Big memories: _dream/graph.html is an overview of areas, _dream/viz/<area>.html one viewer per area, rewritten
    only when something in the area changed. → number of area pages written."""
    def area(p):
        return p.split("/")[0] if "/" in p else "(root)"
    tpl = viz_template()
    notes = {n["path"]: n for n in g["notes"]}
    by, e_by, m_by, r_by, c_by = (defaultdict(list) for _ in range(5))
    for n in g["notes"]:
        by[area(n["path"])].append(n)
    for e in g["edges"]:
        for a in {area(e["src"]), area(e["dst"])}:
            e_by[a].append(e)
    for e in g["entities"]:
        ms = defaultdict(list)
        for m in e["mentions"]:
            ms[area(m["path"])].append(m)
        for a, mm in ms.items():
            m_by[a].append((e, mm))
    for r in g["relations"]:
        for a in {area(ev.rsplit(":", 1)[0]) for ev in r["evidence"]}:
            r_by[a].append(r)
    checks = [c for c in g["checks"] if c["code"] != "C5"]
    for c in checks:
        head = c["msg"].split(":")[0]
        if "/" in head:
            c_by[area(head)].append(c)
    pages = dd / "viz"
    pages.mkdir(parents=True, exist_ok=True)
    old = rd(pages / "_sig.json", {}) or {}
    sigs, wrote = {}, 0
    tag_defs = tags_registry(root)[0]
    tsig = hashlib.sha1(tpl.encode()).hexdigest()[:12]
    for a, ns in by.items():
        mine = {n["path"] for n in ns}
        atags = {t: [q for q in ps if q in mine] for t, ps in sorted(g.get("tags", {}).items()) if mine.intersection(ps)}
        sig = hashlib.sha1(json.dumps([tsig, atags, {t: tag_defs.get(t) for t in atags},
                                       [[n["path"], n["sha"], n["kind"], n["superseded_by"]] for n in ns],
                                       [[e["src"], e["dst"], e["rel"]] for e in e_by[a]],
                                       [[e["id"], e["type"], e["home"]] for e, _ in m_by[a]],  # not names: a hub's new spelling would redraw everything
                                       [[r["s"], r["type"], r["o"]] for r in r_by[a]], [c["msg"] for c in c_by[a]]]).encode()).hexdigest()[:16]
        sigs[a] = sig
        out = pages / f"{a}.html"
        if not force and old.get(a) == sig and out.exists():
            continue
        stubs = {p: {**notes[p], "text": []} for e in e_by[a] for p in (e["src"], e["dst"]) if area(p) != a and p in notes}
        render_viz({"schema": g.get("schema", SCHEMA), "mode": "area", "area": a, "home": "../graph.html", "built": g["built"],
                    "families": {"kinds": KIND_PARENT, "types": TYPE_PARENT},
                    "tags": atags, "tag_defs": {t: tag_defs[t] for t in atags if t in tag_defs}, "origins": sorted(ORIGINS),
                    "notes": [{**n, "text": note_text(root, n)} for n in ns] + list(stubs.values()),
                    "entities": [{**e, "names": e["names"][:6], "aka": e["aka"][:6], "mentions": mm} for e, mm in m_by[a]],
                    "relations": [{**r, "evidence": [x for x in r["evidence"] if area(x.rsplit(":", 1)[0]) == a]} for r in r_by[a]],
                    "edges": e_by[a],
                    "checks": c_by[a], "review": [], "proposed": []}, out, tpl)
        wrote += 1
    for a in set(old) - set(sigs):
        (pages / f"{a}.html").unlink() if (pages / f"{a}.html").exists() else None
    wr(pages / "_sig.json", sigs)
    general = general_areas({a: [n["path"] for n in ns] for a, ns in by.items()}, lambda p: notes[p]["kind"])
    w = Counter()
    for e in g["edges"]:
        a, b = area(e["src"]), area(e["dst"])
        if a != b and "log" not in (a, b):
            w[tuple(sorted((a, b)))] += 1
    for e in g["entities"]:
        ps = sorted({area(m["path"]) for m in e["mentions"]} - {"log"})
        if 2 <= len(ps) <= 50:  # an entity everywhere links nothing in particular
            for i in range(len(ps)):
                for j in range(i + 1, len(ps)):
                    w[(ps[i], ps[j])] += 1 / (len(ps) - 1)
    best = defaultdict(list)
    for k, x in w.items():
        for a in k:
            best[a].append((x, k))
    keep = {k for lst in best.values() for _, k in sorted(lst, reverse=True)[:3]}
    linked = {p for e in g["edges"] for p in (e["src"], e["dst"])}
    render_viz({"schema": g.get("schema", SCHEMA), "mode": "overview", "built": g["built"], "pages": "viz/",
                "totals": {"notes": len(g["notes"]), "entities": len(g["entities"]), "relations": len(g["relations"]),
                           "edges": len(g["edges"]), "areas": len(by), "checks": dict(Counter(c["code"] for c in g["checks"]))},
                "areas": [{"id": a, "n": len(by[a]), "general": a in general,
                           "kinds": dict(Counter(n["kind"] for n in by[a]).most_common()),
                           "updated": max(n["updated"] for n in by[a]), "superseded": sum(bool(n["superseded_by"]) for n in by[a]),
                           "warnings": len(c_by[a]), "edges": len(e_by[a])} for a in sorted(by)],
                "area_links": [{"a": a, "b": b, "w": round(w[(a, b)], 2)} for a, b in sorted(keep)],
                "checks": checks[:300],
                "chains": [{"path": n["path"], "title": n["title"], "by": n["superseded_by"]} for n in g["notes"] if n["superseded_by"]][:300],
                "orphans": [{"path": n["path"], "title": n["title"], "kind": n["kind"]} for n in g["notes"]
                            if n["path"] not in linked and n["kind"] != "log"][:300],
                "review": g["review"], "proposed": g["proposed"], "conflicts": g.get("conflicts", [])[:300],
                "notes": [], "entities": [], "relations": [], "edges": []}, dd / "graph.html", tpl)
    return wrote


# ---- the knowledge-graph page (_dream/knowledge-graph.html): the things and their links alone, to show a memory to
# people. assets/knowledge-graph.html is the page (it moves, lays out and draws); these functions only fill its data.
# Nothing in them knows a domain. A thing carries tags, one value (or several) in each tag column, and a value is a
# path whose levels are split by '/' (dataset/table/daily); the page colours by any column, the seven top-level
# values with the most things a colour each, and its legend opens each value into the levels under it. A memory's
# columns are its type (family/type, from TYPES.md `family:`), the projects whose notes name a thing, and the tags of
# those notes; islands are its folders or, when the folders do not part the things, the communities of its links.
# scripts/graph_page.py feeds them any other graph, every column of its nodes a tag column.
KG_COLOURS = {  # one muted hue per common family, the same in every memory; the page gives any other value a spare one
    "model": "#2a55a3", "dataset": "#2b8073", "feature": "#62904a", "metric": "#6b7a90", "document": "#b0874a",
    "decision": "#7c5ea6", "finding": "#8c6bb8", "term": "#b5677d", "system": "#a2574f", "party": "#8a939d",
    "experiment": "#4a9fc8", "question": "#9a83c2", "rule": "#8a6d3b", "project": "#7f8c8d"}


def kg_plural(f):
    """A family as the legend names it: 'model' -> 'Models', 'party' -> 'People and organisations'."""
    if f == "party":
        return "People and organisations"
    w = f.replace("-", " ").replace("_", " ")
    w = w if w.endswith("s") else w[:-1] + "ies" if w.endswith("y") and w[-2:-1] not in "aeiou" else w + "s"
    return w[:1].upper() + w[1:]


def kg_path(v, parents=None):
    """A tag value as the page reads it: a path, its levels split by '/'. A value whose head has a parent in `parents`
    ({value: parent}, a hierarchy given beside flat values) is put under it, and under that one's parent, and so on:
    with {"table": "dataset"}, 'table/daily' -> 'dataset/table/daily'."""
    p = "/".join(s.strip() for s in str(v).split("/") if s.strip())
    seen = {p.split("/")[0]}
    while p and parents and parents.get(p.split("/")[0]) not in (None, "") and str(parents[p.split("/")[0]]) not in seen:
        up = "/".join(s.strip() for s in str(parents[p.split("/")[0]]).split("/") if s.strip())
        seen.add(up)
        p = up + "/" + p if up else p
    return p


KG_NUMBER = re.compile(r"^-?\d+(\.\d+)?$")
KG_TIME = re.compile(r"^(\d{4})-(\d{2})(?:-(\d{2}))?(?:[T ][0-9:.]+(?:Z|[+-]\d{2}:?\d{2})?)?$")
KG_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def kg_time(v):
    """A date or a moment (ISO 8601: 2025-11, 2025-11-03, 2025-11-03T10:22Z) as a path: year/month[/day]."""
    m = KG_TIME.match(str(v).strip())
    if not m or not 1 <= int(m.group(2)) <= 12:
        return None
    return "/".join(g for g in m.groups() if g)


def kg_time_names(paths):
    """How a time tag's levels read: 2025, Nov 2025, 3 Nov 2025."""
    out = {}
    for p in paths:
        seg = p.split("/")
        out.setdefault(seg[0], seg[0])
        if len(seg) > 1:
            out.setdefault("/".join(seg[:2]), f"{KG_MONTHS[int(seg[1]) - 1]} {seg[0]}")
        if len(seg) > 2:
            out.setdefault(p, f"{int(seg[2])} {KG_MONTHS[int(seg[1]) - 1]} {seg[0]}")
    return out


def kg_cell(v, parents=None, sort="category"):
    """One value in one tag column: a path, a list of them (several values), or None (no value). A list, or text with
    ';' between values, gives several; yes/no are text; anything nested is left out. By the column's sort: a category
    is a path (its levels split by '/'); text is kept as it is (no levels, no ';'); a number is a number; a time is a
    path year/month/day."""
    if sort is True:                                       # kg_cell(v, parents, True): a text column, as before
        sort = "text"
    vs = v if isinstance(v, (list, tuple)) else str(v).split(";") if isinstance(v, str) and ";" in v and sort != "text" else [v]
    out = []
    for x in vs:
        if x is None or isinstance(x, (dict, list, tuple)):
            continue
        x = "yes" if x is True else "no" if x is False else x
        if sort == "number":
            try:
                f = float(x)
            except (TypeError, ValueError):
                continue
            p = int(f) if f == int(f) and abs(f) < 1e15 else round(f, 6)
        elif sort == "time":
            p = kg_time(x)
        elif sort == "text":
            p = " ".join(str(x).split())
        else:
            p = kg_path(x, parents)
        if p not in (None, "") and p not in out:
            out.append(p)
    return None if not out else out[0] if len(out) == 1 else out


def kg_vals(c):
    """A cell's values as a list: none, one, or several."""
    return [] if c is None or c == "" else list(c) if isinstance(c, (list, tuple)) else [c]


KG_BOTH = {"same-as", "related-to", "similar-to", "equivalent-to", "compared-with"}   # link types with no direction


def kg_counts(rows, cols):
    """How many rows (things or links) hold each value of each category or time column, at every level: what search
    offers. rows: [tags]; cols: the columns -> {key: {path: n}}."""
    out = {}
    for c in cols:
        if c.get("text") or c.get("number"):
            continue
        n = Counter()
        for t in rows:
            seen = set()
            for v in kg_vals(t.get(c["key"])):
                seg = str(v).split("/")
                seen.update("/".join(seg[:d]) for d in range(1, len(seg) + 1))
            n.update(seen)
        out[c["key"]] = dict(n)
    return out


KG_NULLS = {"", "n/a", "na", "null", "none", "nil", "-", "—", "?", "unknown", "nan"}   # a value that says there is none


def kg_sort(cells):
    """A tag column's sort, told by its values: number when every value is one, time when every value is an ISO date
    (a value such as n/a, none or unknown says there is none, and does not count), text when they are long or mostly
    their own (kg_is_text), else category."""
    vals = [x for c in cells for x in (c if isinstance(c, (list, tuple)) else [c])
            if x is not None and not isinstance(x, (dict, list, tuple)) and str(x).strip().lower() not in KG_NULLS]
    if not vals:
        return "category"
    if all(not isinstance(x, bool) and (isinstance(x, (int, float)) or KG_NUMBER.match(str(x).strip())) for x in vals):
        return "number"
    if all(isinstance(x, str) and kg_time(x) for x in vals):
        return "time"
    return "text" if kg_is_text(cells) else "category"


def kg_is_text(cells):
    """Whether a tag column holds text (a definition, a description, a link) rather than categories: its values long
    (over 40 characters on average) or mostly their own (more distinct than half the things holding one, and over 12).
    A text column is shown and searched with each thing; categories are what the page colours by and lists."""
    vals = [str(x).strip() for c in cells for x in (c if isinstance(c, (list, tuple)) else [c])
            if x is not None and not isinstance(x, (dict, list, tuple)) and str(x).strip()]
    if not vals:
        return False
    held = sum(1 for c in cells if c not in (None, "", [], ()))
    distinct = len(set(vals))
    return sum(len(v) for v in vals) / len(vals) > 40 or (distinct > 12 and distinct > 0.5 * held)


def kg_names(paths, name=kg_plural):
    """The legend's name for every level of the given paths ({path: name}), each level named by `name`."""
    out = {}
    for p in paths:
        seg = p.split("/")
        for d in range(1, len(seg) + 1):
            out.setdefault("/".join(seg[:d]), name(seg[d - 1]))
    return out


def kg_louvain(n, edges, levels=3):
    """Communities of a weighted undirected graph (nodes 0..n-1, edges [(a, b, w)]): Louvain's local moves, then the
    same on the communities found, `levels` times. Deterministic: nodes in order, ties to the first. -> community per node."""
    member, cur, es = list(range(n)), n, edges
    for _ in range(levels):
        adj, deg, m2 = [defaultdict(float) for _ in range(cur)], [0.0] * cur, 0.0
        for a, b, w in es:
            adj[a][b] += w
            adj[b][a] += w
            deg[a] += w
            deg[b] += w
            m2 += 2 * w
        if not m2:
            break
        com, tot = list(range(cur)), deg[:]
        for _sweep in range(30):
            moved = False
            for i in range(cur):
                ci, ki, near = com[i], deg[i], defaultdict(float)
                for j, w in adj[i].items():
                    if j != i:
                        near[com[j]] += w
                tot[ci] -= ki
                best, gain = ci, near.get(ci, 0.0) - tot[ci] * ki / m2
                for cj in sorted(near):
                    if near[cj] - tot[cj] * ki / m2 > gain + 1e-12:
                        best, gain = cj, near[cj] - tot[cj] * ki / m2
                tot[best] += ki
                if best != ci:
                    com[i], moved = best, True
            if not moved:
                break
        ids = {c: k for k, c in enumerate(sorted(set(com)))}
        if len(ids) == cur:
            break
        member = [ids[com[m]] for m in member]
        agg = defaultdict(float)
        for a, b, w in es:
            x, y = ids[com[a]], ids[com[b]]
            agg[(min(x, y), max(x, y))] += w
        es, cur = [(a, b, w) for (a, b), w in sorted(agg.items())], len(ids)
    return member


def kg_folder_homes(paths, general):
    """Each thing's folder island from the notes that name it ({thing: [paths]}): the project holding at least 60% of
    its project mentions; a thing no project names, the shared folder naming it most; one several projects share, the
    middle ("")."""
    def area(p):
        return p.split("/")[0] if "/" in p else ""
    home = {}
    for t, ps in paths.items():
        proj = Counter(area(p) for p in ps if area(p) and area(p) not in general)
        if proj:
            top, n = min(proj.items(), key=lambda z: (-z[1], z[0]))
            home[t] = top if n / sum(proj.values()) >= 0.6 else ""
        else:
            fs = Counter(area(p) for p in ps)
            home[t] = min(fs, key=lambda a: (-fs[a], a)) if fs else ""
    return home


def kg_islands(home, links, labels, general=frozenset(), middle="shared by several projects", kind="project"):
    """Islands: the folder homes ({thing: folder or ""}) when they part the things (no island holds more than half of
    them, three hold three or more); else the communities of the links, each named for its most linked thing, and the
    things of communities under three on one island. -> ({thing: island}, {island: {name, kind}}), kind one of
    `kind` (project, or group for another graph), folder, shared (the middle, named `middle`), cluster."""
    size = Counter(h for h in home.values() if h)
    if size and max(size.values()) <= len(home) / 2 and sum(n >= 3 for n in size.values()) >= 3:
        return home, {h: {"name": h.replace("-", " ") if h else middle,
                          "kind": "shared" if not h else "folder" if h in general else kind} for h in set(home.values())}
    things = sorted(home)
    idx = {t: i for i, t in enumerate(things)}
    w = Counter()
    for a, b in links:
        if a in idx and b in idx and a != b:
            w[(min(idx[a], idx[b]), max(idx[a], idx[b]))] += 1
    com = kg_louvain(len(things), [(a, b, x) for (a, b), x in sorted(w.items())])
    deg = Counter()
    for (a, b), x in w.items():
        deg[a] += x
        deg[b] += x
    members = defaultdict(list)
    for i, c in enumerate(com):
        members[c].append(i)
    out, isles = {}, {}
    for c, ms in sorted(members.items()):
        h = f"c{c}" if len(ms) >= 3 else "small"
        if h not in isles:
            lead = things[min(ms, key=lambda i: (-deg[i], things[i]))]
            name = labels.get(lead, lead)
            isles[h] = {"name": "around " + (name if len(name) <= 26 else name[:25].rstrip() + "…") if h != "small" else "small groups",
                        "kind": "cluster"}
        for i in ms:
            out[things[i]] = h
    return out, isles


def kg_page(title, headline, lede, stats, meta, columns, things, links, notes, eyebrow="Knowledge graph", theme="paper"):
    """The page itself: assets/knowledge-graph.html with its data islands and masthead filled, d3 (ISC) pasted in.
    columns: the tag columns, the first the one it colours by at first ([{key, name, names?: {path: name},
    colours?: {value: hex}, text?: true}]); each thing's tags: {key: path or [paths]}, or text in a text column.
    meta may name the link types: forward ({type: name}) and inverse ({type: how it reads backwards}).
    theme: the look it opens in: paper, star (a star map at night), gala (a purple show at night), moon (moonlit: pale
    lilac and silver under a great moon), fanfare (a violet stage under sweeping spotlights) or noir (black and white
    on a checkered stage, purple only as an accent); a switch in its header picks among them."""
    def island(rows):  # one record per line, and nothing in it that closes a script
        return ("[\n" + ",\n".join("  " + json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in rows)
                + "\n]").replace("</", "<\\/")
    assets = Path(__file__).resolve().parent.parent / "assets"
    page = read(assets / "knowledge-graph.html")
    fill = {"@@THEME@@": theme if theme in ("paper", "star", "gala", "moon", "fanfare", "noir") else "paper",
            "@@TITLE@@": html.escape(title), "@@EYEBROW@@": html.escape(eyebrow), "@@HEADLINE@@": html.escape(headline),
            "@@LEDE@@": html.escape(lede),
            "@@STATS@@": "".join(f"<div><dt>{html.escape(a)}</dt><dd>{b:,}</dd></div>" for a, b in stats),
            "@@META@@": json.dumps(meta, ensure_ascii=False).replace("</", "<\\/"), "@@COLUMNS@@": island(columns),
            "@@THINGS@@": island(things), "@@LINKS@@": island(links), "@@NOTES@@": island(notes)}
    for k, v in fill.items():
        assert page.count(k) == 1, k
        page = page.replace(k, v)
    return page.replace("@@D3@@", read(assets / "d3.v7.9.0.min.js"))  # last: the library's text is never searched


def kg_inverse(edges_text):
    """How each relation type reads backwards, from EDGES.md: its first `~` alias ("calls" -> "Called by")."""
    out = {}
    for t, d in parse_edges(edges_text)[0].items():
        back = next((a[1:] for a in d["aka"] if a.startswith("~")), None)
        if back:
            out[t] = back.replace("-", " ")[:1].upper() + back.replace("-", " ")[1:]
    return out


def kg_data(root, g):
    """The page's data from a memory's graph: every thing with a link, every relation between two of them once with
    the line of the note that states it. -> kg_page's arguments, or None when no two things are linked."""
    notes = {n["path"]: n for n in g["notes"]}
    ents = {e["id"]: e for e in g["entities"]}
    lines, seen, links = {}, set(), []

    def quote(path, line):
        if path not in lines:
            try:
                lines[path] = read(root / path).split("\n")
            except OSError:
                lines[path] = []
        ls = lines[path]
        if not line.isdigit() or not 0 < int(line) <= len(ls):
            return ""
        q = re.sub(r"^\s*(#+|[-*])\s*", "", ls[int(line) - 1]).strip()
        return q if len(q) <= 220 else q[:217].rstrip() + "…"
    # a link's direction: none when its type reads the same both ways (EDGES.md's ~ alias is the type itself, or a
    # type such as compared-with); its tags, from the note that states it: its kind, when, whether it was replaced
    inverse = kg_inverse(vocab_texts(root)[0])
    both = KG_BOTH | {t for t, b in inverse.items() if fold(b) == fold(t)}
    for r in g["relations"]:
        s, o = r["s"], r["o"]
        d = 0 if r["type"] in both else 1
        key = (s, o, r["type"], d) if d else (min(s, o), max(s, o), r["type"], d)
        if s == o or s not in ents or o not in ents or key in seen:
            continue
        seen.add(key)
        path, _, line = ((r.get("evidence") or [""])[0]).rpartition(":")
        link = {"s": s, "t": o, "type": r["type"], "q": quote(path, line) if path else "", "note": path if path in notes else None}
        n = notes.get(path)
        if n:
            tags = {"kind": n.get("kind") or "note"}
            when = kg_time(n.get("updated") or "")
            if when:
                tags["stated"] = when
            if n.get("superseded_by"):
                tags["replaced"] = "replaced"
            link["tags"] = tags
        if not d:
            link["dir"] = 0
        links.append(link)
    if not links:
        return None
    linked = {x for l in links for x in (l["s"], l["t"])}
    kept = sorted(linked, key=lambda i: (-len({m["path"] for m in ents[i]["mentions"]}), i))
    paths = {i: sorted({m["path"] for m in ents[i]["mentions"]}) for i in kept}
    labels = {i: ((ents[i].get("names") or [{"name": i}])[0]["name"]).strip("`") for i in kept}
    by_area = defaultdict(list)
    for p in notes:
        by_area[p.split("/")[0] if "/" in p else ""].append(p)
    general = general_areas(by_area, lambda p: notes[p].get("kind") or "note")
    home, isles = kg_islands(kg_folder_homes(paths, general), [(l["s"], l["t"]) for l in links], labels, general)
    # the tag columns: the type under its family (segment -> dataset/segment), the projects whose notes name a thing
    # (most mentions first), and the tags of those notes
    kind = {}
    for i in kept:
        base, _, rest = ents[i]["type"].partition("/")
        fam = "other" if base == "other" else TYPE_PARENT.get(base, base)
        kind[i] = "/".join([fam] + ([base] if base != fam else []) + ([rest] if rest else []))
    def area(p):
        return p.split("/")[0] if "/" in p else ""
    proj = {i: [a for a, _ in Counter(area(p) for p in paths[i] if area(p) and area(p) not in general).most_common()] for i in kept}
    tag_of = defaultdict(list)
    tfam = {t: f for t, f in parse_edges(tags_text(root), {})[5]["family"].items() if f != t}  # TAGS.md `family:`: a tree,
    for t, ps in sorted((g.get("tags") or {}).items()):                                        # as a type sits under its own
        for p in ps:
            tag_of[p].append(kg_path(t, tfam))
    tagged = {i: [t for t, _ in Counter(t for p in paths[i] for t in tag_of.get(p, ())).most_common()] for i in kept}
    names = kg_names(kind.values())
    names["other"] = "Other kinds"
    # and a text tag, what it is: the key line of the note that best says so (its headline note)
    about = {}
    for i in kept:
        h = ents[i].get("headline")
        n = notes.get(h) if h else None
        about[i] = quote(h, str(n.get("line") or "")) if n else ""
    columns = [{"key": "type", "name": "Type", "names": names, "colours": KG_COLOURS}]
    if any(proj.values()):
        columns.append({"key": "project", "name": "Project"})
    if any(tagged.values()):
        columns.append({"key": "tag", "name": "Tag"})
    noted = {i: max((kg_time(notes[p].get("updated") or "") or "" for p in paths[i] if p in notes), default="") for i in kept}
    if any(noted.values()):                                # a time tag: when a note last named it
        columns.append({"key": "noted", "name": "Last noted", "time": True, "names": kg_time_names(v for v in noted.values() if v)})
    if any(about.values()):
        columns.append({"key": "about", "name": "About", "text": True})
    def tags(i):
        out = {"type": kind[i]}
        for key, vs in (("project", proj[i]), ("tag", tagged[i])):
            if vs:
                out[key] = vs[0] if len(vs) == 1 else vs
        if noted[i]:
            out["noted"] = noted[i]
        if about[i]:
            out["about"] = about[i]
        return out
    note_list = sorted({p for i in kept for p in paths[i]} | {l["note"] for l in links if l["note"]})
    note_at = {p: k for k, p in enumerate(note_list)}
    index = {i: k for k, i in enumerate(kept)}
    things = [{"id": i, "label": labels[i], "n": len(paths[i]), "home": home[i], "tags": tags(i),
               "names": [x["name"].strip("`") for x in (ents[i].get("names") or [])[:6]], "notes": [note_at[p] for p in paths[i]]}
              for i in kept]
    for l in links:
        l["s"], l["t"], l["note"] = index[l["s"]], index[l["t"]], note_at.get(l["note"]) if l["note"] else None
    rows = [{"p": p, "t": notes[p]["title"], "k": notes[p]["kind"], "d": notes[p].get("updated") or "",
             "a": p.split("/")[0] if "/" in p else "", "old": 1 if notes[p].get("superseded_by") else 0} for p in note_list]
    stated = [l["tags"]["stated"] for l in links if (l.get("tags") or {}).get("stated")]
    link_cols = [{"key": "kind", "name": "Note kind"}] if any(l.get("tags") for l in links) else []
    if stated:
        link_cols.append({"key": "stated", "name": "Stated", "time": True, "names": kg_time_names(stated)})
    if any((l.get("tags") or {}).get("replaced") for l in links):
        link_cols.append({"key": "replaced", "name": "Replaced"})
    clusters = any(v["kind"] == "cluster" for v in isles.values())
    count = sum(v["kind"] == ("cluster" if clusters else "project") for v in isles.values())
    lede = ("Every thing the notes name and every link a note states between two of them, each with the line that says "
            "so. " + ("An island is a group of things that link mostly to each other." if clusters
                      else "An island is a project; the middle holds what several projects share."))
    return {"title": "Knowledge graph", "eyebrow": "Memory · knowledge graph", "headline": f"What {len(g['notes']):,} notes know",
            "lede": lede, "stats": [("things", len(things)), ("links", len(links)), ("clusters" if clusters else "projects", count),
                                    ("notes", len(g["notes"]))],
            "meta": {"notes": len(g["notes"]), "isles": isles, "inverse": inverse, "link_columns": link_cols,
                     "link_values": kg_counts([l.get("tags") or {} for l in links], link_cols), "both": sum(1 for l in links if l.get("dir") == 0)},
            "columns": columns, "things": things, "links": links, "notes": rows}


def write_kg(root, g, out, theme="paper"):
    """Write _dream/knowledge-graph.html when the memory has links between things (a dream with a model command). -> bool"""
    data = kg_data(root, g)
    if data:
        wr(out, kg_page(**data, theme=theme))
    elif out.exists():
        out.unlink()  # its things or links went away: no page that shows a graph no longer there
    return bool(data)


def main(argv=None):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--root", help="memory dir (default: $MEMORY_DIR, nearest memory/ upward, ./memory)")
    ap = argparse.ArgumentParser(prog="memory.py", description="memory-dream v0.4")
    ap.add_argument("--root", dest="root0", help=argparse.SUPPRESS)
    sp = ap.add_subparsers(dest="verb", required=True)
    d = sp.add_parser("dream", parents=[common], help="index new notes, review vocabularies, merge")
    d.add_argument("--cmd", help='model command, prompt on stdin (default $MEMORY_LLM; none = file mode)')
    d.add_argument("-j", type=int, default=4, help="parallel calls")
    d.add_argument("--review", action="store_true", help="review the vocabulary even if nothing is due")
    d.add_argument("--all", action="store_true", help="re-index every note")
    d.add_argument("--prompts", action="store_true", help="no model: write one prompt a note for a helper agent to _dream/pending/")
    d.add_argument("--packets", action="store_true", help="read many notes a call: with a command, a packet a call; without one, packets written to _dream/pending/")
    d.add_argument("--dry-run", action="store_true", help="print what would be read and about what it would cost; call and write nothing")
    a = sp.add_parser("ask", parents=[common], help="answer questions: grep with memory, one call for many questions")
    a.add_argument("questions", nargs="*")
    a.add_argument("-f", "--file", help="questions, one per line")
    a.add_argument("-p", help="project")
    a.add_argument("--budget", type=int, help="chars before switching from whole notes to surgical lines")
    a.add_argument("--list", action="store_true", help="no question: one line per note of -p and --kind, with its lineage")
    a.add_argument("--kind", help="with --list: only notes of this kind")
    a.add_argument("--tag", help="with --list: only notes that carry this tag (TAGS.md defines the tags)")
    a.add_argument("--all", action="store_true", help="with --list: every line, however many (pipe it through grep)")
    vz = sp.add_parser("viz", parents=[common], help="write the HTML viewer (dream refreshes it too)")
    vz.add_argument("--out", help="output file (default memory/_dream/graph.html)")
    vz.add_argument("--theme", choices=["paper", "star", "gala", "moon", "fanfare", "noir"], default="paper",
                    help="the look _dream/knowledge-graph.html opens in (a switch in it picks among the six)")
    sp.add_parser("check", parents=[common], help="warnings in full")
    ab = sp.add_parser("absorb", parents=[common], help="take another base in as an origin: prints what it would take, acts with --yes")
    ab.add_argument("folder", help="a folder of notes: .md files, with its readings or a relations.jsonl if it has them")
    ab.add_argument("--as", dest="origin", required=True, help="the folder it becomes here")
    ab.add_argument("--trust", default="", help="preferences: its preference and rule notes may shape tasks here")
    ab.add_argument("--yes", action="store_true", help="copy the notes, write ORIGIN.md, bring the readings, rebuild with no model")
    dr = sp.add_parser("drop", parents=[common], help="remove a note or a folder: prints what goes with it, acts with --yes")
    dr.add_argument("target", help="a note (its path or its id) or a folder")
    dr.add_argument("--yes", action="store_true", help="delete it, leave a tombstone in CONFLICTS.md, rebuild with no model")
    ex = sp.add_parser("export", parents=[common], help="the graph as CSV + Cypher for a graph database (no driver needed)")
    ex.add_argument("--to", required=True, help="output directory")
    lg = sp.add_parser("log", parents=[common], help="append to today's log")
    lg.add_argument("text")
    lg.add_argument("-p", help="project")
    args = ap.parse_args(argv)
    root = find_root(args.root or args.root0)
    load_domain(root)
    if args.verb in ("dream", "log", "drop", "absorb") or (args.verb == "viz" and not args.out):  # REVIEW.md §8 R2: never write there
        why = claude_code_owned(root)
        if why:
            sys.stderr.write(f"memory.py: {root} is Claude Code's own memory ({why}); memory-dream reads it but never "
                             "writes there. Point --root at your notes.\n")
            sys.exit(2)
    {"dream": dream, "ask": ask, "viz": viz, "check": check, "log": log, "export": export, "drop": drop, "absorb": absorb}[args.verb](args, root)


if __name__ == "__main__":
    try:
        main()
        sys.stdout.flush()  # a reader that left early (`… | head`) shows up here, not as a traceback at exit
    except BrokenPipeError:
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())  # nothing more to say to a closed pipe
        sys.exit(0)
