import math

def make_hull(points):
    """
    """

def get_angle(point1, point2):
    """Returns the angle between two two-dimensional points.

    Args:
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

print get_angle((0, 0), (0, -1))

