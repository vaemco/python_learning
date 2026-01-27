"""
Purpose: Iterating through a list of dictionaries with condition checking.
Status: Educational / Completed
Topics: Loops, Conditionals, Dictionaries
"""

# List of dictionaries with an If/Else selection
ergebnisse = [
    {"name": "GPT-4", "accuracy": 0.95},
    {"name": "Llama-2", "accuracy": 0.88},
]

winner_threshold = 0.9

for model in ergebnisse:
    name = model["name"]
    accuracy = model["accuracy"]
    if accuracy >= winner_threshold:
        print(f"Der Gewinner ist {name} mit {accuracy} Genauigkeit!")
    else:
        print(f"{name} ist raus.")
