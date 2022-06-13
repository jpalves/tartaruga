#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from std_msgs.msg import Int16, Empty
import time

#código para o volante logitech G29



def teste(data):
        #print('tic-tac')
        pub.publish(twist)

def callback(data):
     twist.linear.x =  data.axes[2]/2.0 + 0.5
     twist.angular.z = data.axes[0]
     
     
# Intializes everything
def start():
     # publishing to "turtle1/cmd_vel" to control turtle1
     global pub, pub2, twist
     twist = Twist()
     rospy.init_node('tartaruga')
     pub  = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
     
     # subscribed to joystick inputs on topic "joy"
     rospy.Subscriber("joy", Joy, callback)
     # starts the node
     rospy.Timer(rospy.Duration(0.1), teste)
     rospy.spin()
 
if __name__ == '__main__':
     start()
