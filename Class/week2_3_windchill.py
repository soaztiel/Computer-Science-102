t = int(input('Enter temperature in Fahrenheit'))
w = int(input('Enter wind speed in mph'))
# Model parameters
a = 35.74
b = .6215
# compute and display the windchill
wc = (a+b*t) * w
print(wc)