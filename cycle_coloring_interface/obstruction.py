"""Finite normal form for the five-layer boundary-property obstruction."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import math
from typing import Iterable


Vertex = tuple[str, int] | tuple[str, int, int]
Graph = dict[Vertex, set[Vertex]]


def falling_factorial(value: int, length: int) -> int:
    """Return (value)_length exactly."""

    if value < 0 or length < 0:
        raise ValueError("value and length must be nonnegative")
    if length > value:
        return 0
    product = 1
    for offset in range(length):
        product *= value - offset
    return product


def _add_edge(graph: Graph, first: Vertex, second: Vertex) -> None:
    graph.setdefault(first, set()).add(second)
    graph.setdefault(second, set()).add(first)


@dataclass(frozen=True)
class BoundaryLayerObstruction:
    """Integral finite member of the Stern-Zamir Section 8.1 family.

    Setting q = n^(1/5) turns the five layer sizes into
    q^4, q^5, q, q^5, q^4. The resulting graph is canonically the
    one-subdivision of K_{q, 2q^4}.
    """

    q: int

    def __post_init__(self) -> None:
        if self.q < 2:
            raise ValueError("q must be at least 2")

    @property
    def base_left_size(self) -> int:
        return self.q

    @property
    def base_right_size(self) -> int:
        return 2 * self.q**4

    @property
    def layer_sizes(self) -> tuple[int, int, int, int, int]:
        return (
            self.q**4,
            self.q**5,
            self.q,
            self.q**5,
            self.q**4,
        )

    @property
    def vertex_count(self) -> int:
        a = self.base_left_size
        b = self.base_right_size
        return a + b + a * b

    @property
    def edge_count(self) -> int:
        return 2 * self.base_left_size * self.base_right_size

    @property
    def cycle_rank(self) -> int:
        return self.edge_count - self.vertex_count + 1

    @property
    def chromatic_number(self) -> int:
        return 2

    @property
    def compressed_boundary_edge_count(self) -> int:
        """Number of A1-A5 edges after endpoint-pair compression."""

        return self.q**8

    @property
    def length_four_paths_per_boundary_pair(self) -> int:
        return self.q

    def cycle_count(self, cycle_length: int) -> int:
        """Count unoriented simple cycles of the requested length.

        Every cycle is the subdivision of a cycle in K_{q,2q^4}. Hence
        only lengths 4r occur, and their count is

            (q)_r (2q^4)_r / (2r).
        """

        if cycle_length < 3:
            raise ValueError("cycle length must be at least 3")
        if cycle_length % 4:
            return 0
        r = cycle_length // 4
        if r < 2:
            return 0
        numerator = (
            falling_factorial(self.base_left_size, r)
            * falling_factorial(self.base_right_size, r)
        )
        denominator = 2 * r
        if numerator % denominator:
            raise ArithmeticError("cycle count formula lost integrality")
        return numerator // denominator

    def cycle_profile(
        self,
        lengths: Iterable[int] = range(3, 21),
    ) -> dict[int, int]:
        return {length: self.cycle_count(length) for length in lengths}

    def adjacency_spectrum_multiplicities(
        self,
    ) -> tuple[dict[str, int | str], ...]:
        """Return the exact adjacency spectrum in symbolic rows."""

        a = self.base_left_size
        b = self.base_right_size
        return (
            {
                "eigenvalue": f"+sqrt({a + b})",
                "eigenvalue_squared": a + b,
                "multiplicity": 1,
            },
            {
                "eigenvalue": f"-sqrt({a + b})",
                "eigenvalue_squared": a + b,
                "multiplicity": 1,
            },
            {
                "eigenvalue": f"+sqrt({b})",
                "eigenvalue_squared": b,
                "multiplicity": a - 1,
            },
            {
                "eigenvalue": f"-sqrt({b})",
                "eigenvalue_squared": b,
                "multiplicity": a - 1,
            },
            {
                "eigenvalue": f"+sqrt({a})",
                "eigenvalue_squared": a,
                "multiplicity": b - 1,
            },
            {
                "eigenvalue": f"-sqrt({a})",
                "eigenvalue_squared": a,
                "multiplicity": b - 1,
            },
            {
                "eigenvalue": "0",
                "eigenvalue_squared": 0,
                "multiplicity": a * b - a - b + 2,
            },
        )

    def spectral_radius(self) -> float:
        return math.sqrt(self.base_left_size + self.base_right_size)

    def build_graph(self, maximum_vertices: int = 100_000) -> Graph:
        """Construct the five-layer graph explicitly."""

        if self.vertex_count > maximum_vertices:
            raise ValueError(
                f"graph has {self.vertex_count} vertices; "
                f"limit is {maximum_vertices}"
            )
        graph: Graph = {}
        q4 = self.q**4
        for middle in range(self.q):
            a3: Vertex = ("A3", middle)
            graph.setdefault(a3, set())
            for left in range(q4):
                a1: Vertex = ("A1", left)
                a2: Vertex = ("A2", left, middle)
                _add_edge(graph, a1, a2)
                _add_edge(graph, a2, a3)
            for right in range(q4):
                a4: Vertex = ("A4", middle, right)
                a5: Vertex = ("A5", right)
                _add_edge(graph, a3, a4)
                _add_edge(graph, a4, a5)
        return graph

    def canonical_bipartition(self) -> tuple[set[Vertex], set[Vertex]]:
        original: set[Vertex] = set()
        subdivision: set[Vertex] = set()
        q4 = self.q**4
        original.update(("A1", index) for index in range(q4))
        original.update(("A3", index) for index in range(self.q))
        original.update(("A5", index) for index in range(q4))
        subdivision.update(
            ("A2", left, middle)
            for left in range(q4)
            for middle in range(self.q)
        )
        subdivision.update(
            ("A4", middle, right)
            for middle in range(self.q)
            for right in range(q4)
        )
        return original, subdivision

    def exact_summary(self) -> dict[str, int | float | str]:
        a = self.base_left_size
        b = self.base_right_size
        zero_multiplicity = a * b - a - b + 2
        return {
            "q": self.q,
            "normal_form": f"S(K_{{{a},{b}}})",
            "layer_A1": self.layer_sizes[0],
            "layer_A2": self.layer_sizes[1],
            "layer_A3": self.layer_sizes[2],
            "layer_A4": self.layer_sizes[3],
            "layer_A5": self.layer_sizes[4],
            "vertex_count": self.vertex_count,
            "edge_count": self.edge_count,
            "cycle_rank": self.cycle_rank,
            "chromatic_number": self.chromatic_number,
            "compressed_boundary_edge_count": (
                self.compressed_boundary_edge_count
            ),
            "length_four_paths_per_boundary_pair": (
                self.length_four_paths_per_boundary_pair
            ),
            "cycle_length_period": 4,
            "spectral_radius_squared": a + b,
            "zero_eigenvalue_multiplicity": zero_multiplicity,
            "zero_multiplicity_equals_cycle_rank_plus_one": (
                zero_multiplicity == self.cycle_rank + 1
            ),
        }


def graph_edge_count(graph: Graph) -> int:
    return sum(len(neighbors) for neighbors in graph.values()) // 2


def is_connected(graph: Graph) -> bool:
    if not graph:
        return True
    root = next(iter(graph))
    seen = {root}
    queue = deque((root,))
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return len(seen) == len(graph)


def verify_bipartition(
    graph: Graph,
    first: set[Vertex],
    second: set[Vertex],
) -> bool:
    if first & second or first | second != set(graph):
        return False
    return all(
        (vertex in first) != (neighbor in first)
        for vertex, neighbors in graph.items()
        for neighbor in neighbors
    )


def count_simple_paths_of_length(
    graph: Graph,
    start: Vertex,
    end: Vertex,
    length: int,
) -> int:
    """Count simple start-to-end paths with an exact small length."""

    if length < 1:
        raise ValueError("length must be positive")
    visited = {start}

    def search(vertex: Vertex, depth: int) -> int:
        if depth == length:
            return int(vertex == end)
        if vertex == end:
            return 0
        total = 0
        for neighbor in graph[vertex]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            total += search(neighbor, depth + 1)
            visited.remove(neighbor)
        return total

    return search(start, 0)


def count_simple_cycles_of_length(graph: Graph, length: int) -> int:
    """Count unoriented simple cycles by canonical minimum vertex."""

    if length < 3:
        raise ValueError("length must be at least 3")
    vertices = sorted(graph)
    count = 0
    for start in vertices:
        visited = {start}

        def search(vertex: Vertex, depth: int) -> None:
            nonlocal count
            if depth == length:
                if start in graph[vertex]:
                    count += 1
                return
            for neighbor in graph[vertex]:
                if neighbor == start or neighbor in visited:
                    continue
                if neighbor < start:
                    continue
                visited.add(neighbor)
                search(neighbor, depth + 1)
                visited.remove(neighbor)

        search(start, 1)
    if count % 2:
        raise ArithmeticError("orientation quotient is not integral")
    return count // 2
