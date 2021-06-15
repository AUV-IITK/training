#!/usr/bin/env python3
import numpy as np
import rospy
from sensor_msgs.msg import Image as image
from cv_bridge import CvBridge
def callback(data):
    img = np.frombuffer(data.data,dtype=np.uint8).reshape(data.height,data.width,-1)
    pub = rospy.Publisher("modified_image",image,queue_size=1)
    c = rospy.get_param('contrast',1)
    b = rospy.get_param('brightness',1)
    img = img*c+b
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        # msg = image()
        # msg.header.stamp = rospy.Time.now()
        # msg.height = img.shape[0]
        # msg.width = img.shape[1]
        # msg.encoding = '8UC3'
        # msg.is_bigendian = 0
        # msg.data = img.tobytes()
        bridge = CvBridge()
        msg = bridge.cv2_to_imgmsg(img)
        pub.publish(msg)
        rate.sleep()


def listner():
    rospy.init_node('image_changer')
    rospy.Subscriber('checkerboard',image,callback)
    rospy.spin()

if __name__ == '__main__':
    listner()