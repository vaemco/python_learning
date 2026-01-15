import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]) # Ab 7 Stunden besteht man

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# 5. Der Vergleich (Printen)
print("--- Die Prüfung ---")
print(f"Schüler mit Stunden: \n{X_test.flatten()}") # .flatten() macht es flach für schönere Optik
print(f"Echte Lösung (y_test): {y_test}")
print(f"KI Vorhersage:         {predictions}")

# Zusatz: Hat es gestimmt?
if np.array_equal(y_test, predictions):
    print("--> Perfekt! Alle richtig vorhergesagt.")
else:
    print("--> Da waren Fehler drin.")