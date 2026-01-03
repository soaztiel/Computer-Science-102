# Author: Anthony Cavallo
# Date: 09/23/25
# Description: A diamond pattern
# Code of honesty: I have not copied from any source without proper citation.

rows = int(input("Enter an odd number of rows for the diamond: "))
while rows % 2 == 0:
    rows = int(input("That is not odd. Please enter an odd number: "))

i = 1
while i <= rows:
    if i % 2 != 0:
        spaces = (rows - i) // 2
        print(" " * spaces + "*" * i)
    i += 1

i = rows - 2
while i > 0:
    if i % 2 != 0:
        spaces = (rows - i) // 2
        print(" " * spaces + "*" * i)
    i -= 1
