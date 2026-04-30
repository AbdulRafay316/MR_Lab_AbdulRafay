import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class TurtleFollower(Node):
    def __init__(self):
        super().__init__('turtle_follower')

        # Subscribe to turtle1's pose
        self.leader_pose = None
        self.follower_pose = None

        self.sub_leader = self.create_subscription(
            Pose, '/turtle1/pose', self.leader_callback, 10)

        self.sub_follower = self.create_subscription(
            Pose, '/turtle2/pose', self.follower_callback, 10)

        # Publish velocity to turtle2
        self.pub = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)

        # Control loop at 10 Hz
        self.timer = self.create_timer(0.1, self.control_loop)

    def leader_callback(self, msg):
        self.leader_pose = msg

    def follower_callback(self, msg):
        self.follower_pose = msg

    def control_loop(self):
        if self.leader_pose is None or self.follower_pose is None:
            return

        # Calculate distance and angle to leader
        dx = self.leader_pose.x - self.follower_pose.x
        dy = self.leader_pose.y - self.follower_pose.y
        distance = math.sqrt(dx**2 + dy**2)
        angle_to_leader = math.atan2(dy, dx)
        angle_diff = angle_to_leader - self.follower_pose.theta

        # Normalize angle to [-pi, pi]
        angle_diff = math.atan2(math.sin(angle_diff), math.cos(angle_diff))

        msg = Twist()

        # Only move if far enough away (avoid jitter)
        if distance > 0.5:
            msg.linear.x = 1.5 * distance
            msg.angular.z = 4.0 * angle_diff
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleFollower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()