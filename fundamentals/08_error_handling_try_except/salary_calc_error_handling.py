mitarbeiter_liste = [
    {"name": "Ali", "stunden": 40, "lohn": 20},  # Standard
    {"name": "Bea", "stunden": 50, "lohn": 25},  # Überstunden!
    {"name": "Chris", "stunden": 0, "lohn": 20},  # War im Urlaub (0 Stunden)
    {"name": "Dave", "stunden": "40", "lohn": 20},  # Fehler: Text statt Zahl
    {"name": "Eddy", "lohn": 15},  # Fehler: Stunden fehlen ganz
]


# Try/Except, um fehlerhafte Gehaltsdaten zu überspringen
def berechne_gehalt(mitarbeiter):
    stunden = mitarbeiter["stunden"]
    lohn = mitarbeiter["lohn"]
    if not isinstance(stunden, (int, float)) or not isinstance(lohn, (int, float)):
        raise TypeError("Stunden und Lohn müssen Zahlen sein.")

    if stunden > 40:
        ueberstunden = stunden - 40
        zahlung = (40 * lohn) + (ueberstunden * lohn * 2)
    else:
        zahlung = stunden * lohn
    return zahlung


auszahlungen = []

for mitarbeiter in mitarbeiter_liste:
    try:
        zahlung = berechne_gehalt(mitarbeiter)
        auszahlungen.append({"name": mitarbeiter["name"], "zahlung": zahlung})
    except (KeyError, TypeError) as error:
        print(f"Konnte Gehalt für {mitarbeiter.get('name', 'Unbekannt')} nicht berechnen: {error}")

print(f"Auszahlungen: {auszahlungen}")
