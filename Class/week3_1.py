x = int(input("Please enter the temperature outside in Celsius: "))

if x < 0 :
    print("It's freezing outside! Wear a coat!")
elif x <= 15 :
    print("It's cold, wear a jacket!")
elif x <= 25 :
    print("It's a bit chilly, a sweater should be enough!")
else:
    print("It's warm! You don't need heavy clothing.")