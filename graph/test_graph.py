from graph import Vertex
from graph import Edge
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
