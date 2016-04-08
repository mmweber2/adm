from adjacency_list import AdjacencyList
from nose.tools import assert_raises

#TODO: Test Vertex?

def test_create_non_existent_file():
    assert_raises(IOError, AdjacencyList, "made_up_file.txt")

def test_create_no_vertex_count():
    assert_raises(ValueError, AdjacencyList, "no_int.txt")

def test_small_vertex_count():
    """Tests if there are more unique vertex names than expected.
    """
    assert_raises(ValueError, AdjacencyList, "wrong_vertex.txt")

def test_invalid_vertex_count():
    pass

def test_large_vertex_count():
    """Tests if the vertex count > remaining lines."""
    pass

def test_invalid_edge_format():
    pass

def test_no_edges():
    pass
