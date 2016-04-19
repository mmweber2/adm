from adjacency_list import AdjacencyList

def top_sort(graph):
    """Returns a topological sort of a graph.

    Orders the vertices in graph on a line such that all directed
    edges go from left to right. Works only on directed acyclic graphs.

    Args:
        graph: AdjacencyList graph to sort. Must be acyclic.

    Returns:
        A list of the vertices of the graph in topological order.
    """
    discovered = set()
    processed = []
    # How do we get a valid starting point?
    for vertex in graph.vertices.iterkeys():
        for edge in vertex.edges:
            _process_edge(graph.vertices[edge])
        if vertex not in processed:
            processed.append(vertex)
    return processed[::-1]


def _process_edge(edges, edge, discovered, processed):
    """Process an edge and its own edges."""
    if edge in discovered:
        if edge.name in processed:
            return
        else:
            raise ValueError("graph cannot contain a cycle")
    discovered.add(edge)
    for y in edge.edges.iterkeys():
        _process_edge(edges[y])
    processed.append(edge.name)


