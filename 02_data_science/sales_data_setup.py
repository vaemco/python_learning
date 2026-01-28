"""
Purpose: Simulating and saving raw sales data.
Status: Educational / Completed
Topics: Pandas, Data Generation, CSV
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
csv_path = DATA_DIR / "global_sales.csv"

raw_data = {
    "order_id": [1001, 1002, 1003, 1004, 1005],
    "region": ["Europe", "US", "Asia", "Europe", "Europe"],
    "product": ["Tablet", "Phone", "Laptop", "Headset", "Phone"],
    "quantity": [10, 5, 2, 50, 20],
    "price_per_unit": [200, 800, 1200, 50, 800],
}

df = pd.DataFrame(raw_data)
df.to_csv(csv_path, index=False)
print(f"Datei '{csv_path.name}' wurde in {DATA_DIR} erstellt!")
