from kd_tree import KDTree

def test_build_tree_valid():
    data = [(30, 40), (5, 25), (10, 12), (70, 70), (50, 30), (35, 45)]
    tree = KDTree.build_tree(data)
    tree.print_tree()


    
