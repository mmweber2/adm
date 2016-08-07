import random
def three_sat(clauses):
    """Returns True if all clauses are satisfiable.

    Args:
        clauses: a list of strings where each string contains up to three
            literals separated by spaces, and each literal represents a variable
            to satisfy. May not contain '!' as a literal.
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
    if not clauses:
        return True
    # Avoid -0
    literals = [0]
    # Literal itself ('a') to index (1)
    literals_table = {}
    parsed_clauses = parse_clauses(clauses, literals, literals_table)
    # Track whether each literal is True or False
    assignments = {literal:True for literal in literals_table.values()}
    unsatisfied_clauses = find_unsatisfied(parsed_clauses, assignments)
    current_best = len(unsatisfied_clauses)
    for _ in xrange(10000):
        if current_best == 0:
            return True
        # Permute one of the variables in one of the unsatisfied clauses
        clause = parsed_clauses[random.choice(unsatisfied_clauses)]
        swap = random.choice([abs(x) for x in clause])
        assignments[swap] = not assignments[swap]
        # Find clauses that are not met by the new assignment
        now_unsatisfied = find_unsatisfied(parsed_clauses, assignments)
        new_score = len(now_unsatisfied)
        if new_score <= current_best:
            current_best = new_score
            unsatisfied_clauses = now_unsatisfied
        else:
            # Undo the swap since it did not improve
            assignments[swap] = not assignments[swap]
    return False

def find_unsatisfied(clauses, assignments):
    """Helper function for three_sat to check all clauses."""
    clause_indices = []
    for i in xrange(len(clauses)):
        if not is_satisfied(clauses[i], assignments):
            clause_indices.append(i)
    return clause_indices

def is_satisfied(clause, assignments):
    """Helper function for three_sat to check a single clause."""
    for literal in clause:
        positive = literal > 0
        if positive and assignments[abs(literal)]:
            return True
        if not positive and not assignments[abs(literal)]:
            return True

def parse_clauses(clauses, literals, literals_table):
    parsed_clauses = []
    """Helper function for three_sat to parse input clauses."""
    for clause in clauses:
        parsed_clause = []
        clause = clause.split()
        if len(clause) > 3:
            raise ValueError("clause {} contains > 3 literals".format(clause))
        for literal in clause:
            # Don't treat negated literals as separate entities
            negated = literal[0] == "!"
            literal = literal[negated:]
            if literal not in literals_table:
                literals_table[literal] = len(literals)
                literals.append(literal)
            if negated:
                parsed_clause.append(0 - literals_table[literal])
            else:
                parsed_clause.append(literals_table[literal])
        parsed_clauses.append(parsed_clause)
    return parsed_clauses
