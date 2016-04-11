from adjacency_list import AdjacencyList
from adjacency_list import Vertex
from nose.tools import assert_raises

def test_vertex_create():
    a = Vertex("Chicago")
    assert a.name == "Chicago"
    assert a.edges == []

def test_vertex_create_empty_string():
    assert_raises(ValueError, Vertex, "")

def test_create_non_existent_file():
    assert_raises(IOError, AdjacencyList, "made_up_file.txt")

def test_create_no_vertex_count():
    assert_raises(ValueError, AdjacencyList, "no_int.txt")

def test_small_vertex_count():
    """Tests if there are more unique vertex names than expected."""
    assert_raises(ValueError, AdjacencyList, "wrong_vertex.txt")

def test_negative_vertex_count():
    assert_raises(ValueError, AdjacencyList, "invalid_vertex.txt")

def test_large_vertex_count():
    """Tests if the vertex count is allowed to be > remaining lines."""
    assert_raises(ValueError, AdjacencyList, "large_vertex.txt")

def test_list_creates_vertex():
    a = AdjacencyList("no_edges.txt")
    vert1 = a.vertices["Tory"]
    assert isinstance(vert1, Vertex)
    assert vert1.name == "Tory"
    assert vert1.edges == []

def test_no_edges():
    """Tests if a graph can be created without any edges."""
    a = AdjacencyList("no_edges.txt")
    assert len(a.vertices) == 3

def test_vertex_name_with_pipe():
    pass

def test_invalid_edge_format():
    pass
