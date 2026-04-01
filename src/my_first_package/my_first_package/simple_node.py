import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MySimpleNode(Node):
    def __init__(self):
        # 1. Initialize the node with the name 'simple_node' on the network
        super().__init__('simple_node')
        
        # 2. Create a Publisher
        # It broadcasts a 'String' message over a radio channel named 'chatter'
        # The '10' is the queue size (keep 10 messages in backup if network is slow)
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        
        # 3. Create a Timer (The Heartbeat)
        # Run the timer_callback function every 1.0 seconds
        timer_period = 1.0 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # A counter to keep track of our messages
        self.i = 0

    def timer_callback(self):
        # 4. The Action
        msg = String()
        msg.data = f'Hello ROS 2! Message number: {self.i}'
        
        # Blast it into the DDS Network
        self.publisher_.publish(msg)
        
        # Print it to the terminal so we can see it working
        self.get_logger().info(f'Publishing: "{msg.data}"')
        
        self.i += 1

def main(args=None):
    # Turn on the ROS 2 plumbing
    rclpy.init(args=args)
    
    # Stamp out one instance of our blueprint
    node = MySimpleNode()
    
    # Keep the node alive and spinning in an infinite loop
    rclpy.spin(node)
    
    # Clean up and shut down if we press Ctrl+C
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()