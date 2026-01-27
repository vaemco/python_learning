"""
Purpose: Safe division function preventing crashes.
Status: Educational / Completed
Topics: Exceptions, Functions
"""

def calculate_roi(profit,cost):
    try:
        roi = profit / cost
        return roi
    except ZeroDivisionError:
        print("Kosten sind 0!")
        return 0
    
a = calculate_roi(100, 50)
b = calculate_roi(100, 0)


print(a)
print(b)   