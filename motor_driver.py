from microbit import *
from motor import *

class Motordriver:
    def __init__(self, motor1Pin1, motor1Pin2, min1, max1,
                 motor2Pin1, motor2Pin2, min2, max2, speed=0):
        self.motor1 = Motor(motor1Pin1, motor1Pin2, min1, max1)
        self.motor2 = Motor(motor2Pin1, motor2Pin2, min2, max2)
        self.__speed = self.setspeed(speed)

    @property
    def speed(self):
        return self.__speed

    def setspeed(self, speed):
        if self.motor1.minval <= speed <= self.motor1.maxval and self.motor2.minval <= speed <= self.motor2.maxval:
            return speed
        else:
            print("Speed moet tussen minVal en maxVal zijn")
            return None

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def forward(self, speed):
        self.__speed = speed
        self.motor1.forward(self.__speed)
        self.motor2.forward(self.__speed)

    def backward(self, speed):
        self.__speed = speed
        self.motor1.backward(self.__speed)
        self.motor2.backward(self.__speed)

    def turnLeft(self, speed):
        self.__speed = speed
        self.motor1.stop()
        self.motor2.forward(self.__speed)

    def turnRight(self, speed):
        self.__speed = speed
        self.motor1.forward(self.__speed)
        self.motor2.stop()

    def spin(self, speed):
        self.__speed = speed
        self.motor1.forward(self.__speed)
        self.motor2.backward(self.__speed)

    def stop(self):
        self.motor1.stop()
        self.motor2.stop()