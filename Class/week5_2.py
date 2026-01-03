import random

rows = 4
cols = 4

mat = []
for i in range (rows):
    row = []
    for h in range(cols):
        row.append(random.randint(10,100))
    mat.append(row)
print(mat)

length = int(input('enter a list length:'))
L = []
for i in range(length):
    N = input("enter a number")
    L.append(N)
print(L)