# Cycle-Coloring Boundary-Layer Audit

An exact finite companion to two July 2026 papers:

- Or Stern and Or Zamir,
  [*Enumerating Small Cycles*](https://arxiv.org/abs/2607.27147)
- Or Zamir,
  [*k-Coloring is Faster than Computing the Chromatic Number*](https://arxiv.org/abs/2607.25973)

It also contains a small, explicitly scoped shift-graph audit motivated by
Ben Green's
[*On Alweiss's example for multiple recurrence*](https://arxiv.org/abs/2607.24594).

## Headline

The five-layer boundary-property obstruction from Section 8.1 of the cycle
paper is exactly

\[
J_q \cong S(K_{q,2q^4}),
\]

the graph obtained by subdividing every edge of \(K_{q,2q^4}\) once.

This elementary normal form gives closed cycle counts and the complete
adjacency spectrum:

\[
t_{4r}(J_q)=\frac{(q)_r(2q^4)_r}{2r},
\qquad 2\le r\le q,
\]

with every other simple-cycle count equal to zero. The graph is connected
and bipartite, so \(\chi(J_q)=2\).

That makes the relationship between the papers precise: the exact-length
cycle-enumeration obstruction already occurs in the polynomial coloring
base case. It is a loss-of-path-residue problem, not a hard-coloring
problem.

## New-Result Status

The exact normal form, cycle formula, and spectrum are proved in this
repository and independently checked on the explicit `q=2` graph.

The evidence-based novelty verdict is deliberately narrower:

- identifying the specific Section 8.1 construction as
  `S(K_(q,2q^4))` is a **plausibly original structural observation**;
- the cycle and spectrum formulas are **classical consequences
  instantiated on that construction**; and
- literature priority remains unresolved pending specialist and author
  review.

The source paper already proves the mod-4 path obstruction. This
repository does not claim that result.

See the [results league table](RESULTS_LEAGUE_TABLE.md) for a concise,
Economist-style ranking that separates proved results, comparative
syntheses, algorithmic leads, and replications. See the
[literature novelty audit](LITERATURE_NOVELTY_AUDIT.md) for the search
record, prior art, confidence levels, and safe contact language.

## Reproduce

```bash
python -m pip install -e ".[test]"
python -m pytest -q
python scripts/run_finite_audit.py
```

The audit uses only the Python standard library. It constructs the
98-vertex \(q=2\) instance, independently counts its short cycles by DFS,
and compares them with the symbolic formula.

## Results

- [Finite proposition](notes/FINITE_OBSTRUCTION_PROPOSITION.md)
- [Results league table](RESULTS_LEAGUE_TABLE.md)
- [Literature novelty audit](LITERATURE_NOVELTY_AUDIT.md)
- [Machine-readable ranking](results/result_ranking.csv)
- [Paper interface](notes/PAPER_INTERFACE.md)
- [Green/Alweiss scope note](notes/ALWEISS_GREEN_SCOPE.md)
- [Two-color pattern hypergraph interface](notes/ALWEISS_BOWEN_SABOK_HYPERGRAPH_INTERFACE.md)
- [Applicability matrix](notes/APPLICABILITY_MATRIX.md)
- [Generated report](results/RESULTS.md)
- [Family summary](results/obstruction_family_summary.csv)
- [Exact cycle profiles](results/exact_cycle_profiles.csv)
- [Adjacency spectra](results/adjacency_spectrum_multiplicities.csv)
- [Small shift-graph audit](results/shift_graph_small_audit.csv)
- [Small brute-force certificate](results/q2_bruteforce_certificate.json)
- [Draft author note](CONTACT_NOTE.md)

## Claim Boundary

This repository supplies an exact reformulation, formulas, and a finite
certificate. It does **not** claim:

- a correction to either source paper;
- a faster cycle-enumeration or coloring algorithm;
- a proof that residue-aware compression preserves near-quadratic
  preprocessing;
- a new general cycle-counting or subdivision-spectrum theorem; or
- established literature priority for the normal form.

The natural next question is whether retaining a small set of attainable
path-length residues on each compressed edge can bypass this particular
obstruction without making the data structure too large.

The graph routines can also be applied to projection, partition, and
coarse-graining graphs, provided the representation loss is recorded. A
cycle profile, coloring, or spectrum of such a graph does not by itself
preserve knot type, geometric embedding, or an underlying physical field.

## Authorship

Initiated by Ravi Andrew Bajaj. Alexander Burns is invited as coauthor and
formalization reviewer; his public coauthorship remains pending explicit
confirmation. See [AUTHORS.md](AUTHORS.md).

## License

MIT for the repository code and original notes. The cited papers retain
their own licenses; no figures or substantial text from them are copied
here.
