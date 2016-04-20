from adjacency_list import AdjacencyList

def top_sort(graph):
    """Returns a topological sort of a graph.

    Orders the vertices in graph on a line such that all directed
    edges go from left to right.

    Args:
        graph: AdjacencyList graph to sort. Must be acyclic.

    Returns:
        A list of the vertices of the graph in topological order.

    Raises:
        ValueError: graph contains a cycle.
    """
    discovered = set()
    processed = []
    verts = graph.vertices
    # How do we get a valid starting point?
    for vertex in verts.itervalues():
        for edge in vertex.edges.iterkeys():
            _process_edge(verts, verts[edge], discovered, processed)
        if vertex.name not in processed:
            processed.append(vertex.name)
    return processed[::-1]


def _process_edge(vertices, edge, discovered, processed):
    """Process an edge and its own edges."""
    if edge in discovered:
        if edge.name in processed:
            return
        else:
            raise ValueError("graph cannot contain a cycle")
    discovered.add(edge)
    for y in edge.edges.iterkeys():
        _process_edge(vertices, vertices[y], discovered, processed)
    if edge.name not in processed:
        processed.append(edge.name)


