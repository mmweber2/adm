import random
def three_sat(clauses):
    """Returns True if all clauses are satisfiable.

    Args:
        clauses: a list of strings where each string contains up to three
            literals separated by spaces, and each literal represents a variable
            to satisfy.
            Negated literals are marked with a preceding !.
            For example:
            ["A B !C", "B C", "!B", "!A C"]

    Returns:
        True iff there exists an assignment for all variables in clauses such
            that all clauses can be satisfied, or if clauses is empty.

    Raises:
        ValueError: At least one clause in clauses contains more than three
            literals.
    """
    # Based on Python returning True for all([]), treat empty list as True
    if not clauses:
        return True
    # Start with 0 so we can 1-index and not worry about -0
    literals = [0]
    # Literal itself ('a') to index (1)
    literals_table = {}
    # Translate each clause
    parsed_clauses = []
    # Collect all unique literals
    for clause in clauses:
        parsed_clause = []
        clause = clause.split()
        if len(clause) > 3:
            raise ValueError("clause {} contains >3 literals".format(clause))
        for literal in clause:
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
        parsed_clauses.append(parsed_clause)
    # Track whether each literal is True or False. Set all to True by default.
    assignments = {literal:True for literal in literals_table.values()}
    unsatisfied = check_if_satisfied(parsed_clauses, assignments)
    current_best = len(unsatisfied)
    # TODO: At what point should we break and give up looking?
    for _ in xrange(10000):
        if current_best == 0:
            return True
        # Permute a random assignment and see if it improves
        swap = random.choice(xrange(1, len(literals)))
        assignments[swap] ^= True
        new_score = len(check_if_satisfied(parsed_clauses, assignments))
        if new_score <= current_best:
            current_best = new_score
            unsatisfied = check_if_satisfied(parsed_clauses, assignments)
        else:
            # Undo the swap since it did not improve
            assignments[swap] ^= True
    # Couldn't find a perfect match, so return the best we found
    return False

def check_if_satisfied(clauses, assignments):
    """Helper function for three_sat to check all clauses."""
    unsatisfied = []
    for i in xrange(len(clauses)):
        if not is_satisfied(clauses[i], assignments):
            unsatisfied.append(i)
    return unsatisfied

def is_satisfied(clause, assignments):
    """Helper function for three_sat to check a single clause."""
    outcome = False
    for literal in clause:
        negated = False
        if literal < 0:
            negated = True
        outcome |= (assignments[abs(literal)] ^ negated)
    return outcome
