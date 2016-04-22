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
    a = Edge("X")
    assert a.name == "X"
    assert a.weight == None

def test_add_edge_normal():
    a = Vertex("Test")
    b = Edge("Test 2")
    a.add_edge(b)
    assert len(a.edges) == 1
    assert b in a.edges

def test_add_edge_duplicate():
    a = Vertex("AB")
    b = Edge("ABC")
    c = Edge("ABC")
    a.add_edge(b)
    a.add_edge(c)
    assert len(a.edges) == 2
    assert b in a.edges
    assert c in a.edges

def test_add_edge_invalid():
    a = Vertex("AC")
    assert_raises(TypeError, a.add_edge, "B")
