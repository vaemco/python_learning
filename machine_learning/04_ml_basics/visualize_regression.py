"""
Purpose: Visualizing a linear regression model with Matplotlib.
Status: Educational / Completed
Topics: Scikit-Learn, Matplotlib, Regression Line
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 

x = np.array([[20], [25], [30], [40], [50]])
y = np.array([[6], [8], [10], [14], [18]])

model = LinearRegression()
model.fit(x, y)
'''pizza = np.array([[60]])
prediction = model.predict(pizza)
print(prediction)'''
x_line = np.linspace(19, 51, 100).reshape(-1, 1)
y_line = model.predict(x_line)

plt.scatter(x,y, color="red", label="Preis Datenpunkte")
plt.plot(x_line,y_line, color="blue", label="Regression Line")
plt.title("Pizza Price Prediction")
plt.xlabel("Diameter (cm)")  
plt.ylabel("Price (EUR)")
plt.legend()
plt.show()