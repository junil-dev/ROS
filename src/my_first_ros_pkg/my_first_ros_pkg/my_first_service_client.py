import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class MyServiceClient(Node):
    def __init__(self):
        super().__init__('my_service_client')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, watting again......')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)

    my_srv_cli = MyServiceClient()
    response = my_srv_cli.send_request(int(sys.argv[1]), int(sys.argv[2]))
    my_srv_cli.get_logger().info(
        f'Result of add_two_ints : {my_srv_cli.req.a} + {my_srv_cli.req.b} = {response.sum}')
    my_srv_cli.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

