rohdaten = [
    {"id": 1, "umsatz": 100, "kosten": 50},  # Gut
    {"id": 2, "umsatz": 200, "kosten": "n/a"},  # Fehler: Text
    {"id": 3, "umsatz": 300, "kosten": 0},  # Fehler: Division durch 0
    {"id": 4, "umsatz": 150, "kosten": 10},  # Gut
    {"id": 5},  # Fehler: Keys fehlen
]


# Try/Except, um schmutzige Datensätze zu überspringen
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
