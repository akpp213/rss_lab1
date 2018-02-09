#!/usr/bin/env python

import math
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan

def callback(data):
     longest = max(data.ranges)
     angle = data.angle_min + data.angle_increment*data.ranges.index(longest)
     pub1 = rospy.Publisher('open_space/distance', Float32, queue_size=10)
     pub2 = rospy.Publisher('open_space/angle', Float32, queue_size = 10)
     rospy.loginfo(longest)
     rospy.loginfo(angle)
     pub1.publish(longest)
     pub2.publish(angle)

def open_space_publisher():

    rospy.init_node('open_space_publisher')

    rospy.Subscriber('fake_scan', LaserScan, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    open_space_publisher()
