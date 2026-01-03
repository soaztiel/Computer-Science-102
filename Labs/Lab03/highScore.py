# Author: Anthony Cavallo
# Date: 09/23/25
# Description: A high score tracker
# Code of honesty: I have not copied from any source without proper citation.

first_score = 0
second_score = 0
third_score = 0

first_initials = ""
second_initials = ""
third_initials = ""

choice = "Y"

while choice == "Y":
    score = int(input("Enter a high score: "))
    initials = input("Enter player initials: ")

    if score > first_score:
        third_score = second_score
        third_initials = second_initials

        second_score = first_score
        second_initials = first_initials

        first_score = score
        first_initials = initials

    elif score > second_score:
        third_score = second_score
        third_initials = second_initials

        second_score = score
        second_initials = initials

    elif score > third_score:
        third_score = score
        third_initials = initials

    choice = input("Do you want to enter another score? (Y/N): ").upper()

print("\nTop 3 High Scores:")
print("1.", first_initials, first_score)
print("2.", second_initials, second_score)
print("3.", third_initials, third_score)
