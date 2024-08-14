import sys
import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute

class TurtleClient(Node):
    def __init__(self):
        super().__init__('turtle_client')
        self.cli = self.create_client(TeleportAbsolute, 'turtle1/teleport_absolute')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(f'connect to server....')
        self.req = TeleportAbsolute.Request()

    def send_request(self, x, y):
        self.req.x = x
        self.req.y = y
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args = None):
    rclpy.init(args=args)
    node = TurtleClient()
    try:
        node.send_request(float(sys.argv[1]), float(sys.argv[2]))
        node.get_logger().info(f'Request : {node.req.x} , {node.req.y}')
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == "__main__":
    main()
