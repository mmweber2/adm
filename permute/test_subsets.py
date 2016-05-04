from subsets import subsets
from nose.tools import assert_equals
from nose.tools import assert_raises

def test_subsets_empty():
    assert_equals([], subsets([]))

def test_subsets_non_iterable():
    assert_raises(TypeError, subsets, 25)

def test_subsets_single_item():
    result = subsets([1])
    assert [1] in result
    assert [] in result

def test_subsets_two_items():
    result = subsets([1, 2])
    for subset in [[], [1], [2], [1, 2]]:
        assert subset in result

def test_subsets_two_repeating_items():
    result = subsets([2, 2])
    for subset in [[], [2], [2, 2]]:
        assert subset in result
    # Duplicate item should appear by itself twice
    assert result.count([2]) == 2

# Test a non-list input
def test_subsets_strings():
    result = subsets("ab")
    for subset in [[], ["a"], ["b"], ["a", "b"]]:
        assert subset in result

def test_subsets_three_items():
    result = subsets([1, 2, 3])
    for subset in [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]:
        assert subset in result
