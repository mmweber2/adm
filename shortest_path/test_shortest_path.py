from shortest_path import shortest_path
from shortest_path import a_star
from shortest_path import _get_dist
from nose.tools import assert_equals
from nose.tools import assert_raises

def test_shortest_path_empty_edges():
    assert_equals(shortest_path([], "A"), {"A":0})

def test_shortest_path_single_edge():
    assert_equals(shortest_path([("A", "B", 2)], "A"), {"A":0, "B":2})

def test_shortest_path_no_path():
    expected =  {"A":float("inf"), "B":0}
    assert_equals(shortest_path([("A", "B", 2)], "B"), expected)

def test_shortest_path_shorter_of_two_paths_from_start():
    paths = [(1, 2, 5), (1, 2, 2)]
    assert_equals(shortest_path(paths, 1), {1:0, 2:2})

def test_shortest_path_shorter_of_two_paths_split():
    paths = [(1, 2, 5), (2, 3, 4), (2, 4, 2), (4, 5, 4), (3, 5, 1)]
    assert_equals(shortest_path(paths, 1), {1:0, 2:5, 3:9, 4:7, 5:10})

def test_shortest_path_has_cycle():
    paths = [(1, 2, 1), (2, 3, 2), (3, 1, 4)]
    assert_equals(shortest_path(paths, 1), {1:0, 2:1, 3:3})

def test_shortest_path_self_loop():
    paths = [(1, 2, 2), (2, 3, 2), (1, 1, 1)]
    assert_equals(shortest_path(paths, 1), {1:0, 2:2, 3:4})

# Parameters: vertices, edges, start, goal
def test_a_star_no_vertex_list_no_edges():
    assert_raises(ValueError, a_star, [], [], 3, 2)

def test_a_star_no_vertex_list():
    assert_raises(ValueError, a_star, [], [(2, 1)], 1, 2)

def test_a_star_no_edges():
    vertices = [(1, 0.0, 0.0), (2, 1.0, 1.0)]
    assert_equals(a_star(vertices, [], 1, 2), float("inf"))

# Also covers code testing for inclusion of the goal vertex
def test_a_star_start_not_in_vertices():
    assert_raises(ValueError, a_star, [(1, 0.0, 0.0), (2, 1.0, 1.0)], [], 3, 2)

def test_a_star_no_path():
    vertices = [(1, 0.0, 0.0), (2, 1.0, 1.0)]
    assert_equals(a_star(vertices, [(2, 1)], 1, 2), float("inf"))

def test_a_star_single_edge():
    vertices = [(1, 0.0, 0.0), (2, 1.0, 1.0)]
    assert_equals(a_star(vertices, [(1, 2)], 1, 2), 2**0.5)

def test_a_star_shorter_of_two_paths_from_start():
    vertices = [(1, 10.0, 10.0), (2, 90.0, 90.0), (3, 5.0, 3.0), (4, 0.0, 1.0)]
    paths = [(1, 2), (1, 3), (2, 4), (3, 4)]
    # Resulting path should be 1 - 3 - 4
    expected = (25 + 49)**0.5 + (25 + 4)**0.5
    assert_equals(a_star(vertices, paths, 1, 4), expected)

def test_a_star_cycle():
    vertices = [(1, 10.0, 10.0), (2, 90.0, 90.0), (3, 5.0, 3.0), (4, 0.0, 1.0)]
    paths = [(1, 2), (1, 3), (3, 1), (2, 4), (3, 4)]
    expected = (25 + 49)**0.5 + (25 + 4)**0.5
    assert_equals(a_star(vertices, paths, 1, 4), expected)

def test_a_star_self_loop():
    vertices = [(1, 10.0, 10.0), (2, 90.0, 90.0), (3, 5.0, 3.0), (4, 0.0, 1.0)]
    paths = [(1, 2), (1, 3), (1, 1), (3, 4)]
    expected = (25 + 49)**0.5 + (25 + 4)**0.5
    assert_equals(a_star(vertices, paths, 1, 4), expected)

def test_a_star_large():
    vertices = [(0, -5, 0.5), (1, 8, -4), (2, 1, 0.5), (3, -1.5, -2), 
            (4, 5.5, 4), (5, 4, -20.6), (6, 1.2, -2), (7, -6, -1),
            (8, 10, 0.5), (9, 5.6, -52.3)]
    paths = [(0, 7), (0, 3), (7, 3), (7, 9), (3, 6), (3, 2), (3, 5), (5, 1),
            (9, 1), (2, 4), (4, 8), (4, 1)]
    # Path should be 0, 3, 2, 4, 1
    zero_three_dist = (3.5**2 + 2.5**2)**0.5
    assert_equals(_get_dist(vertices[0][1:], vertices[3][1:]), zero_three_dist)
    three_two_dist = (2.5**2 + 2.5**2)**0.5
    assert_equals(_get_dist(vertices[3][1:], vertices[2][1:]), three_two_dist)
    two_four_dist = (4.5**2 + 3.5**2)**0.5
    assert_equals(_get_dist(vertices[2][1:], vertices[4][1:]), two_four_dist)
    four_one_dist = (2.5**2 + 64)**0.5
    assert_equals(_get_dist(vertices[4][1:], vertices[1][1:]), four_one_dist)
    expected = zero_three_dist + three_two_dist + two_four_dist + four_one_dist
    assert_equals(a_star(vertices, paths, 0, 1), expected)




