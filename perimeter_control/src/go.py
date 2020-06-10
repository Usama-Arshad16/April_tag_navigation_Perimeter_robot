#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
def callback(msg):
    global x, y, z
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    z = msg.pose.pose.orientation.z
    print ""+str(x)+","+str(y)+","+str(z)
    print""

rospy.init_node('odo_sub')
odo_sub = rospy.Subscriber('/odometry/filtered', Odometry, callback)
rospy.spin()