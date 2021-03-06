from collections import defaultdict
import heapq

def shortest_path(edges, start):
    """Returns the shortest path length to each vertex from a start vertex.

    Finds the length of the shortest path from start to every other vertex
        in edges using Dijkstra's algorithm.

    Args:
        edges: A list of edge tuples in the form (v1, v2, weight), where
            v1 and v2 are vertex names and may be numbers or strings.
            weight must be a non-negative number.
            All edges are treated as directed, with the edge going from
            v1 to v2.

        start: The name of the vertex from which to find a path.
            start may be a string or number, but must be included as a v1
            in edges in order to have any non-infinite, non-zero path lengths.

    Returns:
        A dictionary of the format {v: length}, where v is the name of the
            vertex and length is the length of the shortest path to that
            vertex from start.
            The distance to start is always 0, and the distance for any
            unreachable vertex is the float value for infinity.
            Returns the dictionary {start:0} if edges is empty.
    """
    # Edges originating from each vertex
    vertex_edges = defaultdict(list)
    # Set of all vertices, including vertices with no outgoing edges
    all_vertices = set()
    for edge in edges:
        vertex_edges[edge[0]].append(edge)
        all_vertices.update((edge[0], edge[1]))
    # Minimum known distances for each vertex
    distances = {vertex:float("inf") for vertex in all_vertices}
    distances[start] = 0
    # The set of vertices for which we know we have the minimum path
    visited = set()
    visited.add(start)
    # A shorter path could exist to these vertices, so don't mark them visited
    for edge in vertex_edges[start]:
        v1, v2, weight = edge
        # Don't change the 0 from start if there is a self loop from start
        distances[v2] = weight if v2 != start else 0
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
            distances[v2] = min(distances[v2], distances[v1] + weight)
        # Now have the minimum possible distance for current
        visited.add(current)
    return distances

def a_star(vertices, edges, start, goal):
    """Returns the distance of the shortest path from start to goal.

    Using the A* heuristic, finds the length of the shortest path
        from start to goal.

    Args:
        vertices: A list of vertex tuples in the following format:
            (name, x coordinate, y coordinate)
            name may be a number or string. x and y must be numbers,
            but can be positive, negative, or zero floating point values.

        edges: A list of edge tuples in the form (v1, v2), where
            v1 and v2 are vertex names, and may be numbers or strings.
            All edges are treated as directed, with the edge going from
            v1 to v2. All vertex names must also be included in the vertices
            parameter.

        start: The name of the vertex from which to find a path to goal.
            May be a string or number, but must be included in vertices.

        goal: The name of the end/destination vertex. May be a string or number,
            but must be included in vertices.

        start and goal must be both included in edges in order to return a
            non-infinite result.

    Returns:
        A floating point number that shows the shortest path distance
            from start to goal using a subset of the edges in edges.
            Returns the float value for infinity if there is no path from start
            to goal.
    """
    # The x,y coordinates of each vertex
    coords = {name:(x,y) for name, x, y in vertices}
    if start not in coords or goal not in coords:
        raise ValueError("Start and goal vertices must be in vertex list")
    # Track the connected vertices from each vertex
    graph = {vertex:[] for vertex in coords}
    for edge in edges:
        graph[edge[0]].append(edge[1])
    # The best known path length for each vertex
    distances = {vertex:float("inf") for vertex in coords}
    distances[start] = 0.0
    # The vertices for which we have confirmed the shortest path
    visited = set()
    # Track vertices in priority queue as (estimated distance, vertex) tuples
    queue = [(_get_dist(coords[start], coords[goal]), start)]
    while len(queue) > 0:
        # Get the vertex itself, no longer need to track its priority
        current = heapq.heappop(queue)[1]
        if current == goal:
            return distances[goal]
        # If we reach a neighbor with an outdated estimated value, it will
        # already have been visited with its updated (smaller) value
        if current in visited:
            continue
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor in visited:
                continue
            edge_distance = _get_dist(coords[current], coords[neighbor])
            # Distance from start to this neighboring node
            new_score = distances[current] + edge_distance
            if new_score >= distances[neighbor]:
                # This path is not an improvement
                continue
            # This path is an improvement, so add it
            distances[neighbor] = new_score
            # Neighbor's minimum distance (if it had an edge directly to goal)
            remaining_dist = _get_dist(coords[neighbor], coords[goal])
            # Estimated distance has been updated; re-add to heap
            heapq.heappush(queue, (new_score + remaining_dist, neighbor))
    return distances[goal]

def _get_dist(node, goal):
    """Returns the straight-line distance from node to goal."""
    x_dist = node[0] - goal[0]
    y_dist = node[1] - goal[1]
    return (x_dist**2 + y_dist**2)**0.5
