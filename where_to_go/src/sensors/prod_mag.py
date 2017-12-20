def prod_mag(queue):
    datetime_sys = (2017, 12, 15, 22, 56, 52, 123456)
    orientation_due_north_mag = 3.14159 # radian (counter?) clockwise TODO
    while True:
        queue.put(('mag', datetime_sys, orientation_due_north_mag))
