#!/usr/bin/env python

import rospy
from pymavlink import mavutil


rospy.init_node("node_reboot", anonymous=True)

device1='udpout:localhost:14557'
dialect='pixhawk'
target_system=255
target_component=0
MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN=246


autopilot = mavutil.mavlink_connection(device=device1) #, dialect=dialect)
"""
autopilot.mav.command_long_send(target_system, target_component,
                                       MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN, 1,
                                       1, 0, 0, 0, 0, 0, 0)
"""
autopilot.reboot_autopilot()
#autopilot.mav.command_long_send(255, 0, 246, 1, 0, 0, 1.5, 0, 0, 0, 5)
