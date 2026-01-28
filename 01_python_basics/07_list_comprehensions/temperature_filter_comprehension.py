"""
Purpose: Filtering a list using loops vs. list comprehensions.
Status: Educational / Completed
Topics: List Comprehensions, Loops, Filtering
"""

import random


# Build list and then filter (Loop vs. List Comprehension)
temperatures = [random.randint(-5, 10) for _ in range(20)]
print("Rohdaten:", temperatures)


def is_valid(temp):
    """Temperatures below 0 are removed."""
    return temp >= 0


clean_with_loop = []
for temp in temperatures:
    if is_valid(temp):
        clean_with_loop.append(temp)

clean_with_comprehension = [temp for temp in temperatures if is_valid(temp)]

print("Gefiltert (Loop):", clean_with_loop)
print("Gefiltert (Comprehension):", clean_with_comprehension)
print(f"Es sind noch {len(clean_with_comprehension)} Werte übrig.")
