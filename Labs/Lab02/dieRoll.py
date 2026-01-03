# Author: Anthony Cavallo
# Date: 09/14/2025
# Description: A die roll simulator
# Honor Code: I affirm this work is my own and I've credited external sources.

import random

x = random.randint(1, 20)

if x == 20:
    print("Critical success! You found the hidden door and a pouch with 5 gold pieces inside.")
elif x == 1:
    print("Critical failure! You didn't find the hidden door and you accidentally alerted the guards.")
elif x >= 12:
    print("You found the hidden door.")
elif x < 12:
    print("You did not find the hidden door.")
