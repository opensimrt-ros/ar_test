#!/usr/bin/env python3
#http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20listener%20%28Python%29

import rospy
import tf
import std_msgs.msg

def publisher():

    
    #pub = rospy.Publisher('pose', PoseStamped, queue_size=1)
    rospy.init_node('pose_publisher', anonymous=True)
    listener = tf.TransformListener()
    rate = rospy.Rate(2) # Hz
    h = std_msgs.msg.Header()
    h.frame_id = 'map'
    br = tf.TransformBroadcaster()
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/map', '/torax', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        print(rot)
    br.sendTransform((0.5, 0.5, 0),
                     #tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     trans,
                     rospy.Time.now(),
                     "torax2",
                     "map")

        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy:
        pass

