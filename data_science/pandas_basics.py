"""
Purpose: Introduction to Pandas DataFrames, filtering, and basic statistics.
Status: Educational / Completed
Topics: Pandas, DataFrames, Filtering
"""

import pandas as pd

# First steps: Build DataFrame, filter, and get statistics
data = {
    "model_name": ["GPT-4", "Claude 3", "Llama 2", "Mistral"],
    "parameters": [1700, 1000, 70, 7],
    "type": ["Closed", "Closed", "Open", "Open"],
}

df = pd.DataFrame(data)

print("--- My First DataFrame ---")
print(df)
print("\nNur die Spalte model_name:")
print(df["model_name"])
print("\nBasis-Statistiken:")
print(df.describe())

open_source_models = df[df["type"] == "Open"]
small_models = df[df["parameters"] < 100]
print("\n--- Open Source Models ---")
print(open_source_models)
print("\n--- Small Models (< 100B) ---")
print(small_models)
