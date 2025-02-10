```mermaid
classDiagram
    namespace microbit1 {
        class Autootje {
            
            + drive()
            + turn()
            + stop()
            + setSpeed()
            + receiveCommand()
            
        }

        class Motor {
            - motorPin1
            - motorPin2
            - minVal
            - maxVal
            + forward()
            + backward()
        }
        
        class MotorDriver {
            - speed
            - motor1
            - motor2
            + turnLeft()
            + turnRight()
            + forward()
            + backward()
            + spin()
            + stop()
        }

        class RadioCom {
            - channel
            - recieved
            + read_channel()
            + setChannel()
            + write()
        }
    }

    namespace microbit2 {
        class Remote {
            - btnPin1
            - btnPin2
            - btnPin3
            - btnPin4
            + update()
        }
    
        class Button {
            - buttonPin
            - lastTimeStateChanged
            + readState()
            + isPressed()
            
        }
    }

    Autootje *-- RadioCom
    Autootje <|-- MotorDriver
    RadioCom --|> Remote
    Remote *-- Button
    Motor --* MotorDriver

```
