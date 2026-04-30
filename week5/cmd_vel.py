import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CmdVelPublisher(Node):
    def __init__(self):
        super().__init__('cmd_vel_publisher')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.forward = True  # toggle flag

    def timer_callback(self):
        msg = Twist()
        if self.forward:
            msg.linear.x = 0.2   # forward velocity
            msg.angular.z = 0.0
            self.get_logger().info('Publishing: FORWARD velocity = 0.2')
        else:
            msg.linear.x = 0.0   # zero velocity
            msg.angular.z = 0.0
            self.get_logger().info('Publishing: STOP velocity = 0.0')
        
        self.publisher_.publish(msg)
        self.forward = not self.forward  # alternate every 2 seconds

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
