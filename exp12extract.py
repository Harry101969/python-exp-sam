with open("words.txt", "r") as file:
    words = file.read().split()
    print("Words:", words)

# if u dont want it to be an array
with open("words.txt", "r") as file:
    words = file.read().split()
    print("Words:", " ".join(words))
