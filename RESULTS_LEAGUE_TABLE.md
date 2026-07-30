# Results League Table

## The Short Version

The repository has one strong exact result package, two useful comparative
observations, one algorithmic lead, and two supporting audits. The first
package may be a compact formulation not previously recorded, but
literature priority is still unknown.

| Rank | Result | Score / 100 | Our verdict | Status |
| ---: | --- | ---: | --- | --- |
| 1 | The Section 8.1 obstruction is exactly `S(K_(q,2q^4))`, with closed cycle counts and spectrum | 92 | **The lead result** | Proved here; finite certificate passed; literature priority unknown |
| 2 | Exact-cycle difficulty already occurs at chromatic number two | 84 | **A sharp separation** | Immediate proved corollary; comparison across two papers |
| 3 | Path-length residues expose this boundary obstruction before full path materialization | 72 | **The best algorithmic lead** | Exact on this family; no general data-structure bound proved |
| 4 | Alweiss-pattern avoidance is hypergraph 2-coloring, while its incidence graph is always bipartite | 66 | **A useful warning** | Standard reduction plus project-level synthesis; not a new theorem |
| 5 | Small shift graphs reproduce the expected chromatic jump at `m=9` | 51 | **A sound audit** | Exact computation of known behavior |
| 6 | Projection and coarse-graining graphs can be tested without pretending they preserve knot or field geometry | 38 | **A necessary guardrail** | Methodological scope, not a mathematical result |

## What Is Actually New Here?

### Candidate for literature novelty

The compact identification

```text
J_q = S(K_(q,2q^4))
```

and the resulting invariant package were not found in the source paper or
in a targeted phrase search:

```text
t_(4r)(J_q) = (q)_r (2q^4)_r / (2r)
```

with no cycles of other lengths, together with the complete adjacency
spectrum and the identity

```text
zero-eigenvalue multiplicity = cycle rank + 1.
```

These statements are proved in this repository. Their mathematical
correctness does not establish publication novelty. A specialist
literature review and author feedback are still needed.

### New synthesis, not a new theorem

Two comparisons are useful:

1. The Stern-Zamir boundary obstruction is bipartite, so its failure mode
   is about exact path-length information rather than chromatic hardness.
2. The Alweiss-Bowen-Sabok finite pattern object is a hypergraph. Its
   incidence graph remains bipartite even when the hypergraph is not
   2-colorable, so ordinary graph chromatic number again misses the real
   obstruction.

Together these examples make a broader diagnostic point: a bipartite
derived graph can conceal a hard constraint carried by paths or
hyperedges.

## Scoring

The score is an editorial ranking, not a probability, citation metric, or
peer-review judgment. It weights:

- proof strength: 35%;
- plausible novelty: 25%;
- research leverage: 25%; and
- reproducibility: 15%.

The table should be revised if the source authors identify prior art or if
residue-aware compression gains a proved complexity bound.
