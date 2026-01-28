"""
Purpose: Filling missing values with column mean.
Status: Educational / Completed
Topics: Pandas, NaN, Imputation
"""

import pandas as pd
import numpy as np

data = {
    "Sensor_ID": ["S1", "S2", "S3", "S4", "S5"],
    "Temperature": [20.5, np.nan, 22.1, np.nan, 19.8],
    "Status": ["Active", "Offline", "Active", "Offline", "Active"]
}
df = pd.DataFrame(data)
print(df["Temperature"])

df["Temperature"].fillna(df["Temperature"].mean(), inplace=True)
print(df["Temperature"])