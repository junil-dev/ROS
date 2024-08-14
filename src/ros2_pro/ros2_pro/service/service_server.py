import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute

class teleportTurtle(Node):
    def __init__(self):
        super().__init__('teleport_turtle')
        self.srv = self.create_service(TeleportAbsolute, 'turtle1/teleport_absolute', self.move_turtlesim)
        self.x = 0.0
        self.y = 0.0

    def move_turtlesim(self, request, response):
        self.x = request.x
        self.y = request.y
        self.get_logger().info(f'teleport_turtle {request.x}, {request.y}')

        return response

def main(args=None):
    rclpy.init(args=args)
    node = teleportTurtle()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == "__main__":
    main()
