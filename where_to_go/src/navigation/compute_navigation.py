def compute_navigation(cur_time, cur_pos, cur_head, cur_velo, target_pos, target_time):
    target_heading = 3.14159 # radian (counter?) clockwise TODO
    target_velocity = 15.0 # m/s
    estimated_toa = (2018, 12, 15, 22, 56, 52, 123456)
    return target_heading, target_velocity, estimated_toa
