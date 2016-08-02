from topol import topol
from nose.tools import assert_equals
from nose.tools import assert_raises

def test_topol_empty():
    assert_equals(topol([]), [])

def test_topol_two_points_linked():
    graph = [(1, 2)]
    assert_equals(topol(graph), [1, 2])

def test_topol_single_self_loop():
    graph = [(1, 1)]
    assert_raises(ValueError, topol, graph)

def test_topol_two_point_cycle():
    graph = [(1, 2), (2, 1)]
    assert_raises(ValueError, topol, graph)

def test_topol_three_points_linked():
    graph = [(1, 2), (1, 3)]
    # Some graphs will have multiple valid sorts
    assert topol(graph) in [[1, 3, 2], [1, 2, 3]]

def test_topol_three_point_cycle():
    graph = [("a", "b"), ("b", "c"), ("c", "a")]
    assert_raises(ValueError, topol, graph)

def test_topol_six_points():
    graph = [(5, 0), (5, 2), (3, 1), (2, 3), (4, 0), (4, 1)]
    valid = [[5, 4, 2, 3, 1, 0], [4, 5, 2, 3, 1, 0]]
    assert topol(graph) in valid


