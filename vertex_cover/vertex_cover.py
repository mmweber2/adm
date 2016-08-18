from collections import defaultdict
def cover(edges):
    """Returns a vertex cover of the vertices in edges.
    
    Returns a maximal matching subset of the vertices in edges such that each
        edge is incident to at least one vertex in the subset.
    Uses a greedy algorithm that finds a cover at most twice as large as the
        optimal cover, with some additional optimizations to reduce the size
        of the cover.

    Args:
        edges: A list of tuples in the form (v1, v2), where v1 and v2 are
            vertex names. v1 and v2 may be strings or numbers.

    Raises:
        TypeError: edges does not consist of tuples.

        ValueError: At least one tuple in edges contains fewer than 2 vertices.

    Returns:
        A set of vertex names (strings or numbers as listed in edges) indicating
            the vertex cover of the graph.
            Returns an empty set if edges is empty.
    """
    graph = defaultdict(list)
    for edge in edges:
        start, end = edge
        graph[start].append(end)
        graph[end].append(start)
    remaining_edges = edges[:]
    # Result vertex cover
    cover = set()
    # Vertices 'covered' through an edge to a vertex in cover or cover itself
    covered = set()
    while len(remaining_edges) > 0:
        current = _find_best_edge(remaining_edges, graph, covered)
        start, end = current
        if _get_vertex_count(graph[start], covered) < 2:
            # Avoid adding vertices with 1 edge, unless both have only one edge
            cover.add(end)
        elif _get_vertex_count(graph[end], covered) < 2:
            cover.add(start)
        else:
            cover.update(current)
        # Both should now be covered, regardless of which were added to cover
        covered.update(current)
        # Filter out any edges that touch a vertex in current
        remaining_edges = _get_remaining_edges(edges, covered)
    return cover

def _get_remaining_edges(edges, covered):
    """Returns a list of edges such that each has two uncovered vertices."""
    return [x for x in edges if x[0] not in covered and x[1] not in covered]

def _find_best_edge(edges, graph, covered):
    """Returns the edge indirectly connected to the most active vertices."""
    # An edge is considered indirectly connected to a vertex if it connects
    # to another vertex that has an edge to the first vertex.
    max_edges = 0
    best_edge = edges[0]
    for edge in edges:
        # Get sum of active (not already covered) vertices
        affects = sum(_get_vertex_count(graph[v], covered) for v in edge)
        if affects > max_edges:
            max_edges = affects
            best_edge = edge
    return best_edge

def _get_vertex_count(vertex_list, covered):
    """Returns the number of uncovered vertices in vertex_list."""
    # Filter out vertices already covered
    return sum(1 for v in vertex_list if v not in covered)

def is_valid_cover(edges, cover):
    """Returns True iff cover is a valid set cover of edges.

    A set cover is a subset of vertices such that for each edge in edges,
    at least one of the two vertices touching that edge is part of the cover.
    This function does not check whether the cover is the minimum possible
    cover, only whether all of the edges are covered by this cover.
    If cover contains vertex names that are not part of edges, they will not
    affect the result of this function, since they only serve to make the
    cover larger.

    Args:
        edges: A list of tuples in the form (v1, v2), where v1 and v2 are
            vertex names. v1 and v2 may be strings or numbers.

        cover: A set of vertex names to test for coverage of edges.

    Raises:
        TypeError: edges does not consist of tuples.

        ValueError: At least one tuple in edges contains fewer than 2 vertices.

    Returns:
        True if cover is sufficient to cover all edges, or False otherwise.
        This function always returns True if edges is empty.
    """
    for edge in edges:
        start, end = edge
        if not (start in cover or end in cover):
            return False
    return True
