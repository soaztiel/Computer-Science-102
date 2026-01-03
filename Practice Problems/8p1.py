# problem 1
def greet():
    print("hello world")
greet()

# problem 2
def add (a,b):
    return a+b
print(add(2,5))

# problem 3
def count_char(s, char):
    count = 0
    for letters in s:
        if letters == char:
            count += 1
    print(count)
count_char("ur mom", "m")

# problem 4
def find_max(lst):
    for ns in lst:
        if ns > max:
            max = ns
    print(max)
find_max([1,4,15,2,34,5,12])

# problem 5
def factorial(n):
    multiples = 1
    while round < n:
        multiples = multiples * round
        round +=1
    print(multiples)
factorial(3)

# problem 6
def count_vowels(s):
    vowel = ["a","e","i","o","u"]
    for chars in s.lower():
        if chars in vowel:
            i += 1
    print(count)
count_vowels("We all know mario is super awesome")

# problem 7
def find_index(lst, target):
    i = 0
    if target not in lst:
        return -1
    while i < len(lst):
        if lst(i) != target:
            i += 1
        else:
            break
    return i
print(find_index([12,3,4,45,56,7,8,2,4,554], 56))

# problem 8
def generate_events(n):
    even = []
    for i in range[1, n+1]:
        if i%2 == 0:
            even.append(i)
    return even
print(generate_events(14))