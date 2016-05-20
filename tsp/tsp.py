from random import uniform, shuffle, random, randint
from math import sqrt
from itertools import permutations

def create_dataset(n, min_val=-10.0, max_val=10.0):
    """Creates a list of n tuples.
            
    Each tuple contains two randomly generated float values in the
    range between min_val and max_val. Some float values may be the
    same, but all tuples will be unique.

    Args:
        n: The number of tuples (points) to create. Must be an integer
        greater than 0.

        min_val: The minimum value of the points. Defaults to -10.0.

        max_val: The maximum value of the points. Defaults to 10.0. 
        Must be > min_val.

    Returns:
        A list of n unique 2-float tuples in the range specified.

    Raises:
        ValueError: min_val is equal to max_val, or n is < 1.

        TypeError: min_val or max_val are not numbers, or n is not an integer.
    """
    # If n isn't type checked, it can cause an infinite loop while len < n
    # in the while loop below.
    if type(n) != int:
        raise TypeError("n must be an integer")
    if n < 1:
        raise ValueError("n must be greater than zero")
    # If min_val and max_val are equal, we can only create one point and will
    # get an infinite loop if n > 1.
    # uniform works for (max, min) as well, so don't check for max > min
    if min_val == max_val:
        raise ValueError("min_val must not be equal to max_val")
    points = set()
    # Since we could find duplicates, it may take more than n tries
    while len(points) < n:
        point = (uniform(min_val, max_val), uniform(min_val, max_val))
        points.add(point)
    return list(points)

def find_distance(point1, point2):
    """Finds straight line distance between points (x1, y1) and (x2, y2)."""
    x_dist = point1[0] - point2[0]
    y_dist = point1[1] - point2[1]
    return sqrt(x_dist**2 + y_dist**2)

def find_path_distance(path):
    """Calculates the distance of a path.
    
    Calculates the sum of the straight-line distances from the first point
    to the second, the second to the third, and so on until the last point
    on the path is reached. Does not include the distance from the last point
    back to the first; if this is needed, the first point can be added again.

    Args:
        path: A list or tuple of items, where each item is a 2-tuple or 2-item
        list consisting of two floats.

    Raises:
        TypeError: path is not a list or tuple, or is not in the correct
        format.
    """
    distance = 0
    # Index into the points on the path
    for i in xrange(1, len(path)):
        distance += find_distance(path[i-1], path[i])
    return distance

def tsp_brute(dataset):
    """Finds the shortest distance through all nodes in dataset by brute force.

    Explores all permutations of the points in dataset and searches for the
    ordering of points (path) with the smallest sum distance. 
    This function is only suitable for small datasets consisting of less than 15
    items.

    Args:
        dataset: A list or tuple of 2-item tuples or lists containing only floats.

    Returns:
        A tuple containing two items: A float indicating the length of the
        shortest path, and a list of points indicating that path.
    """
    min_distance = float("inf")
    min_path = None
    for path in permutations(dataset):
        distance = find_path_distance(path)
        if distance < min_distance:
            min_distance = distance
            min_path = path[:]
    return (min_distance, min_path)

def tsp_montecarlo(dataset, n=100):
    """Finds a distance through all nodes in dataset through random search.

    Explores n random permutations of the points in dataset and returns the
    ordering of points (path) with the smallest sum distance found.

    Args:
        dataset: A list or tuple of 2-item tuples or lists containing only floats.

        n: The integer number of permutations to explore. Defaults to 100.

    Returns:
        A tuple containing two items: A float indicating the length of the
        shortest path discovered, and a list of points indicating that path.

    Raises:
        TypeError: dataset is not in the correct format, or n is not an integer.
    """
    # May as well take the distance of the first/default path
    min_distance = find_path_distance(dataset)
    min_path = dataset
    # path will be shuffled, so we need a copy
    path = dataset[:]
    for _ in xrange(n):
        shuffle(path)
        distance = find_path_distance(path)
        if distance < min_distance:
            min_distance = distance
            min_path = path[:]
    return (min_distance, min_path)

def tsp_hill_climb(dataset, n=10):
    """Finds a distance of a path through all nodes in dataset.

    Swaps each pair of points in dataset, then compares the overall path
    distance to what it was before. If it is shorter, the swap is kept;
    otherwise, the swap is discarded. In either case, the swaps continue
    until the end of dataset is reached.
    This pattern repeats until all swaps are made with no improvements.
    Repeats n times and returns the best results found.

    Args:
        dataset: A list or tuple of 2-item tuples or lists containing only floats.

        n: The integer number of swap iterations to explore. Defaults to 10.

    Returns:
        A tuple containing two items: A float indicating the length of the
        shortest path discovered, and a list of points indicating that path.

    Raises:
        TypeError: dataset is not in the correct format, or n is not an integer.
    """
    min_distance = find_path_distance(dataset)
    min_path = dataset
    start_path = dataset[:]
    for _ in xrange(n):
        shuffle(start_path)
        distance, path = _hill_climb(start_path)
        if distance < min_distance:
            min_distance = distance
            min_path = path[:]
    return (min_distance, min_path)

def _hill_climb(path):
    """Helper method for tsp_hill_climb."""
    while True:
        improved = False
        current_distance = find_path_distance(path)
        for i in xrange(len(path)):
            for j in xrange(i+1, len(path)):
                path[i], path[j] = path[j], path[i]
                new_distance = find_path_distance(path)
                # Look for improvement, not just < min_distance
                if new_distance < current_distance:
                    improved = True
                    current_distance = new_distance
                else:
                    # Revert path changes that didn't improve distance
                    path[i], path[j] = path[j], path[i]
        if not improved:
            break
    return (current_distance, path)

def tsp_simulated_annealing(dataset, n=1000):
    """Finds a distance of a path through all nodes in dataset.

    Chooses a random point in dataset and swaps it with the following point.
    If this results in a shorter total distance, maintain this change. 
    Otherwise, maintains the change with a small probability, which decreases
    as the number of swaps increases.

    Repeats until n swaps are performed without encountering improvements,
    and returns the best results found.

    Args:
        dataset: A list or tuple of 2-item tuples or lists containing only floats.

        n: The limit of swaps without improvement to allow before stopping.
        Defaults to 1000.

    Returns:
        A tuple containing two items: A float indicating the length of the
        shortest path discovered, and a list of points indicating that path.

    Raises:
        TypeError: dataset is not in the correct format, or n is not an integer.
    """
    t = .1
    min_distance = find_path_distance(dataset)
    min_path = dataset
    path = dataset[:]
    # current_distance could get bigger than min_distance, so track both
    current_distance = min_distance
    last_change = 0
    cycle = 0
    while last_change < n:
        # Decrease temperature every 100 cycles
        if cycle % 100 == 0:
            t *= .9
        cycle += 1
        # -2 because the last item doesn't have a next element to swap with
        swap = randint(0, len(dataset) - 2)
        path[swap], path[swap+1] = path[swap+1], path[swap]
        new_distance = find_path_distance(path)
        if _keep_swap(current_distance, new_distance, t):
            current_distance = new_distance
            last_change = 0
            if current_distance < min_distance:
                min_path = path[:]
                min_distance = current_distance
        else:
            path[swap], path[swap+1] = path[swap+1], path[swap]
            last_change += 1
    return (min_distance, min_path)

def _keep_swap(previous_dist, new_dist, t):
    """Helper function for tsp_simulated_annealing."""
    if previous_dist > new_dist:
        return True
    chance = (previous_dist / new_dist) * t
    return random() < chance
