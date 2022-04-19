#!/usr/bin/env python3
#http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20listener%20%28Python%29

import rospy
import tf
import std_msgs.msg
#import tf_transformations

from dynamic_reconfigure.server import Server
from ar_test.cfg import TutorialsConfig
from sensor_msgs.msg import Imu

global r
global p
global y

r = 0
p = 0
y = 0


class ImF:

    def __init__(self):
        self.r = 0 
        self.p = 0
        self.y = 0
        self.ix = False
        self.iy = False
        self.iz = False


    def reconf_callback(self, config, level):
        rospy.loginfo("""Reconfigure Request: {int_param}, {double_paramr},\ 
              {str_param}, {bool_paramx}, {size}""".format(**config))
        
        self.r = config["double_paramr"]
        self.p = config["double_paramp"]
        self.y = config["double_paramy"]
        
        self.ix = config["bool_paramx"]
        self.iy = config["bool_paramy"]
        self.iz = config["bool_paramz"]
        
        return config

    def loop_callback(self, msg):
        orientation = (msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w)  # is a tuple

        self.br.sendTransform(self.origin, orientation, rospy.Time.now(), self.tf_name, self.originalframe)

    def publisher(self):
        rospy.init_node('tf_from_imu_publisher', anonymous=True)
        self.origin = rospy.get_param("origin",(.1,.2,.3))
        self.originalframe= rospy.get_param("ori_frame", 'map')
        self.tf_name = rospy.get_param("tf_name",'toraxx')
        self.br = tf.TransformBroadcaster()
        base_name = rospy.resolve_name("imu")
        rospy.Subscriber(base_name + "/data", Imu, self.loop_callback )
        srv = Server(TutorialsConfig, self.reconf_callback)
        rospy.spin()

if __name__ == '__main__':
    try:
        a = ImF()
        a.publisher()
    except rospy:
        pass

