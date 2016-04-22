class Vertex(object):
    """Represents a vertex node in a graph."""

    existing = set()

    def __init__(self, name, edges=None):
        """Creates a new Vertex.

        Args:
            name: The string used to identify this Vertex.
                Must be unique, but is not case sensitive.
            edges (optional): A list of edges from this Vertex. If no list is
                given, a new one will be created.

        Raises:
            ValueError: The name given for this Vertex is already in use.
            TypeError: edges is given, but is not a list.
        """
        if name in self.existing:
            raise ValueError("Name {} already exists".format(name))
        self.name = name
        self.existing.add(name)
        if edges == None:
            self.edges = []
        else:
            if not isinstance(edges, list):
                raise TypeError("edges attribute must be a list")
            self.edges = edges

    def __repr__(self):
        """Provides a string representation for this Vertex."""
        return "Vertex: {}".format(self.name)


    def add_edge(self, edge):
        """Adds a new Edge to this Vertex.

        Multiedges are supported, so Edges with the same name may
            be added multiple times.

        Args:
            edge: The Edge to add. May or may not have a weight.

        Raises:
            TypeError: edge is not an Edge object.
        """
        if not isinstance(edge, Edge):
            raise TypeError("edge must be an Edge object")
        self.edges.append(edge)

class Edge(object):

    def __init__(self, vertex, weight=0):
        """Create a new Edge.

        Edges are assumed to be directed. If an undirected edge is
        required, one edge should be created for each direction.

        Args:
            vertex: The Vertex this Edge points to.
            weight: The weight of this Edge. If provided, must be
                an integer or a float. Defaults to 0.
        """
        self.vertex = vertex
        self.weight = weight

class Graph(object):

    def __init__(self, vertices):
        """Create a new Graph with the given vertices.

        Args:
            vertices: An iterable of Vertex objects.
        """
        self.vertices = vertices

def find_path(start, end):
    """Returns a path from start to end.
       
    Determines the shortest path (by number of vertices) between the
    two vertices. If the edges are weighted, the weights are disregarded.
    If there are multiple paths with the minimum length, one such path
    is returned arbitrarily.

    Args:
        start, end: Vertex objects between which to find a path.

    Returns:
        Returns a list of Vertex objects representing the shortest path
        (by number of vertices) between the two vertices. If no such path
        exists, returns [].

    Raises:
        AttributeError: start is not a valid Vertex object.
    """
    # Start may be end to begin with, so don't overlook it
    queue = [start]
    # Track how we got to each Vertex
    parent = {start:None}
    while queue != []:
        current = queue.pop(0)
        if current == end:
            path = []
            while current != None:
                path.insert(0, current)
                current = parent[current]
            return path
        # Only add edges we haven't already looked at
        new_edges = []
        for edge in current.edges:
            if edge.vertex not in parent:
                new_edges.append(edge.vertex)
                parent[edge.vertex] = current
        queue.extend(new_edges)
    # Ran out of queue; no path exists
    return []

def dfs(start, goal):
    """Search for goal using depth first search.

    In order for dfs to find the goal node, there must exist a path
    from start to goal.

    Args:
        start: The starting Vertex from which to search.
        goal: The Vertex for which to search.
    Returns:
        True if goal was found, or False otherwise.
    """
    discovered = set()
    stack = [start]
    while stack != []:
        current = stack.pop()
        if current == goal:
            return True
        for edge in current.edges:
            if edge.vertex not in discovered:
                discovered.add(edge.vertex)
                stack.append(edge.vertex)
    # Ran out of edges; no such path
    return False



