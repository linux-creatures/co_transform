####Aurhor: Kiran Kumar Lekkala######

import pymesh
import csv
import rospy
from sensor_msgs.msg import PointCloud
import std_msgs.msg

def talker(ranges):
	num_readings = 100
    pub = rospy.Publisher('laserscan_debug', LaserScan, queue_size=50)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
    	debug_laserscan = LaserScan()
        debug_laserscan.header = std_msgs.msg.Header()
        debug_laserscan.header.stamp = rospy.Time.now()
        debug_laserscan.header.frame_id = "camera_optical"
        debug_laserscan.angle_min = -3.14
        debug_laserscan.angle_max = 3.14
        debug_laserscan.angle_increment = 6.28/num_readings
        debug_laserscan.time_increment = (1.0 / laser_frequency) / (num_readings)
        debug_laserscan.angle_max = 3.14
        debug_laserscan.ranges = ranges
        pub.publish(debug_laserscan)
        rate.sleep()

def distance(x1, x2, y1, y2):
	return sqrt((x1 - x2)^2 + (y1 - y2)^2)

plydata = PlyData.read($2)
csvfile = open($1)
range_val = $3

trajreader = csv.reader(csvfile)


for i in range(1:len(trejdata)):

	xval = csvfile[0]
	yval = csvfile[1]
	zval = csvfile[2]

	for j in range(1:len(plydata['vertex'])):
		if(plydata['vertex']['z'][j] == zval):
			if (distance(plydata['vertex']['x'][j], plydata['vertex']['x'][j], xval, yval) <= range_val):
				ranges.append(xval)
			talker(ranges)
