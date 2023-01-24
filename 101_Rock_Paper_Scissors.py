import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors) : ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {
                "player"     : player_choice, 
                "computer"   : computer_choice
              }
    
    return choices

def check_win(player, computer):
    print(f"\nYou chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock": 
        if computer == "scissors":
            return "Rock smashes Scissors, You win!"
        else:
            return "Paper covers Rock! You lose."
    elif player == "paper": 
        if computer == "rock":
            return "Paper covers Rock!, You win!"
        else:
            return "Scissors cut Paper, You lose."
    elif player == "scissors": 
        if computer == "paper":
            return "Scissor cut Paper!, You win!"
        else:
            return "Rock smashes Scissors, You lose."
    


while True: 
    choices = get_choices()
    results = check_win(choices["player"], choices["computer"])
    print(results)
    print("\n"+ "*"*20 +"\n")
    game_loop = input("Would you like to play again? (y/n) : ")
    if game_loop.lower() == 'n':
        print("Goodbye.")
        break
