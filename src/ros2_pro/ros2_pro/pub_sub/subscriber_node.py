import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RecvData(Node):
    def __init__(self):
        super().__init__('recv_data')
        self.recv = self.create_subscription(Twist, 'turtle1/cmd_vel', self.sub_callback, 10)
        self.create_timer(0.5, self.sub_print)
        self.x = 0.0
        self.y = 0.0

    def sub_callback(self, msg:Twist):
        self.x = msg.linear.x
        self.y = msg.linear.y

    def sub_print(self):
        self.get_logger().info(f'axis X={self.x}, axis Y={self.y}')

def main():
    rclpy.init()
    node = RecvData()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == "__main__":
    main()
