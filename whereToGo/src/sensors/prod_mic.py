def prod_mic(queue):
    datetime_sys = (2017, 12, 15, 22, 56, 52, 123456)
    while True:
        queue.put(('mic', datetime_sys))
