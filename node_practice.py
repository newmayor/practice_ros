#!/usr/bin/env python

#example of a Publisher

import rospy 
from geometry_msgs.msg import Twist, Vector3

if __name__ == '__main__':
    pub = rospy.Publisher("test", Twist, queue_size=10)
    rospy.init_node('cartesian')
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        rospy.loginfo("Next")
        pub.publish(Twist(Vector3(1,2,3), Vector3(4,5,6)))
        rate.sleep()

