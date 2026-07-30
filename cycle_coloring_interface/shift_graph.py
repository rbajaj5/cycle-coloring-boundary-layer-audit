"""Small exact audits for the shift graphs used in recurrence arguments."""

from __future__ import annotations

from itertools import combinations


ShiftVertex = tuple[int, ...]
ShiftGraph = dict[ShiftVertex, set[ShiftVertex]]


def build_shift_graph(m: int, k: int) -> ShiftGraph:
    """Build the undirected shift graph G_{m,k}.

    Vertices are increasing k-tuples from {1, ..., m}. Each increasing
    (k+1)-tuple contributes the edge joining its first and last k entries.
    """

    if m < 1:
        raise ValueError("m must be positive")
    if k < 1 or k > m:
        raise ValueError("k must satisfy 1 <= k <= m")

    graph: ShiftGraph = {
        vertex: set() for vertex in combinations(range(1, m + 1), k)
    }
    for extended in combinations(range(1, m + 1), k + 1):
        first = extended[:-1]
        second = extended[1:]
        graph[first].add(second)
        graph[second].add(first)
    return graph


def is_k_colorable(graph: ShiftGraph, color_count: int) -> bool:
    """Decide a small graph's colorability by exact DSATUR backtracking."""

    if color_count < 0:
        raise ValueError("color_count must be nonnegative")
    if not graph:
        return True
    if color_count == 0:
        return False

    colors: dict[ShiftVertex, int] = {}

    def search() -> bool:
        if len(colors) == len(graph):
            return True

        uncolored = (vertex for vertex in graph if vertex not in colors)
        vertex = max(
            uncolored,
            key=lambda item: (
                len(
                    {
                        colors[neighbor]
                        for neighbor in graph[item]
                        if neighbor in colors
                    }
                ),
                len(graph[item]),
                item,
            ),
        )
        forbidden = {
            colors[neighbor]
            for neighbor in graph[vertex]
            if neighbor in colors
        }
        for color in range(color_count):
            if color in forbidden:
                continue
            colors[vertex] = color
            if search():
                return True
            del colors[vertex]
        return False

    return search()


def exact_chromatic_number(graph: ShiftGraph) -> int:
    """Return the exact chromatic number of a small explicit graph."""

    if not graph:
        return 0
    for color_count in range(1, len(graph) + 1):
        if is_k_colorable(graph, color_count):
            return color_count
    raise RuntimeError("finite graph unexpectedly had no coloring")
