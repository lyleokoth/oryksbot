#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

"""
This node converts Joystick inputs from the joy node into velocity 
commands. Receives joystick messages(subscribed to Joy topic) then
converts the joystick inputs into twist commands.
#Axis 1 (left stick vertical) controls the linear speed
#Axis 3 (right stick horizontal) controls angular speed
"""

def callback(data):
    twist = Twist()
    twist.linear.x = data.axes[1]
    twist.angular.z = data.axes[3]
    pub.publish(twist)

def start():
    #Publishing to /cmd_vel
    global pub 
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    #Subscribe to joystick inputs on topic joy
    rospy.Subscriber("joy", Joy, callback)
    #Starts the node
    rospy.init_node('JoyToBot')
    rospy.spin()

if __name__ == '__main__':
    start()