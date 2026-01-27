"""
Purpose: Grouping data and calculating aggregated statistics (e.g., mean price by location).
Status: Educational / Completed
Topics: Pandas, GroupBy, Aggregation
"""

import pandas as pd
from pathlib import Path
file_path = Path(__file__).parent / "data" / "house_prices.csv"
df = pd.read_csv(file_path)

group_loc = df.groupby("Location")["Price"].mean()
print(group_loc)

group_rooms = df.groupby("Location")["Rooms"].max()
print(group_rooms)