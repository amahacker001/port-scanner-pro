def save_result(data):
    with open("output/results.txt", "a") as f:
        f.write(data + "\n")