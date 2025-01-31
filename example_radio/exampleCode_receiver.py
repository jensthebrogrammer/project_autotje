from microbit import *
import radio

radio.on()  # Turn on the radio
radio.config(channel=7)  # Set the same channel as the sender

while True:
    message = radio.receive()  # Check for messages
    if message:
        display.show("R")  # Show "R" to indicate received
        sleep(500)
        display.clear()
