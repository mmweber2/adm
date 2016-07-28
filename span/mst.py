from collections import namedtuple
from collections import defaultdict
from operator import attrgetter

# Namedtuple format: Edge, vertices, weight
# Points aren't start and end because they're undirected
Edge = namedtuple('Edge', ('vertex1', 'vertex2', 'value'))

class SpanningTree(object):
    """A representation of a spanning tree."""
    # Share known vertices and total weight among all of the nodes
    vertices = {}
    total_weight = 0

    def __init__(self, name, weight):
        """Creates a new SpanningTree node with no edges.
        
        Args:
            name: The name to assign to this node. May be a number or
                string. 
            weight: Float, the weight between this node and its parent.
                Should be 0 for the root, or a positive number otherwise.
        """
        self.name = name
        self.weight = weight
        self.total_weight += weight
        self.children = []
        self.vertices[name] = self

    def add_child(self, edge):
        """Adds a new node to the Spanning Tree.

        Args:
            edge: A namedtuple Edge to add. Must connect a node in the
                tree with a new node not yet in the tree.

        Raises:
            ValueError: Edge links two nodes already in the SpanningTree,
                or Edge links two nodes and neither is in the SpanningTree.
        """
        # Expect format (old, new) by default and swap if opposite order
        parent = edge.vertex1
        child = edge.vertex2
        if child in self.vertices:
            if parent in self.vertices:
                raise ValueError("Edge links two nodes already in tree")
            parent, child = child, parent
        elif parent not in self.vertices:
            # Neither vertex is in the SpanningTree
            raise ValueError("Edge must contain one node already in tree")
        new_vertex = SpanningTree(child, edge.value)
        self.vertices[parent].children.append(new_vertex)

    # TODO: Complete
    def __str__(self):
        """Returns a string representation of this SpanningTree.

        Represents the tree in level order as follows:
        Root: (root name)
        Level 1: [((name of child), weight = <weight>) for child in children]
        Level 2: [((name of child), weight = <weight>) for child in children of each Level 1 child]
        .....
        """ 

# TODO: What to do if the list of edges contains non-minimum edges?
def build_mst(edges):
    """Builds a Minimum Spanning Tree using the provided edges.
    
    Args:
        edges: A list of edges with the minimum sum of weights to connect
            all vertices, as from get_min_edges_kruskal or get_min_edges_prim.

    Returns:
        A SpanningTree connected by the edges in edges.
    """
    # 0 distance to get from root to root
    root = SpanningTree(edges[0][0], 0)
    # Logic for handling edges and error checking is in add_child()
    for edge in edges:
        root.add_child(edge)
    return root

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
    forest = defaultdict(set)
    mst_edges = []
    for edge in edges:
        # TODO: Instead of attaching every vertex to every vertex it's connected
        # to, get rid of the individual vertices in the defaultdict and add new
        # vertices that merge them (ex. AB when merging A and B).
        # This will mean that we need to go through all forests to find the
        # vertices we are looking to merge.
        v1, v2 = edge.vertex1, edge.vertex2
        # Can check these in either order, we will add both
        if v1 in forest[v2]:
            # Discard edge, points already connected
            continue
        # Merge connections of both vertices
        forest[v1].add(v2)
        for vertex in forest[v1]:
            forest[vertex].update(forest[v1])
        forest[v2].add(v1)
        for vertex in forest[v2]:
            forest[vertex].update(forest[v2])
        mst_edges.append(edge)
    return mst_edges

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
    # Map of vertices to list of edges that involve them
    graph = defaultdict(list)
    for edge in edges:
        # Add edges instead of points because we need to be able to look up the
        # edges when we add them to grow the components
        graph[edge.vertex1].append(edge)
        graph[edge.vertex2].append(edge)
    # Vertices included so far
    forest = set()
    mst_edges = []
    # Pick arbitrary vertex to start from
    forest.add(edges[0].vertex1)
    while len(forest) < len(graph):
        # Get all edges that connect to points in the component
        best_edge = None
        for vertex in forest:
            for edge in graph[vertex]:
                # We don't know which end of the edge is connected in
                # forest, but one of them must be.
                #If both are connected, discard it.
                if edge.vertex1 in forest and edge.vertex2 in forest:
                    continue
                # Edge connects a new vertex to the forest; keep it
                if (not best_edge) or (edge.value < best_edge.value):
                    best_edge = edge
        # Shortest edge that connects the forest to a new element; keep it
        mst_edges.append(best_edge)
        # One of these vertices is already in forest, but add both
        # to the set to ensure the new one is added
        forest.update(best_edge.vertex1, best_edge.vertex2)
    return mst_edges
