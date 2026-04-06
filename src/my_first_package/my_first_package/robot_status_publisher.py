import rclpy
from rclpy.node import Node

# 1. IMPORT OUR BRAND NEW CUSTOM MESSAGE!
from my_custom_msgs.msg import RobotStatus

import random

class RobotStatusPublisher(Node):
    def __init__(self):
        super().__init__('robot_status_publisher')
        
        # 2. CREATE THE PUBLISHER
        # Notice we use 'RobotStatus' as the message type, not 'String' or 'Float64'
        self.publisher_ = self.create_publisher(RobotStatus, 'robot_status', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        # 3. CREATE THE MESSAGE OBJECT
        msg = RobotStatus()
        
        # 4. FILL IN THE DATA (Precise writing)
        # We MUST use the exact variable names we defined in the .msg file
        msg.battery_percentage = random.randint(10, 100)
        msg.current_state = "Exploring the room"
        
        # Simulate a 10% chance of a random error occurring
        if random.random() < 0.10:
            msg.has_error = True
            msg.current_state = "ERROR: Wheel slipped!"
        else:
            msg.has_error = False

        # 5. PUBLISH IT!
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing Status: Battery={msg.battery_percentage}%, State="{msg.current_state}", Error={msg.has_error}')

def main(args=None):
    rclpy.init(args=args)
    node = RobotStatusPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
