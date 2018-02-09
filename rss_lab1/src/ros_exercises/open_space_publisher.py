#!/usr/bin/env python

import math
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
from ros_exercises.msg import OpenSpace

def callback(data):
     space = OpenSpace()
     longest = max(data.ranges)
     angle = data.angle_min + data.angle_increment*data.ranges.index(longest)
     pub = rospy.Publisher(rospy.get_param("pub_topic",'open_space'), OpenSpace, queue_size = 10)
     space.distance = longest
     space.angle = angle
     rospy.loginfo(longest)
     rospy.loginfo(angle)
     pub.publish(space)

def open_space_publisher():

    rospy.init_node('open_space_publisher')

    rospy.Subscriber(rospy.get_param("subs_topic",'fake_scan'), LaserScan, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    open_space_publisher()
