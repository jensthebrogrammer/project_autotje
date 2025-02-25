from microbit import *

class Motor:
    def __init__(self, motorPin1, motorPin2, minVal, maxVal):
        display.off
        self.__motorPin1 = motorPin1
        self.__motorPin2 = motorPin2
        self.__minVal = minVal
        self.__maxVal = maxVal

    #########################################################################################
    # MINVAL
    @property
    def minval(self):
        return self.__minVal

    @minval.setter
    def minval(self, minVal):
        if 0 <= minVal <= 255:
            self.__minVal = minVal
        else:
            print("minVal moet tussen 0 en 255 liggen")

    #########################################################################################
    # MAXVAL
    @property
    def maxval(self):
        return self.__maxVal

    @maxval.setter
    def maxval(self, maxVal):
        if 0 <= maxVal <= 255:
            self.__maxVal = maxVal
        else:
            print("maxVal moet tussen 0 en 255 liggen")


    ##################################################################################################
    # MOTORPIN1
    @property
    def motorpin1(self):
        return self.__motorPin1

    @motorpin1.setter
    def motorpin1(self, motorPin1):
        VALID_PINS = [pin0, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10, pin11, pin12, pin13, pin14, pin15, pin16]
        if motorPin1 in VALID_PINS:
            self.__motorPin1 = motorPin1
        else:
            print("Kies een geldige pin voor motorPin1")

    ##################################################################################################
    # MOTORPIN2
    @property
    def motorpin2(self):
        return self.__motorPin2

    @motorpin2.setter
    def motorpin2(self, motorPin2):
        VALID_PINS = [pin0, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10, pin11, pin12, pin13, pin14, pin15, pin16]
        if motorPin2 in VALID_PINS:
            self.__motorPin2 = motorPin2
        else:
            print("Kies een geldige pin voor motorPin2")
