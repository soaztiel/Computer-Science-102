# Author: Anthony Cavallo
# Date: 10/07/2025
# Description: Update high scores using lists instead of individual variables
# Code of honesty: I certify that this lab is entirely my own work.

# create lists for scores and initials
scores = [0, 0, 0]
initials = ["", "", ""]

print("Root Beer Tapper - High Scores (type 'exit' to stop)")
print("Current High Scores:")
for i in range(3):
    print(i + 1, ".", initials[i], "-", scores[i])

entry = ""

while entry.lower() != "exit":
    entry = input("Enter a new score (or 'exit' to finish): ")
    if entry.lower() == "exit":
        break

    if not entry.isdigit():
        print("Please enter a number or 'exit'.")
        continue

    score = int(entry)
    player = input("Enter the player's initials (max 3 letters): ")[:3]

    # check where to place new score
    if score > scores[0]:
        scores[2] = scores[1]
        scores[1] = scores[0]
        scores[0] = score

        initials[2] = initials[1]
        initials[1] = initials[0]
        initials[0] = player
    elif score > scores[1]:
        scores[2] = scores[1]
        scores[1] = score

        initials[2] = initials[1]
        initials[1] = player
    elif score > scores[2]:
        scores[2] = score
        initials[2] = player
    else:
        print("That score did not make the top three.")

    print("\nUpdated High Scores:")
    for i in range(3):
        print(i + 1, ".", initials[i], "-", scores[i])
    print()

print("Final High Scores:")
for i in range(3):
    print(i + 1, ".", initials[i], "-", scores[i])
print("Goodbye!")
