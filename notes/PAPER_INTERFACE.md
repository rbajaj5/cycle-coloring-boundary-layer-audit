# Interface Between the Two July 2026 Papers

## Enumerating Small Cycles

Stern and Zamir obtain near-quadratic preprocessing and polylogarithmic
delay for exact even-cycle enumeration through \(C_{16}\). Their
path-reporting construction compresses replaceable layered paths and
charges table entries to genuine cycles. The exact-length analysis depends
on a boundary-layer property that they prove for \(s=2,3\) and disprove
for \(s=4\).

The five-layer counterexample has a dense endpoint compression but permits
boundary-to-boundary paths only in one residue class modulo four.

## k-Coloring

Zamir proves that every fixed-\(k\) coloring problem has a randomized
\((2-\varepsilon_k)^n\) algorithm. The proof is phrased through
fixed-palette list coloring, with an iterative reduction that begins from
polynomial-time 2-list-coloring. Its quantitative saving has reciprocal
tower height \(\Theta(k)\), and improving that dependence is an explicit
open problem.

## Exact Intersection

The boundary-layer obstruction is bipartite. Therefore its failure mode
does not come from chromatic complexity: a linear-time bipartiteness test
settles its coloring.

The more relevant common abstraction is **state retained under
compression**:

- list-coloring reductions retain allowed color subsets;
- cycle path tables retain endpoint reachability and witnesses;
- the boundary obstruction shows that endpoint reachability without
  length residue loses information needed for exact-cycle charging.

This motivates a residue-aware path-table experiment. Each compressed edge
would carry the attainable path-length residues modulo a small modulus.
For the obstruction family the boundary residue is \(0\bmod 4\), so the
impossibility of a \(4r+2\) cycle is visible without expanding paths.

No claim is made that residue labels preserve the papers' target
preprocessing or delay bounds.
