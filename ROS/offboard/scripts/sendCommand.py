#!/usr/bin/env python

import rospy
from mavros_msgs.srv import CommandLong


if __name__ == '__main__':
    try:

        rospy.init_node('command_sender', anonymous=True)

        #command = CommandLong(True, 246, 1, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        '''
        command.broadcast = True
        command.command = 246
        command.confirmation = 1
        command.param1 = 1.0
        command.param2 = 0.0
        command.param3 = 0.0
        command.param4 = 0.0
        command.param5 = 0.0
        command.param6 = 0.0
        command.param7 = 0.0
        '''

        rosservice = rospy.ServiceProxy('mavros/cmd/command', CommandLong)
        response = rosservice.call(True, 246, 0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        print("Success: " + str(response.success))
        print("Result: " + str(response.result))


    except rospy.ROSInterruptException:
        print("ROS Interruption exception")
        pass