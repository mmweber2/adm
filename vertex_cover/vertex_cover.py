from collections import defaultdict
def cover(edges):
    """Returns a vertex cover of the vertices in edges.
    
    Returns a maximal matching subset of the vertices in edges such that each
        edge is incident to at least one vertex in the subset.
    Uses a greedy algorithm that finds a cover at most twice as large as the
        optimal cover.

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
        if _get_vertex_count(graph[current[0]], covered) < 2:
            # Avoid adding vertices with 1 edge, unless both have only one edge
            cover.add(current[1])
        elif _get_vertex_count(graph[current[1]], covered) < 2:
            cover.add(current[0])
        else:
            cover.update(current)
        # Both should now be covered, regardless of which were added to cover
        covered.update(current)
        # Filter out any edges that touch a vertex in current
        remaining_edges = _get_remaining_edges(edges, covered)
    return cover

def _get_remaining_edges(edges, covered):
    """Returns a list of edges where each has two uncovered vertices."""
    return [x for x in edges if x[0] not in covered and x[1] not in covered]

def _find_best_edge(edges, graph, covered):
    """Returns the edge affecting the most highly connected vertices."""
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
    """Returns the number of vertices that are connected to this vertex."""
    # Filter out vertices already covered
    return sum(1 for v in vertex_list if v not in covered)
