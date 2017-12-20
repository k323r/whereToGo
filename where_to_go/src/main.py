#!/usr/bin/python

from fusion import gen_fusion
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
from ui import get_user_input, display, sonar_ping

import multiprocessing
import sys


def main():

    target_pos, target_time = get_user_input()

    queue = multiprocessing.Queue()

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

    fused_datas = gen_fusion(queue)
    for fused_data in fused_datas:
        cur_time, cur_pos, cur_head, cur_alt, cur_velo = fused_data

        navigation = compute_navigation(
            cur_time,
            cur_pos,
            cur_head,
            cur_velo,
            target_pos,
            target_time
        )
        target_heading, target_velocity, estimated_toa = navigation

        if is_valid(target_heading, target_velocity, estimated_toa):
            display(target_heading, target_velocity, estimated_toa)
            sonar_ping(target_heading, target_velocity, estimated_toa)


if __name__ == '__main__':
    main()
