#!/usr/bin/env python

import time
from pymavlink import mavutil
from pymavlink.dialects.v20 import mypx4 as px4

f = open("prueba.txt", "w+")
mav = px4.MAVLink(f)
mav.estimator_control_msg_send(target_system=0, target_component=0, command=1, force_mavlink1=False)

'''
sender = mavutil.mavlink_connection(device='udpout:127.0.0.1:5555', dialect="mypx4")
sender.mav.battery_status_send(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
'''

'''
while True:
    mav.battery_status_send(99, 3, 1, 36, 12, -1, -1, -1, -1, 0, 0, False)
    time.sleep(1)
'''

