import rclpy
from rclpy.node import Node

class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')

        # Declare a parameter with default value None
        self.declare_parameter('student_name', 'not set')

        # Get the parameter value
        student_name = self.get_parameter('student_name').value

        # Print based on whether it's set or not
        if student_name == 'not set':
            self.get_logger().info('student_name not set')
        else:
            self.get_logger().info(f'Student name: {student_name}')

def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    rclpy.spin_once(node, timeout_sec=0.1)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
