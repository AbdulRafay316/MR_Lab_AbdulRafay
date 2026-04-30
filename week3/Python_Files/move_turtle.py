#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import time

class VelocityPublisher(Node):
    def __init__(self):
        super().__init__('VelocityPublisher')
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
    def timer_callback(self):
        msg = Twist()
        for _ in range(4):
            msg.linear.x = 2.0 
            msg.angular.z = 0.0 
            self.publisher.publish(msg)
            time.sleep(2)
            msg.linear.x = 0.0
            msg.angular.z = 1.57 # Turn 90 degrees
            self.publisher.publish(msg) 
            time.sleep(1)

def main(args=None):
    rclpy.init(args=args)
    velocity_publisher = VelocityPublisher()
    rclpy.spin(velocity_publisher)
    velocity_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()