from microbit import *

class Motordriver:
    def __init__(self, motorPin1, motorPin2, minVal, maxVal):
        self.motorPin1 = motorPin1
        self.motorPin2 = motorPin2
        self.__minVal = minVal
        self.__maxVal = maxVal

    @property
    def minVal(self):
        return self.__minVal  # Correcte referentie naar het attribuut

    @minVal.setter
    def minValSetter(self, minVal):
        if minVal in range(255):
            self.__minVal = minVal
        else:
            print("minVal moet tussen 0 en 255 liggen")
