def prod_velo_from_acc(queue):
    datetime_sys = (2017, 12, 15, 22, 56, 52, 123456)
    velocity_from_acc = 5.0 # m/s
    while True:
        queue.put(('velo_from_acc', datetime_sys, velocity_from_acc))
