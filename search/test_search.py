from search import create_dataset
from search import tsp_brute
from search import tsp_montecarlo
from search import find_path_distance
from nose.tools import assert_equals
from nose.tools import assert_raises

def test_find_path_distance():
    path = ((-1, 1), (1, 1), (1, -1), (-1, -1))
    # Each step is distance of 2, so should be 6
    assert_equals(find_path_distance(path), 6)

# Datasets are random every time, so I just make sure it's a possibly valid distance
def test_tsp_brute():
    set1 = create_dataset(3)
    assert tsp_brute(set1) > 0
    set2 = create_dataset(6)
    assert tsp_brute(set2) > 0
    set3 = create_dataset(8)
    assert tsp_brute(set3) > 0

def test_tsp_brute_vs_montecarlo():
    set1 = create_dataset(2)
    assert tsp_brute(set1) <= tsp_montecarlo(set1)
    print "Brute force result: {}. MC result: {}".format(tsp_brute(set1), tsp_montecarlo(set1))
