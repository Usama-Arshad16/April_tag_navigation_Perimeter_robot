#!/usr/bin/env python
import rospy, cv2, cv_bridge
import cv2.aruco as aruco
import sys, time, math
from sensor_msgs.msg import Image
import numpy as np

marker_size  = 50 #- [cm]



def main(msg):

    #--- Get the camera calibration path
    calib_path  = ""
    camera_matrix   = np.loadtxt("/home/markhoor/catkin_ws/src/perimeter_robot/perimeter_control/src/cameraMatrix.txt", delimiter=',')
    camera_distortion   = np.loadtxt('/home/markhoor/catkin_ws/src/perimeter_robot/perimeter_control/src/cameraDistortion.txt', delimiter=',')


    #--- Define the aruco dictionary
    aruco_dict  = aruco.getPredefinedDictionary(aruco.DICT_ARUCO_ORIGINAL)
    parameters  = aruco.DetectorParameters_create()


    #--- Capture the videocamera (this may also be a video or a picture)
    cap = cv_bridge.CvBridge()



    #-- Font for the text in the image
    font = cv2.FONT_HERSHEY_PLAIN

    #while True:

    #-- Read the camera frame
    frame = cap.imgmsg_to_cv2(msg,desired_encoding='bgr8')
    #cap = cv2.VideoCapture(frame)
    #ret, frame = cap.read(frame)

    #-- Convert in gray scale
    gray    = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # remember, OpenCV stores color images in Blue, Green, Red

    #-- Find all the aruco markers in the image
    corners, ids, rejected = aruco.detectMarkers(image=gray, dictionary=aruco_dict, parameters=parameters,
                              cameraMatrix=camera_matrix, distCoeff=camera_distortion)

    
    if ids is not None:
	print "Row = " + str(ids[0])

    cv2.imshow('right_camera', frame)

    #--- use 'q' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        cv2.destroyAllWindows()

def land():
	global cmd_vel_pub, pub
	rospy.init_node('landing')
	image_sub = rospy.Subscriber('/up_left_d435/camera/image', Image, main)

	
	
if __name__ == '__main__':
		cv2.destroyAllWindows()
		land()
		rospy.spin()
