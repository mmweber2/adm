from maxflow import max_flow
from nose.tools import assert_equals

def test_no_edges():
    assert_equals(max_flow([], 1, 2), 0.0)
    
def test_source_not_in_edges():
    assert_equals(max_flow([(1, 2, 3)], 3, 2), 0.0)

def test_sink_not_in_edges():
    assert_equals(max_flow([(1, 2, 3)], 1, 4), 0.0)

def test_source_sink_reversed():
    assert_equals(max_flow([(0, 1, 5)], 1, 0), 0.0)

def test_single_edge():
    assert_equals(max_flow([(0, 1, 5)], 0, 1), 5.0)

def test_float_capacities():
    assert_equals(max_flow([(0, 1, 2.5), (1, 2, 0.99)], 0, 2), 0.99)

def test_negative_capacity():
    assert_equals(max_flow([(0, 1, -3), (1, 2, 3)], 0, 2), 0)

def test_zero_capacity():
    assert_equals(max_flow([(0, 1, 3), (1, 2, 0)], 0, 2), 0)

def test_two_edges_bottleneck():
    assert_equals(max_flow([(0, 1, 10), (1, 2, 1)], 0, 2), 1.0)

def test_three_edges_bottleneck():
    edges = [("a", "b", 10), ("b", "d", 1), ("a", "c", 10), ("c", "b", 3)]
    assert_equals(max_flow(edges, "a", "d"), 1.0)

def test_four_edges_bottleneck():
    edges = [("a", "b", 10), ("b", "d", 1), ("a", "c", 10), ("c", "d", 3)]
    assert_equals(max_flow(edges, "a", "d"), 4.0)

def test_large():
    edges = [("s", "a", 16), ("a", "b", 12), ("b", "t", 20), ("s", "c", 13), 
                ("a", "c", 10), ("c", "a", 4), ("b", "c", 9), ("c", "d", 14),
                ("d", "b", 7), ("d", "t", 4)]
    assert_equals(max_flow(edges, "s", "t"), 23.0)
