# problem 1
def arearec(width,length):
    area = width * length
    return area
print(arearec(5,3))

# problem 2
def countlines(file):
    count = 0
    myfile = open("sample.txt", "r")
    lines = myfile.readlines()
    for item in lines:
        count += 1
    return count
print(countlines("sample.txt"))

# problem 3
def divide(a,b):
    try:
        div = a/b
        return div
    except:
        return "cannot divide by 0"
print(divide(51,17))
print(divide(2,0))

# problem 4
def maxval(dict):
    max = 0
    for num in dict.values():
        if num > max:
            max = num
    return max
dictionary = {"a":7, "b":17, "c":10, "d":2, "e":3}
print(maxval(dictionary))

# problem 5
def sumlist(mylist):
    try:
        sum = 0
        lines = open(mylist, "r")
        vallist = lines.readlines()
        for num in vallist:
            val = int(num)
            sum += val
        return sum
    except IOError:
        return "file does not exist"
    except ValueError:
        return "not a number"
print(sumlist("nums.txt"))

# problem 6
def removekey(d, key):
    try:
        del d[key]
        return d
    except:
        return "key not in dictionary"
# dictionary = {"a":7, "b":17, "c":10, "d":2, "e":3} used same as up there
print(removekey(dictionary, "b"))
print(removekey(dictionary, "g"))

# problem 7
def countletter(string):
    count = {}
    for letter in string:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1
    return count
print(countletter("hello"))

# problem 8
def countletter(string):
    words = string.split(" ")
    count = {}
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    return count
print(countletter("hello world from the world of hello"))