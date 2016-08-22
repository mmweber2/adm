import math
from collections import namedtuple

def make_hull(points):
    """Returns a list of points representing a convex hull.

        Uses the Graham Scan technique:

        Starts with one point, p, known to be on the hull, and proceeds through
        the rest of the points in order of increasing angle size from p.

        If the angle formed by the new point and the last hull edge is < 180
        degrees, adds the point to the hull.
        If the angle is > 180 degrees, deletes vertices from the last hull edge
        as needed to maintain convexity.
        If the angle is exactly 180 degrees, skips the point and moves on to the
        next point. Due to this, some points on the boundary of the hull may not
        be included in the result.

        Args:
            points: A list of Point namedtuples of the format (x, y), where
                x and y are numbers representing the coordinates of the point.

        Returns:
            A list of Point namedtuples representing the points from the points
                argument that make up its convex hull.
            If points contains fewer than 3 Points, returns points unchanged,
                as a smaller convex hull cannot be formed.
    """
    if len(points) < 3:
        return points
    # Find start point with lowest y coordinate (lowest x as tiebreaker)
    p = _get_start_point(points)
    # Sort non-p points in increasing order of angle from p
    point_angles = sorted((get_angle(p, x), x) for x in points if x != p)
    # Points that make up the convex hull; must include p
    hull_points = [p]
    # We need a hull edge to compare to, so try including the first point
    hull_points.append(point_angles[0][1])
    for angle, point in point_angles:
        turn = _get_turn(hull_points[-2], hull_points[-1], point)
        if turn > 0:
            hull_points.append(point)
        elif turn < 0:
            # Number of interior points if we add this point
            num_interior = 0
            while turn < 0:
                num_interior += 1
                # Get lookup of previous two points in the hull
                two_back = hull_points[-2 - num_interior]
                one_back = hull_points[-1 - num_interior]
                turn = _get_turn(two_back, one_back, point)
            # Remove all interior points and replace with the current point
            hull_points[-num_interior:] = [point]
        else:
            # On the same line as the previous point, so replace previous point
            hull_points[-1] = point
    return hull_points

def _get_start_point(points):
    """Returns the point with the lowest y coordinate."""
    min_values = []
    min_y = points[0].y
    for point in points:
        if point.y < min_y:
            # Reset min values since a new minimum was found
            min_values = [point]
            min_y = point.y
        elif point.y == min_y:
            min_values.append(point)
    # If there is more than one, tiebreak by minimum x value
    return min(min_values)

def _get_turn(p1, p2, p3):
    """Determines whether adding a line to p3 creates a left or right turn."""
    # Find the cross product of p1, p2, and p3.
    # If it is positive, the points make a "left turn",
    # if negative, a "right turn", and if 0, a straight line.
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

def get_angle(point1, point2):
    """Returns the angle between two two-dimensional points.

    Args:
        point1, point2: Point namedtuples in the format (x, y) representing the
            location of two points in two dimensions.
            point 1 is the start point (the point from which to find an angle),
            and point2 is the end point.

    Returns: 
        A floating point number indicating the angle of point2 from point1
            in degrees.

        For example:
            point2 is directly to the right of point1: returns 0.0
            point2 is directly above point1: returns 90.0
            point2 is directly to the left of point1: returns 180.0
            point2 is directly below point1: returns 270.0

        Returns 0.0 if point1 and point2 are identical.
    """
    # TODO: Error checking
    y_dist = point2.y - point1.y
    x_dist = point2.x - point1.x
    degrees = (math.atan2(y_dist, x_dist))/math.pi * 180
    return degrees if degrees > 0 else degrees + 360
