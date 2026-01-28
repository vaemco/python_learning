"""
Purpose: Visualizing correlations between features using a Seaborn heatmap.
Status: Educational / Completed
Topics: Seaborn, Correlation, Heatmap
"""

import seaborn as sns
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt 

filepath = Path(__file__).parent / "data" / "house_prices.csv"
df = pd.read_csv(filepath)
df_numeric = df[["Square_Meters", "Rooms", "Price"]]
corr = df_numeric.corr()
sns.heatmap(corr, annot=True , cmap="coolwarm")
plt.title("Correlation Heatmap of House Features")
plt.show()
