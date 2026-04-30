#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn

class MultiTurtles(Node):
    def __init__(self):
        super().__init__('multi_turtles')

        # Spawn service
        self.spawn_client = self.create_client(Spawn, 'spawn')
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            pass

        self.spawn_turtle(2.0, 2.0, 'turtle2')
        self.spawn_turtle(6.5, 6.5, 'turtle3')

        # Publishers
        self.pub1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pub2 = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.pub3 = self.create_publisher(Twist, '/turtle3/cmd_vel', 10)

        # Timers
        self.timer = self.create_timer(0.1, self.move)

        # Counters for triangle and square
        self.tri_step = 0
        self.tri_count = 0

        self.sq_step = 0
        self.sq_count = 0

    def spawn_turtle(self, x, y, name):
        req = Spawn.Request()
        req.x = x
        req.y = y
        req.theta = 0.0
        req.name = name
        self.spawn_client.call_async(req)

    def move(self):
        # -------- turtle1: circle --------
        msg1 = Twist()
        msg1.linear.x = 2.0
        msg1.angular.z = 1.0
        self.pub1.publish(msg1)

        # -------- turtle2: triangle --------
        msg2 = Twist()

        if self.tri_step % 2 == 0:
            msg2.linear.x = 2.0
            msg2.angular.z = 0.0
            self.tri_count += 1

            if self.tri_count >= 20:
                self.tri_count = 0
                self.tri_step += 1
        else:
            msg2.linear.x = 0.0
            msg2.angular.z = 2.094   # 120 degree
            self.tri_count += 1

            if self.tri_count >= 10:
                self.tri_count = 0
                self.tri_step += 1

        if self.tri_step >= 6:
            self.tri_step = 0

        self.pub2.publish(msg2)

        # -------- turtle3: square --------
        msg3 = Twist()

        if self.sq_step % 2 == 0:
            msg3.linear.x = 1.5
            msg3.angular.z = 0.0
            self.sq_count += 1

            if self.sq_count >= 20:
                self.sq_count = 0
                self.sq_step += 1
        else:
            msg3.linear.x = 0.0
            msg3.angular.z = 1.57   # 90 degree
            self.sq_count += 1

            if self.sq_count >= 10:
                self.sq_count = 0
                self.sq_step += 1

        if self.sq_step >= 8:
            self.sq_step = 0

        self.pub3.publish(msg3)


def main(args=None):
    rclpy.init(args=args)

    node = MultiTurtles()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()