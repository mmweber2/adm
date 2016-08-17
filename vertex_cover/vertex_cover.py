from collections import defaultdict
def cover(edges):
    """Returns a vertex cover of the vertices in edges.
    
    Returns a maximal matching subset of vertices listed in edges such that each
        edge is incident to at least one vertex in the subset.

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
        graph[start].append(edge)
        graph[end].append(edge)
    remaining_edges = edges[:]
    cover = set()
    while len(remaining_edges) > 0:
        current = remaining_edges.pop()
        cover.update(edge)
        adj_edges = set(graph[current[0]] + graph[current[1]])
        remaining_edges = [x for x in remaining_edges if x not in adj_edges]
    return cover

        
