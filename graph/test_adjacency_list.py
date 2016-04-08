from adjacency_list import AdjacencyList
from nose.tools import assert_raises

#TODO: Test Vertex?

def test_create_non_existent_file():
    assert_raises(IOError, AdjacencyList, "made_up_file.txt")

def test_create_no_vertex_count():
    assert_raises(ValueError, AdjacencyList, "no_int.txt")

def test_incorrect_vertex_count():
    """Check the vertex count against the vertices.

    We can only tell if a vertex is too small, not too large,
    because a combination of two vertex names could be a valid
    third vertex name. For example, Mary, Jane, and Mary Jane could
    all be valid vertex names.
    """
    assert_raises(ValueError, AdjacencyList, "wrong_vertex.txt")

def test_invalid_vertex_count():
    pass
