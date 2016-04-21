from adjacency_list import AdjacencyList

def find_path(graph, start, end):
    """Attempts to find a path between start and end.

    Searches the graph from start to end using breadth-first search.

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
        if current in processed:
            continue
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
            if edge not in discovered:
                queue.append(edge)
                parent[edge] = current
                discovered.add(edge)
        processed.add(current)
    # No path found
    return []

def connected(graph):
    """Tells whether the graph is connected.

    Connectivity is defined as follows: for every vertex a, b
    in the graph, there exists a path from a to b. If there is
    only a path from b to a, the graph is not considered connected.

    Args:
        graph: The AdjacencyList to check for connectivity.
    Returns:
        True if every vertex in the graph can be reached from every
        other vertex in the graph, and False otherwise.
    Raises:
        AttributeError: graph is not a valid AdjacencyList object.
    """
    all_vertices = graph.vertices
    for start in all_vertices.iterkeys():
        for end in all_vertices.iterkeys():
            path = find_path(graph, start, end)
            if path == []:
                return False
    return True

def dfs(graph, start, end, finished=False, path=[], processed=None):
    """Search for a node in the graph using depth-first search.

        Args:
            graph: The AdjacencyList to search.
            start: The name of the start vertex.
            end: The name of the end vertex to which the path leads.
            finished: True if the graph has already found the end vertex.
                Defaults to False.
            path: The path taken to find the end vertex. Defaults to [].
            processed: The set of nodes traversed so far. Defaults to
                None.

        Returns:
            A list of edge names beginning with start and ending with
            end, showing a path from start to end.
            Returns an empty list if there are no valid paths from
            start to end.

        Raises:
            KeyError: start and/or end do not match vertex names in
            this graph.
    """
    if not end in graph.vertices:
        raise KeyError
    if processed == None:
        processed = set()
    if start == end:
        finished = True
    if finished:
        path += start
        return path[::-1]
    if start in processed:
        return path
    else:
        print "Start is ", start
        print "End is ", end
        for edge in graph.vertices[start].edges.iterkeys():
            print "Looking at edge ", edge
            if edge not in processed:
                dfs(graph, edge, end, finished, path, processed)
    processed.add(start)
    return path

     # If match: do something
     # If edges: search the edges
     # Go back
     # TODO
# Articulation vertices: Tree edges, back edges, forward edge, cross edge

def has_cycle(graph):
    """Determines whether graph contains one or more cycles."""

def is_bipartite(graph):
    """Determines whether the graph is bipartite."""
