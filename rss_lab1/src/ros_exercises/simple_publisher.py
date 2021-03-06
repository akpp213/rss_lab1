#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Float32

def simple_publisher():
    rospy.init_node('simple_publisher')
    pub = rospy.Publisher('my_random_float', Float32, queue_size=10)
    rate = rospy.Rate(20) # 20hz
    while not rospy.is_shutdown():
	rand = random.uniform(0,10.0)
        rospy.loginfo(rand)
        pub.publish(rand)
        rate.sleep()

if __name__ == '__main__':
    try:
        simple_publisher()
    except rospy.ROSInterruptException:
        pass
