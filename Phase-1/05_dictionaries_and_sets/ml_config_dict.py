"""
Purpose: Managing experiment statistics using a dictionary.
Status: Educational / Completed
Topics: Dictionaries, Key-Value Pairs
"""

experiment_stats = {
    "accuracy": 0.85,
    "loss": 0.4,
    "status": "running"
}

experiment_stats["status"] = "finished"
experiment_stats["training_time"] = 120
experiment_stats["loss"] = 0.35

for key in experiment_stats:
    print(f"Parameter {key} hat Wert {experiment_stats[key]}")