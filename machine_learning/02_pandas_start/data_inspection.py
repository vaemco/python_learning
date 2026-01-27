"""
Purpose: Inspecting DataFrame structure and statistics.
Status: Educational / Completed
Topics: Pandas, info(), describe(), head()
"""

import pandas as pd 
from pathlib import Path
file_path = Path(__file__).parent / "data" / "house_prices.csv"
df = pd.read_csv(file_path)


print(df.head())
print(df.info())      
print(df.describe())