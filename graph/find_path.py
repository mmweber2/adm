from adjacency_list import AdjacencyList

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
    # Before checking the whole graph for end, make sure it exists
    if not end in graph.vertices:
        raise KeyError
    queue = [start]
    # TODO: Make parent table, then back up through it from end.
    parent = dict()
    # TODO: Special case start = end?
    while queue != []:
        current = queue.pop(0)
        print "Current is {} and end is {}".format(current, end)
        if current == end:
            path = [end]
            while current != start:
                path.append(parent[current])
                current = graph.vertices[parent[current]]
            return [v for v in path[::-1]]
        for edge in graph.vertices[current].edges:
            queue.append(graph.vertices[edge])
            parent[edge] = current
    # No path found
    return []
