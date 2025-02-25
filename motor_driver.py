from microbit import *
from Motor import *

class Motordriver:
    def __init__(self, motor1, motor2, speed=0):
        self.motor1 = Motor(1, 2, 3, 0, 255 )
        self.motor2 = Motor(4, 5, 6, 0, 255)
        self.__speed = speed

    @property
    def speed (self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if self.motor1.minval <= speed <= self.motor1.maxval and self.motor2.minval <= speed <= self.motor2.maxval :
            self.__speed = speed
        else:
            print("Speed moet tussen minVal en maxVal zijn")

    def forward(self):
        self.motor1.motorpin1.write_digital(1)
        self.motor1.motorpin2.write_digital(0)
        self.motor1.motorpwmpin.write_analog(self.__speed)

        self.motor2.motorpin1.write_digital(1)
        self.motor2.motorpin2.write_digital(0)
        self.motor2.motorpwmpin.write_analog(self.__speed)

    def backward(self):
        self.motor1.motorpin1.write_digital(0)
        self.motor1.motorpin2.write_digital(1)
        self.motor1.motorpwmpin.write_analog(self.__speed)

        self.motor2.motorpin1.write_digital(0)
        self.motor2.motorpin2.write_digital(1)
        self.motor2.motorpwmpin.write_analog(self.__speed)

    def turnLeft(self):
        self.motor1.motorpwmpin.write_analog(0)
        self.motor2.motorpwmpin.write_analog(self.__speed)

    def turnRight(self):
        self.motor1.motorpwmpin.write_analog(self.__speed)
        self.motor2.motorpwmpin.write_analog(0)

    def spin(self):
        self.motor1.motorpin1.write_digital(1)
        self.motor1.motorpin2.write_digital(0)
        self.motor1.motorpwmpin.write_analog(self.__speed)

        self.motor2.motorpin1.write_digital(0)
        self.motor2.motorpin2.write_digital(1)
        self.motor2.motorpwmpin.write_analog(self.__speed)

    def stop(self):
        self.motor1.motorpwmpin.write_analog(0)
        self.motor2.motorpwmpin.write_analog(0)
