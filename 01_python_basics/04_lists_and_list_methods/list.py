"""
Purpose: Filtering and sorting a list of prediction scores.
Status: Educational / Completed
Topics: Lists, List Comprehensions, Sorting
"""

'''predictions = [0.91, 0.45, 0.78, 0.62, 0.99, 0.31]

for num in predictions:
    predictions.remove(num) if num < 0.5 else None
    
predictions.append(0.85)


predictions.sort(reverse=True)
print(predictions)

length = len(predictions)
print(length)'''

predictions = [0.91, 0.45, 0.78, 0.62, 0.99, 0.31]

predictions = sorted([p for p in predictions if p >= 0.5] + [0.85], reverse=True)

print(predictions)
print(len(predictions))