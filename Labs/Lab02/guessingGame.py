# Author: Anthony Cavallo
# Date: 09/14/2025
# Description: A guessing game
# Honor Code: I affirm this work is my own and I've credited external sources.

import random

x = random.randint(1, 100)

y = int(input("A random number between 1 and 100 has been generated. Try to guess it: "))

if y < x:
    print("Your answer was too low. Better luck next time.")
elif y > x:
    print("Your answer was too high. Better luck next time.")
else:
    print("Congratulations! You guessed the correct number.")