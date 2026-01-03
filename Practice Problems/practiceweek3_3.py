x = int(input("Enter a x value: "))
y = int(input("Enter a y value: "))

if x == 0 and y == 0:
    print("Your point is at the origin")
elif x > 0 and y > 0:
    print("Your point is in quadrant 1")
elif x < 0 and y > 0: 
    print("Your point is in quadrant 2")
elif x < 0 and y < 0:
    print("Your point is in quadrant 3")
elif x > 0 and y < 0:
    print("Your point is in quadrant 4")
else:
    print("Your point is on an axis")