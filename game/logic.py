import random

choices = ["stone", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def decide_winner(player, computer):
    rules = {
        "stone": "scissors",
        "scissors": "paper",
        "paper": "stone"
    }

    if player == computer:
        return "draw"
    elif rules[player] == computer:
        return "player"
    else:
        return "computer"