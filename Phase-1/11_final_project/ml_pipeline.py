raw_results = [
    {"name": "Model_A", "accuracy": 0.85, "loss": 0.4},
    {"name": "Model_B", "accuracy": "FEHLER", "loss": 0.9}, # Kaputte Daten!
    {"name": "Model_C", "accuracy": 0.92, "loss": 0.1},
    {"name": "Model_D", "accuracy": 0.70, "loss": 0.8}
]
class ModelEvaluator:
    def __init__(self, results):
        self.results = results

    def filter_models(self, min_accuracy):
        good_models = []
        for entry in self.results:
            try:
                if entry["accuracy"] >= min_accuracy:
                    good_models.append(entry["name"])
            except TypeError:
                print(f"Datenfehler bei Modell {entry["name"]} gefunden.")
        return good_models
    def save_report(self, filename):
        filtered_models = self.filter_models(0.80)
        with open(filename, "w") as file:
            for model in filtered_models:
                file.write(f"Bestes Modell: {model}\n")
data = ModelEvaluator(raw_results)
data.save_report("final_report.txt")