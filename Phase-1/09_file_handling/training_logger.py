results = [0.75, 0.82,0.91]
with open("training_log.txt", "w") as file:
    for result in results:
        file.write(f"Epoch X: Loss {result}\n")