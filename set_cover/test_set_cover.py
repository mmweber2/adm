from set_cover import set_cover
from nose.tools import assert_equals

def test_greedy_empty():
    assert_equals(set_cover([]), [])

def test_greedy_single_set():
    sets = [set([1, 3])]
    assert_equals(set_cover(sets), sets)

def test_greedy_best_of_two_sets():
    sets = [set([1, 3]), set([3])]
    assert_equals(set_cover(sets), [sets[0]])

def test_greedy_requires_two_sets():
    sets = [set([1, 3]), set([2, 3])]
    result = set_cover(sets)
    # Cannot put sets into sets to compare equality
    assert_equals(len(result), 2)
    for subset in result:
        assert subset in sets

def test_greedy_requires_best_of_four_sets():
    sets = [set([1, 3]), set([2, 3]), set([1, 3, 4]), set([1, 4])]
    result = set_cover(sets)
    expected = sets[1:3]
    assert_equals(len(result), 2)
    for subset in result:
        assert subset in expected

