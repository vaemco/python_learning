"""
Purpose: Demonstrates saving and loading data to/from CSV.
Status: Educational / Completed
Topics: Pandas, CSV, I/O
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
csv_path = DATA_DIR / "clients.csv"

clients = {
    "id": [101, 102, 103],
    "customer": ["Apple", "Google", "Amazon"],
    "budget": [50000, 120000, 95000],
}
df = pd.DataFrame(clients)
df.to_csv(csv_path, index=False)

df_loaded = pd.read_csv(csv_path)
print(df_loaded)
