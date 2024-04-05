import random

def get_choices():
    player_choice = input("Enter a choice (rock paper scissors) : ")
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    return check_win(player_choice, computer_choice)


def check_win(player,computer):
    print(f"You chose {player}, Computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors": return "Rock smashes scissors. You win!"
        else: return "Paper covers rock. You lose."
    elif player == "scissors":
        if computer == "paper": return "Scissors cut paper. You win!"
        else: return "Rock smashes scissors. You lose."
    else:
        if computer == "rock": return "Paper covers rock. You win!"
        else: return "Scissors cut paper. You lose."

result = get_choices()
print(result)