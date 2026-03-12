import rclpy
from rclpy.node import Node
from ros_study_msgs.msg import TH

class TemperatureSubscriber(Node):
    def __init__(self):
        super().__init__('temperature_subscriber')
        self.create_subscription(TH,
                                 'information',
                                 self.temp_callback,
                                 10)
        
        self.get_logger().info("Measure started")

    def temp_callback(self,msg):
        if msg.onoff == 50:
            self.get_logger().info(f"Received temperature:{msg.temp:.2f} °C")
            self.get_logger().info(f"Received temperature:{msg.hum:.2f} %")
        else :
            self.get_logger().info(f"please Turn On")



def main(args=None):
    rclpy.init(args=args)
    node = TemperatureSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
