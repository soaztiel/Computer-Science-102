# Author: Anthony Cavallo
# Date: 10/26/2025
# Description: A simple slot machine simulation using functions, loops, lists, and conditionals.
# Code of honesty: I certify that this lab is entirely my own work.

import random

player_balance = 100.0
machine_balance = 0.0
current_bet = 1.0
reel_symbols = ["cherry", "lemon", "bell", "star", "diamond"]

def print_welcome():
    print("Welcome to Midnight Sunshine Slots!")
    print("Matching two of a kind will win you 2X your bet!")
    print("Matching three of a kind will win you 5X your bet!")
    print("The current bet is $", current_bet)
    print("Good luck!")
    print("")

def print_status():
    print("Your balance: $", round(player_balance, 2), 
          " Machine's balance: $", round(machine_balance, 2), 
          " Current bet: $", round(current_bet, 2))

def print_menu():
    print("What would you like to do?")
    print("1. Add money to the machine")
    print("2. Change your bet amount")
    print("3. Play the game")
    print("4. Cash out and quit")

def add_money():
    global player_balance, machine_balance
    amount = input("How much money would you like to add to the machine: ")
    amount = float(amount)

    if amount <= 0:
        print("Amount must be positive.")
        print("")
    elif amount <= player_balance:
        machine_balance = machine_balance + amount
        player_balance = player_balance - amount
        print("$", amount, "has been added to the machine.")
        print("Machine balance is now $", machine_balance)
        print("You still have $", player_balance)
        print("")
    else:
        print("You do not have that much money.")
        print("")

def change_bet():
    global current_bet
    amount = input("How much money would you like the bet to be (Minimum is $1.00): ")
    amount = float(amount)

    if amount >= 1:
        current_bet = amount
        print("The bet amount has been changed to $", current_bet)
        print("")
    else:
        print("Invalid bet amount. Bet must be at least $1.00.")
        print("")

def play_game():
    global machine_balance

    if machine_balance < current_bet:
        print("The machine does not have enough money to pay for the current bet amount.")
        print("")
        return

    print("Spinning the reels...")
    print("")

    machine_balance = machine_balance - current_bet

    reel1 = random.choice(reel_symbols)
    reel2 = random.choice(reel_symbols)
    reel3 = random.choice(reel_symbols)

    print("--", reel1, "--", reel2, "--", reel3, "--")

    if reel1 == reel2 and reel2 == reel3:
        payout = 5 * current_bet
        machine_balance = machine_balance + payout
        print("Big win! You matched three of a kind and the machine was credited $", payout)
        print("")
    elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
        payout = 2 * current_bet
        machine_balance = machine_balance + payout
        print("Nice! You matched two of a kind and the machine was credited $", payout)
        print("")
    else:
        print("Boo! You did not match any of the reels. Try again!")
        print("")

def cash_out_and_quit():
    global player_balance, machine_balance
    print("Thanks for playing! Here is $", machine_balance, "dollars!")
    player_balance = player_balance + machine_balance
    machine_balance = 0.0
    print("Goodbye!")
    save_results()
    quit()

def save_results():
    file = open("slot_results.txt", "w")
    file.write("Final Player Balance: $" + str(player_balance) + "\n")
    file.write("Final Machine Balance: $" + str(machine_balance) + "\n")
    file.close()

def main():
    print_welcome()
    while True:
        print_status()
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_money()
        elif choice == "2":
            change_bet()
        elif choice == "3":
            play_game()
        elif choice == "4":
            cash_out_and_quit()
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")
            print("")

main()