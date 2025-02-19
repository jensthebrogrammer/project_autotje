from microbit import *
import radio


class RadioCom:
    def __init__(self, channel=1):
        # set the channel to a valid channel number
        self.channel = channel
        # received is for when the user wants to know the last thing RadioCom received
        # if you just run read_channel you only get what is currently being received
        self.received = None

    @property
    def channel(self):
        return self.__channel

    @channel.setter
    def channel(self, channel):
        # making sure the channel is within the right range
        if channel in range(80):
            self.__channel = channel
        else:
            print("the channel is not valid")
            # the default channel
            self.__channel = 1

        # setting the radio
        radio.config(self.channel)

    def read_channel(self):
        # reads the channel and returns the found data
        self.received = radio.receive()
        return self.received

    # to write to the channel
    @staticmethod
    def write(message):
        radio.send(message)

    # a static method is a method that doesn't require self to operate
    @staticmethod
    def on():
        radio.on()

    @staticmethod
    def off():
        radio.off()
