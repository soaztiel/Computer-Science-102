# Author: Anthony Cavallo
# Date: 10/07/2025
# Description: Creates a 7x7 grid with random elevations and finds the highest and lowest
# Code of honesty: I certify that this lab is entirely my own work.

import random

rows = 7
cols = 7
elevations = []

# create 7x7 list filled with 0
for r in range(rows):
    row = []
    for c in range(cols):
        row.append(0)
    elevations.append(row)

# fill with random numbers between 10 and 99
for r in range(rows):
    for c in range(cols):
        elevations[r][c] = random.randint(10, 99)

# find highest and lowest
highest = -1
low = 999
high_x = 0
high_y = 0
low_x = 0
low_y = 0

for r in range(rows):
    for c in range(cols):
        if elevations[r][c] > highest:
            highest = elevations[r][c]
            high_x = r
            high_y = c
        if elevations[r][c] < low:
            low = elevations[r][c]
            low_x = r
            low_y = c

print("Highest elevation:", highest, "at row", high_x, "column", high_y)
print("Lowest elevation:", low, "at row", low_x, "column", low_y)
print()

print("Elevation Map:")
for r in range(rows):
    for c in range(cols):
        print(elevations[r][c], end=" ")
    print()
