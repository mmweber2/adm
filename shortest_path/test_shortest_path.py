from shortest_path import shortest_path
from nose.tools import assert_equals

def test_empty_edges():
    assert_equals(shortest_path([], "A"), {"A":0})

def test_single_edge():
    assert_equals(shortest_path([("A", "B", 2)], "A"), {"A":0, "B":2})

def test_no_path():
    assert_equals(shortest_path([("A", "B", 2)], "B"), {"A":float("inf"), "B":0})

def test_shorter_of_two_paths_from_start():
    paths = [(1, 2, 5), (1, 2, 2)]
    assert_equals(shortest_path(paths, 1), {1:0, 2:2})

def test_shorter_of_two_paths_split():
    paths = [(1, 2, 5), (2, 3, 4), (2, 4, 2), (4, 5, 4), (3, 5, 1)]
    assert_equals(shortest_path(paths, 1), {1:0, 2:5, 3:9, 4:7, 5:10})

def test_has_cycle():
    paths = [(1, 2, 1), (2, 3, 2), (3, 1, 4)]
    assert_equals(shortest_path(paths, 1), {1:0, 2:1, 3:3})

