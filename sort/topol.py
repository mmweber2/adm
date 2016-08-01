def topol(edges):
    """Returns a list of vertices in topological order.

    Args:
        edges: A list of edge tuples in the format (start, end), where each
            tuple represents a directed edge, and start and end are each names
            of vertices. These names can be strings or numbers.
            These edges may not contain cycles or self-loops.

            For example:
            [(1, 2), (2, 4)]
            [('a', 'c'), ('b', 'c'), ('c', 'd')]

    Returns:
        A list of vertices in edges in topological ordering, or an empty list
            if edges is empty.

    Raises:
        ValueError: edges contains at least one cycle, or at least one edge
            contains fewer or more than two vertex names.
    """
    if len(edges) == 0:
        return []
    # Collect the vertices reachable from each vertex
    # Use a dict instead of a defaultdict because a lookup on a vertex with
    # no edges would cause the defaultdict graph to grow in size, which doesn't
    # work if we are using graph to iterate through the vertices.
    # It would also be possible to make a list/tuple of graph and iterate
    # through the vertices that way.
    graph = dict()
    for edge in edges:
        start, end = edge
        if start not in graph:
            graph[start] = []
        graph[start].append(end)
        # Set graph[end] to empty list to avoid KeyError when getting its edges
        if end not in graph:
            graph[end] = []
    visited = set()
    stack = []
    sorted_vertices = []
    for vertex in graph:
        # The first vertex in a topological sort has no incoming edges, so it
        # cannot be visited before we try starting a search from it.
        if vertex not in visited:
            visit_vertex(vertex, graph, visited, set(), sorted_vertices)
    return sorted_vertices

def visit_vertex(vertex, graph, visited, seen, sorted_vertices):
    if vertex in seen:
        raise ValueError("edges contains a cycle at vertex {}".format(vertex))
    seen.add(vertex)
    for end_vertex in graph[vertex]:
        visit_vertex(end_vertex, graph, visited, seen, sorted_vertices)
    visited.add(vertex)
    seen.remove(vertex)
    sorted_vertices.insert(0, vertex)

    



