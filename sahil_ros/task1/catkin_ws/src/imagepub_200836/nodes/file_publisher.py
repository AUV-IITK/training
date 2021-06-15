#!/usr/bin/env python3
import rospy 
import cv2
from cv_bridge import CvBridge
import numpy as np
from sensor_msgs.msg import Image

def talker():
    pub = rospy.Publisher('checkerboard',Image,queue_size=1)
    rospy.init_node('file_publisher')
    frequency=rospy.get_param('frequency',0.1)
    rate = rospy.Rate(frequency)
    bridge = CvBridge()
    while not rospy.is_shutdown():
        image_file = rospy.get_param('file','/home/sahil/Pictures/image1.png')
        img = cv2.imread(image_file)
        img_msg = bridge.cv2_to_imgmsg(img)
        pub.publish(img_msg)
        rate.sleep()

if __name__=='__main__':
    talker()