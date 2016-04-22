from graph import Vertex
from graph import Edge
from graph import find_path
from nose.tools import assert_raises

def test_new_vertex():
    a = Vertex("A")
    assert a.name == "A"
    assert a.edges == []

def test_duplicate_vertex_name():
    a = Vertex("B")
    assert_raises(ValueError, Vertex, "B")

def test_vertex_invalid_edges():
    assert_raises(TypeError, Vertex, "C", "B")

def test_edge_default():
    b = Vertex("X")
    a = Edge(b)
    assert a.vertex.name == "X"
    assert a.weight == 0

def test_add_edge_normal():
    a = Vertex("Test")
    b = Vertex("Test 2")
    c = Edge(b)
    a.add_edge(c)
    assert len(a.edges) == 1
    assert c in a.edges

def test_add_edge_duplicate():
    a = Vertex("AB")
    b = Vertex("ABC")
    c = Edge(b)
    d = Edge(b)
    a.add_edge(d)
    a.add_edge(c)
    assert len(a.edges) == 2
    assert d in a.edges
    assert c in a.edges

def test_add_edge_invalid():
    a = Vertex("AC")
    assert_raises(TypeError, a.add_edge, "B")

def test_find_path_no_path():
    a = Vertex("Start")
    b = Vertex("End")
    assert find_path(a, b) == []

def test_find_path_start_is_end():
    a = Vertex("A3")
    assert find_path(a, a) == [a]

def test_find_path_direct_connection():
    a = Vertex("A1")
    b = Vertex("A2")
    a.add_edge(Edge(b))
    ans = find_path(a, b)
    assert find_path(a, b) == [a, b]


