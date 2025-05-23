```mermaid
classDiagram
    namespace microbit1 {
        class Autotje {
            - com: RadioCom
            - driver: Motordriver
            - __speed
            + Simple_remote_control()
        }

        class Motor {
            - __motorPin1
            - __motorPin2
            - __speed
            - __speedscalingf
            - __speedSignal
            + forward()
            + backward()
            + stop()
            <<class attribute>> __display_pins
            <<class attribute>> UNVALID_PINS
            <<class attribute>> __all_pins
        }
        
        class Motordriver {
            - motor1: Motor
            - motor2: Motor
            - __speed
            + forward()
            + backward()
            + turnLeft()
            + turnRight()
            + spinLeft()
            + spinRight()
            + stop()
        }

        class RadioCom {
            - __channel
            - received
            + read_channel()
            + write(message)
            + on()
            + off()
        }
    }

    namespace microbit2 {
        class Remote {
            - __btnT
            - __btnA
            - __btnB
            + update()
        }
    }

    Autotje *-- RadioCom 
    Autotje *-- Motordriver 
    Motordriver *-- Motor 
    Remote <|-- RadioCom



 ```
