# Author: Anthony Cavallo
# Date: 10/07/2025
# Description: Simple Inventory Manager using lists
# Code of honesty: I certify that this lab is entirely my own work.

rucksack = []
max_items = 5
choice = ""

while choice != "4":
    print("\nInventory Manager")
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Display the Contents")
    print("4. Leave the Inventory Manager")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        if len(rucksack) >= max_items:
            print("Your rucksack is full. You can't add more items.")
        else:
            item = input("Enter the item to add: ")
            if item == "":
                print("You didn't type anything.")
            else:
                rucksack.append(item)
                print(item, "has been added.")
    elif choice == "2":
        if len(rucksack) == 0:
            print("Your rucksack is empty.")
        else:
            item = input("Enter the item to remove: ")
            if item in rucksack:
                rucksack.remove(item)
                print(item, "has been removed.")
            else:
                print("That item is not in your rucksack.")
    elif choice == "3":
        if len(rucksack) == 0:
            print("Your rucksack is empty.")
        else:
            print("\nItems in your rucksack:")
            for i in range(len(rucksack)):
                print(i + 1, ".", rucksack[i])
    elif choice == "4":
        print("Leaving the Inventory Manager. Goodbye!")
    else:
        print("Invalid option, please choose between 1 and 4.")
