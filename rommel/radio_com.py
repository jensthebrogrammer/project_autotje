from microbit import *
import radio


class RadioCom:
    def __init__(self, channel=1):
        # set the channel to a valid channel number
        self.__channel = self.set_channel(channel)
        # received is for when the user wants to know the last thing RadioCom received
        # if you just run read_channel you only get what is currently being received
        self.received = None

    @property
    def channel(self):
        return self.__channel

    @channel.setter
    def channel(self, channel):
        self.__channel = self.set_channel(channel)

        # setting the radio
        radio.config(self.channel)

    @staticmethod
    def set_channel(channel):
        # making sure the channel is within the right range
        if channel in range(80):
            return channel
        else:
            print("the channel is not valid")
            # the default channel
            return 1

    def read_channel(self):
        # reads the channel and returns the found data
        # it also stores it in received for ease of use
        self.received = radio.receive()

        # the delay is needed because otherwise the receiver will try to read to quickly
        # this will result in the microbit sometimes doing unexpected tings
        sleep(10)

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