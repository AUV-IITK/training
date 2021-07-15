#!/usr/bin/env python3
import rospy
import numpy as np
from sensor_msgs.msg import Image as image
from cv_bridge import CvBridge
import cv2
import matplotlib.pyplot as plt

def talker():
    pub = rospy.Publisher('checkerboard',image,queue_size=2)
    rospy.init_node('cb_publisher')
    bridge = CvBridge()
    h = rospy.get_param('height',400)
    w = rospy.get_param('width',400)
    f = rospy.get_param('frequency',0.1)
    size = rospy.get_param('square_size',50)
    # h =400
    # w= 400
    # f= 0.5
    # size =50
    im = np.zeros([h,w])

    for i in np.arange(0,int(h//size),2):
        for j in np.arange(0,int(w//size),2):
            r= i*size
            c = j*size
            im[r:r+size,c:c+size] = np.ones([size,size])
    f = 0.5
    rate = rospy.Rate(f)
    while not rospy.is_shutdown():
        # h =400
        # w= 400
        # f= 0.5
        # size =50
        # im = np.zeros([h,w])
        # for i in np.arange(0,int(h//size),2):
        #     for j in np.arange(0,int(w//size),2):
        #         r= i*size
        #         c = j*size
        #         im[r:r+size,c:c+size] = np.ones([size,size])
        # msg = image()
        # msg.header.stamp = rospy.Time.now()
        # msg.height = h
        # msg.width = w
        # msg.encoding = "64FC1"
        # msg.is_bigendian = 0
        # msg.step = 1 * w
        # msg.data = im.tobytes()
        # print(im.shape)
        # cv2.imshow('w',im)
        # cv2.waitKey(0)
        msg = bridge.cv2_to_imgmsg(im,encoding='passthrough')
        pub.publish(msg)
        # print(im[0:50,0:50])
        # rospy.loginfo(msg)
        rate.sleep()

if __name__=='__main__':
    talker()