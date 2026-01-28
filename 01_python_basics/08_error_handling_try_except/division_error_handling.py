"""
Purpose: Handling division by zero and type errors using try/except.
Status: Educational / Completed
Topics: Exceptions, Error Handling
"""

eingaben = ["10", "5", "hallo", "20", "0"]

# Try/Except catches two typical errors: wrong type and division by zero
for raw_value in eingaben:
    try:
        number = int(raw_value)
        ergebnis = 100 / number
    except ValueError:
        print(f"Fehler bei Wert (kein int): {raw_value}")
    except ZeroDivisionError:
        print("Division durch 0 ist nicht erlaubt.")
    else:
        print(f"Ergebnis: {ergebnis}")
