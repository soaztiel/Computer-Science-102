input_string = "Hello World"

letter = {}

for c in input_string:
    letter[c] = 0
    
for c in input_string:
    letter[c] += 1


print(letter)