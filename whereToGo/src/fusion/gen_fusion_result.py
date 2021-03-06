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


def _gen_snapshot(queue, timeout=0.1, max_get_attempts=3):
    """
    Yield a list of all items currently on the queue.
    Wait timeout seconds to avoid hammering the cpu.
    Repeat unless queue was empty max_get_attempts times in a row.
    """
    n_get_attempts = 0
    while True:
        n_get_attempts += 1
        if n_get_attempts > max_get_attempts:
            break
        snapshot = []
        while not queue.empty():
            snapshot.append(queue.get())
        if snapshot:
            n_get_attempts = 0
            yield snapshot
        time.sleep(timeout)

def _update_fusion_state(snapshot, fusion_state):
    """
    TODO:
    do stuff with snapshot AND fusion_state old to compute
    fusion_state new
    """
    fusion_state = snapshot

def _compute_fusion_result(fusion_state=None):
    """
    Return fusion_result based on fusion_state.
    """
    cur_time = datetime.datetime(2017, 12, 20, 14, 29, 0, 123456)
    cur_pos = Latlon(53.0571713, 8.8167359)
    cur_head = 3.14159
    cur_alt = 5.9
    cur_velo = 10.0
    fusion_result = (cur_time, cur_pos, cur_head, cur_alt, cur_velo)
    return fusion_result

def gen_fusion_result(queue, timeout=0.1, max_get_attempts=3):
    fusion_state = None
    for snapshot in _gen_snapshot(queue, timeout, max_get_attempts):
        fusion_state = _update_fusion_state(snapshot, fusion_state)
        fusion_result = _compute_fusion_result(fusion_state)
        yield fusion_result


if __name__ == '__main__':
    print 'gen_fusion_result'
    _compute_fusion_result(None)
    
    from multiprocessing import Queue
    queue = Queue()
    queue.put('0')
    queue.put('1')
    for x in gen_fusion_result(queue, timeout=1, max_get_attempts=2):
        print x
