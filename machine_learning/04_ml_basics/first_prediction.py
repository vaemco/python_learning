import numpy as np
from sklearn.linear_model import LinearRegression

'''x = np.array([[20], [25], [30], [40], [50]])
y = np.array([[6], [8], [10], [14], [18]])

model = LinearRegression()
model.fit(x, y)
pizza = np.array([[60]])
prediction = model.predict(pizza)

print(prediction)'''

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([[3], [5], [7], [9], [11]])
model = LinearRegression()
model.fit(x, y)
new_data = np.array([[6]])
prediction = model.predict(new_data)
print(prediction)