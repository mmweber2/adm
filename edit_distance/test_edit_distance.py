from edit_distance import edit_distance
from nose.tools import assert_equals

def test_edit_same_string():
    assert_equals(edit_distance("one", "one"), 0)

def test_edit_one_empty_string():
    assert_equals(edit_distance("", "one"), 3)

def test_edit_two_empty_strings():
    assert_equals(edit_distance("", ""), 0)

def test_edit_one_swap():
    assert_equals(edit_distance("cat", "car"), 1)

def test_edit_one_del():
    assert_equals(edit_distance("chat", "chaut"), 1)

def test_edit_one_add():
    assert_equals(edit_distance("char", "chair"), 1)
    
def test_edit_longer_strings():
    # pineapple, peneapple, penelpple, penelople, penelope
    assert_equals(edit_distance("pineapple", "penelope"), 4)
