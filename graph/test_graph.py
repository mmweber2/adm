from graph import Vertex
from nose.tools import assert_raises

def test_new_vertex():
    a = Vertex("A")
    assert a.name == "A"
    assert a.edges == []

def test_duplicate_vertex_name():
    a = Vertex("A")
    assert_raises(ValueError, Vertex, "A")

def test_vertex_invalid_edges():
    assert_raises(TypeError, Vertex, "A", "B")
