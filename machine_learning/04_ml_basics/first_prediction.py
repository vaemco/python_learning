import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[20], [25], [30], [40], [50]])
y = np.array([[6], [8], [10], [14], [18]])

model = LinearRegression()
model.fit(x, y)
pizza = np.array([[60]])
prediction = model.predict(pizza)

print(prediction)