import sys
import rclpy
from rclpy.node import Node

# 1. IMPORT OUR CUSTOM SERVICE DEFINITION
from my_custom_msgs.srv import AddTwoInts

class MinimalClientAsync(Node):
    def __init__(self):
        super().__init__('minimal_client_async')
        
        # 2. CREATE THE CLIENT
        # It needs to dial the exact same "phone number" as the server ('add_two_ints')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        
        # 3. WAIT FOR THE SERVER TO WAKE UP
        # We check every 1 second to see if the server is alive on the network
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
            
        # 4. CREATE A BLANK REQUEST BOX
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        # 5. PUT DATA IN THE BOX
        self.req.a = a
        self.req.b = b
        
        # 6. MAIL THE BOX AND WAIT FOR THE RETURN BOX
        # This sends the request to the server and returns a "future" object 
        # (a promise that an answer will arrive eventually)
        self.future = self.cli.call_async(self.req)
        
        # We tell the program to pause and wait until the server responds
        rclpy.spin_until_future_complete(self, self.future)
        
        # 7. RETURN THE FINAL ANSWER
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)
    minimal_client = MinimalClientAsync()
    
    # We grab the two numbers you typed into the terminal 
    # (e.g., if you typed: ros2 run ... client 5 10)
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    
    # Call our function to dial the server
    response = minimal_client.send_request(a, b)
    
    # Print the final result!
    minimal_client.get_logger().info(f'Result of add_two_ints: {a} + {b} = {response.sum}')

    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
