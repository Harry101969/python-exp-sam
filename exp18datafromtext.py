with open("words.txt", "r") as file:
    data = file.readlines()
    for line in data:
        print("Line:", line.strip())


