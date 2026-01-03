# Python Phase 1: Cheatsheet 🐍

## 1. Basics

```python
# Variablen
age = 21           # Integer
price = 19.99      # Float
name = "Valen"     # String
is_active = True   # Boolean

# Output
print(f"Hallo {name}")  # f-String (Beste Variante!)
```

---

## 2. Listen (Lists)

Geordnete Sammlung, veränderbar.

```python
models = ["A", "B", "C"]
models.append("D")      # Hinzufügen
first = models[0]       # Erstes Element
last = models.pop()     # Letztes entfernen & holen
```

---

## 3. Dictionaries (Dicts)

Key-Value Paare. Wichtig für Configs.

```python
config = {"lr": 0.01, "optimizer": "Adam"}
print(config["lr"])           # Zugriff (Crashgefahr wenn fehlt)
print(config.get("epochs"))   # Sicherer Zugriff (None wenn fehlt)
```

---

## 4. Loops & Logic

```python
# For Loop (Standard)
for model in models:
    if model == "A":
        print("Winner")
    else:
        print("Loser")

# List Comprehension (Profi-Loop)
# [WAS_TUN for VARIABLE in LISTE]
squared = [x**2 for x in [1, 2, 3]]
```

---

## 5. Funktionen

```python
def calculate_loss(pred, real):
    return abs(pred - real)  # Return gibt Wert zurück!

result = calculate_loss(10, 12)
```

---

## 6. Error Handling (Try/Except)

Verhindert Abstürze.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Nicht durch 0 teilen!")
except Exception as e:
    print(f"Anderer Fehler: {e}")
```

---

## 7. File I/O

Speichern und Laden.

```python
# "w" = Schreiben (Write), "a" = Anhängen (Append), "r" = Lesen (Read)
with open("log.txt", "w") as file:
    file.write("Training finished\n")  # \n für neue Zeile
```

---

## 8. Klassen (OOP)

Baupläne für Objekte.

```python
class Model:
    # Der Konstruktor (startet automatisch)
    def __init__(self, name):
        self.name = name    # Attribut speichern

    # Methode
    def train(self):
        print(f"{self.name} trainiert...")

# Objekt erstellen (Instanz)
my_model = Model("GPT-4")
my_model.train()
```


