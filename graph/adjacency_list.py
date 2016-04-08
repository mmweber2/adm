import sys

class Vertex(object):
    """Represents a vertex."""

    def __init__(self, name):
        """Create a new Vertex with the given name.

        By default, a new Vertex has no values associated with it.
        """
        self.name = name
        self.edges = None

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
                a space

            For example:
            5
            Tokyo
            Chicago
            San Francisco
            Madison
            Beijing
            Tokyo Chicago
            Tokyo Beijing
            Tokyo San Francisco
            Chicago Tokyo
            Chicago Madison
            San Francisco Tokyo
            Madison Chicago
            Beijing Tokyo

        Raises:
            IOError: input_data does not exist.
        """
        input_file = []
        vertices = []
        with open(input_data, 'r') as filename:
            input_file = filename.readlines()
        # Strip all trailing newlines
        input_file = [line.strip() for line in input_file]
        vertex_count = int(input_file.pop(0))
        # Gather vertex names
        for line in input_file[:vertex_count]:
            vertices.append(line)
        # Gather edges
        for line in input_file[vertex_count:]:
            pass

