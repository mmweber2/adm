from adjacency_list import AdjacencyList
from adjacency_list import Vertex
from nose.tools import assert_raises

def test_vertex_create():
    a = Vertex("Chicago")
    assert a.name == "Chicago"
    assert a.edges == dict()

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
    assert vert1.edges == dict()

def test_no_edges():
    """Tests if a graph can be created without any edges."""
    a = AdjacencyList("no_edges.txt")
    assert len(a.vertices) == 3

def test_vertex_name_with_pipe():
    assert_raises(ValueError, AdjacencyList, "with_pipe.txt")

def test_invalid_edge_format():
    assert_raises(ValueError, AdjacencyList, "edge_no_pipe.txt")

def test_valid_edge_directed():
    a = AdjacencyList("valid_edge.txt")
    chicago = a.vertices["Chicago"]
    assert "Tokyo" in chicago.edges
    assert "Boston" in chicago.edges
    boston = a.vertices["Boston"]
    assert "Tokyo" in boston.edges
    assert "Chicago" not in boston.edges

def test_valid_edge_all_weighted():
    a = AdjacencyList("all_weighted_edges.txt")
    assert a.vertices["Sam"].edges["Sally"].weight == "100"
    assert a.vertices["Sally"].edges["Sam"].weight == "2"
    assert a.vertices["Mike"].edges["Sam"].weight == "15"

def test_valid_edge_start_weights():
    a = AdjacencyList("start_edges.txt")
    assert a.vertices["Sam"].edges["Sally"].weight == "10"
    assert a.vertices["Sally"].edges["Sam"].weight == "1"

def test_valid_edge_end_weights():
    a = AdjacencyList("end_edges.txt")
    assert a.vertices["Sam"].edges["Sally"].weight == "1"
    assert a.vertices["Sally"].edges["Sam"].weight == "2"

def test_extra_pipes():
    pass

def test_duplicate_edges():
    pass
