from vertex_cover import cover
from nose.tools import assert_raises
from nose.tools import assert_equals

def test_empty():
    assert_equals(cover([]), set())

def test_edges_not_modified():
    edges = [("a", "b")]
    cover(edges)
    assert_equals(len(edges), 1)

def test_single_edge():
    edges = [("a", "b")]
    assert_equals(cover(edges), set(edges[0]))

