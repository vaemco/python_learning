"""
Purpose: Calculating new columns (net/gross prices) in a DataFrame.
Status: Educational / Completed
Topics: Pandas, column arithmetic
"""

import pandas as pd

data = {
    "product": ["Gaming Laptop", "Mechanical Keyboard", "USB-C Cable", "Monitor 27"],
    "price_net": [1200.00, 80.00, 15.00, 300.00],
    "quantity": [5, 50, 200, 10],
    "tax_rate": [0.19, 0.19, 0.19, 0.19],
}

df = pd.DataFrame(data)

df["total_value"] = df["price_net"] * df["quantity"]
df["price_gross"] = df["price_net"] * (1 + df["tax_rate"])

top_sellers = df[df["total_value"] > 3500]
print("Alle Produkte mit Nettowert und Bruttowert:")
print(df)
print("\nTop-Seller (Wert > 3500):")
print(top_sellers)
