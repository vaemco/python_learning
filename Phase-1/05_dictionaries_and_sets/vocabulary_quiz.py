"""
Purpose: Simple vocabulary quiz application.
Status: Educational / Completed
Topics: Dictionaries, Loops, Input
"""

# Mini Vocabulary Trainer: Dictionary + Loop + Input
vokabel = {
    "Haus": "house",
    "Baum": "tree",
    "Wasser": "water",
    "Feuer": "fire",
    "Erde": "earth",
}

score = 0

for german, english in vokabel.items():
    ask = input(f"Was ist die englische Übersetzung von '{german}'? ")
    if ask.strip().lower() == english.lower():
        score += 1
        print("Richtig! ✅")
    else:
        print(f"Falsch! ❌ Die richtige Antwort ist '{english}'.")

print("Vokabeltest beendet!")
print(f"Dein Score war: {score}")
