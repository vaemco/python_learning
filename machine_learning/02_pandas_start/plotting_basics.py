import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

file_path = Path(__file__).parent / "house_prices.csv"
df = pd.read_csv(file_path)

plt.scatter(df["Square_Meters"], df["Price"])
plt.xlabel("Square Meters")
plt.ylabel("Price") 
plt.title("House Prices vs. Square Meters")
plt.show()