#!/usr/bin/env python
import rospy
import matplotlib as m
from sensor_msgs.msg import Image
import cv2, cv_bridge
def image_callback(msg):
	bridge = cv_bridge.CvBridge()
	cv2.namedWindow("right_camera", 1)
	image = bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
	cv2.imshow("right_camera", image)
	cv2.waitKey(3)

#right_sub = rospy.Subscriber('/up_right_d435/camera/image',Image, image_callback)
rospy.init_node('camera')
right_sub = rospy.Subscriber('/up_left_d435/camera/image',Image, image_callback)
rospy.spin()