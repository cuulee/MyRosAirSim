#!/usr/bin/env python

from pymavlink import mavutil
import time


receiver = mavutil.mavlink_connection('udpin:0.0.0.0:5555')

while True:
    try:
        print(receiver.recv_match())

    except:
        pass
    time.sleep(0.1)