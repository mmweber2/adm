from topol import top_sort
from adjacency_list import AdjacencyList
from nose.tools import assert_raises

def test_sort_two_nodes():
    a = AdjacencyList("simple_graph.txt")
    assert top_sort(a) == ["Carrot", "Onion"]

def test_with_cycle():
    a = AdjacencyList("cycle.txt")
    assert_raises(ValueError, top_sort, a)

def test_multiple_orderings():
    pass

def test_three_steps():
    pass

# There is no test for undirected graphs because AdjacencyList cannot
# create them.
