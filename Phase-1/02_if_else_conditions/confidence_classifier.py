"""
Purpose: Simple threshold decision using if/else.
Status: Educational / Completed
Topics: Control Flow, Logic
"""

# If/Else: Simple threshold decision
confidence = 0.9
threshold = 0.8

if confidence >= threshold:
    print("Das Modell ist sicher: Das ist eine Katze.")
else:
    print("Das Modell ist unsicher: besser noch mal prüfen.")
