from math import atan2, cos, sin, pi

### >>> magic to allow imports from lib etc. ##################
###     courtesy: https://stackoverflow.com/a/1054293
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
### <<< magic

from lib import deg_to_rad as rad


EARTH_RADIUS_METERS = 6371000


def _get_distance(a, b):
    """
    Return the great arc distance in meters, using the haversine formula.

    Input: Latlons a, b (lat, lon in degrees).

    Courtesy:
        http://www.movable-type.co.uk/scripts/latlong.html
    """
    x = sin((rad(b.lat) - rad(a.lat)) / 2.0)**2 + cos(rad(a.lat)) * cos(rad(b.lat)) * sin((rad(b.lon) - rad(a.lon)) / 2.0)**2
    y = 2.0 * atan2(x**0.5, (1-x)**0.5)
    distance = EARTH_RADIUS_METERS * y
    return distance


if __name__ == '__main__':

    berlin = Latlon(52.52000659999999, 13.404953999999975)
    paris = Latlon(48.856614, 2.3522219000000177)
    print 'berlin -> paris', _get_distance(berlin, paris), 'm'
