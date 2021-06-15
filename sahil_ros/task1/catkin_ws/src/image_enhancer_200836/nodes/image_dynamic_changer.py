#!/usr/bin/env python3

from image_enhancer_200836.cfg import imagechangerconfigConfig as config_type
import numpy as np
import rospy
from sensor_msgs.msg import Image as image
from cv_bridge import CvBridge
from dynamic_reconfigure.server import Server

def image_changer(data,parameters):
    bridge = CvBridge()
    img = bridge.imgmsg_to_cv2(data)
    b = parameters.brightness
    c = parameters.contrast
    pub = rospy.Publisher('modified_image',image,queue_size=1)
    img = img*c+b
    rate = rospy.Rate(1)
    img_msg = bridge.cv2_to_imgmsg(img)
    pub.publish(img_msg)
    rate.sleep()

def callback(config,level):
    rospy.Subscriber('checkerboard',image,image_changer,config)
    return config

if __name__=='__main__':
    rospy.init_node('image_dynamic_changer')
    srv = Server(config_type,callback)
    # rospy.Subscriber('chekerboard',image,image_changer,srv)
    rospy.spin()
