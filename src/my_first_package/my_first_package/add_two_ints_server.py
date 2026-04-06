import rclpy
from rclpy.node import Node

# 1. IMPORT OUR CUSTOM SERVICE DEFINITION
from my_custom_msgs.srv import AddTwoInts

class MinimalService(Node):
    def __init__(self):
        super().__init__('minimal_service')
        
        # 2. CREATE THE SERVER
        # It listens on a specific "phone number" (the service name: 'add_two_ints')
        # When someone calls, it runs the 'add_two_ints_callback' function
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        # 3. DO THE MATH (The Outside Logic)
        # The 'request' object contains 'a' and 'b' from the caller
        response.sum = request.a + request.b
        
        # 4. LOG IT
        self.get_logger().info(f'Incoming request: a={request.a}, b={request.b}. Returning sum={response.sum}')
        
        # 5. RETURN THE RESPONSE 
        # (This is like hanging up the phone after giving the answer)
        return response

def main(args=None):
    rclpy.init(args=args)
    minimal_service = MinimalService()
    
    # Keep the server alive forever, waiting for calls
    rclpy.spin(minimal_service)
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()
