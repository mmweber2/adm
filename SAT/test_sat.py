from sat import three_sat
from nose.tools import assert_raises
import random

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

def test_sat_large():
    variables = xrange(1, 1001)
    satisfied_by = {}
    for variable in variables:
        if random.random() >= 0.5:
            satisfied_by[variable] = True
        else:
            satisfied_by[variable] = False
    formulas = []
    while len(formulas) < 100:
        # Choose three variables to include in clause
        pick_three = random.sample(variables, 3) 
        # Pick one of those variables to satisfy
        satisfied = random.choice(pick_three)
        # Building clause
        assignments = ""
        for v in pick_three:
            # Add satisfied version of v 
            if v == satisfied:
                if not satisfied_by[v]:
                    assignments += "!"
                assignments += str(v)
            else:
                if satisfied_by[v]:
                    assignments += "!"
                assignments += str(v)
            assignments += " "
        formulas.append(assignments)
    assert three_sat(formulas)

    
