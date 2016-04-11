import sys

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
        self.edges = set()

class AdjacencyList(object):
    """Represents a graph as an adjacency list."""

    # TODO: Support weights.
    # TODO: Determine exceptions
    # TODO: Is the graph static once created?
    def __init__(self, input_data):
        """Creates a new adjacency list.

        Creates an adjacency list for the data provided. Data is
        assumed to be directed and cannot be weighted.

        Args:
            input_data: The filename of the data to read in to create
            the graph. Data should be in the following format:

            Number of vertices as an integer. Must be greater than 0.
            Names of vertices. May contain spaces, but no pipes.
            Links between vertices, shown as both names separated by
                a pipe.

            For example:
            5
            Tokyo
            Chicago
            San Francisco
            Madison
            Beijing
            Tokyo|Chicago
            Tokyo|Beijing
            Tokyo|San Francisco
            Chicago|Tokyo
            Chicago|Madison
            San Francisco|Tokyo
            Madison|Chicago
            Beijing|Tokyo

        Raises:
            IOError: input_data does not exist.

            ValueError: input_data is not formatted correctly.
            Either the number of vertices is not a valid integer,
            the list of vertices does not match the number provided,
            or the list of edges contains at least one line that is not
            two vertices separated by a pipe.
            KeyError: input_data contains at least one vertex name
            not provided in the vertex list.
        """
        self.vertices = self._parse_file(input_data)

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
            if len(line) != 2:
                # Use i + 1 because we removed the vertex count line
                error = (
                    "Line {} does not consist of two vertex names" +
                    " separated by a pipe").format(i + 1)
                raise ValueError(error)
            vertex, edge = line[0], line[1]
            vertices[vertex].edges.add(edge)
        return vertices
