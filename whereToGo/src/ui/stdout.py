import sys

### >>> magic to allow imports from lib etc. ##################
###     courtesy: https://stackoverflow.com/a/1054293
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
### <<< magic

from lib import m_to_km as km
from lib import s_to_h as h
from lib import ms_to_kmh as kmh
from lib import datetime_to_timestamp as timestamp


def stdout(
        target_heading,
        target_distance,
        target_time_left,
        target_velocity,
        current_velocity,
        estimated_duration,
        estimated_toa):
    sys.stdout.write(
'''\
(%s, %s, %s, %s, %s, %s, %s)
'''        % (
            'head: %.3f dg' % target_heading,
            'dist: %.3f km' % km(target_distance),
            't_left: %.2f h' % h(target_time_left),
            'v_must: %.2f kmh' % kmh(target_velocity),
            'v_cur: %.2f kmh' % kmh(current_velocity),
            'dura_oa: %.2f h' % h(estimated_duration),
            't_oa: %s' % timestamp(estimated_toa)
        )
    )
