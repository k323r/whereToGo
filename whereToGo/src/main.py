#!/usr/bin/python

import multiprocessing
import sys

from fusion import gen_fusion_result
from navigation import compute_navigation, is_valid
from sensors import (
    prod_acc,
    prod_gps,
    prod_gyro,
    prod_head_from_acc,
    prod_mag,
    prod_mic,
    prod_velo_from_acc,
)
from ui import get_user_input, display, sonar_ping, stdout


OUTPUT_DEVICES = [stdout]#, display, sonar_ping]


def _make_producer_process(target, queue, kwargs):
    p = multiprocessing.Process(
        target=target,
        args=(queue,),
        kwargs=kwargs
    )
    return p

def _launch_producers(queue, targets, kwargss=None):
    kwargss = kwargss or [dict() for _ in targets]
    producers = [
        _make_producer_process(target, queue, kwargs)
        for target, kwargs in zip(targets, kwargss)
    ]
    for p in producers:
        p.start()

def _launch_consumer(queue, user_input, timeout=0.1, max_get_attemps=3):
    for count_fusion, fusion_result in enumerate(gen_fusion_result(queue, timeout, max_get_attemps)):
        navigation = compute_navigation(*(fusion_result + user_input))
        if is_valid(*navigation):
            print count_fusion, '',
            for device in OUTPUT_DEVICES:
                device(*navigation)
#            display(*navigation)
#            sonar_ping(*navigation)
#            stdout(*navigation)

def main():
    user_input = get_user_input()
    queue = multiprocessing.Queue()

    targets = [prod_acc, prod_gps]
    kwargss = [{"period": 0.2}, {"period": 0.2}]
    _launch_producers(queue, targets, kwargss)

    timeout = 0.1
    max_get_attemps = 3
    _launch_consumer(queue, user_input, timeout, max_get_attemps)



if __name__ == '__main__':
    main()


    """
    target_pos, target_time = user_input
    cur_time, cur_pos, cur_head, cur_alt, cur_velo = fusion_result
    navigation = compute_navigation(
        cur_time,
        cur_pos,
        cur_head,
        cur_alt,
        cur_velo,
        target_pos,
        target_time
    )
    (
        target_heading,
        target_distance,
        target_time_left,
        target_velocity,
        estimated_duration,
        estimated_toa
    ) = navigation
    """
    """
    acc_producer_p = multiprocessing.Process(
        target=prod_acc,
        args=(queue,),
        kwargs={"period": 0.2}
    )
    gps_producer_p = multiprocessing.Process(
        target=prod_gps,
        args=(queue,),
        kwargs={"period": 0.2}
    )
    acc_producer_p.start()
    gps_producer_p.start()
    """
