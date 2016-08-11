from collections import defaultdict

def shortest_path(edges, start):
    """Returns the lengths of the shortest paths from a given start point.

    Finds the length of the shortest path from start to every other vertex
        in edges using Dijkstra's algorithm.

    Args:
        edges: A list of edge tuples in the form (v1, v2, weight),
            where v1 and v2 are vertex names.
            v1 and v2 may be numbers or strings.
            weight must be a non-negative number.
            All edges are assumed to be directed.

        start: The name of the vertex from which to find a path.
            start may be a string or number, but must be included as a v1
            in edges in order to have any non-infinite, non-zero path lengths.

    Returns:
        A dictionary of the format {v: length}, where v is the name of the
            vertex and length is the length of the shortest path to that
            vertex from start.
            The distance to start is always 0, and the distance for any
            unreachable vertex is infinity.
            Returns the dictionary {start:0} if edges is empty.
    """
    vertex_edges = defaultdict(list)
    for edge in edges:
        vertex_edges[edge[0]].append(edge)
    # Minimum known distances for each vertex
    distances = {vertex:float("inf") for vertex in vertex_edges}
    distances[start] = 0
    # The set of vertices for which we know we have the minimum path
    visited = set()
    visited.add(start)
    # A shorter path could exist to these vertices, so don't mark them visited
    for edge in vertex_edges[start]:
        v1, v2, weight = edge
        distances[v2] = weight
    # Reach all accessible vertices by traversing all outgoing edges
    while len(visited) < len(vertex_edges):
        current = None
        closest_distance = float("inf")
        # Select next vertex from which to branch
        for v in distances:
            if v not in visited and distances[v] < closest_distance:
                closest_distance = distances[v]
                current = v
        if current is None:
            # Only unreachable vertices are unvisited
            break
        for edge in vertex_edges[current]:
            v1, v2, weight = edge
            distances[v2] = min(distances[v2], distances[v] + weight)
        visited.add(current)
    return distances

        

    


