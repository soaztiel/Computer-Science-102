phone = {'jimmy': "674-7190", 'yogul': "891-4583"}

name = input("Enter a name: ")

if name in phone:
    print(phone[name])
else:
    print("name not found")