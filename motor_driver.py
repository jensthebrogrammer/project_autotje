from microbit import *
from motor import *

class Motordriver:
    def __init__(self, motorpwmpin1, motorpwmpin2, speed=0):
        self.motor1 = Motor(1, 2, 0, 255 )
        self.motor2 = Motor(4, 5, 0, 255)
        self.__speed = self.setspeed(speed)
        self.__motorPwmPin1 = motorpwmpin1
        self.__motorPwmPin2 = motorpwmpin2

    ###########################################################################################
    # MOTORPWMPIN1

    @property
    def motorpwmpin1(self):
        return self.__motorPwmPin1

    @motorpwmpin1.setter
    def motorpwmpin1(self, motorPwmPin1):
        VALID_PINS = [pin0, pin1, pin2, pin8, pin12, pin13, pin14, pin15, pin16]
        if motorPwmPin1 in VALID_PINS:
            self.__motorPwmPin1 = motorPwmPin1
        else:
            print("Kies een geldige PWM pin (pin0, pin1, pin2, pin8, pin12, pin13, pin14, pin15, pin16)")


###########################################################################################
    # MOTORPWMPIN2

    @property
    def motorpwmpin2(self):
        return self.__motorPwmPin2

    @motorpwmpin2.setter
    def motorpwmpin2(self, motorPwmPin2):
        VALID_PINS = [pin0, pin1, pin2, pin8, pin12, pin13, pin14, pin15, pin16]
        if motorPwmPin2 in VALID_PINS:
            self.__motorPwmPin2 = motorPwmPin2
        else:
            print("Kies een geldige PWM pin (pin0, pin1, pin2, pin8, pin12, pin13, pin14, pin15, pin16)")

    @property
    def speed (self):
        return self.__speed


    def setspeed (self, speed):
        if self.motor1.minval <= speed <= self.motor1.maxval and self.motor2.minval <= speed <= self.motor2.maxval :
            return speed
        else:
            print("Speed moet tussen minVal en maxVal zijn")
            return None


    @speed.setter
    def speed(self, speed):
        self.__speed = speed


    def forward(self):
        self.motor1.forward(self.__speed)
        self.motor2.forward(self.__speed)

    def backward(self):
        self.motor1.backward(self.__speed)
        self.motor2.backward(self.__speed)

    def turnLeft(self):
        self.motor1.stop()
        self.motor2.forward(self.__speed)

    def turnRight(self):
        self.motor1.forward(self.__speed)
        self.motor2.stop()

    def spin(self):
        self.motor1.forward(self.__speed)
        self.motor2.backward(self.__speed)

    def stop(self):
        self.motor1.stop()
        self.motor2.stop()
