import math
from collections import namedtuple

def make_hull(points):
    """Returns a list of points representing a convex hull.

        Uses Graham Scan:
        Start with one point, p, known to be on the hull, and sort the rest of
        the points in order of increasing angle size from p.
        Proceed through the sorted vertices.
        If the angle formed by the new point and the last hull edge is < 180
        degrees, add the point to the hull.
        If the angle is > 180 degrees, delete vertices from the last hull edge
        as needed to maintain convexity.
    """
    # Find start point with lowest y coordinate (lowest x as tiebreaker)
    p = _get_start_point(points)
    # Sort non-p points in increasing order of angle from p
    point_angles = sorted((get_angle(p, x), x) for x in points if x != p)
    # Points that make up the convex hull; must include p
    hull_points = [p]
    # We need a hull edge to compare to, so try including the first point
    hull_points.append(point_angles[0])
    for point in point_angles:
        turn = _get_turn(hull_points[-2], hull_points[-1], point)


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
    return (p2.x - p1.x)(p3.y - p1.y) - (p2.y - p1.y)(p3.x - p1.x)



# TODO: Use namedtuples
def get_angle(point1, point2):
    """Returns the angle between two two-dimensional points.

    Args:
     # TODO: Namedtuple
        point1, point2: Tuples of the format (x, y) representing the location of
            two points in two dimensions.
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
    y_dist = point2[1] - point1[1]
    x_dist = point2[0] - point1[0]
    degrees = (math.atan2(y_dist, x_dist))/math.pi * 180
    return degrees if degrees > 0 else degrees + 360
