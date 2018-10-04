#!/usr/bin/env python

import rospy
from pymavlink import mavutil

'''
rospy.init_node("node_999", anonymous=True)

device1='udpout:localhost:14557'
target_system=1
target_component=1
ESTIMATOR_CONTROL_MSG = 999


autopilot = mavutil.mavlink_connection(device=device1)

autopilot.mav.command_long_send(target_system,
                                target_component,
                                ESTIMATOR_CONTROL_MSG,
                                5)
'''


