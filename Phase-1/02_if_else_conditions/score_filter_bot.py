# If/Else in einem Loop: Scores durchgehen und markieren
threshold = 0.8
scores = [0.95, 0.2, 0.85, 0.55, 0.1]

for score in scores:
    if score < threshold:
        print(f"Score {score} ist zu niedrig. Löschen! ❌")
    else:
        print(f"Score {score} ist hoch genug. Behalten! ✅")
