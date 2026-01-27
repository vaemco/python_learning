"""
Purpose: Calculating the dot product of two vectors.
Status: Educational / Completed
Topics: NumPy, Dot Product, Model Comparison
"""

import numpy as np

weights = np.array([0.6, 0.3, 0.1])
model_a = np.array([0.9, 0.8, 0.5])
model_b = np.array([0.7, 0.9, 0.9])

a = np.dot(model_a, weights)
b = np.dot(model_b, weights)

if a > b:
    print("Model A is better")
else:
    print("Model B is better")
