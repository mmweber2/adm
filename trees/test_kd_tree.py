from kd_tree import KDTree
from nose.tools import assert_raises

def test_build_tree_2k():
    print "K = 2:"
    data = [(30, 40), (5, 25), (10, 12), (70, 70), (50, 30), (35, 45)]
    KDTree.build_tree(data).print_tree()

def test_build_tree_inconsistent_k():
    data = [(30, 40), (5, 25, 3)]
    assert_raises(IndexError, KDTree.build_tree, data)
    data = [(30, 40, 1), (5, 25)]
    assert_raises(IndexError, KDTree.build_tree, data)

def test_build_tree_3k():
    print "K = 3:"
    data = [
        (30, 40, 10), (5, 25, 2), (10, 12, 30), (70, 70, 10), (50, 30, 5), 
        (35, 45, 15)]
    KDTree.build_tree(data).print_tree()

def test_build_tree_single_point():
    print "K = 2, single point"
    data = [(10, 15)]
    KDTree.build_tree(data).print_tree()

def test_build_tree_1k():
    assert_raises(ValueError, KDTree.build_tree, [(1,), (2,)])

def test_kd_construct_valid():
    tree = KDTree((10, 15), 1)
    assert tree.value == (10, 15)
    assert tree.dimension == 1
    tree = KDTree((10, 15), 2)
    assert tree.dimension == 2
    


    
