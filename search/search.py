from random import randint

def create_dataset(n):
    """Creates a list of n 2-item tuples."""
    points = []
    min_point = -10
    max_point = 10
    for _ in xrange(n):
        points.append((randint(min_point, max_point), randint(min_point, max_point)))
    return points

def tsp_brute(n):
    data = create_dataset(n)
