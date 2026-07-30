"""Generate exact tables and a brute-force certificate for the obstruction."""

from __future__ import annotations

import csv
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from cycle_coloring_interface.obstruction import (
    BoundaryLayerObstruction,
    count_simple_cycles_of_length,
    count_simple_paths_of_length,
    graph_edge_count,
    is_connected,
    verify_bipartition,
)
from cycle_coloring_interface.shift_graph import (
    build_shift_graph,
    exact_chromatic_number,
)


RESULTS = ROOT / "results"


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def make_q2_certificate() -> dict[str, Any]:
    family = BoundaryLayerObstruction(2)
    graph = family.build_graph()
    first, second = family.canonical_bipartition()
    brute_cycle_counts = {
        str(length): count_simple_cycles_of_length(graph, length)
        for length in (4, 6, 8)
    }
    formula_cycle_counts = {
        str(length): family.cycle_count(length)
        for length in (4, 6, 8)
    }
    return {
        "q": 2,
        "graph_vertex_count": len(graph),
        "expected_vertex_count": family.vertex_count,
        "graph_edge_count": graph_edge_count(graph),
        "expected_edge_count": family.edge_count,
        "connected": is_connected(graph),
        "canonical_bipartition_valid": verify_bipartition(
            graph,
            first,
            second,
        ),
        "bipartition_sizes": [len(first), len(second)],
        "length_four_paths_A1_0_to_A5_0": (
            count_simple_paths_of_length(
                graph,
                ("A1", 0),
                ("A5", 0),
                4,
            )
        ),
        "expected_length_four_path_count": family.q,
        "brute_cycle_counts": brute_cycle_counts,
        "formula_cycle_counts": formula_cycle_counts,
        "cycle_counts_match": brute_cycle_counts == formula_cycle_counts,
        "status": "exact_finite_certificate",
    }


def make_report(
    summaries: list[dict[str, Any]],
    cycle_rows: list[dict[str, Any]],
    certificate: dict[str, Any],
    shift_rows: list[dict[str, Any]],
) -> str:
    q2 = summaries[0]
    q3 = summaries[1]
    q4 = summaries[2]
    shift_table = "\n".join(
        "| {m} | {vertex_count} | {edge_count} | {chromatic_number} | "
        "{cycle_3_count} | {cycle_4_count} | {cycle_6_count} |".format(
            **row
        )
        for row in shift_rows
    )
    return f"""# Boundary-Layer Cycle/Coloring Audit

## Result

The five-layer obstruction in Section 8.1 of Stern and Zamir's
*Enumerating Small Cycles* has the exact normal form

```text
J_q is the one-subdivision S(K_{{q, 2q^4}}).
```

Here `q = n^(1/5)` in the paper's integral parameterization. This
reformulation yields the following exact finite proposition:

1. `J_q` is connected and bipartite, so its chromatic number is `2`.
2. Every simple cycle has length divisible by `4`.
3. For `2 <= r <= q`,

   ```text
   number of C_(4r) = (q)_r (2q^4)_r / (2r).
   ```

4. Its adjacency spectrum is obtained from the signless-Laplacian spectrum
   of `K_{{q,2q^4}}`; in particular the spectral radius is
   `sqrt(q + 2q^4)` and the zero-eigenvalue multiplicity is the cycle rank
   plus one.
5. Every pair in `A1 x A5` has exactly `q` internally distinct
   length-four paths, so the compressed boundary graph has `q^8` edges.

This is a compact derivation of the paper's residue-class obstruction, not
a correction to either cited paper. We did not find this subdivision
normal form or the resulting cycle/spectrum formulas stated in their
texts. Literature priority has not been established.

## Small Exact Instances

| q | Vertices | Edges | Compressed boundary edges | C8 | C12 | C16 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | {q2["vertex_count"]} | {q2["edge_count"]} | {q2["compressed_boundary_edge_count"]} | {next(row["cycle_count"] for row in cycle_rows if row["q"] == 2 and row["cycle_length"] == 8)} | {next(row["cycle_count"] for row in cycle_rows if row["q"] == 2 and row["cycle_length"] == 12)} | {next(row["cycle_count"] for row in cycle_rows if row["q"] == 2 and row["cycle_length"] == 16)} |
| 3 | {q3["vertex_count"]} | {q3["edge_count"]} | {q3["compressed_boundary_edge_count"]} | {next(row["cycle_count"] for row in cycle_rows if row["q"] == 3 and row["cycle_length"] == 8)} | {next(row["cycle_count"] for row in cycle_rows if row["q"] == 3 and row["cycle_length"] == 12)} | {next(row["cycle_count"] for row in cycle_rows if row["q"] == 3 and row["cycle_length"] == 16)} |
| 4 | {q4["vertex_count"]} | {q4["edge_count"]} | {q4["compressed_boundary_edge_count"]} | {next(row["cycle_count"] for row in cycle_rows if row["q"] == 4 and row["cycle_length"] == 8)} | {next(row["cycle_count"] for row in cycle_rows if row["q"] == 4 and row["cycle_length"] == 12)} | {next(row["cycle_count"] for row in cycle_rows if row["q"] == 4 and row["cycle_length"] == 16)} |

The explicit `q=2` graph has `{certificate["graph_vertex_count"]}`
vertices and `{certificate["graph_edge_count"]}` edges. Independent DFS
counts `C4=0`, `C6=0`, and
`C8={certificate["brute_cycle_counts"]["8"]}`, exactly matching the
closed formula. The canonical bipartition and the two length-four paths
between the tested boundary pair also pass.

## Interface Between the Papers

Stern and Zamir show that their exact-cycle path-reporting abstraction
stops at `C16`: the `s=4` boundary-layer property is false, and their
construction has no cycles of lengths congruent to `2 mod 4` despite a
dense compressed endpoint graph.

Zamir's coloring paper proves sub-`2^n` algorithms for every fixed
`k`, bootstrapping from polynomial-time `2`-list-coloring. The same
obstruction family is already bipartite. Thus:

> The exact-length cycle-enumeration obstruction is orthogonal to
> chromatic difficulty; it occurs inside the easiest nontrivial coloring
> class.

This observation suggests a residue-aware path table rather than a
coloring-based repair. An auxiliary edge could retain attainable path
lengths modulo a small modulus. On `J_q`, the boundary label is immediately
`0 mod 4`, exposing the impossible `C18` charge before materializing the
large table. No improved asymptotic bound is claimed here.

## Shift-Graph Recurrence Audit

Ben Green's note on Alweiss's example uses finite shift graphs
`G_(m,k)` in one combinatorial step of its recurrence proof. For the
classical `k=2` shift graph, vertices are increasing pairs `(i,j)` and
edges join `(i,j)` to `(j,l)` when `i < j < l`.

| m | Vertices | Edges | Chromatic number | C3 | C4 | C6 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
{shift_table}

These rows are independently generated by explicit graph construction,
exact DSATUR coloring, and DFS cycle counting. They audit the finite graph
mechanism only. They do not reproduce or replace Green's nilmanifold,
equidistribution, or measure-theoretic arguments.

## Scope

- Exact finite combinatorics: proved and checked.
- `q=2` brute-force certificate: passed.
- Reformulation's literature novelty: unknown.
- New cycle-enumeration or coloring algorithm: not claimed.
- Improvement to either paper's theorem: not claimed.
- Green's analytic recurrence theorem: not independently verified here.

## Sources

- Or Stern and Or Zamir, *Enumerating Small Cycles*:
  https://arxiv.org/abs/2607.27147
- Or Zamir, *k-Coloring is Faster than Computing the Chromatic Number*:
  https://arxiv.org/abs/2607.25973
- Ben Green, *On Alweiss's example for multiple recurrence*:
  https://arxiv.org/abs/2607.24594
"""


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    families = [BoundaryLayerObstruction(q) for q in range(2, 7)]
    summaries = [family.exact_summary() for family in families]
    cycle_rows = [
        {
            "q": family.q,
            "cycle_length": length,
            "cycle_count": family.cycle_count(length),
            "nonzero": family.cycle_count(length) > 0,
            "length_residue_mod_4": length % 4,
            "status": "exact_formula",
        }
        for family in families
        for length in range(4, 25, 2)
    ]
    spectral_rows = [
        {
            "q": family.q,
            **row,
            "spectral_radius_squared": (
                family.base_left_size + family.base_right_size
            ),
            "status": "exact_symbolic",
        }
        for family in families
        for row in family.adjacency_spectrum_multiplicities()
    ]
    shift_rows = []
    for m in range(4, 10):
        graph = build_shift_graph(m, 2)
        shift_rows.append(
            {
                "m": m,
                "k": 2,
                "vertex_count": len(graph),
                "edge_count": sum(map(len, graph.values())) // 2,
                "chromatic_number": exact_chromatic_number(graph),
                "cycle_3_count": count_simple_cycles_of_length(graph, 3),
                "cycle_4_count": count_simple_cycles_of_length(graph, 4),
                "cycle_6_count": count_simple_cycles_of_length(graph, 6),
                "status": "exact_explicit_graph",
            }
        )
    certificate = make_q2_certificate()

    write_csv(RESULTS / "obstruction_family_summary.csv", summaries)
    write_csv(RESULTS / "exact_cycle_profiles.csv", cycle_rows)
    write_csv(RESULTS / "adjacency_spectrum_multiplicities.csv", spectral_rows)
    write_csv(RESULTS / "shift_graph_small_audit.csv", shift_rows)
    (RESULTS / "q2_bruteforce_certificate.json").write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (RESULTS / "RESULTS.md").write_text(
        make_report(summaries, cycle_rows, certificate, shift_rows),
        encoding="utf-8",
    )
    print(
        "Wrote exact q=2..6 tables and q=2 brute-force certificate; "
        f"C8(q=2)={certificate['brute_cycle_counts']['8']}."
    )


if __name__ == "__main__":
    main()
