from microbit import *


class Motor:
    def __init__(self, motorPin1, motorPin2, minVal, maxVal):
        display.off()
        self.__motorPin1 = motorPin1
        self.__motorPin2 = motorPin2

        # minVal en maxVal zijn er om de motoren te kunnen calibreren
        # op deze manier kunnen 2 motoren op exact dezelfde snelheid draaien
        self.__minVal = minVal
        self.__maxVal = maxVal

    def forward(self, speed):
        """Laat de motor vooruit draaien met een gegeven snelheid."""
        if self.__minVal <= speed <= self.__maxVal:
            self.__motorPin1.write_analog(speed)
            self.__motorPin2.write_digital(0)
        else:
            print("Snelheid moet tussen minVal en maxVal liggen.")

    def backward(self, speed):
        """Laat de motor achteruit draaien met een gegeven snelheid."""
        if self.__minVal <= speed <= self.__maxVal:
            self.__motorPin1.write_digital(0)
            self.__motorPin2.write_analog(speed)
        else:
            print("Snelheid moet tussen minVal en maxVal liggen.")

    def stop(self):
        self.__motorPin1.write_digital(0)
        self.__motorPin2.write_digital(0)


    @property
    def minval(self):
        return self.__minVal

    @minval.setter
    def minval(self, minVal):
        if 0 <= minVal <= 255:
            self.__minVal = minVal
        else:
            print("minVal moet tussen 0 en 255 liggen.")

    @property
    def maxval(self):
        return self.__maxVal

    @maxval.setter
    def maxval(self, maxVal):
        if 0 <= maxVal <= 255:
            self.__maxVal = maxVal
        else:
            print("maxVal moet tussen 0 en 255 liggen.")

    @property
    def motorpin1(self):
        return self.__motorPin1

    @motorpin1.setter
    def motorpin1(self, motorPin1, motorPin2):
        UNVALID_PINS = [motorPin2]
        if motorPin1 in UNVALID_PINS:

            print("Kies een geldige pin voor motorPin1.")
        else:
            self.__motorPin1 = motorPin1


    @property
    def motorpin2(self):
        return self.__motorPin2

    @motorpin2.setter
    def motorpin2(self, motorPin1, motorPin2):
        UNVALID_PINS = [motorPin1]
        if motorPin2 in UNVALID_PINS:
            print("Kies een geldige pin voor motorPin2.")
        else:
            self.__motorPin2 = motorPin2
