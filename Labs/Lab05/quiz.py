# Author: Anthony Cavallo
# Date: 10/14/2025
# Description: A simple quiz game.
# Code of honesty: I certify that this lab is entirely my own work.

quiz = {
"What is the capital of France?": "Paris",
"What is 2 + 2?": "4",
"What is the largest planet in our solar system?": "Jupiter",
"Who wrote 'Romeo and Juliet'?": "Shakespeare"
}

score = 0

for question in quiz:
    print(question)
    answer = input("Enter your answer: ")

    if answer.lower() == quiz[question].lower():
        print("That's the correct answer!")
        score = score + 1
    else:
        print("That's the wrong answer! The correct one is:", quiz[question])

if score == 4:
    print("Congratulations! You got all questions correctly!")
else:
    print("Aw..you didn't get all the questions correct. Better luck next time.")

print("You got", score,"/4 correct.")

print("Thank you for playing the game!")