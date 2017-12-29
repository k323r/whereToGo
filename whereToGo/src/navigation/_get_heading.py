from math import atan2, cos, sin, pi

### >>> magic to allow imports from lib etc. ##################
###     courtesy: https://stackoverflow.com/a/1054293
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
### <<< magic

from lib import deg_to_rad as rad
from lib import rad_to_deg as deg


def _get_heading_rad(a, b):
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
        https://en.wikipedia.org/wiki/Bearing_%28navigation%29
        https://en.wikipedia.org/wiki/Course_(navigation)
        https://en.wikipedia.org/wiki/Geographic_coordinate_system
    """
    y = cos(rad(b.lat)) * sin(rad(b.lon) - rad(a.lon))
    x = (cos(rad(a.lat)) * sin(rad(b.lat)) - sin(rad(a.lat)) * cos(rad(b.lat)) * cos(rad(b.lon) - rad(a.lon)))
    heading_rad = atan2(y, x)
    return heading_rad

def _get_heading_deg(a, b):
    """
    Return the initial heading from a to b, clockwise from north in DEGREES:

             0
             N
      -90 W     E 90
             S
           +-180

    Input: Latlons a, b (lat, lon in degrees).

    Courtesy:
        http://www.igismap.com/formula-to-find-bearing-or-heading-angle-between-two-points-latitude-longitude/
        http://www.movable-type.co.uk/scripts/latlong.html
        http://mathforum.org/library/drmath/view/55417.html

    Other sources to check out:
        http://www.geomidpoint.com/destination/
        https://community.esri.com/thread/88164
        https://en.wikipedia.org/wiki/Bearing_%28navigation%29
        https://en.wikipedia.org/wiki/Course_(navigation)
        https://en.wikipedia.org/wiki/Geographic_coordinate_system
    """
    return deg(_get_heading_rad(a, b))


if __name__ == '__main__':

    O = Latlon(0.0, 0.0)
    N = Latlon(80.0, 0.0)
    S = Latlon(-80.0, 0.0)
    E = Latlon(0.0, 80.0)
    W = Latlon(0.0, -80.0)

    assert _get_heading(O, N) == 0.0
    assert _get_heading(N, O) == pi

    assert _get_heading(O, S) == pi
    assert _get_heading(S, O) == 0.0

    assert _get_heading(O, E) == pi / 2.0
    assert _get_heading(E, O) == -pi / 2.0

    assert _get_heading(O, W) == -pi / 2.0
    assert _get_heading(W, O) == pi / 2.0

"""
    a = Latlon(10.0, 10.0)
    b = Latlon(20.0, 10.0)
    c = Latlon(20.0, 20.0)

    print a, b, _get_heading(a, b)
    print b, a, _get_heading(b, a)

    print a, c, _get_heading(a, c)
    print c, a, _get_heading(c, a)
"""
