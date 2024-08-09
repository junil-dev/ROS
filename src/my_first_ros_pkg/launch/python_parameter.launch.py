from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_first_ros_pkg',
            executable='my_first_parameter',
            name='custom_my_parameter_node',
            output='screen',
            emulate_tty=True,
            parameters=[
                {'my_parameter': 'junil'}
            ]
        )
    ])
