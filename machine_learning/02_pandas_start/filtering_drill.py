import pandas as pd
from pathlib import Path

file_path = Path(__file__).parent / "house_prices.csv"
df = pd.read_csv(file_path)

family_mask = (df["Rooms"] == 2) & (df["Price"] < 500000)
family_houses = df[family_mask]
print(family_houses.to_string(index=False))

luxury_mask = (df["Location"] == "Munich") | (df["Price"] > 800000)
luxury_houses = df[luxury_mask]
print(luxury_houses.to_string(index=False))

no_berlin_mask = (df["Location"] != "Berlin")
no_berlin_houses = df[no_berlin_mask]
print(no_berlin_houses.to_string(index=False))