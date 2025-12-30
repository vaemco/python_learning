model_results = [
    {"name": "LinearRegression", "accuracy": 0.82},
    {"name": "RandomForest", "accuracy": 0.91},
    {"name": "SVM", "accuracy": 0.88},
    {"name": "NeuralNet", "accuracy": 0.95}
]

# Eine leere Liste für die Gewinner
top_models = []

for key in model_results:
    if key["accuracy"] >= 0.90:
        top_models.append(key['name'])

print(f"Die besten Modelle sind: {top_models}")

  