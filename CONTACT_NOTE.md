# Draft Note to the Paper Authors

Subject: A finite normal form for the Section 8.1 boundary-layer obstruction

Dear Or Stern and Or Zamir,

While reading *Enumerating Small Cycles* alongside
*k-Coloring is Faster than Computing the Chromatic Number*, we noticed a
compact exact description of the five-layer obstruction in Section 8.1.

With \(q=n^{0.2}\), the graph is the one-subdivision
\(S(K_{q,2q^4})\). This immediately gives:

- bipartiteness and chromatic number two;
- cycle lengths only in \(0\bmod 4\);
- the exact formula
  \(t_{4r}=(q)_r(2q^4)_r/(2r)\);
- a closed adjacency spectrum; and
- the \(q^8\)-edge compressed boundary graph, with \(q\) length-four
  witnesses per boundary pair.

We prepared a small public repository with the proof, exact tables, and an
independent brute-force check for \(q=2\). We view this as a concise
reformulation of your obstruction, not a correction or improvement to the
algorithmic bounds.

The comparison with the coloring paper also makes one boundary clear: the
cycle-enumeration obstruction already occurs in a bipartite graph, so it is
orthogonal to chromatic difficulty. We included a cautious suggestion that
residue-labeled path compression might be a useful diagnostic, without
claiming a new running-time result.

We would be grateful to know whether you have seen this subdivision normal
form used elsewhere, or whether the exact cycle/spectrum formulas are
useful to your presentation of the barrier.

Best,

Ravi Andrew Bajaj
Alexander Burns (invited coauthor; confirmation pending)
