import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from turtlesim.action import RotateAbsolute

class RotateServer(Node):
    def __init__(self):
        super().__init__('rotate_server')
        self.action_srv = ActionServer(
            self,
            RotateAbsolute,
            'turtle1/rotate_absolute',
            self.action_callback)

    def action_callback(self, goal_handle):
        self.get_logger().info(f'execute goal...')
        feedback_msg = RotateAbsolute.Feedback()

        goal_handle.publish_feedback(feedback_msg)
        self.get_logger().info(f'feedback = {feedback_msg.remaining}')
        result = RotateAbsolute.Result()
        return result

def main(args=None):
    rclpy.init(args=args)
    node = RotateServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == '__main__':
    main()
