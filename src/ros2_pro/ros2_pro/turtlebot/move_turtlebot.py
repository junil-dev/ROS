#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleBot3Move(Node):
    def __init__(self):
        super().__init__('turtlebot3_move')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move_callback)
        self.move_cmd = Twist()
        self.move_cmd.linear.x = 0.2  # 전진 속도
        self.move_cmd.angular.z = 0.0  # 회전 속도

    def move_callback(self):
        self.publisher_.publish(self.move_cmd)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleBot3Move()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
