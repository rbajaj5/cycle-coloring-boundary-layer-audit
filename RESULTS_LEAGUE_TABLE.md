# Results League Table

## Evidence-Based Ranking

This is an editorial ranking of what is worth communicating, not a claim
that the highest entry is a new theorem. The accompanying
[literature novelty audit](LITERATURE_NOVELTY_AUDIT.md) separates
source-specific observations from classical consequences.

| Rank | Result | Score / 100 | Novelty class | Literature verdict |
| ---: | --- | ---: | --- | --- |
| 1 | The Section 8.1 obstruction is canonically `S(K_(q,2q^4))` | 76 | **Plausibly original structural observation** | Not stated in v1; two targeted reviews found no direct antecedent in accessible sources; moderate confidence; author confirmation needed |
| 2 | Closed cycle counts and spectrum for that obstruction | 63 | **Classical consequences, new instantiation** | Useful exact package; complete-bipartite counting and subdivision spectral machinery are established |
| 3 | Exact-cycle difficulty already occurs at chromatic number two | 52 | **Cross-paper synthesis** | Sharp explanatory comparison, but an immediate consequence rather than a new theorem |
| 4 | Residue-labeled path compression as a route around the barrier | 42 | **Research proposal** | Stern-Zamir already identify the residue obstruction; no new complexity bound is proved |
| 5 | Pattern avoidance as hypergraph 2-coloring with bipartite incidence graph | 28 | **Standard reduction plus synthesis** | Useful interface warning, not novel graph theory |
| 6 | Small shift graphs reproduce the expected chromatic jump at `m=9` | 15 | **Replication** | Known behavior, exactly reproduced |
| 7 | Representation-loss accounting for projection and coarse-graining graphs | 12 | **Methodological guardrail** | Good practice, not a mathematical result |

## The Lead Result

The only result with a presently supportable originality case is

```text
J_q is canonically the one-subdivision S(K_(q,2q^4)).
```

The source paper defines all the ingredients and proves the mod-4
path-length obstruction, but it does not use the terms `subdivision`,
`complete bipartite`, or `bipartite`. A targeted exact and conceptual
search did not locate a prior source applying this normal form to the
newly published Section 8.1 construction.

That supports **plausibly original observation**, not **established
literature priority**. A second bounded review reached the same result but
also lacked subscription-level MathSciNet and zbMATH access.

## What the Normal Form Buys

Once the normal form is recognized, standard facts give

```text
t_(4r)(J_q) = (q)_r (2q^4)_r / (2r)
```

and the complete adjacency spectrum. Those calculations are proved and
machine-checked here, but counting cycles in complete bipartite graphs and
deriving subdivision spectra from the signless Laplacian are established
methods. The formulas should be described as exact corollaries for this
specific obstruction, not as new general theorems.

## The Best Synthesis

The cycle-enumeration barrier lives in a connected bipartite graph with
chromatic number two. This cleanly separates exact path-length information
from chromatic hardness when the cycle and coloring papers are read
together. It is a useful explanatory point for the authors, but its proof
is immediate after the normal-form recognition.

## The Open Lead

Residue-labeled compression remains a question:

> Can the path-reporting tables retain enough path-length residue
> information to reject the Section 8.1 obstruction while preserving the
> target near-quadratic preprocessing and polylogarithmic delay?

Stern-Zamir already identify the wrong-residue mechanism. This repository
does not prove that adding residue state improves their algorithm.

## Scoring

The score measures communication value:

- mathematical correctness and proof strength: 35%;
- source-specific originality evidence: 25%;
- research leverage: 25%; and
- reproducibility: 15%.

It is not a novelty probability or citation metric. A score above 70 means
"lead with this when contacting the authors," not "claim a theorem."
