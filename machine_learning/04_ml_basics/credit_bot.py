"""
Purpose: Simple decision tree classifier for credit approval.
Status: Educational / Completed
Topics: Scikit-Learn, Decision Trees, Classification
"""

import numpy as np  
from sklearn.linear_model import tree

x = np.array([[50000, 0], [60000, 0], [20000, 1], [25000, 0], [80000, 1]])
y = np.array([1, 1, 0, 1, 0])

model = tree.DecisionTreeClassifier()
model.fit(x, y)
new_data = np.array([[40000, 1]])
prediction = model.predict(new_data)
print(prediction)