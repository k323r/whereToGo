import datetime
from math import atan2, cos, sin, pi

### >>> magic to allow imports from lib etc. ##################
###     courtesy: https://stackoverflow.com/a/1054293
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
### <<< magic

from lib import Latlon, deg_to_rad


EARTH_RADIUS_METERS = 6371000


def get_distance(a, b):
    """
    Return the great arc distance in meters, using the haversine formula.

    Input: Latlons a, b (lat, lon in degrees).

    Courtesy:
        http://www.movable-type.co.uk/scripts/latlong.html
    """
    a_lat_rad = deg_to_rad(a.lat)
    a_lon_rad = deg_to_rad(a.lon)
    b_lat_rad = deg_to_rad(b.lat)
    b_lon_rad = deg_to_rad(b.lon)
    x = sin((b_lat_rad - a_lat_rad) / 2.0)**2 + cos(a_lat_rad) * cos(b_lat_rad) * sin((b_lon_rad - a_lon_rad) / 2.0)**2
    y = 2.0 * atan2(x**0.5, (1-x)**0.5)
    distance = EARTH_RADIUS_METERS * y
    return distance

def get_heading(a, b):
    """
    Return the initial heading from a to b, clockwise from north in radian:

             0
             N
    -pi/2 W     E pi/2
             S
           +-pi

    Input: Latlons a, b (lat, lon in degrees).

    Courtesy:
        http://www.igismap.com/formula-to-find-bearing-or-heading-angle-between-two-points-latitude-longitude/
        http://www.movable-type.co.uk/scripts/latlong.html
        http://mathforum.org/library/drmath/view/55417.html

    Other sources to check out:
        http://www.geomidpoint.com/destination/
        https://community.esri.com/thread/88164
        http://mathforum.org/library/drmath/view/55417.html
        https://en.wikipedia.org/wiki/Bearing_%28navigation%29
        https://en.wikipedia.org/wiki/Course_(navigation)
        https://en.wikipedia.org/wiki/Geographic_coordinate_system
    """
    a_lat_rad = deg_to_rad(a.lat)
    a_lon_rad = deg_to_rad(a.lon)
    b_lat_rad = deg_to_rad(b.lat)
    b_lon_rad = deg_to_rad(b.lon)
    y = cos(b_lat_rad) * sin(b_lon_rad - a_lon_rad)
    x = cos(a_lat_rad) * sin(b_lat_rad) - sin(a_lat_rad) * cos(b_lat_rad) * cos(b_lon_rad - a_lon_rad)
    heading = atan2(y, x)
    return heading

def compute_navigation(
                    cur_time,
                    cur_pos,
                    cur_head,
                    cur_velo,
                    target_pos,
                    target_time):
    target_heading = get_heading(cur_pos, target_pos)
    target_distance = get_distance(cur_pos, target_pos)
    target_time_left = (target_time - cur_time).total_seconds()
    target_velocity = target_distance / target_time_left
    estimated_duration = target_distance / cur_velo
    estimated_toa = cur_time + datetime.timedelta(0, estimated_duration)
    return (
        target_heading,
        target_distance,
        target_time_left,
        target_velocity,
        estimated_duration,
        estimated_toa
    )


if __name__ == '__main__':

    cur_time = datetime.datetime(2017, 12, 20, 14, 29, 0, 123456)
    cur_pos = Latlon(53.0571713, 8.8167359)
    cur_head = 3.14159
    cur_alt = 5.9
    cur_velo = 10.0

    target_pos = Latlon(52.0571713, 9.8167359)
    target_time = datetime.datetime(2017, 12, 20, 15, 39, 10, 234567)

    O = Latlon(0.0, 0.0)
    N = Latlon(80.0, 0.0)
    S = Latlon(-80.0, 0.0)
    E = Latlon(0.0, 80.0)
    W = Latlon(0.0, -80.0)

    assert get_heading(O, N) == 0.0
    assert get_heading(N, O) == pi

    assert get_heading(O, S) == pi
    assert get_heading(S, O) == 0.0

    assert get_heading(O, E) == pi / 2.0
    assert get_heading(E, O) == -pi / 2.0

    assert get_heading(O, W) == -pi / 2.0
    assert get_heading(W, O) == pi / 2.0

"""
    berlin = Latlon(52.52000659999999, 13.404953999999975)
    paris = Latlon(48.856614, 2.3522219000000177)

    print 'berlin -> paris', get_distance(berlin, paris), 'm'
    
    a = Latlon(10.0, 10.0)
    b = Latlon(20.0, 10.0)
    c = Latlon(20.0, 20.0)

    print a, b, get_heading(a, b)
    print b, a, get_heading(b, a)

    print a, c, get_heading(a, c)
    print c, a, get_heading(c, a)
"""