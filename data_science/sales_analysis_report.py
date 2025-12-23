from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"
sales_path = DATA_DIR / "global_sales.csv"
report_path = DATA_DIR / "europe_report.csv"

df = pd.read_csv(sales_path)

df["revenue"] = df["quantity"] * df["price_per_unit"]
europe_df = df[df["region"] == "Europe"]
europe_df = europe_df[["revenue", "product"]]

europe_df.to_csv(report_path, index=False)

print(f"Bericht erstellt ({report_path.name}). Gesamtumsatz Europa: {europe_df['revenue'].sum()}")
