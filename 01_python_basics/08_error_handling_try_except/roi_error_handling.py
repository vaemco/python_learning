"""
Purpose: Calculating ROI with robust error handling for bad data.
Status: Educational / Completed
Topics: Exceptions, Dictionaries, Arithmetic
"""

rohdaten = [
    {"id": 1, "umsatz": 100, "kosten": 50},  # Good
    {"id": 2, "umsatz": 200, "kosten": "n/a"},  # Error: Text
    {"id": 3, "umsatz": 300, "kosten": 0},  # Error: Division by 0
    {"id": 4, "umsatz": 150, "kosten": 10},  # Good
    {"id": 5},  # Error: Keys missing
]


# Try/Except to skip dirty datasets
def berechne_roi(datensatz):
    return datensatz["umsatz"] / datensatz["kosten"]


saubere_ergebnisse = []

for daten in rohdaten:
    try:
        roi_wert = berechne_roi(daten)
    except (KeyError, TypeError, ZeroDivisionError):
        print(f"Achtung: Fehler bei ID {daten.get('id', 'unbekannt')}")
    else:
        ergebnis_paket = {"id": daten["id"], "roi": roi_wert}
        saubere_ergebnisse.append(ergebnis_paket)

print(f"Saubere Ergebnisse: {saubere_ergebnisse}")
