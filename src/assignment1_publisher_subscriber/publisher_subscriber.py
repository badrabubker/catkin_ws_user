#!/usr/bin/python

import rospy
from std_msgs.msg import Float32


def print_yaw(data):
	pub.publish(data)
	rospy.loginfo("yaw is being Published %F"%(data.data))
	rate.sleep

if __name__ == '__main__':
	rospy.init_node('assignment2', anonymous=True)
	pub = rospy.Publisher('yaw_publisher', Float32, queue_size=10)
	rate = rospy.Rate(10) # 10hz
	rospy.Subscriber("yaw", Float32, print_yaw)
	rospy.spin()