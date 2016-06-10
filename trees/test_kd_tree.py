from kd_tree import KDTree
from nose.tools import assert_raises
from nose.tools import assert_equals

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
    print "K = 2, single point"
    data = [(10, 15)]
    KDTree(data).print_tree()

def test_construct_1k():
    assert_raises(ValueError, KDTree, [(1,), (2,)])

def test_kd_construct_zero():
    assert_raises(ValueError, KDTree, ((3, 4), ), 0)

def test_kd_construct_non_iterable():
    assert_raises(TypeError, KDTree, 2, 1)

# TODO: Tests:
# Is closer on a different dimension
def test_find_closest_non_leaf_node():
    data = [(30, 40), (5, 25), (10, 12), (70, 70), (50, 30), (35, 45)]
    tree = KDTree(data)
    new_point = (50, 50)
    result = tree.find_closest(new_point)
    result_distance = KDTree._get_distance(result, new_point)
    distances = [KDTree._get_distance(point, new_point) for point in data]
    assert_equals(result, (35, 45))
    assert_equals(result_distance, min(distances))

def test_find_closest_leaf_node():
    data = [(30, 40), (5, 25), (10, 12), (70, 70), (50, 30), (35, 45)]
    tree = KDTree(data)
    new_point = (45, 35)
    result = tree.find_closest(new_point)
    result_distance = KDTree._get_distance(result, new_point)
    distances = [KDTree._get_distance(point, new_point) for point in data]
    assert_equals(result, (50, 30))
    assert_equals(result_distance, min(distances))

def test_find_closest_other_dimension():
    data = [(30, 40), (5, 25), (10, 12), (70, 70), (50, 30), (35, 45)]
    tree = KDTree(data)
    new_point = (34, 100)
    result = tree.find_closest(new_point)
    result_distance = KDTree._get_distance(result, new_point)
    distances = [KDTree._get_distance(point, new_point) for point in data]
    assert_equals(result, (70, 70))
    assert_equals(result_distance, min(distances))

def test_find_closest_different_k():
    tree = KDTree([(30, 40)])
    assert_raises(ValueError, tree.find_closest, (1, 2, 3))


    
