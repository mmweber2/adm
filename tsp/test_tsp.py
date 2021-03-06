from tsp import create_dataset, find_path_distance
from tsp import tsp_brute, tsp_montecarlo, tsp_hill_climb, tsp_simulated_annealing
from nose.tools import assert_equals
from nose.tools import assert_raises

def test_create_dataset_default():
    data = create_dataset(5)
    uniques = set()
    for x, y in data:
        assert -10 <= x <= 10
        assert -10 <= y <= 10
        assert (x, y) not in uniques
        uniques.add((x, y))
    assert_equals(len(uniques), len(data))

def test_create_dataset_change_defaults():
    data = create_dataset(5, 11, 20)
    for x, y in data:
        assert 11 <= x <= 20
        assert 11 <= y <= 20

def test_create_dataset_invalid_n_int():
    assert_raises(ValueError, create_dataset, 0)

def test_create_dataset_same_min_max():
    assert_raises(ValueError, create_dataset, 4, 2.0, 2.0)

def test_create_dataset_bigger_min_than_max():
    assert create_dataset(4, 3.0, 2.0) != None

def test_create_dataset_min_or_max_not_numbers():
    assert_raises(TypeError, create_dataset, 4, "-5", 5)

def test_find_path_distance():
    path = ((-1, 1), (1, 1), (1, -1), (-1, -1))
    # Each step is distance of 2, so should be 6
    assert_equals(find_path_distance(path), 6)

# Datasets are random every time, so I just make sure it's a possibly valid distance
def test_tsp_brute():
    set1 = create_dataset(3)
    result = tsp_brute(set1)
    assert_equals(len(result), 2)
    assert_equals(len(result[1]), 3)
    assert_equals(find_path_distance(result[1]), result[0])
    assert result[0] > 0
    set2 = create_dataset(6)
    result = tsp_brute(set2)
    assert_equals(len(result[1]), 6)
    assert_equals(find_path_distance(result[1]), result[0])
    assert result[0] > 0
    set3 = create_dataset(8)
    result = tsp_brute(set3)
    assert_equals(len(result[1]), 8)
    assert result[0] > 0
    assert_equals(find_path_distance(result[1]), result[0])

def test_tsp_brute_vs_montecarlo():
    set1 = create_dataset(6)
    ma_result = tsp_montecarlo(set1)
    assert_equals(find_path_distance(ma_result[1]), ma_result[0])
    assert tsp_brute(set1)[0] <= ma_result[0]

def test_tsp_hill_climb():
    set1 = create_dataset(6)
    hc_result = tsp_hill_climb(set1)
    assert_equals(find_path_distance(hc_result[1]), hc_result[0])
    assert tsp_brute(set1)[0] <= hc_result[0]

def test_tsp_sa():
    set1 = create_dataset(20)
    sa_result = tsp_simulated_annealing(set1)
    assert_equals(find_path_distance(sa_result[1]), sa_result[0])
    print "MC result: ", tsp_montecarlo(set1)[0]
    print "HC result (1 iteration): ", tsp_hill_climb(set1, 1)[0]
    print "HC result (10 iterations): ", tsp_hill_climb(set1, 10)[0]
    #print "HC result (100 iterations): ", tsp_hill_climb(set1, 100)[0]
    print "SA result 1: ", sa_result[0]
    print "SA result 2: ", tsp_simulated_annealing(set1)[0]
