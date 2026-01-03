number = int(input("Enter a number: "))

for i in range(0, 100):
    if number % i == 0 and i !=1 and i != number:
        print(number, "is a prime number")
        break