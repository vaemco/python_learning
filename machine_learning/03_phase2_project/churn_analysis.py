"""
Purpose: End-to-end churn analysis (load, clean, calculate, visualize, save).
Status: Educational / Completed
Topics: Pandas, Cleaning, Feature Engineering, Visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   
from pathlib import Path

file_path = Path(__file__).parent / "data" / "churn_raw.csv"
df = pd.read_csv(file_path)
clean_df = df.dropna(subset=["CustomerID"])

age_mean = clean_df["Age"].mean()
clean_df["Age"].fillna(age_mean, inplace=True)
clean_df["Yearly_Cost"] = clean_df["Monthly_Bill"] * 12

sns.heatmap(clean_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

export_path = Path(__file__).parent / "data" / "churn_cleaned.csv"
export_path.parent.mkdir(parents=True, exist_ok=True)
clean_df.to_csv(export_path, index=False)
print(f"Exported cleaned data to {export_path}")