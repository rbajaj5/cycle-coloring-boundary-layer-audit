# Literature Novelty Audit

Audit date: 2026-07-30

## Verdict

The strongest supportable originality claim is narrow:

> The identification of the Section 8.1 five-layer counterexample in
> Stern-Zamir as the one-subdivision
> \(S(K_{q,2q^4})\) appears to be an unstated structural observation about
> that construction.

This is **plausibly original with moderate confidence**, not established
priority. It is not a new theorem about subdivision graphs. The exact cycle
counts and adjacency spectrum are useful consequences of the normal form,
but their underlying counting and spectral methods are classical.

No stronger novelty claim should be sent to the authors or placed in an
abstract without a specialist search and author confirmation.

## Audit Method

The audit checked:

1. the full text and references of arXiv:2607.27147v1;
2. exact and concept searches for the displayed normal form and for a
   complete-bipartite subdivision description of the boundary-layer
   counterexample;
3. prior work on cycle counting in complete bipartite graphs;
4. prior work relating subdivision-graph spectra to signless Laplacians;
5. prior work on path lengths modulo an integer; and
6. the adjacent coloring, shift-graph, and hypergraph papers used in this
   repository.

An independent bounded review subsequently repeated the conceptual search
and also found no direct antecedent. Its search scope and access
limitations are recorded in
[`notes/EXTERNAL_PRIORITY_REVIEW.md`](notes/EXTERNAL_PRIORITY_REVIEW.md).

The source paper is dated 2026-07-29, one day before this audit. Searches
therefore have little time to capture commentary about that specific
construction. Absence from a targeted search is evidence, not proof of
priority.

## Claim-by-Claim Findings

| ID | Claim | Source-paper status | Prior-art status | Novelty class | Confidence |
| --- | --- | --- | --- | --- | --- |
| N1 | The Section 8.1 graph is \(S(K_{q,2q^4})\) | The construction is present, but the terms "subdivision," "complete bipartite," and "bipartite" do not occur in v1 | No direct match was located for this recognition of the specific counterexample | **Plausibly original structural observation** | Moderate |
| N2 | \(t_{4r}(J_q)=(q)_r(2q^4)_r/(2r)\), with no other cycle lengths | Not stated in v1 | Counting \(2r\)-cycles in \(K_{a,b}\) is standard; subdivision doubles cycle lengths | **Classical consequence instantiated on a new construction** | High |
| N3 | The displayed complete adjacency spectrum of \(J_q\) | Not stated in v1 | Subdivision spectra via the signless Laplacian are established | **Classical consequence instantiated on a new construction** | High |
| N4 | The obstruction is connected, bipartite, and has \(\chi=2\) | Not stated explicitly, but immediate from the construction | Standard | **Expository observation, not a new theorem** | High |
| N5 | The exact-length barrier already occurs at chromatic number two | Not phrased this way in either paper | Follows immediately from N4 and comparison with the coloring paper | **Original cross-paper synthesis** | Moderate |
| N6 | Boundary-to-boundary path lengths lie in \(0\bmod 4\) | Proved as Lemma 8.9 and discussed in the overview | Modular path-length questions have a substantial literature | **Owned by Stern-Zamir; not novel here** | High |
| N7 | A residue-labeled compression may bypass this barrier | Not analyzed as a data-structure variant | Residue tracking is standard in other graph settings; the target complexity is unproved | **Research proposal only** | High |
| N8 | Pattern avoidance is hypergraph 2-coloring while the incidence graph is bipartite | Not the focus of the cycle paper | Standard reduction and standard incidence-graph fact | **Project synthesis, not a new theorem** | High |
| N9 | Small shift graphs show their known chromatic jump | Not applicable | Classical shift-graph behavior | **Replication** | High |

## Primary Prior Art

- O. Stern and O. Zamir, *Enumerating Small Cycles*,
  [arXiv:2607.27147v1](https://arxiv.org/abs/2607.27147). Section 8.1
  defines the five layers and proves the path-length divisibility result
  in Lemma 8.9.
- A. Arman, D. S. Gunderson, and S. Tsaturian,
  *Triangle-free graphs with the maximum number of cycles*,
  [Discrete Mathematics 339 (2016), 699-711](https://doi.org/10.1016/j.disc.2015.10.008).
  This is representative prior literature explicitly counting cycles in
  complete bipartite graphs.
- S. Durocher, D. S. Gunderson, P. C. Li, and M. Skala,
  *Cycle-maximal triangle-free graphs*,
  [Discrete Mathematics 338 (2015), 274-290](https://doi.org/10.1016/j.disc.2014.10.002).
  Its complete-bipartite cycle formula directly anticipates the counting
  ingredient used here.
- H. S. Ramane, S. B. Gudimani, and S. S. Shinde,
  *Signless Laplacian Polynomial and Characteristic Polynomial of a
  Graph*, [Journal of Discrete Mathematics (2013)](https://doi.org/10.1155/2013/105624).
  Theorem 6 gives the established subdivision-graph characteristic
  polynomial relation used by the spectral calculation.
- D. Cvetkovic, P. Rowlinson, and S. K. Simic,
  *Signless Laplacians of finite graphs*,
  [Linear Algebra and its Applications 423 (2007), 155-171](https://doi.org/10.1016/j.laa.2007.01.009).
- X. Deng and C. H. Papadimitriou, *On path lengths modulo three*,
  [Journal of Graph Theory 15 (1991), 267-282](https://doi.org/10.1002/jgt.3190150305).
  This does not settle the proposed data-structure question, but it shows
  that modular path-length structure is established subject matter.
- N. Alon and M. Krivelevich, *Divisible subdivisions*,
  [Journal of Graph Theory 98 (2021), 623-629](https://doi.org/10.1002/jgt.22716),
  and O. Janzer, *The Extremal Number of the Subdivisions of the Complete
  Bipartite Graph*,
  [SIAM Journal on Discrete Mathematics 34 (2020), 241-250](https://doi.org/10.1137/19M1269798).
  These establish nearby subdivision and divisibility literature but use
  the graph family in different structural roles.

## Search Record

The exact/source-specific searches included:

- `"S(K_{q,2q^4})"`
- `"one-subdivision" "boundary-layer" cycles Stern Zamir`
- `"subdivision graph" "complete bipartite graph" spectrum`
- `"path length modulo" graph data structure`
- full-text searches of arXiv:2607.27147v1 for `subdivision`,
  `complete bipartite`, `bipartite`, and `residue`

The first three structural terms do not occur in the source paper.
`residue` does occur: the authors explicitly identify the wrong-residue
phenomenon in their overview. Generic searches returned substantial prior
art for complete-bipartite cycle counts and subdivision spectra, but no
direct indexed antecedent for naming this particular Section 8.1 graph as
\(S(K_{q,2q^4})\).

## What Can Be Communicated

Safe:

> I noticed an apparently unstated normal form for your Section 8.1
> counterexample: after writing \(q=n^{1/5}\), it is canonically the
> one-subdivision \(S(K_{q,2q^4})\). A targeted search did not locate this
> observation, although the consequences use standard subdivision-graph
> machinery. The normal form gives the cycle profile and spectrum in
> closed form. Was this description already known or intended?

Unsafe:

- "We proved a new theorem about subdivision graphs."
- "We solved the \(C_{18}\) barrier."
- "Residue-aware compression gives a faster algorithm."
- "The cycle formula or spectral theorem is new."
- "No one in the literature has ever observed this."

## Limitations

Neither review included subscription-level MathSciNet or zbMATH searching,
and neither was an exhaustive thesis or citation-network review. The
searches cannot detect unpublished notes or observations known to the
authors. The proper status is therefore **priority unresolved, with two
targeted reviews supporting the moderate-confidence claim that the
source-specific normal-form recognition is unrecorded in accessible
sources**.
