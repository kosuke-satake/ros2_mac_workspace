import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MySimpleSubscriber(Node):
    def __init__(self):
        # 1. Initialize the node with the name 'simple_subscriber'
        super().__init__('simple_subscriber')
        
        # 2. Create a Subscriber
        # It listens for a 'String' message over the radio channel named 'chatter'
        # When a message arrives, it triggers the 'listener_callback' function
        # The '10' is the queue size
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # 3. The Action when a message is received
        # Print the received message to the terminal
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    # Turn on the ROS 2 plumbing
    rclpy.init(args=args)
    
    # Stamp out one instance of our subscriber
    node = MySimpleSubscriber()
    
    # Keep the node alive and spinning in an infinite loop, waiting for messages
    rclpy.spin(node)
    
    # Clean up and shut down if we press Ctrl+C
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
