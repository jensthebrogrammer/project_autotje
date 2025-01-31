from microbit import *
import radio
radio.on() # Turn on the radio
radio.config(channel=7) # Set a channel (0-100)
while True:
    if button_a.was_pressed():
        radio.send("Hello!") # Send a message
        display.show("S") # Show "S" to indicate sending
        sleep(500)
        display.clear()