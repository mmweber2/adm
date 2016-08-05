from sat import three_sat
from nose.tools import assert_raises

def test_sat_empty():
    assert three_sat([])

def test_sat_clause_too_large():
    assert_raises(ValueError, three_sat, ["A B C D"])

def test_sat_single_clause():
    assert three_sat(["A B !C"])

def test_sat_single_literal_negated():
    assert three_sat(["!A"])

def test_sat_conflicting_single_literal():
    assert not three_sat(["B", "!B"])

def test_sat_unsatisfiable_3CNF():
    formulas = ["A B C", "A B !C", "A !B C", "A !B !C", "!A B C", "!A B !C",
            "!A !B C", "!A !B !C"]
    assert not three_sat(formulas)

def test_sat_satisfiable_3CNF():
    formulas = ["A B !C", "B C", "!B", "!A C"]
    assert three_sat(formulas)
    
