"""
Purpose: Quick recap of linear regression (train and predict).
Status: Educational / Completed
Topics: Scikit-Learn, Linear Regression
"""

import numpy as np
from sklearn.linear_model import LinearRegression
x = np.array([[1], [2], [4], [6]])
y = np.array([[50], [60], [80], [100]])

model = LinearRegression()
model.fit(x, y)
new_data = np.array([[3]])
prediction = model.predict(new_data)
print(prediction)
