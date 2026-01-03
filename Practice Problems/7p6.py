data = [
    {"apple": 2, "banana": 3},
    {"banana": 1, "orange": 5},
    {"apple": 4}
]
fru = {}

for fruits in data:
    for fruit, n in fruits.items():
        if fruit not in fru:
            fru[fruit] = n
        else:
            fru[fruit] += n
print(fru)