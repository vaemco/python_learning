"""
Purpose: Simulate a password prompt using a while loop.
Status: Educational / Completed
Topics: Loops, Input Handling
"""

# While-Loop: keep asking until the password is correct
password = "secret"
user_input = ""

while user_input != password:
    user_input = input("Bitte Passwort eingeben: ")
    if user_input != password:
        print("Falsches Passwort, versuch es nochmal!")

print("Zugang gewährt!")
