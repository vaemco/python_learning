"""
Purpose: Simulating random scores and checking them against a threshold.
Status: Educational / Completed
Topics: Functions, Default Arguments, Random Module
"""

import random


def check_score(score, threshold=0.8):
    """Decides based on a threshold."""
    return "Behalten" if score >= threshold else "Löschen"


simulierte_scores = [random.random() for _ in range(5)]
print("Simulierte Scores:", simulierte_scores)

for score in simulierte_scores:
    ergebnis = check_score(score)
    print(f"KI sagt zu {score:.2f}: {ergebnis}")
