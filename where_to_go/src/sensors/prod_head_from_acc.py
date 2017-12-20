def prod_head_from_acc(queue, init_heading):
    datetime_sys = (2017, 12, 15, 22, 56, 52, 123456)
    heading_from_acc = 3.1415 # radian due north ??? TODO
    while True:
        queue.put(('head_from_acc', datetime_sys, heading_from_acc))
