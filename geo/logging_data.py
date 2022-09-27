# Denis Muravev
from geopy.distance import geodesic
from .mkad import MKAD
from .settings import NAME_LOG_FILE

def find_min_distance(point, polygon):
    """Finding the minimum distance to a polygon.

    Arguments:
    point -- point with latitude and longitude coordinates.
    polygon -- list of points with latitude and longitude coordinates.

    """
    if abs(point[0]) > 90 or abs(point[1]) > 180:
        return None
    min = geodesic(point, polygon[0]).kilometers
    for i in range(1, len(polygon)):
        if abs(polygon[i][0]) > 90 or abs(polygon[i][1]) > 180:
            return None
        tmp_min = geodesic(point, polygon[i]).kilometers
        if min > tmp_min:
            min = tmp_min
    return min
    
def not_inside(point, polygon):
    """Сhecking whether a point belongs to a polygon

    Arguments:
    point -- point with latitude and longitude coordinates.
    polygon -- list of points with latitude and longitude coordinates.

    Results:
    True -- point belongs to the polygon.
    False -- point not belongs to the polygon.

    """
    if abs(point[0]) > 90 or abs(point[1]) > 180:
        return None
    x = point[0]
    y = point[1]
    xp = [polygon[i][0] for i in range(len(polygon))]
    yp = [polygon[i][1] for i in range(len(polygon))]
    for i in range(len(polygon)):
        if abs(xp[i]) > 90 or abs(yp[i]) > 180:
            return None
    c = 0
    for i in range(len(xp)):
        p = (y - yp[i]) / (yp[i-1] - yp[i]) if (yp[i-1] - yp[i]) != 0 else (x - xp[i]) / (xp[i-1] - xp[i])
        if p >= 0 and p <= 1:
            return False
        if (((yp[i]<=y and y<yp[i-1]) or (yp[i-1]<=y and y<yp[i])) and 
            (x > (xp[i-1] - xp[i]) * p + xp[i])): c = 1 - c  
    return True if c == 0 else False

def logging(coordinates, address, file = NAME_LOG_FILE):
    """Logging a point if it does not belong to a polygon (MKAD).

    Arguments:
    coordinates -- point with latitude and longitude coordinates.
    addres -- user request.

    Result:
    Adding a distance and address-request entry to the end of the "log.log" file

    """
    if abs(coordinates[0]) > 90 or abs(coordinates[1]) > 180:
        return None
    if not_inside(coordinates, MKAD):
        distance_to_mkad = find_min_distance(coordinates, MKAD)
        log_data = "{:.3f} km to {}\n".format(distance_to_mkad, address)
        with open(file, "a+") as f:
            f.write(log_data)
            return log_data
    return None
