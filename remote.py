from microbit import *
from radio_com import RadioCom as Com


class Remote(Com):
    def __init__(self, channel=1):
        # declaring super for inheritance
        super().__init__(channel)

        # declaring every button
        self._btnT = pin_logo
        self._btnA = pin5
        self._btnB = pin11

        # turn the radio on
        self.on()

    # reading the buttons and sending the correct message
    def update(self):
        # the function write sends it via the radio channel

        # the message sends a string of bits (010 for example). 0 means not pressed. the order is top, left, right
        message = str(int(self._btnT.is_touched())) + str(int(not self._btnA.read_digital())) + str(
            int(not self._btnB.read_digital()))

        self.write(message)
