"""
Purpose: Logistic regression for binary classification (diabetes check).
Status: Educational / Completed
Topics: Scikit-Learn, Logistic Regression
"""

import numpy as np
from sklearn.linear_model import LogisticRegression

x = np.array([[80], [100], [150], [200]])
y = np.array([0, 0, 1, 1])

model = LogisticRegression()
model.fit(x, y)
new_data = np.array([[120]])
prediction = model.predict(new_data)
print(prediction)
