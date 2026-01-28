"""
Purpose: Cleaning data by handling missing values (NaN).
Status: Educational / Completed
Topics: Pandas, Data Cleaning, fillna, dropna
"""

import pandas as pd

raw_data = {
    "customer_id": [1, 2, 3, 4, 5],
    "age": [25, 30, None, 22, 35],  
    "rating": [5, None, 4, 1, 5],  
    "country": ["DE", "US", "DE", "US", "DE"],
}

df = pd.DataFrame(raw_data)
print("Fehlende Werte pro Spalte:")
print(df.isna().sum())

avg_age = df["age"].mean()
df["age"] = df["age"].fillna(avg_age)
df = df.dropna(subset=["rating"])

print("\nBereinigte Daten:")
print(df)
