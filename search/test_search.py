from search import create_dataset
from search import tsp_brute

# Datasets are random every time, so I just make sure it's a possibly valid distance
def test_tsp_brute():
    set1 = create_dataset(3)
    assert tsp_brute(set1) > 0
    set2 = create_dataset(6)
    assert tsp_brute(set2) > 0
    set3 = create_dataset(8)
    assert tsp_brute(set3) > 0
