#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
t = Twist()

rospy.init_node('turn')
twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

def turn():
	t.angular.z = 0.2
	t.linear.x = 0.2
	print("yes")
	twist_pub.publish(t)

while not rospy.is_shutdown():
	turn()
	rospy.sleep(0.01)