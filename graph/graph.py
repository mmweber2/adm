class Vertex(object):
    """Represents a vertex node in a graph."""

    existing = set()

    def __init__(self, name, edges=None):
        """Create a new Vertex.

        Args:
            name: The name to be used to identify this Vertex.
                Must be unique.
            edges (optional): A list of edges from this Vertex. If no list is
                given, a new one will be created.

        Raises:
            ValueError: The name given for this Vertex is already in use.
            TypeError: edges is given, but is not a list.
        """
        if name in existing:
            raise ValueError("Name {} already exists".format(name))
        self.name = name
        self.existing.add(name)
        if edges == None:
            self.edges = []
        else:
            if not isinstance(edges, list):
                raise TypeError("edges attribute must be a list")
            self.edges = edges
