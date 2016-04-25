import graph

def graph_from_file(handle):
    """Creates a new Graph from a file.

    The file handle must be in the following format:

    Number of vertices (as integer >= 0)
    Vertex names (one line each, must be unique)
    Edges, in the format of two vertex names linked by a pipe
    (Optional) Weights, linked to the edges by a pipe

    For example:
    Without weights:
    3
    John
    Paul
    George
    John|George
    George|Paul

    With weights:
    2
    Chicago
    San Francisco
    Chicago|San Francisco|200
    San Francisco|Chicago|100

    If the number of vertices is 0, an empty graph will be created.
    Edges without weights will be assigned a weight of 0 by default.

    Args:
        handle: The file handle from which to create the Graph.

    Returns:
        A Graph object with vertices and edges as described in the file.

    Raises:
        ValueError: The file handle was incorrectly formatted.
    """
    lines = handle.read().split('\n')
    # Check vertex count for floats
    if float(lines[0]) % 1 != 0.0:
        raise ValueError("Vertex count must be an integer")
    vertex_count = int(lines[0])
    if vertex_count < 0:
        raise ValueError("Vertex count must be a non-negative integer")
    # If we don't check for a 0 vertex count here, it will cause the parser
    # to look for edges starting at line 0.
    if vertex_count == 0:
        return graph.Graph([])
    vertices = []
    # Offset by 1 to account for the vertex count line
    for vertex_name in lines[1:vertex_count+1]:
        if "|" in vertex_name:
            raise ValueError("Vertex names may not contain pipes")
        vertices.append(graph.Vertex(vertex_name))
        print "Made Vertex with name {}.".format(vertex_name)
    for edge_data in lines[vertex_count+1:]:
        line = edge_data.split("|")
        if len(line) < 2:
            raise ValueError("Edge lines must contain at least one pipe")
        for vertex in vertices:
            # Find the Vertex objects that match these names
            from_vertex = None
            to_vertex = None
            if vertex.name == line[0]:
                from_vertex = vertex
            # Not an elif because it could be a self loop
            if vertex.name == line[1]:
                to_vertex = vertex
        if len(line) > 2:
            new_edge = graph.Edge(to_vertex, line[2])
        else:
            new_edge = graph.Edge(to_vertex)
        from_vertex.add_edge(new_edge)
    return graph.Graph(vertices)

