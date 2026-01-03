year = int(input("Enter the year here: "))

if year % 100 != 0 and year % 4 == 0 :
    print("This is a leap year.")
else:
    print("This is not a leap year.")