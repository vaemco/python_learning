import pandas as pd
from pathlib import Path

file_path = Path(__file__).parent / "house_prices.csv"
df = pd.read_csv(file_path)
muc_mask = df["Location"] == "Munich"

muc_houses = df[muc_mask]
print(muc_houses.to_string(index=False))
avg_price = muc_houses["Price"].mean()
print(f"Durchschnitt in München: {avg_price}")