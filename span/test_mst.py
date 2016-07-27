from mst import get_min_edges_kruskal
from mst import get_min_edges_prim
from collections import namedtuple
from nose.tools import assert_equals
from nose.tools import assert_raises

Edge = namedtuple('Edge', ('vertex1', 'vertex2', 'value'))

# TODO: Add tests for SpanningTree itself

def test_get_min_edges_kruskal_empty():
    assert_equals(get_min_edges_kruskal([]), [])

def test_get_min_edges_kruskal_single():
    a = Edge('a', 'b', 3)
    assert_equals(get_min_edges_kruskal([a]), [a])

def test_get_min_edges_kruskal_disconnected_components():
    a = Edge('a', 'b', 2)
    b = Edge('c', 'd', 2)
    assert_raises(ValueError, get_min_edges_kruskal, [a, b])

def test_get_min_edges_kruskal_best_of_two_comes_first():
    a = Edge('a', 'b', 2)
    b = Edge('a', 'b', 3)
    assert_equals(get_min_edges_kruskal([a, b]), [a])

def test_get_min_edges_kruskal_best_of_two_comes_second():
    a = Edge('a', 'b', 3)
    b = Edge('a', 'b', 2)
    assert_equals(get_min_edges_kruskal([a, b]), [b])

def test_get_min_edges_kruskal_two_edges_opposite_order():
    a = Edge('a', 'b', 3)
    b = Edge('b', 'a', 2)
    assert_equals(get_min_edges_kruskal([a, b]), [b])

def test_get_min_edges_kruskal_three_point_cycle():
    a = Edge('a', 'b', 3)
    b = Edge('b', 'c', 2)
    c = Edge('c', 'a', 4)
    assert_equals(get_min_edges_kruskal([a, b, c]), [b, a])

def test_get_min_edges_kruskal_large():
    ad = Edge('a', 'd', 5)
    ab = Edge('a', 'b', 7)
    bc = Edge('b', 'c', 8)
    be = Edge('b', 'e', 7)
    bd = Edge('b', 'd', 9)
    ce = Edge('c', 'e', 5)
    de = Edge('d', 'e', 15)
    df = Edge('d', 'f', 6)
    ef = Edge('e', 'f', 8)
    eg = Edge('e', 'g', 9)
    fg = Edge('f', 'g', 11)
    points = [ad, ab, bc, be, bd, ce, de, df, ef, eg, fg]
    result = get_min_edges_kruskal(points)
    assert_equals(result, [ad, ce, df, ab, be, eg])

def test_get_min_edges_prim_empty():
    assert_equals(get_min_edges_prim([]), [])

def test_get_min_edges_prim_single():
    a = Edge('a', 'b', 3)
    assert_equals(get_min_edges_prim([a]), [a])

def test_get_min_edges_prim_disconnected_components():
    a = Edge('a', 'b', 2)
    b = Edge('c', 'd', 2)
    assert_raises(ValueError, get_min_edges_prim, [a, b])

def test_get_min_edges_prim_best_of_two_comes_first():
    a = Edge('a', 'b', 2)
    b = Edge('a', 'b', 3)
    assert_equals(get_min_edges_prim([a, b]), [a])

def test_get_min_edges_prim_best_of_two_comes_second():
    a = Edge('a', 'b', 3)
    b = Edge('a', 'b', 2)
    assert_equals(get_min_edges_prim([a, b]), [b])

def test_get_min_edges_prim_two_edges_opposite_order():
    a = Edge('a', 'b', 3)
    b = Edge('b', 'a', 2)
    assert_equals(get_min_edges_prim([a, b]), [b])

def test_get_min_edges_prim_three_point_cycle():
    a = Edge('a', 'b', 3)
    b = Edge('b', 'c', 2)
    c = Edge('c', 'a', 4)
    assert_equals(get_min_edges_prim([a, b, c]), [a, b])

def test_get_min_edges_prim_large():
    ad = Edge('a', 'd', 5)
    ab = Edge('a', 'b', 7)
    bc = Edge('b', 'c', 8)
    be = Edge('b', 'e', 7)
    bd = Edge('b', 'd', 9)
    ce = Edge('c', 'e', 5)
    de = Edge('d', 'e', 15)
    df = Edge('d', 'f', 6)
    ef = Edge('e', 'f', 8)
    eg = Edge('e', 'g', 9)
    fg = Edge('f', 'g', 11)
    points = [ad, ab, bc, be, bd, ce, de, df, ef, eg, fg]
    result = sorted(get_min_edges_prim(points))
    expected = sorted([ad, ce, df, ab, be, eg])
    assert_equals(result, expected)




