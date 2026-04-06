import rclpy
from rclpy.node import Node
# We are no longer importing 'String'. We are importing 'Float64' (a decimal number)
from std_msgs.msg import Float64

# Import standard Python libraries for our "outside logic"
import random

class TemperatureSensorNode(Node):
    def __init__(self):
        super().__init__('temperature_sensor')
        
        # --- NEW: DECLARING A PARAMETER ---
        # 1. We tell ROS: "I have a parameter named 'publish_frequency'. Its default value is 2.0."
        self.declare_parameter('publish_frequency', 2.0)
        
        # 2. We READ the parameter's current value from ROS and store it in a Python variable.
        # The .get_parameter_value().double_value extracts the actual decimal number.
        timer_period = self.get_parameter('publish_frequency').get_parameter_value().double_value
        
        # 1. THE PLUMBING (ROS 2)
        # Create a publisher that sends Float64 messages on the 'temperature' topic
        self.publisher_ = self.create_publisher(Float64, 'temperature', 10)
        
        # Create a timer that runs our callback using the parameter we just read!
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # 2. THE OUTSIDE LOGIC (Traditional Python)
        
        # A. Simulate reading from a hardware sensor. 
        # We generate a random decimal number between 20.0 and 30.0 (Celsius)
        raw_celsius = random.uniform(20.0, 30.0)
        
        # B. Perform some traditional math to convert Celsius to Fahrenheit
        fahrenheit = (raw_celsius * 9/5) + 32
        
        # C. Round the number to 2 decimal places so it looks nice
        fahrenheit_rounded = round(fahrenheit, 2)
        
        # 3. BACK TO THE PLUMBING (ROS 2)
        
        # A. Create a blank message of type Float64
        msg = Float64()
        
        # B. Put our calculated number into the message's data field
        msg.data = fahrenheit_rounded
        
        # C. Publish it to the network
        self.publisher_.publish(msg)
        
        # Print it to our terminal so we can verify it's working
        self.get_logger().info(f'Published Temperature: {msg.data} F')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureSensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
