marks = {"Alice": 90, "Bob": 65, "Charlie": 82, "Diana": 58}
above70 = {}

for student, grade in marks.items():
    if grade > 70:
        above70[student] = grade

print(above70)