# While-Loop: so lange fragen, bis das Passwort stimmt
password = "secret"
user_input = ""

while user_input != password:
    user_input = input("Bitte Passwort eingeben: ")
    if user_input != password:
        print("Falsches Passwort, versuch es nochmal!")

print("Zugang gewährt!")
