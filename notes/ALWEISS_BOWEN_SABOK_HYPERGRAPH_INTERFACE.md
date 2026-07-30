# Two-Color Pattern Hypergraph Interface

Ryan Alweiss, Matthew Bowen, and Marcin Sabok prove that every two-coloring
of the positive integers contains, for each fixed `k`, monochromatic
patterns of the forms

```text
{x, y, xy, x + iy : i <= k}
{x, y, x^y, xy^i : i <= k}.
```

The natural finite computational object is a hypergraph, not an ordinary
graph. For a cutoff `N`, let the vertices be `[N]` and insert one hyperedge
for every instance of the selected pattern whose entries all lie in
`[N]`. A red/blue coloring avoids the pattern exactly when every hyperedge
contains both colors. This is:

- hypergraph property B;
- hypergraph 2-colorability; or
- a monotone not-all-equal SAT instance.

For each hyperedge `E`, the Boolean encoding adds the two clauses

```text
OR(x_v for v in E)
OR(not x_v for v in E).
```

The infinite theorem has a standard finite compactness consequence: for
each fixed `k`, some finite cutoff `N(k)` already gives a non-2-colorable
pattern hypergraph. Otherwise, a nested subsequence of avoiding colorings
on every `[N]` would produce an avoiding coloring of all positive
integers.

## Important Diagnostic Boundary

The incidence graph of every such hypergraph is bipartite, regardless of
whether the hypergraph itself is 2-colorable. Therefore:

> Ordinary chromatic number of the incidence graph cannot detect the
> monochromatic-pattern obstruction.

Cycle counts and spectra of the incidence graph can still quantify pattern
overlap, but a decisive finite experiment must solve hypergraph
2-colorability or the equivalent not-all-equal SAT instance.

This paper supplies a structure-versus-randomness perspective and a clean
future finite-witness experiment. It does not directly strengthen the
simple-cycle enumeration formulas, the fixed-`k` graph-coloring algorithm,
the four-color theorem, or a knot invariant.

Source:

- Ryan Alweiss, Matthew Bowen, and Marcin Sabok,
  *Sums, products, and exponents in two-colorings of the naturals*,
  https://arxiv.org/abs/2512.09598
