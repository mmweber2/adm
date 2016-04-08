import sys

class Vertex(object):
    """Represents a vertex."""

    def __init__(self, name):
        """Create a new Vertex with the given name.

        By default, a new Vertex has no values associated with it.

        Args:
            name: The name of the Vertex, as it would appear on
            a graph. Used to identify this Vertex.
        """
        self.name = name
        self.edges = []

class AdjacencyList(object):
    """Represents a graph as an adjacency list."""

    # TODO: Support weights.
    # TODO: Determine exceptions
    # TODO: Is the graph static once created?
    def __init__(self, input_data):
        """Creates a new adjacency list.

        Creates an adjacency list for the data provided. Data may be
        directed or undirected, but cannot be weighted.

        Args:
            input_data: The filename of the data to read in to create
            the graph. Data should be in the following format:

            Number of vertices as an integer
            Names of vertices (may contain spaces)
            Links between vertices, shown as both names separated by
                a pipe

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
        """
        input_file = []
        vertices = dict()
        with open(input_data, 'r') as filename:
            input_file = filename.readlines()
        # Strip all trailing newlines
        input_file = [line.strip() for line in input_file]
        vertex_count = int(input_file.pop(0))
        # Gather vertex names and assign indices
        for i in xrange(len(input_file[:vertex_count])):
            vertices[i] = []
        # Gather edges; look at remaining indices
        for i in xrange(vertex_count, len(input_file)):
            line = input_file[i].split('|')
            if len(line) != 2:
                error = (
                    "Line {} does not consist of two vertex names" +
                    " separated by a pipe").format(i)
                raise ValueError(error)
            # TODO: Break into vertex names

