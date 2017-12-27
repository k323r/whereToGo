import datetime
from math import pi

### >>> magic to allow imports from lib etc. ##################
###     courtesy: https://stackoverflow.com/a/1054293
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
### <<< magic

from lib import Latlon

from _get_distance import _get_distance as get_distance
from _get_heading import _get_heading as get_heading


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

