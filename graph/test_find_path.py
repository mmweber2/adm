from adjacency_list import AdjacencyList
from find_path import find_path
from find_path import connected
from nose.tools import assert_raises

def test_no_start():
    a = AdjacencyList("simple_graph.txt")
    assert_raises(KeyError, find_path, a, "Pear", "Onion")

def test_no_end():
    a = AdjacencyList("simple_graph.txt")
    assert_raises(KeyError, find_path, a, "Carrot", "Apple")

def test_same_name():
    a = AdjacencyList("simple_graph.txt")
    assert find_path(a, "Carrot", "Carrot") == ["Carrot"]

def test_adjacent():
    a = AdjacencyList("simple_graph.txt")
    assert find_path(a, "Carrot", "Onion") == ["Carrot", "Onion"]

def test_no_path():
    a = AdjacencyList("no_path.txt")
    assert find_path(a, "Janine", "Edane") == []

def test_only_opposite():
    """Test when a path exists from end to start, but not start to end."""
    a = AdjacencyList("simple_graph.txt")
    assert find_path(a, "Onion", "Carrot") == []

def test_one_away():
    a = AdjacencyList("chain.txt")
    assert find_path(a, "Jade", "Edane") == ["Jade", "Janine", "Edane"]

def test_cycle():
    a = AdjacencyList("cycle.txt")
    assert find_path(a, "A", "D") == []

def test_ignores_weights():
    a = AdjacencyList("weights.txt")
    assert find_path(a, "A", "D") == ["A", "D"]

# Cannot test an empty graph or single vertex because AdjacencyList
# does not allow us to create those.

def test_connected_singles():
    a = AdjacencyList("no_edges.txt")
    assert not connected(a)

def test_connected_two_single_direction():
    a = AdjacencyList("simple_graph.txt")
    assert not connected(a)

def test_connected_two_double_directions():
    a = AdjacencyList("doubly_connected.txt")
    assert connected(a)

def test_connected_broken_three():
    a = AdjacencyList("no_path.txt")
