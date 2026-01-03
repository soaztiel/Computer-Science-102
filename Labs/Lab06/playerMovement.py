# Author: Anthony Cavallo
# Date: 10/22/2025
# Description: Player movement in a game.
# Code of honesty: I certify that this lab is entirely my own work.

def move_player():
    x = 0
    y = 0
    grid_size = 5

    print("Player Movement Started! (Grid size: 5x5)")
    print("Controls: up, down, left, right | Press 's' to stop.")
    print("Starting position:", "(", x, ",", y, ")")

    while True:
        direction = input("Enter direction: ")
        direction = direction.lower()

        if direction == 's':
            break
        if direction == 'up':
            if y < grid_size - 1:
                y = y + 1
            else:
                print("You hit the top boundary!")
        elif direction == 'down':
            if y > 0:
                y = y - 1
            else:
                print("You hit the bottom boundary!")
        elif direction == 'left':
            if x > 0:
                x = x - 1
            else:
                print("You hit the left boundary!")
        elif direction == 'right':
            if x < grid_size - 1:
                x = x + 1
            else:
                print("You hit the right boundary!")
        else:
            print("Invalid input! Please enter up, down, left, right, or 's'.")

        print("Current position:", "(", x, ",", y, ")")

    print("Final position:", "(", x, ",", y, ")")
move_player()