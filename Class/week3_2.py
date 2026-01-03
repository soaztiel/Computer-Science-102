x = int(input("Please enter the value of x as an integer: "))
y = int(input("Please enter the value of y as an integer: "))
z = int(input("Please enter the value of z as an integer: "))

if (x < y):
    if (x < z):
        print("x is less than both y and z")
    else:
        print("x is less than y but not less than z")
else:
    print("x is greater than or equal to z")