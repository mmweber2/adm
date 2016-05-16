from random import randint
from random import shuffle
from math import sqrt
from itertools import permutations

def create_dataset(n):
    """Creates a list of n 2-item tuples."""
    points = []
    min_point = -10
    max_point = 10
    for _ in xrange(n):
        points.append((randint(min_point, max_point), randint(min_point, max_point)))
    return points

# TODO: Consider using an Edge to store this data once it's calculated
def find_distance(point1, point2):
    """Finds straight line distance between points (x1, y1) and (x2, y2)."""
    # These distances could be negative, but they'll be squared anyway
    x_dist = point1[0] - point2[0]
    y_dist = point1[1] - point2[1]
    return sqrt(x_dist**2 + y_dist**2)

# TODO: Error checking
def find_path_distance(path):
    """Calculates the distance from the first point on a path to the last."""
    distance = 0
    # Index into the points on the path
    for i in xrange(1, len(path)):
        distance += find_distance(path[i-1], path[i])
    return distance

def tsp_brute(dataset):
    """Finds the shortest distance through all nodes in dataset by brute force."""
    min_distance = float("inf")
    for path in permutations(dataset):
        min_distance = min(find_path_distance(path), min_distance)
    return min_distance

def tsp_montecarlo(dataset):
    """Finds a distance through all nodes in dataset through random search."""
    # May as well take the distance of the first/default path
    min_distance = find_path_distance(dataset)
    NUM_TRIES = 100
    # Shuffle will alter the list, so make a copy for shuffling
    path = [x for x in dataset]
    for _ in xrange(NUM_TRIES):
        # Doesn't matter whether we are shuffling path or dataset
        shuffle(path)
        min_distance = min(find_path_distance(path), min_distance)
    return min_distance



