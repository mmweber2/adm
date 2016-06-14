from kd_tree import KDTree
from random import uniform
from nose.tools import assert_raises
from nose.tools import assert_equals

# Decorator for counting function calls
def counted(func):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return func(*args, **kwargs)
    wrapped.calls = 0
    return wrapped

def test_construct_2k():
    print "K = 2:"
    data = [(30, 40), (5, 25), (10, 12), (70, 70), (50, 30), (35, 45)]
    KDTree(data).print_tree()

def test_construct_inconsistent_k():
    data = [(30, 40), (5, 25, 3)]
    assert_raises(IndexError, KDTree, data)
    data = [(30, 40, 1), (5, 25)]
    assert_raises(IndexError, KDTree, data)

def test_construct_3k():
    print "K = 3:"
    data = [
        (30, 40, 10), (5, 25, 2), (10, 12, 30), (70, 70, 10), (50, 30, 5), 
        (35, 45, 15)]
    KDTree(data).print_tree()

def test_construct_single_point():
    data = [(10, 15)]
    tree = KDTree(data)
    assert_equals(tree.value, data[0])
    assert_equals(tree.left, None)
    assert_equals(tree.right, None)
    assert_equals(tree.dimension, 1)

def test_construct_1k():
    assert_raises(ValueError, KDTree, [(1,), (2,)])

def test_kd_construct_zero():
    assert_raises(ValueError, KDTree, ((3, 4), ), 0)

def test_kd_construct_non_iterable():
    assert_raises(TypeError, KDTree, 2, 1)


def test_find_closest_three_points():
    tree = KDTree([(10, 12), (70, 70), (35, 45)])
    new_point = (50, 50)
    KDTree.find_closest = counted(KDTree.find_closest)
    result = tree.find_closest(new_point)
    assert_equals(result, (35, 45))
    assert_equals(tree.find_closest.calls, 3)

def test_find_closest_same_dimension():
    tree = KDTree([(30, 40), (30, 4), (30, 60)])
    new_point = (30, 55)
    KDTree.find_closest = counted(KDTree.find_closest)
    result = tree.find_closest(new_point)
    assert_equals(result, (30, 60))
    assert_equals(tree.find_closest.calls, 3)

def test_find_closest_distant_point():
    tree = KDTree([(10, 12), (70, 70), (35, 45)])
    new_point = (0, 10000)
    KDTree.find_closest = counted(KDTree.find_closest)
    result = tree.find_closest(new_point)
    assert_equals(result, (70, 70))
    assert_equals(tree.find_closest.calls, 3)

def test_find_closest_very_close_point():
    tree = KDTree([(10, 12), (70, 70), (35, 45)])
    new_point = (8, 10)
    KDTree.find_closest = counted(KDTree.find_closest)
    result = tree.find_closest(new_point)
    assert_equals(result, (10, 12))
    assert_equals(tree.find_closest.calls, 2)

def test_find_closest_identical_point():
    tree = KDTree([(10, 12), (70, 70), (35, 45)])
    new_point = (10, 12)
    KDTree.find_closest = counted(KDTree.find_closest)
    result = tree.find_closest(new_point)
    result_distance = KDTree._get_distance(result, new_point)
    assert_equals(result, (10, 12))
    assert_equals(result_distance, 0)
    assert_equals(tree.find_closest.calls, 2)

def test_find_closest_negative_numbers():
    tree = KDTree([(10, 12), (70, -70), (-35, 45)])
    new_point = (-40, 60)
    KDTree.find_closest = counted(KDTree.find_closest)
    result = tree.find_closest(new_point)
    assert_equals(result, (-35, 45))
    assert_equals(tree.find_closest.calls, 2)

def test_find_closest_randomized():
    RANGES = (-1000, 1000)
    DATA_SIZE = 6000
    data = [(uniform(*RANGES), uniform(*RANGES)) for _ in xrange(DATA_SIZE)]
    tree = KDTree(data)
    new_point = (uniform(*RANGES), uniform(*RANGES))
    KDTree.find_closest = counted(KDTree.find_closest)
    result = tree.find_closest(new_point)
    result_distance = KDTree._get_distance(result, new_point)
    distances = [KDTree._get_distance(point, new_point) for point in data]
    assert_equals(result_distance, min(distances))
    # Number of calls will be inconsistent, but should not check all points
    assert tree.find_closest.calls < len(data)

def test_find_closest_3k():
    data = [
        (30, 40, 10), (5, 25, 2), (10, 12, 30), (70, 70, 10), (50, 30, 5), 
        (35, 45, 15)]
    tree = KDTree(data)
    new_point = (34, 100, 50)
    KDTree.find_closest = counted(KDTree.find_closest)
    result = tree.find_closest(new_point)
    assert_equals(result, (70, 70, 10))
    assert_equals(tree.find_closest.calls, 5)

def test_find_closest_different_k():
    tree = KDTree([(30, 40)])
    assert_raises(ValueError, tree.find_closest, (1, 2, 3))
