numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
goal = 11
for num in numbers:
    if num == goal:
        print("Done!")
        break
    else:
        print("Checking...")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        continue
    print("Odd number:", num)

s = 0
for s in range(1, 6):
    for i in range(1, 11):
        print(s, "*", i, "=", s * i)
    print()