# 🚗 Autootje & Remote Cheatsheet

Voor gebruik met de `autotje`, `motor_driver`, `motor` en `radio_com` bibliotheken op de Micro\:bit.

---

## 📁 Bestanden

* `autotje.py`: Regelt auto en afstandsbediening
* `motor.py`: Stuurt één motor aan
* `motor_driver.py`: Combineert twee motoren
* `radio_com.py`: Radio communicatie
* `main.py`: Start het programma
* `demo_code.py`: Voorbeeld code

---

## 1. Demo code
In `demo_code.py` kan je een voorbeeld vinden over hoe je de module moet gebruiken.

## 2. Autootje (ontvanger)

Gebruik dit op de Microbit in het autootje. Deze ontvangt signalen en stuurt de motoren aan.

### Instellingen

* **motorXPinY**: geeft aan welke pinnen verbonden zijn met de motoren
* **speed**: snelheid van de auto (0–100)
* **channel**: radiokanaal voor communicatie (0–80)

De functie `Simple_remote_control()` zorgt dat het autootje automatisch luistert naar afstandsbediening.

---

## 3. Afstandsbediening (zender)

Gebruik dit op een tweede Microbit. Hiermee stuur je het autootje aan.

### 🎮 Besturing

* **Touch logo**: vooruit rijden
* **Knoppen A + B**: achteruit rijden
* **Knop A**: linksom draaien
* **Knop B**: rechtsom draaien

De `update()` functie kijkt telkens of een knop is ingedrukt en stuurt het juiste signaal naar het autootje.
Het signaal is een lijst van 3 bits `[0,1,0]`.
De waarde van elke bit komt overeen met de status van de knoppen.
`[touch_logo, links, rechts]`

---

## 4. Extra functies

### 📡 Radio

* Je kunt het radiokanaal aanpassen als meerdere groepjes tegelijk werken
* Zet radio aan of uit met `RadioCom.on()` en `RadioCom.off()`

### ⚙️ Motor testen

* Je kunt een motor apart testen door hem handmatig aan te sturen (vooruit, achteruit, stop)
* Instelbare snelheid en schaalfactor
* Bijvoorbeeld:
  
```python
from motor import Motor

m = Motor(pin1, pin2,speed = 80, speedscalingf = 90)
m.forward()
m.backward()
m.stop()
m.speed = 80
m.speedscalingf = 90
```

### 🔁 Motordriver

* De motordriver stuurt twee motoren tegelijk aan
* Je kunt deze laten rijden, draaien of stoppen

  ```python
  from motor_driver import Motordriver

  driver = Motordriver(pin1, pin2, pin8, pin12)

  driver.forward()
   ```

---

## 5. Debug & Tips

* `autotje.help()` toont uitleg op de Microbit

### ⚠️ Belangrijke aandachtspunten

* Gebruik nooit twee keer dezelfde pin voor verschillende motoren
* Vermijd pin3, pin4, pin6, pin7, pin10 (die zijn gereserveerd voor display)
* Gebruik pin12 niet (gereserveerd intern)
* Radiokanaal moet tussen 0 en 80 liggen
* Snelheid en schaalfactor moeten tussen 0 en 100 liggen
