class Vertex(object):
    """Represents a vertex node in a graph."""

    # Vertex names used so far
    existing = set()
    # For use by _make_test_vertex
    _count = 1

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

    @staticmethod
    def _make_test_vertex():
        """Test method for creating new vertices.

        Vertex names must be unique, so this method provides a way
        of generating unique Vertex names without having to manually
        keep track of them.

        Returns:
            A string in the format "Test1", where 1 is the class
            variable count.
        """
        while "Test" + str(Vertex._count) in Vertex.existing:
            Vertex._count += 1
        Vertex._count += 1
        return "Test" + str(Vertex._count)


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

    def __init__(self, vertex, weight=0.0):
        """Create a new Edge.

        Edges are assumed to be directed. If an undirected edge is
        required, one edge should be created for each direction.

        Args:
            vertex: The Vertex this Edge points to.
            weight: The weight of this Edge. If provided, must be
                an integer or a floating point value. Defaults to 0.

        Raises:
            ValueError: weight is not an integer or floating point value.
        """
        self.vertex = vertex
        self.weight = float(weight)

class Graph(object):

    def __init__(self, vertices):
        """Creates a new Graph with the given vertices.

        Args:
            vertices: An iterable of Vertex objects. If it contains
            duplicate vertices, only one of each will be added.
        """
        self.unique = set()
        self.vertices = []
        for vertex in vertices:
            if vertex not in self.unique:
                self.unique.add(vertex)
                self.vertices.append(vertex)

    def size(self):
        """Returns the number of vertices in the Graph."""
        return len(self.vertices)

    def add_vertex(self, vertex):
        """Adds a new Vertex to the Graph.

        Args:
            vertex: The new Vertex object to add. If vertex is already
            part of the graph, it will not be added again.

        Raises:
            TypeError: vertex is not a Vertex object.
        """
        if not isinstance(vertex, Vertex):
            raise TypeError("vertex to add must be a Vertex object")
        if vertex not in self.unique:
            self.vertices.append(vertex)
            self.unique.add(vertex)

    def is_connected(self):
        """Determines whether the Graph is connected.

        A Graph is considered connected if for each Vertex x, y, there
        exists a path from x to y, which also means that there is a path
        from y to x.
        If the Graph has less than two nodes in it, it is also considered
        connected.
        As more Vertices and Edges are added to a graph, its connectivity
        may change.

        Returns:
            True if the Graph is connected, or False otherwise.
        """
        # Check paths in both directions, x to y and y to x
        for i in xrange(len(self.vertices)):
            for j in xrange(len(self.vertices)):
                if find_path(self.vertices[i], self.vertices[j]) == []:
                    return False
        return True

def find_path(start, end):
    """Returns a path from start to end.

    Determines the shortest path (by number of vertices) between the
    two vertices. If the edges are weighted, the weights are disregarded.
    If there are multiple paths with the minimum length, one such path
    is returned arbitrarily.
    If start and end are the same Vertex, returns a list containing one
    element, start.

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
