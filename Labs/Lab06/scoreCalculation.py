# Author: Anthony Cavallo
# Date: 10/22/2025
# Description: Calculation of scores dependent on difficulty.
# Code of honesty: I certify that this lab is entirely my own work.

def calculate_score(hits, misses, difficulty_level):
    if difficulty_level == 1:
        score = hits * 10 - misses * 5
    elif difficulty_level == 2:
        score = hits * 15 - misses * 7
    elif difficulty_level == 3:
        score = hits * 20 - misses * 10
    else:
        print("Invalid difficulty level! Must be 1, 2, or 3.")
        score = None
    return score
def main():
    print("Score Calculation System")
    print("Press 's' at any time to stop.")

    while True:
        hits_input = input("Enter number of hits: ")
        if hits_input.lower() == 's':
            break

        misses_input = input("Enter number of misses: ")
        if misses_input.lower() == 's':
            break

        difficulty_input = input("Enter difficulty level (1–3): ")
        if difficulty_input.lower() == 's':
            break
        if hits_input.isdigit() and misses_input.isdigit() and difficulty_input.isdigit():
            hits = int(hits_input)
            misses = int(misses_input)
            difficulty = int(difficulty_input)
        else:
            print("Please enter valid numbers for hits, misses, and difficulty.")
            continue

        score = calculate_score(hits, misses, difficulty)
        if score is not None:
            print("Your score for this round:", score)
            print("")
    print("Score calculation ended.")
main()