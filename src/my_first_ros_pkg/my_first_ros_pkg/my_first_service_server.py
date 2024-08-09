import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class MyServiceServer(Node):
    def __init__(self):
        super().__init__('my_service_server')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_init_callback)

    def add_two_init_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'Incomming request {request.a} + {request.b}')

        return response

def main(args=None):
    rclpy.init(args=args)
    my_service = MyServiceServer()
    rclpy.spin(my_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
