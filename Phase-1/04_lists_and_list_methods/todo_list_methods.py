"""
Purpose: Basic list operations (indexing, appending, popping, looping).
Status: Educational / Completed
Topics: Lists
"""

# Manipulating lists: Indexing, Append, Loop
todos = ["python üben", "zug fahren", "zocken"]

print("Startliste:", todos)
print("Drittes Element:", todos[2])

todos.append("lesen")
print("Nach append:", todos)

done = todos.pop(1)
print(f"Erledigt: {done}")

for todo in todos:
    print(f"Ich muss noch {todo} erledigen")
