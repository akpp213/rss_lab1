#!/usr/bin/env python

import rospy
import math
import random
from sensor_msgs.msg import LaserScan

def fake_scan_publisher():
    rospy.init_node('fake_scan_publisher')
    pub = rospy.Publisher('fake_scan', LaserScan, queue_size=10)
    rate = rospy.Rate(20) # 20hz
    while not rospy.is_shutdown():
	current_time = rospy.Time.now()
	scan = LaserScan()
	scan.header.stamp = current_time
	scan.header.frame_id = "base_link"
	scan.angle_min = -2*math.pi/3
	scan.angle_max = 2*math.pi/3
	scan.angle_increment = math.pi/300
	scan.scan_time = 1.0/20
	scan.range_min = 1.0
	scan.range_max = 10.0
	num_readings = int((scan.angle_max - scan.angle_min) // scan.angle_increment) + 1
	scan.ranges = [0] * num_readings
	for i in range(0, num_readings):
	     scan.ranges[i] = random.uniform(scan.range_min, scan.range_max)
        #rospy.loginfo(scan)
	pub.publish(scan)
        rate.sleep()

if __name__ == '__main__':
    try:
        fake_scan_publisher()
	rospy.spin()
    except rospy.ROSInterruptException:
        pass
