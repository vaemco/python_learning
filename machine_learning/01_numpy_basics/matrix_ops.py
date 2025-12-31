import numpy as np

houses = np.array([
    [100, 10],
    [150, 5],
    [80,  50],
    [120, 20]
])
weights = np.array([3000, -200])

print(f"House Prices: {houses.shape} ")

ergebnisse = np.dot(houses, weights)
print(f"Ergebnisse: {ergebnisse}")