alle_scores = [0.95, 0.2, 0.85, 0.55, 0.1]


def check_score(score, threshold=0.8):
    """Gibt ein Ergebnis-Label zurück, statt direkt zu drucken."""
    if score >= threshold:
        return "Behalten"
    return "Löschen"


for score in alle_scores:
    ergebnis = check_score(score)
    print(f"Score {score}: {ergebnis}")
