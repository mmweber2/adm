from adjacency_list import AdjacencyList
from find_path import find_path
from nose.tools import assert_raises

def test_find_path_no_start():
    a = AdjacencyList("simple_graph.txt")
    assert_raises(KeyError, find_path, a, "Pear", "Onion")

def test_find_path_no_end():
    a = AdjacencyList("simple_graph.txt")
    assert_raises(KeyError, find_path, a, "Carrot", "Apple")

def test_find_path_same_name():
    a = AdjacencyList("simple_graph.txt")
    assert find_path(a, "Carrot", "Carrot") == ["Carrot"]

def test_find_path_adjacent():
    a = AdjacencyList("simple_graph.txt")
    assert find_path(a, "Carrot", "Onion") == ["Carrot", "Onion"]

def test_find_path_no_path():
    pass

def test_find_path_only_opposite():
    """Test when a path exists from end to start, but not start to end."""
    a = AdjacencyList("simple_graph.txt")
    assert find_path(a, "Onion", "Carrot") == []

def test_find_path_two_away():
    pass
