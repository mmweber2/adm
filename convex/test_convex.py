from convex_hull import make_hull
from collections import namedtuple
from nose.tools import assert_equals
from nose.tools import assert_raises

Point = namedtuple('Point', 'x y')

def test_make_hull_empty():
    assert_equals(make_hull([]), set())

def test_make_hull_three():
    points = [Point(1, 1), Point(0, 0), Point(-1, 1)]
    assert_equals(make_hull(points), set(points))

def test_make_hull_invalid_points():
    points = [Point("a", "b"), Point("1", "2"), Point("b", "a")]
    assert_raises(TypeError, make_hull, points)

def test_make_hull_two_invalid_points():
    points = [Point("a", "b"),  Point("b", "a")]
    assert_equals(make_hull(points), set(points))
    
def test_make_hull_square():
    points = [Point(-2, 2), Point(2, 2), Point(-2, -2), Point(2, -2)]
    assert_equals(make_hull(points), set(points))

def test_make_hull_triangle_with_interior():
    points = [Point(2, -2), Point(-2, -2), Point(-1, -1), Point(-1, 3)]
    expected = set((points[0], points[1], points[3]))
    assert_equals(make_hull(points), expected)

def test_make_hull_large():
    result = make_hull([Point(i/10, i % 10) for i in xrange(100)])
    assert_equals(result, set([Point(0,0), Point(9,0), Point(9,9), Point(0,9)]))
