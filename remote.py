from microbit import *
from radio_com import RadioCom as Com
from push_button import PushButton as Btn
import json


class Remote(Com):
    def __init__(self, pinT, pinB, pinL, pinR, pull_up=False, channel=1):
        # declaring super for inheritance
        super().__init__(channel)

        # declaring every button
        self._btnT = Btn(pinT, pull_up=pull_up)
        self._btnB = Btn(pinB, pull_up=pull_up)
        self._btnL = Btn(pinL, pull_up=pull_up)
        self._btnR = Btn(pinR, pull_up=pull_up)

        # turn the radio on
        self.on()

    # reading the buttons and sending the correct message
    def update(self):
        # the function write sends it via the radio channel
        self.write(json.dumps({
            "topButton": self._btnT.is_pressed(),
            "bottomButton": self._btnB.is_pressed(),
            "leftButton": self._btnL.is_pressed(),
            "rightButton": self._btnR.is_pressed()
        }))
