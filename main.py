import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s/w/g): ").lower()

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

if youstr not in youDict:
    print("Invalid input! Please enter s, w, or g.")
else:
    you = youDict[youstr]

    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")