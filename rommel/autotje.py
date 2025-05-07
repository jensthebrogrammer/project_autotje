from microbit import *
from rommel.radio_com import RadioCom as Com
from rommel.motor_driver import Motordriver as Driver


class Autotje:
    def __init__(self, motor1Pin1, motor1Pin2, min1, max1,
                 motor2Pin1, motor2Pin2, min2, max2, speed=0, channel=1):
        # de radio declareren
        self.com = Com(channel)

        # de motordriver initializeren
        self.driver = Driver(motor1Pin1, motor1Pin2, min1, max1,
                            motor2Pin1, motor2Pin2, min2, max2, speed=speed)


    def Simple_remote_control(self):
        # instructies binnen lezen
        self.com.read_channel()

        # als er iets ontvangen is zet dit stukje het om naar een lijst
        # zoniet worden alle waardes op nul gezet
        # dan beweegt de auto dus niet
        if self.com.received:
            received_list = list(self.com.received)
        else:
            received_list = [0, 0, 0]

        # dit gedeelte zet de lijst met bits om in bewegingen
        if int(received_list[0]):
            self.driver.forward(255)

        # als de bestuurder naar beide kanten stuurt zal hij beginnen draaien
        elif int(received_list[1]) and int(received_list[2]):
            self.driver.spin(255)

        elif int(received_list[1]):
            self.driver.turnLeft(255)

        elif int(received_list[2]):
            self.driver.turnRight(255)

        # als er geen signaal is zal de auto stoppen
        else:
            self.driver.stop()
