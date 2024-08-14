import sys
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from turtlesim.action import RotateAbsolute

class RotateClient(Node):
    def __init__(self):
        super().__init__('rotate_client')
        self.action_cli = ActionClient(
            self,
            RotateAbsolute,
            'turtle1/rotate_absolute')

    def send_goal(self, order):
        goal_msg = RotateAbsolute.Goal()
        goal_msg.theta = order
        self.action_cli.wait_for_server()
        self._send_goal_future = self.action_cli.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Result: {result}')
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg
        self.get_logger().info(f'Received feedback: {feedback}')

def main(args=None):
    rclpy.init(args=args)
    node = RotateClient()
    try:
        node.send_goal(float(sys.argv[1]))
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == '__main__':
    main()
