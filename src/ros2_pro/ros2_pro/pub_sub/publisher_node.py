import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node

class T_move(Node):
    def __init__(self):
        super().__init__('turtle_move')
        self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.create_timer(0.5, self.update_callback)
        self.pub_timer = self.create_timer(1.0 , self.pub_callback)
        self.x = 0.0
        self.y = 0.0

    def pub_callback(self):
        msg = Twist()
        msg.linear.x = self.x
        msg.linear.y = self.y
        self.pub.publish(msg)

    def update_callback(self):
        self.x += 0.1
        self.get_logger().info(f'goging topic X={self.x}, y={self.y}')


def main():
    rclpy.init()
    node = T_move()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()


if __name__ == "__main__":
    main()
