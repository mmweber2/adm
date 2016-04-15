from adjacency_list import AdjacencyList

#TODO: Loops infinitely if there are cycles.
def find_path(graph, start, end):
    """Attempts to find a path between start and end.

    Args:
        graph: The AdjacencyList to search.
        start: The name of the start vertex.
        end: The name of the end vertex to which the path leads.

    Returns:
        A list of edge names beginning with start and ending with
        end, showing the shortest path (consisting of the fewest
        nodes) between the two vertices in an unweighted graph.
        If the graph is weighted, the weights are disregarded.
        Returns a list of a single vertex name (start) if start and
        end have the same name.
        Returns an empty list if there are no valid paths from
        start to end.

    Raises:
        KeyError: start and/or end do not match vertex names in
        this graph.
    """
    # Make sure end exists before traversing the full graph
    if not end in graph.vertices:
        raise KeyError
    queue = [start]
    # How we reached each node
    parent = dict()
    # We could avoid getting stuck in a cycle with just one set,
    # but two will allow us to avoid trying the same paths
    # multiple times.
    discovered = set()
    processed = set()
    while queue != []:
        current = queue.pop(0)
        # If we have a match, we don't need current's edges, so check
        # for a match first.
        if current == end:
            path = [end]
            while current != start:
                path.append(parent[current])
                # Hold onto the name of the vertex rather than
                # the vertex itself to allow for easy match checking,
                # as well as simplifying the resulting list.
                current = graph.vertices[parent[current]].name
            # Path is from end to start, so reverse it.
            return path[::-1]
        for edge in graph.vertices[current].edges:
            queue.append(edge)
            parent[edge] = current
            discovered.add(edge)
        processed.add(current)
    # No path found
    return []
    # TODO: Check discovered and processed before doing anything

    # TODO: Is connected?

