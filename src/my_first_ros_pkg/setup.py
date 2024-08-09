from setuptools import find_packages, setup

package_name = 'my_first_ros_pkg'

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
    maintainer_email='kimjunil@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_first_publisher_node = my_first_ros_pkg.my_first_publisher_node:main',
            'my_first_subscriber_node = my_first_ros_pkg.my_first_subscriber_node:main',
        ],
    },
)
