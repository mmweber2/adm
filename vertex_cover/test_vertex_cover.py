from vertex_cover import cover
from vertex_cover import is_valid_cover
from nose.tools import assert_raises
from nose.tools import assert_equals
from random import choice as rand

def test_empty():
    assert_equals(cover([]), set())

def test_edges_not_modified():
    edges = [("a", "b")]
    cover(edges)
    assert_equals(len(edges), 1)

def test_single_edge():
    edges = [("a", "b")]
    assert_equals(cover(edges), set(("b")))

def test_self_loop():
    edges = [("a", "a"), ("a", "b")]
    assert_equals(cover(edges), set(("a")))

def test_central():
    edges = [(0, 3), (2, 3), (5, 3), (3, 6), (3, 4), (1, 3)]
    assert_equals(cover(edges), set([3]))

def test_larger():
    edges = [("a", "b"), ("b", "c"), ("c", "d"),
            ("c", "e"), ("d", "f"), ("e", "f"),
            ("d", "g")]
    result = cover(edges)
    expected = set(["b", "c", "d", "f"])
    assert is_valid_cover(edges, result)

def test_randomized():
    vertices = range(100)
    edges = [(rand(vertices), rand(vertices)) for _ in xrange(500)]
    assert is_valid_cover(edges, cover(edges))

def test_is_valid_empty():
    assert is_valid_cover([], set())

def test_is_valid_extra():
    edges = [("a", "b")]
    assert is_valid_cover(edges, set(("a", "b", "c")))

def test_is_valid_false():
    edges = [("a", "b"), ("b", "d")]
    assert not is_valid_cover(edges, set(("a")))
