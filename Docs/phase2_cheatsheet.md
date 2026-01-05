# Python Phase 2: Cheatsheet

## 1. Slicing & Comprehensions

Schnelles Filtern und Transformieren.

```python
nums = [0, 1, 2, 3, 4, 5]
middle = nums[1:5:2]   # start:stop:step -> [1, 3]
rev = nums[::-1]       # Rueckwaerts

squares = [x * x for x in nums if x % 2 == 0]
pairs = {x: x * x for x in nums}
unique = {x % 3 for x in nums}
```

---

## 2. Tuples & Sets

Tuple = unveraenderbar, Set = einzigartig.

```python
point = (3, 5)
x, y = point

tags = {"ml", "python", "ml"}
tags.add("data")
common = tags.intersection({"python", "java"})
```

---

## 3. Funktionen Advanced

`*args` sammelt Positional, `**kwargs` sammelt Keywords.

```python
def scale(x, factor=1.0, *extras, **opts):
    return x * factor

def apply(fn, value):
    return fn(value)

double = lambda n: n * 2
result = apply(double, 10)
```

---

## 4. Module & Packages

Sauberes Strukturieren und wiederverwenden.

```python
import math as m
from pathlib import Path

def main():
    print(m.sqrt(9))
    print(Path(".").resolve())

if __name__ == "__main__":
    main()
```

---

## 5. Virtual Envs & Pip (Windows)

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install requests
pip freeze > requirements.txt
```

---

## 6. Dateien & Pfade (pathlib)

```python
from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

path = data_dir / "note.txt"
path.write_text("ok\n", encoding="utf-8")
text = path.read_text(encoding="utf-8")
```

---

## 7. JSON & CSV

```python
import json
import csv

payload = {"lr": 0.01, "epochs": 5}
with open("config.json", "w") as f:
    json.dump(payload, f, indent=2)

with open("data.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"])
```

---

## 8. Iterators & Generators

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(3):
    print(i)

it = iter([1, 2, 3])
first = next(it)
```

---

## 9. OOP Advanced

Vererbung, Properties und Classmethods.

```python
class BaseModel:
    kind = "base"

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @classmethod
    def from_default(cls):
        return cls("default")

class LinearModel(BaseModel):
    kind = "linear"

    def __init__(self, name, lr):
        super().__init__(name)
        self.lr = lr
```

---

## 10. Typing & Dataclasses

```python
from dataclasses import dataclass
from typing import List

@dataclass
class Batch:
    size: int
    labels: List[str]

def total(n: int, m: int) -> int:
    return n + m
```
