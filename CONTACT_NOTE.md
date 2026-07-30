# Draft Note to the Paper Authors

Subject: An apparently unstated normal form for the Section 8.1 counterexample

Dear Or Stern and Or Zamir,

While reading *Enumerating Small Cycles*, I noticed a compact normal form
for the five-layer counterexample in Section 8.1. With
\(q=n^{1/5}\), the graph is canonically the one-subdivision

\[
S(K_{q,2q^4}).
\]

Your Lemma 8.9 already proves the essential mod-4 path-length obstruction.
The subdivision description packages the same construction in standard
graph language and gives, as routine consequences,

\[
t_{4r}=\frac{(q)_r(2q^4)_r}{2r}
\]

for \(2\le r\le q\), no cycles of other lengths, and a closed adjacency
spectrum.

I ran a targeted literature audit. The terms "subdivision," "complete
bipartite," and "bipartite" do not appear in v1, and I did not locate a
direct antecedent applying this normal form to your construction. The
cycle-counting and spectral ingredients themselves are classical, so I am
not claiming a new general theorem or an improvement to your algorithmic
bounds.

The proof, exact tables, a \(q=2\) brute-force certificate, and the
claim-by-claim novelty audit are here:

https://github.com/rbajaj5/cycle-coloring-boundary-layer-audit

Was this normal form already known or intended? I would also be glad to
know whether the exact invariant package is useful to your presentation of
the barrier.

Best,

Ravi Andrew Bajaj

Alexander Burns is invited as a formalization reviewer; public
coauthorship remains pending his explicit confirmation.
