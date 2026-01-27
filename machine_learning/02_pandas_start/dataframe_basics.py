"""
Purpose: Creating a DataFrame manually and calculating a new column.
Status: Educational / Completed
Topics: Pandas, DataFrames, Column Operations
"""

import pandas as pd

data = {
    'Name' : ["Nvidia H100", "RTX 4090", "A100"],
    "VRAM_GB" : [80, 24, 40],
    "Preis_USD" : [30000, 1600, 10000]
}

gpu_df = pd.DataFrame(data)
gpu_df["Price_per_GB"] = gpu_df["Preis_USD"] / gpu_df["VRAM_GB"]
print(gpu_df)

