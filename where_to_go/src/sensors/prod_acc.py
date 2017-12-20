import datetime
import os.path
import time

from _conf_sensors import ROOT

handle = os.path.join(ROOT, 'data/testdata/acceleration.dsv')

def prod_acc(queue, period=0.0):
    with open(handle, 'r') as accelerations:
        # skip headings
        accelerations.next()
        for acc in accelerations:
            time.sleep(period)
            datetime_sys = str(datetime.datetime.now())
            queue.put(('acc', datetime_sys, acc))
