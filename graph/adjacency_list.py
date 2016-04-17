class Vertex(object):
    """Represents a vertex."""

    def __init__(self, name):
        """Create a new Vertex with the given name.

        By default, a new Vertex has no values associated with it.

        Args:
            name: The name of the Vertex, as it would appear on
            a graph. Used to identify this Vertex. May not be an
            empty string.

        Raises:
            ValueError: name is an empty string.
        """
        # Empty strings would make file parsing messy.
        if name == "":
            raise ValueError("name may not be an empty string.")
        self.name = name
        self.edges = dict()

class Edge(object):
    """Represents an edge of a vertex."""


    def __init__(self, name, weight="1"):
        """Creates a new edge.

        Args:
            name: The name of the vertex this edge points to.
            weight: The weight associated with this edge. Defaults to 1.
        """
        self.name = name
        self.weight = weight

class AdjacencyList(object):
    """Represents a graph as an adjacency list."""

    # TODO: Is the graph static once created?
    def __init__(self, input_data):
        """Creates a new adjacency list.

        Creates an adjacency list for the data provided. Data is
        assumed to be directed and weighted.

        Any edges without explicit weights will be assigned a
        weight of 1. Edges are assumed to be strings.

        Each edge may only have one weight; if more than two pipes
        are used in a line, any data after the third pipe will be
        ignored.

        Multiedges are not supported; if the same edge is listed
        multiple times, the last such edge's weight will be used.

        Args:
            input_data: The filename of the data to read in to create
            the graph. Data should be in the following format:

            Number of vertices as an integer. Must be greater than 1.
            Names of vertices. May contain spaces, but no pipes.
            Edges between vertices, in the format of both vertex names
                separated by a pipe. If the edges are weighted,
                a second pipe should be used before the weight.

            For example:
            5
            Tokyo
            Chicago
            San Francisco
            Madison
            Beijing
            Tokyo|Chicago|15
            Tokyo|Beijing|2
            Tokyo|San Francisco|20
            Chicago|Tokyo|35
            Chicago|Madison
            San Francisco|Tokyo|6
            Madison|Chicago|5
            Beijing|Tokyo

            Or:

            2
            Sam
            Paul
            Sam|Paul

        Raises:
            IOError: input_data does not exist.

            ValueError: input_data is not formatted correctly.
            Either the number of vertices is not a valid integer,
            the list of vertices does not match the number provided,
            or the list of edges contains at least one line without
            a pipe.
            KeyError: input_data contains at least one vertex name
            not provided in the vertex list.
        """
        self.vertices = self._parse_file(input_data)

    def size(self):
        """The number of vertices in the AdjacencyList."""
        return len(self.vertices)

    def _parse_file(self, input_data):
        """Parse a file from which to create a new Adjacency List.

        For use by the AdjacencyList constructor.
        """
        input_file = []
        vertices = dict()
        with open(input_data, 'r') as filename:
            input_file = filename.readlines()
        # Strip all trailing newlines
        input_file = [line.strip() for line in input_file]
        vertex_count = int(input_file.pop(0))
        if vertex_count < 2:
            raise ValueError("Number of vertexes must be > 1.")
        # Vertex count might still be incorrect, but we won't know
        # for sure until we check the edge data.
        if vertex_count > len(input_file):
            raise ValueError(
                    "Number of vertexes must not be greater than the" +
                     " number of lines following it in the file."
                    )
        # Gather vertex names
        for vertex_name in input_file[:vertex_count]:
            if '|' in vertex_name:
                raise ValueError("Vertex names may not contain pipes.")
            vertices[vertex_name] = Vertex(vertex_name)
        # Gather edges; look at remaining indices
        for i in xrange(vertex_count, len(input_file)):
            line = input_file[i].split('|')
            if len(line) < 2:
                # Use i + 1 because we removed the vertex count line
                error = ("Line {} does not contain a pipe").format(i + 1)
                raise ValueError(error)
            vertex, edge = line[0], line[1]
            # Ignore any data that might be after a third pipe
            if len(line) > 2:
                new_edge = Edge(edge, line[2])
            else:
                new_edge = Edge(edge)
            vertices[vertex].edges[edge] = new_edge
        return vertices
