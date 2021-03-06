import datetime
import os.path
import time

from _conf_sensors import ROOT

handle = os.path.join(ROOT, 'data/testdata/gps.dsv')
path_gps_raw = os.path.join(ROOT, 'data/testdata/gps-raw_2017-12-28-12-58-26')

def prod_gps(queue, period=0.0):
    with open(handle, 'r') as gpss:
        # skip headings
        gpss.next()
        for gps in gpss:
            datetime_sys = str(datetime.datetime.now())
            datetime_gps, latitude, longitude, altitude, velocity_gps = gps.strip().split()
            queue.put((
                'gps',
                datetime_sys,
                datetime_gps,
                latitude,
                longitude,
                altitude,
                velocity_gps
            ))
            time.sleep(period)
