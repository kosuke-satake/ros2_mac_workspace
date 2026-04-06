import rclpy
from rclpy.node import Node
# We are no longer importing 'String'. We are importing 'Float64' (a decimal number)
from std_msgs.msg import Float64

# Import the specific ROS message type needed to respond to parameter changes
from rcl_interfaces.msg import SetParametersResult

# Import standard Python libraries for our "outside logic"
import random

class TemperatureSensorNode(Node):
    def __init__(self):
        super().__init__('temperature_sensor')
        
        # --- DECLARING A PARAMETER ---
        # 1. We tell ROS: "I have a parameter named 'publish_frequency'. Its default value is 2.0."
        self.declare_parameter('publish_frequency', 2.0)
        
        # 2. We READ the parameter's current value from ROS and store it in a Python variable.
        timer_period = self.get_parameter('publish_frequency').get_parameter_value().double_value
        
        # 1. THE PLUMBING (ROS 2)
        # Create a publisher that sends Float64 messages on the 'temperature' topic
        self.publisher_ = self.create_publisher(Float64, 'temperature', 10)
        
        # Create a timer that runs our callback using the parameter we just read!
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # --- NEW: THE LISTENER FOR PARAMETER CHANGES ---
        # 3. We tell ROS: "If anyone changes ANY parameter on this node over the network, 
        # please immediately run my 'parameter_callback' function."
        self.add_on_set_parameters_callback(self.parameter_callback)

    # This is the new function that runs ONLY when a parameter is changed over the network
    def parameter_callback(self, params):
        # 'params' is a list of all parameters that were just changed. We loop through them.
        for param in params:
            # If the parameter that was changed is 'publish_frequency'...
            if param.name == 'publish_frequency':
                # Extract the new number (e.g., 0.5)
                new_speed = param.value
                
                # We log it so we can see it happened
                self.get_logger().info(f'Changing publish frequency to {new_speed} seconds!')
                
                # Destroy the old timer
                self.timer.cancel()
                
                # Create a brand new timer with the brand new speed!
                self.timer = self.create_timer(new_speed, self.timer_callback)
                
        # We must tell ROS that the parameter change was successful
        return SetParametersResult(successful=True)

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
