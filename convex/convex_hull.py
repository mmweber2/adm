import math
from operator import attrgetter
from collections import namedtuple

def make_hull(points):
    """Returns a set of points representing a convex hull.

        Uses the Graham Scan technique:

        Starts with one point known to be on the hull, and proceeds through
        the rest of the points in order of increasing angle size from the origin
        point.

        If the angle formed by the new point and the last hull edge is < 180
        degrees, adds the point to the hull.
        If the angle is > 180 degrees, deletes vertices from the last hull edge
        as needed to maintain convexity.
        If the angle is exactly 180 degrees and does not expand the size of the
        hull, skips the point and moves on to the next point. Due to this, some
        points on the boundary of the hull may not be included in the result.

        Args:
            points: A list of Point namedtuples of the format (x, y), where
                x and y are numbers representing the coordinates of the point.

        Raises:
            TypeError: At least one Point in points contains non-number values.
            
        Returns:
            A set of Point namedtuples representing the points from the points
                argument that make up its convex hull.
    """
    if len(points) < 1:
        return set()
    origin = _get_start_point(points)
    point_angles = sorted((get_angle(origin, x), x) for x in points)
    # Wrap back around to origin after checking all other points
    point_angles.append(point_angles.pop(0))
    # Points that make up the convex hull; must include origin
    hull_points = [origin]
    # We need a hull edge to compare to, so try including the first point
    hull_points.append(point_angles[0][1])
    # Hull already contains all 2 points
    if len(point_angles) == 2:
        return set(hull_points)
    for angle, point in point_angles[1:]:
        turn = _get_turn(hull_points[-2], hull_points[-1], point)
        if turn > 0:
            hull_points.append(point)
        elif turn < 0:
            num_interior = 0
            # Keep going back until we find the last convex point
            while turn <= 0:
                num_interior += 1
                two_back = hull_points[-2 - num_interior]
                one_back = hull_points[-1 - num_interior]
                turn = _get_turn(two_back, one_back, point)
            # Remove all interior points and replace with the current point
            hull_points[-num_interior:] = [point]
        elif point is origin and len(hull_points) == 2:
            break
        else:
            # On the same line as the previous point, so replace previous point
            hull_points[-1] = point
    return set(hull_points)

def _get_start_point(points):
    """Returns the point with the lowest y coordinate."""
    # If there is more than one, tiebreak by minimum x value
    return min(points, key=lambda point: (point.y, point.x))

def _get_turn(p1, p2, p3):
    """Determines whether adding a line to p3 creates a left or right turn."""
    # Find the cross product of p1, p2, and p3.
    # If it is positive, the points make a "left turn",
    # if negative, a "right turn", and if 0, a straight line.
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

def get_angle(point1, point2):
    """Returns the counterclockwise angle between two two-dimensional Points.

    Args:
        point1, point2: Point namedtuples in the format (x, y) representing the
            location of two points in two dimensions.
            x and y must be numbers for both Points.
            point 1 is the start point (the point from which to find an angle),
            and point2 is the end point.
            The x-axis provides as the third point of the angle.

    Raises:
        TypeError: At least one of the x, y values of point1 or point2 is not
            a number.
        AttributeError: At least one of point1 and point2 is not a
            Point namedtuple.

    Returns: 
        A floating point number indicating the counterclockwise angle of point1
            and point2 from the x-axis, in degrees in the range [0, 360).

        If the angle is within one millionth of a full degree, returns the angle
           plus one millionth of a degree to compensate for floating point
           imprecision.

        For example:
            point2 is directly to the right of point1: returns 0.0
            point2 is directly above point1: returns 90.0
            point2 is directly to the left of point1: returns 180.0
            point2 is directly below point1: returns 270.0

        Returns 0.0 if point1 and point2 are identical.
    """
    EPSILON = 1.0 / 10**6
    y_dist = point2.y - point1.y
    x_dist = point2.x - point1.x
    degrees = (math.atan2(y_dist, x_dist))/math.pi * 180
    if int(degrees + EPSILON) == int(degrees) + 1:
        degrees += EPSILON
    return degrees if degrees >= 0 else degrees + 360
