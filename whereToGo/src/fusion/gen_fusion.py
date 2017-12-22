import datetime
import time

### >>> magic to allow imports from lib etc. ##################
###     courtesy: https://stackoverflow.com/a/1054293
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
### <<< magic

from lib import Latlon


def _do_fusion(raw_data):
    cur_time = datetime.datetime(2017, 12, 20, 14, 29, 0, 123456)
    cur_pos = Latlon(53.0571713, 8.8167359)
    cur_head = 3.14159
    cur_alt = 5.9
    cur_velo = 10.0
    return (cur_time, cur_pos, cur_head, cur_alt, cur_velo)

def gen_fusion(queue):
    while True:
        raw_data = []
        while not queue.empty():
            raw_data.append(queue.get())
        if raw_data:
            fused_data = _do_fusion(raw_data)
            yield fused_data
        # Wait a moment to avoid hammering the cpu.
        time.sleep(0.1)

if __name__ == '__main__':
    print 'gen_fusion'
    _do_fusion(None)
