import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class GoToGoal(Node):
    def __init__(self):
        super().__init__('go_to_goal')

        self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.sub = self.create_subscription(Pose, 'turtle1/pose', self.callback, 10)

        self.goal_x = 8.0
        self.goal_y = 5.0

    def callback(self, pose):
        msg = Twist()

        dx = self.goal_x - pose.x
        dy = self.goal_y - pose.y

        distance = math.sqrt(dx*dx + dy*dy)
        angle = math.atan2(dy, dx)

        if distance > 0.1:
            msg.linear.x = 1.5 * distance
            msg.angular.z = 4.0 * (angle - pose.theta)
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = GoToGoal()
    rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()