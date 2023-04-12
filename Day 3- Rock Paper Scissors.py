import random

while True:
    user_action = input("Enter a choice (rock, paper scissors):")

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action} its a tie")
    elif user_action == 'rock':
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print('Paper covers rock! You lose.')
    elif user_action == "paper":
        if computer_action == 'rock':
            print('Paper covers rock! You win!')
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashs scissors! You lose.")
            
    play_again = input("Play again? (y/n)")
    if play_again.lower != "y":
        break
    
    
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    
def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ', '.join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action


def determine_windder(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("rock smashs scissors! You win!")
        else:
            print("paper covers rock! You lose.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
            
            
            
while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f'[0, {len(Action) - 1}]'
        print(f"Invalid Slection. Enter a value in range {range_str}")
        continue
    
    computer_action = get_computer_selection()
    determine_windder(user_action, computer_action)
    
    play_again = input("Play again (y/n)")
    if play_again.lower() != "y":
        break