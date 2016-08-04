def three_sat(clauses):
    """Returns True if all clauses in clauses are satisfiable.

    Args:
        clauses: a list of tuples where each tuple contains up to three string
            literals, each of which represents a variable to satisfy.
            Negated literals are marked with a preceding !.
            For example:
            [(A, B, !C), (B, C), (!B), (!A, C)]

    Returns:
        True iff there exists an assignment for all variables in clauses such
            that all clauses can be satisfied.

    Raises:
        ValueError: At least one clause in clauses contains more than three
            literals.
    """
    # Start with 0 so we can 1-index and not worry about -0
    literals = [0]
    # Literal itself ('a') to index (0)
    literals_table = {}
    # Translate each clause
    assignments = []
    # Collect all unique literals
    for clause in clauses:
        parsed_clause = []
        for literal in clause.split():
            # Don't treat negated literals as separate entities
            negated = 1 if literal[0] == "!" else 0
            literal = literal[negated:]
            if literal not in literals_table:
                literals_table[literal] = len(literals)
                literals.append(literal)
            if negated:
                parsed_clause.append(0 - literals_table[literal])
            else:
                parsed_clause.append(literals_table[literal])
        assignments.append(parsed_clause)
    print "Literals are ", literals
    print "Literals table is ", literals_table
    print "Assignments are ", assignments

array = [("A B !C"), ("B C"), ("!B"), ("!A C")]
print "Array is ", array
three_sat(array)



