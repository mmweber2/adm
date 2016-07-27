from collections import namedtuple
from collections import defaultdict
from operator import attrgetter

# Namedtuple format: Edge, vertices, weight
# Points aren't start and end because they're undirected
Edge = namedtuple('Edge', ('vertex1', 'vertex2', 'value'))

# TODO: complete and test
class SpanningTree(object):
    """A representation of a spanning tree."""

    # TODO: What are allowable values?
    # TODO: Include root?
    def __init__(self, value):
        """Creates a new SpanningTree vertex with no edges.
        
        Args:
            value: The value to assign to this vertex. May be a number or
                string. 
            root: boolean indicating whether this vertex is the root.
                Defaults to False.
        """
        self.value = value
        self.edges = []

    def add_edge(self, edge):
        """Adds a new edge to this vertex.

        Args:
            edge: A namedtuple Edge to add.
        """
        self.edges.append(edge)

    # TODO
    def get_total_weight(self):
        """Returns the sum of the weights of the edges in this spanning tree."""
        return 0

# TODO: Prim's gives us the edges in the order we want. Does Kruskal's?
def build_mst(edges):
    root = SpanningTree(edges[0][0])
    for edge in edges:


def _is_connected(edges):
    # Avoid IndexError when choosing a vertex to start from
    if len(edges) == 0:
        return True
    connections = defaultdict(list)
    for edge in edges:
        start, end = edge.vertex1, edge.vertex2
        connections[start].append(end)
        connections[end].append(start)
    seen = set()
    # Arbitrary start vertex
    seen.add(edges[0].vertex1)
    queue = [edges[0].vertex1]
    while len(queue) > 0:
        current = queue.pop(0)
        new_edges = [x for x in connections[current] if x not in seen]
        seen.update(new_edges)
        queue.extend(new_edges)
    return len(seen) == len(connections)
    
def get_min_edges_kruskal(edges):
    """Returns a list of edges to connect all vertices with a minimum sum of
    weights.

    Uses Kruskal's algorithm.

    Args:
        edges: A list of Edge namedtuples of points and weights.
            All Edges must be part of one connected component.

    Returns:
        A list of edges connecting all vertices with the minimum sum of weights,
        in order of ascending weight.

    Raises:
        ValueError: At least one edge is disconnected (unreachable) from other
            edges.
    """
    if not _is_connected(edges):
        raise ValueError("Graph must be a single connected component")
    edges.sort(key=attrgetter('value'))
    # We are only building a subset of the graph, so don't add any edges yet
    connections = defaultdict(set)
    subgraph = []
    for edge in edges:
        v1, v2 = edge.vertex1, edge.vertex2
        # Can check these in either order, we will add both
        if v1 in connections[v2]:
            # Discard edge, points already connected
            continue
        # Merge connections of both vertices
        connections[v1].add(v2)
        for point in connections[v1]:
            connections[point].update(connections[v1])
        connections[v2].add(v1)
        for point in connections[v2]:
            connections[point].update(connections[v2])
        subgraph.append(edge)
    return subgraph

def get_min_edges_prim(edges):
    """Returns a list of edges to connect all vertices with a minimum sum of
    weights.

    Uses Prim's algorithm.

    Args:
        edges: A list of Edge namedtuples of points and weights.
            All Edges must be part of one connected component.

    Returns:
        A list of edges connecting all vertices with the minimum sum of weights,
            in arbitrary order, or an empty list if edges is empty.

    Raises:
        ValueError: At least one edge is disconnected (unreachable) from other
            edges.
    """
    if not _is_connected(edges):
        raise ValueError("Graph must be a single connected component")
    if len(edges) == 0:
        return []
    connections = defaultdict(list)
    for edge in edges:
        start, end = edge.vertex1, edge.vertex2
        # Add edges instead of points because we need to be able to look up the
        # edges when we add them to grow the components
        connections[start].append(edge)
        connections[end].append(edge)
    # Vertices included so far
    components = set()
    tree_edges = []
    # Pick arbitrary vertex to start from
    components.add(edges[0][0])
    while len(components) < len(connections):
        # Get all edges that connect to points in the component
        possible_edges = []
        for point in components:
            possible_edges.extend(connections[point])
        best_edge = None
        for edge in possible_edges:
            # We don't know which end of the edge is connected to our component,
            # but one of them must be. If both are connected, discard it.
            if edge.vertex1 in components and edge.vertex2 in components:
                continue
            # Edge connects a new vertex to the component; keep it
            if (not best_edge) or (edge.value < best_edge.value):
                best_edge = edge
        tree_edges.append(best_edge)
        # One of these vertices is already in components, but add both
        # to the set to ensure the new one is added
        components.update(best_edge.vertex1, best_edge.vertex2)
    return tree_edges
