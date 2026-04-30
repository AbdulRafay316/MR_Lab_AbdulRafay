import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TriangleMotion(Node):
    def __init__(self):
        super().__init__('Triangle_motion')
        self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        for _ in range(3):
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.pub.publish(msg)
            time.sleep(2)

            msg.linear.x = 0.0
            msg.angular.z = 2.094  # 120 degrees
            self.pub.publish(msg)
            time.sleep(1)

def main(args=None):
    rclpy.init(args=args)
    node = TriangleMotion()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()