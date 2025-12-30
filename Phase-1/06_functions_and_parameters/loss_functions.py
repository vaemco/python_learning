def calculate_l1_loss(predict, actual):
    return abs(predict - actual)

a = calculate_l1_loss(10, 12)
b = calculate_l1_loss(0.9, 0.9)
print(f"Loss a: {a}")
print(f"Loss b: {b}")