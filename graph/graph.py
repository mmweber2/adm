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

    def __init__(self, name, weight=None):
        """Create a new Edge.

        Args:
            name: The name of the Vertex this Edge points to.
            weight: The weight of this Edge. Defaults to None.
        """
        self.name = name
        self.weight = weight

