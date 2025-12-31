import pandas as pd
from pathlib import Path
file_path = Path(__file__).parent / "house_prices.csv"
df = pd.read_csv(file_path)

group_loc = df.groupby("Location")["Price"].mean()
print(group_loc)

group_rooms = df.groupby("Location")["Rooms"].max()
print(group_rooms)