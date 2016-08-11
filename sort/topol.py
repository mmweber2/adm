def topol(edges):
    """Returns a list of vertices in topological order.

    Args:
        edges: A list of edge tuples in the format (start, end), where each
            tuple represents a directed edge, and start and end are each names
            of vertices. These names can be strings or numbers.

            These edges may not contain cycles or self-loops.

            If there are multiple valid topological sorts for edges, one sort 
            is returned arbitrarily.
            
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
    # Collect the vertices reachable from each vertex.
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
    sorted_vertices = []
    for vertex in graph:
        sorted_vertices.extend(visit_vertex(vertex, graph, visited, set()))
    # Vertices were added in reverse order
    return sorted_vertices[::-1]

def visit_vertex(vertex, graph, visited, seen):
    """Recursive helper method for topol to determine sort."""
    # If we have visited the vertex on a previous pass, it is already part
    # of a vertex list
    if vertex in visited:
        return []
    # Encountered a vertex again while visiting its edges
    if vertex in seen:
        raise ValueError("edges contains a cycle at vertex {}".format(vertex))
    seen.add(vertex)
    vertices = []
    # Vertices with no out degrees will not recurse, so they will be added
    # to the vertices list first, followed by the vertices that linked to them
    for end_vertex in graph[vertex]:
        vertices += visit_vertex(end_vertex, graph, visited, seen)
    visited.add(vertex)
    return vertices + [vertex]

