from setuptools import find_packages, setup

package_name = 'my_first_package'

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
    maintainer='kosuke',
    maintainer_email='246223926+kosuke-satake@users.noreply.github.com',
    description='My first ROS 2 package',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'simple_node = my_first_package.simple_node:main',
            'simple_subscriber = my_first_package.simple_subscriber:main',
            'temperature_sensor = my_first_package.temperature_sensor_node:main'
        ],
    },
)
