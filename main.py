from microbit import *


# dit is een simpele test code om te demonstreren hoe je deze module moet gebruiken
def test_met_autotje():
    from autotje import Autotje

    # het declareren van autotje met de juiste pins
    auto = Autotje(pin2, pin3, 0, 255, pin1, pin0, 0, 255, channel=1)
    while True:
        # het enige wat je hoeft te doen is de functie oproepen in een loop
        auto.Simple_remote_control()


# dit is een simpele voorbeeld code om te module voor de afstandsbediening te gebruiken
def remote_controller():
    from remote import Remote

    # het default channel is 1
    my_remote = Remote()
    while True:
        # update leest alle knoppen binnen verstuurd deze via radio
        my_remote.update()
        display.show("S")


test_met_autotje()
