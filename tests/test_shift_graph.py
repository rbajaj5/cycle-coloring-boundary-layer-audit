"""Exact small-instance checks for shift graphs."""

from __future__ import annotations

import math

import pytest

from cycle_coloring_interface.obstruction import count_simple_cycles_of_length
from cycle_coloring_interface.shift_graph import (
    build_shift_graph,
    exact_chromatic_number,
)


@pytest.mark.parametrize(
    ("m", "expected"),
    ((4, 2), (5, 3), (6, 3), (7, 3), (8, 3), (9, 4)),
)
def test_classical_two_shift_chromatic_numbers(m: int, expected: int) -> None:
    graph = build_shift_graph(m, 2)
    assert exact_chromatic_number(graph) == expected


def test_two_shift_size_and_triangle_free() -> None:
    for m in range(4, 10):
        graph = build_shift_graph(m, 2)
        edge_count = sum(map(len, graph.values())) // 2
        assert len(graph) == math.comb(m, 2)
        assert edge_count == math.comb(m, 3)
        assert count_simple_cycles_of_length(graph, 3) == 0


def test_small_three_shift_graph() -> None:
    graph = build_shift_graph(6, 3)
    assert len(graph) == math.comb(6, 3)
    assert sum(map(len, graph.values())) // 2 == math.comb(6, 4)
    assert exact_chromatic_number(graph) == 2
