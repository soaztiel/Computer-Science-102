x = int(input("Enter the first side length: "))
y = int(input("Enter the second side length: "))
z = int(input("Enter the third side length: "))

if x == y == z :
    print("This is an equilateral triangle.")
elif x == y or x == z or y == z :
    print("This is an isosceles triangle.")
else:
    print("This is a scalene triangle.")