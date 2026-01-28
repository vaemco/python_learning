"""
Purpose: Managing training configuration using a dictionary.
Status: Educational / Completed
Topics: Dictionaries, Updates, get() method
"""

# Read, write, and extend a dictionary
training_config = {
    "learning_rate": 0.01,
    "epochs": 50,
    "model_name": "ResNet",
}

print(
    f"Wir trainieren das Modell {training_config['model_name']} "
    f"für {training_config['epochs']} Epochen."
)

training_config["learning_rate"] = 0.001
training_config["epochs"] = 100
training_config["optimizer"] = "Adam"

print("Aktuelle Config:", training_config)
print("Optimizer via get():", training_config.get("optimizer"))
