from microbit import *


class PushButton:
    DEBOUNCE_DELAY = 50

    def __init__(self, button_pin, pull_up=False, debounce=False):
        self.button_pin = button_pin
        self.pull_up = pull_up
        self.debounce = debounce
        self.lastTimeStateChanged = running_time()

        if pull_up:
            self.button_pin.set_pull(self.button_pin.PULL_UP)

        self.state = self.button_pin.read_digital()

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
