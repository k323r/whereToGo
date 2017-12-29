import datetime
import sys

### >>> magic to allow imports from lib etc. ##################
###     courtesy: https://stackoverflow.com/a/1054293
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
### <<< magic

from lib import Latlon

def get_user_input():
    try:
        target_pos, target_time = sys.argv[1:]
    except ValueError:
        target_pos = Latlon(37.0, 18.0)
        target_time = datetime.datetime(2018, 12, 18, 06, 12, 38, 123456)
    return (target_pos, target_time)
