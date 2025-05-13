```mermaid
classDiagram
    class Autotje {
        - Com com
        - Driver driver
        - int __speed
        + speed
        + speed=value
        + Simple_remote_control()
    }

    class Motordriver {
        - Motor motor1
        - Motor motor2
        - int __speed
        + speed
        + speed=value
        + forward()
        + backward()
        + turnLeft()
        + turnRight()
        + spinLeft()
        + spinRight()
        + stop()
    }

    class Motor {
        - motorPin1
        - motorPin2
        - speed
        - speedscalingf
        - speedSignal
        + speed
        + speed=value
        + speedscalingf
        + speedscalingf=value
        + forward()
        + backward()
        + stop()
    }

    class RadioCom {
        - int __channel
        + received
        + channel
        + channel=value
        + read_channel()
        + write(message)
        + on()
        + off()
    }

    class Remote {
        - pin _btnT
        - pin _btnA
        - pin _btnB
        + update()
    }

    %% Relaties
    Autotje --> RadioCom : gebruikt
    Autotje --> Motordriver : gebruikt
    Motordriver --> Motor : bevat
    Remote --|> RadioCom : erft van

 ```
