import random
import os

def get_choices():
    player_choice = str(input("Write your choice: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    choices = ["rock", "paper", "scissor"]
    computer_choice = random.choice(choices)
    print("Player's choice is: " + player_choice + ", Computer's choice is: " + computer_choice)
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "paper":
        print("Computer Wins")
    elif player_choice == "rock" and computer_choice == "scissor":
        print("Player Wins")
    elif player_choice == "paper" and computer_choice == "rock":
        print("Player Wins")
    elif player_choice == "paper" and computer_choice == "scissor":
        print("Computer Wins")
    elif player_choice == "scissor" and computer_choice == "paper":
        print("Player Wins")
    elif player_choice == "scissor" and computer_choice == "rock":
        print("Computer Wins")
    else:
        print(""" Incorrect Input Please Use "rock", "paper" or "scissor" """)

if __name__ == "__main__":
    get_choices()