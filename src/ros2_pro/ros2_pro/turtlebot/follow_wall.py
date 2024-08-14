import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class WallFollower(Node):
    def __init__(self):
        super().__init__('wall_follower')

        # Publisher for controlling the robot's velocity
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        # Subscriber for receiving LIDAR data
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.laser_callback,
            10)

        self.subscription  # prevent unused variable warning

        # Control parameters
        self.target_distance = 0.01  # 4cm
        self.linear_speed = 0.13     # Linear speed of the robot
        self.angular_speed = 0.1     # Angular speed for corrections

        self.get_logger().info("Wall Follower Node has been started.")

    def laser_callback(self, msg):
        # Find the minimum distance to the left of the robot (close to 90 degrees)
        left_distance = msg.ranges[90]  # Assuming LIDAR's 90 degrees is left

        # Initialize Twist message for robot movement
        move_cmd = Twist()
        move_cmd.linear.x = self.linear_speed

        # Check if the robot is too close or too far from the wall
        if left_distance > self.target_distance + 0.01:
            # If too far from the wall, turn left slightly
            move_cmd.angular.z = self.angular_speed
        elif left_distance < self.target_distance - 0.01:
            # If too close to the wall, turn right slightly
            move_cmd.angular.z = -self.angular_speed
        else:
            # If within the desired range, go straight
            move_cmd.angular.z = 0.0

        # Publish the movement command
        self.publisher_.publish(move_cmd)

def main(args=None):
    rclpy.init(args=args)
    wall_follower = WallFollower()
    try:
        rclpy.spin(wall_follower)
    except KeyboardInterrupt:
        wall_follower.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
