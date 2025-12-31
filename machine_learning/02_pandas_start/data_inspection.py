import pandas as pd 
from pathlib import Path
file_path = Path(__file__).parent / "house_prices.csv"
df = pd.read_csv(file_path)


print(df.head())
print(df.info())      
print(df.describe())