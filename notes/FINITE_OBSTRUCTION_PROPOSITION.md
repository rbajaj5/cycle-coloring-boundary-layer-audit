# Finite Obstruction Proposition

Let \(q\ge 2\). Define the five-layer graph

\[
A_1-A_2-A_3-A_4-A_5
\]

with layer sizes

\[
(q^4,q^5,q,q^5,q^4).
\]

Index \(A_2\) by pairs \((i,\ell)\in[q^4]\times[q]\), joining
\((i,\ell)\) to \(i\in A_1\) and \(\ell\in A_3\). Index \(A_4\) by
\((\ell,j)\in[q]\times[q^4]\), joining it to \(\ell\in A_3\) and
\(j\in A_5\).

## Proposition

The resulting graph \(J_q\) satisfies:

1. \(J_q\cong S(K_{q,2q^4})\), the graph obtained by subdividing every
   edge of \(K_{q,2q^4}\) once.
2. \(J_q\) is connected, bipartite, and \(\chi(J_q)=2\).
3. Every cycle length is divisible by four, and

   \[
   t_{4r}(J_q)=\frac{(q)_r(2q^4)_r}{2r}
   \quad (2\le r\le q).
   \]

   All other simple-cycle counts vanish.
4. The adjacency spectrum is

   \[
   \begin{aligned}
   &\pm\sqrt{q+2q^4} &&\text{each once},\\
   &\pm\sqrt{2q^4} &&\text{each with multiplicity }q-1,\\
   &\pm\sqrt q &&\text{each with multiplicity }2q^4-1,\\
   &0 &&\text{with multiplicity }2q^5-q-2q^4+2.
   \end{aligned}
   \]

5. Every pair \((a_1,a_5)\in A_1\times A_5\) has exactly \(q\)
   length-four paths, one through each vertex of \(A_3\). Endpoint
   compression therefore produces \(K_{q^4,q^4}\), with \(q^8\) edges.

## Proof

Put \(X=A_3\) and \(Y=A_1\sqcup A_5\). Every pair in \(X\times Y\)
has exactly one corresponding vertex in \(A_2\sqcup A_4\), adjacent to
its two endpoints. These intermediate vertices are precisely the
subdivision vertices of \(K_{q,2q^4}\), proving (1).

The canonical bipartition of a one-subdivision places all original
vertices on one side and all subdivision vertices on the other. The graph
has edges and is connected, proving (2).

Subdivision doubles every cycle length and gives a bijection between
cycles of the base and subdivided graphs. A \(2r\)-cycle in \(K_{a,b}\)
can be counted by ordering \(r\) distinct vertices in each part and
dividing by its \(r\) starting points in the first part and two
orientations:

\[
t_{2r}(K_{a,b})=\frac{(a)_r(b)_r}{2r}.
\]

Substituting \(a=q\), \(b=2q^4\), and doubling lengths proves (3).

Let \(R\) be the unsigned vertex-edge incidence matrix of
\(K_{a,b}\). The adjacency matrix of the subdivision graph is

\[
\begin{pmatrix}0&R\\R^\mathsf{T}&0\end{pmatrix}.
\]

Its nonzero eigenvalues are the signed singular values of \(R\).
Moreover,

\[
RR^\mathsf{T}=Q(K_{a,b}),
\]

the signless Laplacian, whose eigenvalues are
\(a+b\), \(b\) with multiplicity \(a-1\), \(a\) with multiplicity
\(b-1\), and \(0\). Rank-nullity supplies the remaining zero
multiplicity, proving (4).

Finally, a boundary pair chooses any of the \(q\) middle vertices in
\(A_3\), with its adjacent subdivision vertices then forced. This proves
(5).

## Status

This is an elementary exact reformulation of the construction in Section
8.1 of *Enumerating Small Cycles*. It is not presented as a correction.
A targeted audit did not locate the source-specific normal-form
observation, so that observation is classified as plausibly original with
moderate confidence. The cycle formula and spectral calculation use
established complete-bipartite and subdivision-graph machinery. See
[`LITERATURE_NOVELTY_AUDIT.md`](../LITERATURE_NOVELTY_AUDIT.md).
