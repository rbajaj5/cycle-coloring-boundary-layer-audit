# Green/Alweiss Shift-Graph Scope

Ben Green's *On Alweiss's example for multiple recurrence* uses the
chromatic growth of finite shift graphs as one combinatorial ingredient.
This repository can test that ingredient on small explicit instances:

- construct `G_(m,k)` from increasing tuples;
- count vertices, edges, and selected cycles;
- compute the exact chromatic number by backtracking; and
- compare `G_(m,2)` with the classical value `ceil(log2(m))`.

That is a genuine graph-level audit, but it is not an audit of the whole
recurrence proof. The following remain outside this repository:

- nil-Bohr sets and nilmanifolds;
- quantitative equidistribution;
- recurrence in measure-preserving systems; and
- the limiting argument that turns finite colorings into the stated
  dynamical conclusion.

The useful interface is methodological: both the cycle-enumeration
obstruction and the recurrence argument have a finite graph layer that can
be computed exactly, while their surrounding analytic claims require
different tools.
