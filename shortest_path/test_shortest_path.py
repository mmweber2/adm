from shortest_path import shortest_path
from shortest_path import a_star
from nose.tools import assert_equals
from nose.tools import assert_raises

def test_shortest_path_empty_edges():
    assert_equals(shortest_path([], "A"), {"A":0})

def test_shortest_path_single_edge():
    assert_equals(shortest_path([("A", "B", 2)], "A"), {"A":0, "B":2})

def test_shortest_path_no_path():
    assert_equals(shortest_path([("A", "B", 2)], "B"), {"A":float("inf"), "B":0})

def test_shortest_path_shorter_of_two_paths_from_start():
    paths = [(1, 2, 5), (1, 2, 2)]
    assert_equals(shortest_path(paths, 1), {1:0, 2:2})

def test_shortest_path_shorter_of_two_paths_split():
    paths = [(1, 2, 5), (2, 3, 4), (2, 4, 2), (4, 5, 4), (3, 5, 1)]
    assert_equals(shortest_path(paths, 1), {1:0, 2:5, 3:9, 4:7, 5:10})

def test_shortest_path_has_cycle():
    paths = [(1, 2, 1), (2, 3, 2), (3, 1, 4)]
    assert_equals(shortest_path(paths, 1), {1:0, 2:1, 3:3})

# Parameters: vertices, edges, start, goal
def test_a_star_no_edges():
    assert_equals(a_star([(1, 0.0, 0.0), (2, 1.0, 1.0)], [], 1, 2), float("inf"))

def test_a_star_start_not_in_vertices():
    assert_raises(ValueError, a_star, [(1, 0.0, 0.0), (2, 1.0, 1.0)], [], 3, 2)



