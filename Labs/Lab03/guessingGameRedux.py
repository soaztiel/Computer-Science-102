# Author: Anthony Cavallo
# Date: 09/23/25
# Description: A guessing game
# Code of honesty: I have not copied from any source without proper citation.

favoriteNumber = 42
guesses = 3

while guesses > 0:
    #Prompt the user for a number between  1 and 100, inclusively
    playerGuess = int(input('I am thinking of a number between 1 and 100, inclusively. What is my number? Guesses left: ' + str(guesses) + ' '))

    #If the number is the same, tell the user they won
    if playerGuess == favoriteNumber:
        print(f"Good guess! {favoriteNumber} was the number!")
        break
    #If the number is outside of the range, tell the user they are outside the range
    elif playerGuess > 100 or playerGuess < 1:
        print(f"No good! {playerGuess} is outside of the range!")
    elif playerGuess < favoriteNumber:
        print(f"Too low! {playerGuess} is less than the number!")
        guesses -= 1
    elif playerGuess > favoriteNumber:
        print(f"Too high! {playerGuess} is greater than the number!")
        guesses -= 1
#Otherwise, tell the user they lost
else:
    print(f"You have run out of guesses. {favoriteNumber} was the number!")
