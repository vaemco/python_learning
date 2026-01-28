"""
Purpose: Visualizing data using Matplotlib (scatter plot).
Status: Educational / Completed
Topics: Matplotlib, Scatter Plot, Visualization
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

file_path = Path(__file__).parent / "data" / "house_prices.csv"
df = pd.read_csv(file_path)

plt.scatter(df["Square_Meters"], df["Price"])
plt.xlabel("Square Meters")
plt.ylabel("Price") 
plt.title("House Prices vs. Square Meters")
plt.show()