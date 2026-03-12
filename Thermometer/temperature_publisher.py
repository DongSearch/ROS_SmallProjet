import rclpy
from rclpy.node import Node
from ros_study_msgs.msg import TH
import random
import sys
import threading
import termios
import tty
import select

class TemperaturePublisher(Node):
    def __init__(self):
        super().__init__("temperature_publisher")
        self.publisher_ = self.create_publisher(TH,"information",10)
        self.timer =self.create_timer(2.0,self.temp_callback)
        self.get_logger().info("Temperature Publisher started.")
        self.onoff = 0
        thread = threading.Thread(target=self.keyboard_listener,daemon=True)
        thread.start()



    def getch_nonblocking(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            if select.select([sys.stdin], [], [], 0.1)[0]:
                return sys.stdin.read(1)
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
    def keyboard_listener(self):
        while rclpy.ok():
            key = self.getch_nonblocking()
            if key:
                if key.lower() =="o":
                    self.onoff = 50
                    self.get_logger().info("Switched ON")

                elif key.lower() == "f":
                    self.onoff = 0
                    self.get_logger().info("Switched OFF")

    def temp_callback(self):
        msg = TH()
        msg.temp = random.uniform(20.0,40.0)
        msg.hum = random.uniform(0.0,100.0)
        msg.onoff = self.onoff
        if msg.onoff == 50 :
            self.get_logger().info(f"Published temperature : {msg.temp:.2f} °C")
            self.get_logger().info(f"Published Humidity : {msg.hum:.2f} %")
        else :
            msg.temp = 0.0
            msg.hum = 0.0
            self.get_logger().info("to start, please press o butteon")
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args =args)
    node = TemperaturePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()