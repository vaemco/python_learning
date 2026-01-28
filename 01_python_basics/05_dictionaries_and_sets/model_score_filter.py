"""
Purpose: Filtering models based on accuracy scores.
Status: Educational / Completed
Topics: List of Dictionaries, Filtering
"""

model_results = [
    {"name": "LinearRegression", "accuracy": 0.82},
    {"name": "RandomForest", "accuracy": 0.91},
    {"name": "SVM", "accuracy": 0.88},
    {"name": "NeuralNet", "accuracy": 0.95}
]

# An empty list for the winners
top_models = []

for key in model_results:
    if key["accuracy"] >= 0.90:
        top_models.append(key['name'])

print(f"Die besten Modelle sind: {top_models}")

  