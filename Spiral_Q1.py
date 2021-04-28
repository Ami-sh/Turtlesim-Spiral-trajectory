#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move_spiral():
	

    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
    rospy.init_node('robot_cleaner', anonymous=True)
    
    move_cmd = Twist()
    move_cmd.linear.x = 1.0
    move_cmd.angular.z = 1.0  
    #I have put 1 as initital velociy both angular and linear , we can change it to anything  or also ask the user to input it.
    #linear.x is nothing but the tangential velocity




    #increased the tangential velocity, to obtain a spiral
    #stop only when terminal shuts down
   
    #basically angular z * Radius = Linear x is the relation and we increase x which increased the r
   #frequency of publishing is very high hence almost continous increase
    while not rospy.is_shutdown():
        pub.publish(move_cmd)
        move_cmd.linear.x = move_cmd.linear.x + 0.000001
        #0.000001 s an arbitrary number which helps in observing the trajectory, we can ask the rate of increase 
         #from user and make the changes in order to increment the radius 
        #here tangentialvelocity is 0.000001 * (default publishing rate in hertz) every sec.
        #i don't know the default publishing rate value in ROS
        

if __name__ == '__main__':
    try:
        move_spiral()
    except rospy.ROSInterruptException:
        pass
