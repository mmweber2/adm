from set_cover import set_cover
from set_cover import set_cover_exact
from set_cover import _generate_subsets
from set_cover import _is_valid_cover
from nose.tools import assert_equals
from nose.tools import assert_raises

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

def test_greedy_best_of_four_sets():
    sets = [set([1, 3]), set([2, 3]), set([1, 3, 4]), set([1, 4])]
    result = set_cover(sets)
    expected = sets[1:3]
    assert_equals(len(result), 2)
    for subset in result:
        assert subset in expected

def test_greedy_large():
    sets = [set(range(i, 10)) for i in xrange(10)]
    result = set_cover(sets)
    assert _is_valid_cover(sets, result)

def test_generate_subsets_empty():
    assert_equals(_generate_subsets([]), [])

def test_generate_subsets_single():
    sets = [set([1, 2])]
    result = _generate_subsets(sets)
    assert_equals([tuple(sets)], result)

def test_generate_subsets_two():
    sets = [set([1, 2]), set([2, 3])]
    result = _generate_subsets(sets)
    assert_equals([tuple(sets)], result)

def test_generate_subsets_size_one():
    sets = [set([1, 2]), set([2, 3]), set([3, 4])]
    expected = [(set([1, 2]),), (set([2, 3]),), (set([3, 4]),)]
    result = _generate_subsets(sets, 1)
    assert_equals(len(result), len(expected))
    for subset in result:
        assert subset in expected
    for subset in expected:
        assert subset in result

def test_generate_subsets_size_two():
    sets = [set([1, 2]), set([2, 3]), set([3, 4])]
    expected = [(set([1, 2]), set([2, 3])), (set([1, 2]), set([3, 4])),
            (set([2, 3]), set([3, 4]))]
    result = _generate_subsets(sets, 2)
    assert_equals(len(result), len(expected))
    for subset in result:
        assert subset in expected
    for subset in expected:
        assert subset in result

def test_generate_subsets_size_0():
    sets = [set([1, 2]), set([2, 3])]
    result = _generate_subsets(sets, 0)
    assert_equals(result, [])

def test_generate_subsets_negative_size():
    sets = [set([1, 2]), set([2, 3])]
    assert_raises(ValueError, _generate_subsets, sets, -1)

def test_is_valid_cover_empty_list():
    assert _is_valid_cover([], [])

def test_is_valid_cover_empty_set():
    # No elements to cover
    assert _is_valid_cover([set()], [])

def test_is_valid_cover_single():
    sets = [set([1, 2])]
    assert _is_valid_cover(sets, sets)
    assert not _is_valid_cover(sets, [])

def test_is_valid_cover_two():
    sets = [set([1, 2]), set([2, 3])]
    assert _is_valid_cover(sets, sets)
    assert not _is_valid_cover(sets, [sets[0]])

def test_is_valid_cover_not_all_sets():
    sets = [set([1, 3]), set([2, 3]), set([1, 3, 4]), set([1, 4])]
    assert _is_valid_cover(sets, set_cover(sets))
    assert _is_valid_cover(sets, sets)

def test_exact_empty():
    assert_equals(set_cover_exact([]), ())

def test_exact_single_set():
    sets = [set([0, 2])]
    assert_equals(set_cover_exact(sets), tuple(sets))

def test_exact_best_of_two_sets():
    sets = [set([0, 3]), set([3])]
    assert_equals(set_cover_exact(sets), (sets[0], ))

def test_exact_requires_two_sets():
    sets = [set([1, 3]), set([2, 3])]
    result = set_cover_exact(sets)
    assert_equals(len(result), 2)
    for subset in result:
        assert subset in sets

def test_exact_best_of_four_sets():
    sets = [set([1, 3]), set([2, 3]), set([1, 3, 4]), set([1, 4])]
    result = set_cover_exact(sets)
    expected = sets[1:3]
    assert_equals(len(result), 2)
    for subset in result:
        assert subset in expected

def test_exact_large():
    sets = [set(range(i, 10)) for i in xrange(10)]
    result = set_cover_exact(sets)
    assert _is_valid_cover(sets, result)
