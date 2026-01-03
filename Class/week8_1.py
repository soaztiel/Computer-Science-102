def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average
numbers = [3,6,9,12,15]
avg = calculate_average(numbers)
print(avg)