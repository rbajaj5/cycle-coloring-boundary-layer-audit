from __future__ import annotations

import pytest

from cycle_coloring_interface.obstruction import (
    BoundaryLayerObstruction,
    count_simple_cycles_of_length,
    count_simple_paths_of_length,
    falling_factorial,
    graph_edge_count,
    is_connected,
    verify_bipartition,
)


def test_falling_factorial() -> None:
    assert falling_factorial(5, 0) == 1
    assert falling_factorial(5, 3) == 60
    assert falling_factorial(3, 4) == 0
    with pytest.raises(ValueError):
        falling_factorial(-1, 2)


def test_q2_normal_form_counts() -> None:
    family = BoundaryLayerObstruction(2)
    assert family.layer_sizes == (16, 32, 2, 32, 16)
    assert family.vertex_count == 98
    assert family.edge_count == 128
    assert family.cycle_rank == 31
    assert family.compressed_boundary_edge_count == 256
    assert family.length_four_paths_per_boundary_pair == 2
    assert family.cycle_count(8) == 496
    assert family.cycle_count(4) == 0
    assert family.cycle_count(6) == 0
    assert family.cycle_count(10) == 0
    assert family.cycle_count(12) == 0


def test_q3_cycle_formula() -> None:
    family = BoundaryLayerObstruction(3)
    assert family.cycle_count(8) == 39_123
    assert family.cycle_count(12) == 4_173_120
    assert family.cycle_count(16) == 0


def test_explicit_q2_graph_and_bipartition() -> None:
    family = BoundaryLayerObstruction(2)
    graph = family.build_graph()
    first, second = family.canonical_bipartition()
    assert len(graph) == family.vertex_count
    assert graph_edge_count(graph) == family.edge_count
    assert is_connected(graph)
    assert verify_bipartition(graph, first, second)
    assert count_simple_paths_of_length(
        graph,
        ("A1", 0),
        ("A5", 0),
        4,
    ) == family.q


def test_q2_brute_force_cycle_count_matches_formula() -> None:
    family = BoundaryLayerObstruction(2)
    graph = family.build_graph()
    for length in (4, 6, 8):
        assert count_simple_cycles_of_length(
            graph,
            length,
        ) == family.cycle_count(length)


def test_symbolic_spectrum_multiplicities_sum_to_vertices() -> None:
    for q in (2, 3, 4):
        family = BoundaryLayerObstruction(q)
        rows = family.adjacency_spectrum_multiplicities()
        assert sum(int(row["multiplicity"]) for row in rows) == (
            family.vertex_count
        )
        zero = next(row for row in rows if row["eigenvalue"] == "0")
        assert zero["multiplicity"] == family.cycle_rank + 1
