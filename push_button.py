from microbit import *


class PushButton:
    DEBOUNCE_DELAY = 50

    def __init__(self, button_pin, pull_up=False, debounce=False):
        self.__button_pin = self.set_btn_pin(button_pin)
        self.pull_up = pull_up
        self.debounce = debounce
        self.lastTimeStateChanged = running_time()

        if pull_up:
            self.button_pin.set_pull(self.button_pin.PULL_UP)

        self.state = self.button_pin.read_digital()

    @property
    def button_pin(self):
        return self.__button_pin

    @button_pin.setter
    def button_pin(self, pin):
        self.__button_pin = self.set_btn_pin(pin)

    @staticmethod
    def set_btn_pin(pin):
        valid_pins = [pin0, pin1, pin2,
                      pin4, pin6, pin7,
                      pin8, pin9, pin10,
                      pin12, pin13, pin14,
                      pin15, pin16]

        if pin in valid_pins:
            return pin
        else:
            print("the pin for this button is invalid")
            return None

    def read_state(self):
        if self.debounce:
            t_0 = running_time()
            if t_0 - self.lastTimeStateChanged > PushButton.DEBOUNCE_DELAY:
                self.state = self.button_pin.read_digital()
                self.lastTimeStateChanged = running_time()
        else:
            self.state = self.button_pin.read_digital()

        return self.state == 1

    def is_pressed(self):
        if self.pull_up:
            return not self.read_state()
        else:
            return self.read_state()
