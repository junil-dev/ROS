from setuptools import find_packages, setup

package_name = 'ros2_pro'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kimjunil',
    maintainer_email='kjlmbs9588@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = ros2_pro.pub_sub.publisher_node:main',
            'subscriber = ros2_pro.pub_sub.subscriber_node:main',
            'service_server = ros2_pro.service.service_server:main',
            'service_client = ros2_pro.service.service_client:main',
            'action_server = ros2_pro.action.action_server:main',
            'action_client = ros2_pro.action.action_client:main',
            'turtle_move = ros2_pro.turtlebot.move_turtlebot:main',
            'follow_wall = ros2_pro.turtlebot.follow_wall:main'
        ],
    },
)
