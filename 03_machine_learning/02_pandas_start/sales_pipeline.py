"""
Purpose: OOP-based sales analysis pipeline including cleaning, calculation, and reporting.
Status: Educational / Completed
Topics: Pandas, Classes, Pipelines
"""

import pandas as pd
from pathlib import Path
file_path = Path(__file__).parent / "data" / "sales_raw.csv"


class SalesAnalyzer:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

    def run_pipeline(self):
        self.df = self.df[self.df["Units_Sold"] > 0]
        
        self.df["Revenue"] = self.df["Units_Sold"] * self.df["Price"]
        
        mask = (self.df["Region"] == "North") & (self.df["Revenue"] > 3000)
        result_df = self.df[mask]
        
        return result_df

analyzer = SalesAnalyzer(file_path)
top_performers = analyzer.run_pipeline()