#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
import time


rospy.init_node('turtlesim_motion_pose', anonymous=True)
cmd_vel_topic='/turtle1/cmd_vel'
velocity_publisher=rospy.Publisher(cmd_vel_topic, Twist, queue_size = 40)
time.sleep(1)

rate = rospy.Rate(10) # 10hz
i=0
mensaje_vel=Twist()

for i in range(8):
    mensaje_vel.linear.x=0.0
    mensaje_vel.angular.z=0.0
    if i%2==0:
        mensaje_vel.linear.x=2.0
    else:
        mensaje_vel.angular.z=2.11
    velocity_publisher.publish(mensaje_vel)  
    i=i+1
    time.sleep(1)
