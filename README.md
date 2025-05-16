# 🚗 Autootje & Remote Cheatsheet

Voor gebruik met de `autotje`, `motor_driver`, `motor`, en `radio_com` bibliotheek op de Micro:bit.

---

## 📁 Structuur van de bibliotheek

- `autotje.py`: Hoofdlogica voor voertuig en afstandsbediening  
- `motor.py`: Controle van een enkele motor  
- `motor_driver.py`: Twee motoren combineren voor beweging  
- `radio_com.py`: Communicatie via radio  
- `main.py`: Startcode om alles te laten draaien  

---

## 1. Autootje gebruiken (ontvanger)

Gebruik dit op de Microbit in het autootje:

```python
from autotje import Autotje

auto = Autotje(
    motor1Pin1=pin2,
    motor1Pin2=pin8,
    motor2Pin1=pin1,
    motor2Pin2=pin0,
    speedscalingfactorf1=100,
    speedscalingfactorf2=100,
    speed=100,
    channel=1
)
```

### 🔧 Parameters

- `motorXPinY`: Motorpinconfiguratie  
- `speed`: snelheid (0–100)  
- `channel`: radiokanaal (0–80)  

---

## 2. Afstandsbediening gebruiken (zender)

Gebruik dit op een tweede Microbit als remote:

```python
from autotje import Remote

remote = Remote(channel=1)

while True:
    remote.update()
```

### 🔘 Knoppen

- Touch logo: vooruit  
- Knop A + B samen: achteruit  
- Knop A: spin links  
- Knop B: spin rechts  

---

## 3. Extra functies & instellingen

### 📡 Radio instellen

```python
remote.channel = 5
RadioCom.on()
RadioCom.off()
```

### ⚙️ Motor handmatig testen

```python
from motor import Motor

m = Motor(pin1, pin2)
m.forward()
m.backward()
m.stop()
m.speed = 80
m.speedscalingf = 90
```

### 🔁 Motordriver handmatig gebruiken

```python
from motor_driver import Motordriver

driver = Motordriver(pin1, pin2, pin8, pin12)
driver.forward()
driver.spinLeft()
driver.turnRight()
driver.stop()
```

---

## 4. Debug & hulp

```python
import autotje
autotje.help()
```

---

## ⚠️ Belangrijke aandachtspunten

- Gebruik niet twee keer dezelfde pin voor een motor.  
- Vermijd display-pinnen: `pin3`, `pin4`, `pin6`, `pin7`, `pin10`.  
- `pin12` is gereserveerd (`UNVALID_PINS`).  
- Radiokanaal moet tussen 0 en 80 liggen.  
- `speed` en `speedscalingf` moeten tussen 0 en 100 liggen.  
- Gebruik `panic(code)` om fouten visueel te tonen op de Microbit.  
