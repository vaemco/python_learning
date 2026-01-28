"""
Purpose: Filtering scores using a helper function.
Status: Educational / Completed
Topics: Functions, Return Values, Loops
"""

alle_scores = [0.95, 0.2, 0.85, 0.55, 0.1]


def check_score(score, threshold=0.8):
    """Returns a result label instead of printing directly."""
    if score >= threshold:
        return "Behalten"
    return "Löschen"


for score in alle_scores:
    ergebnis = check_score(score)
    print(f"Score {score}: {ergebnis}")
