import pandas as pd
from pathlib import Path
file_path = Path(__file__).parent / "sales_raw.csv"

'''class SalesAnalyzer:

    clean_mask = df["Units_Sold"] <= 0 
    cleaned_sales = df[~clean_mask]

    df["Revenue"] = df["Units_Sold"] * df["Price"]

    data_mask = (df["Region"] == "North") & (df["Revenue"] > 3000)
    sales_north = df[data_mask]
    rev_sum = sales_north["Revenue"].sum()
    with open("top_performers.txt", "w") as file:
        file.write((sales_north["Product"].to_string(index=False)) + f"\n\nTotal Revenue: {rev_sum}")'''



class SalesAnalyzer:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

    def run_pipeline(self):
        # 1. Cleaning (Wir überschreiben self.df)
        self.df = self.df[self.df["Units_Sold"] > 0]
        
        # 2. Calculation
        self.df["Revenue"] = self.df["Units_Sold"] * self.df["Price"]
        
        # 3. Analysis (North & > 3000)
        mask = (self.df["Region"] == "North") & (self.df["Revenue"] > 3000)
        result_df = self.df[mask]
        
        return result_df

# Draußen nutzen:
analyzer = SalesAnalyzer(file_path)
top_performers = analyzer.run_pipeline()
# ... dann speichern ...