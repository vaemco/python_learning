"""
Purpose: Managing a model training queue using list operations.
Status: Educational / Completed
Topics: Lists, Append, Pop
"""

models_to_train = ["LinearRegression", "RandomForest","SVM"]

models_to_train.append("XGBoost")
models_to_train.pop(0)


print(models_to_train, f"next model in queue: {models_to_train[0]}")