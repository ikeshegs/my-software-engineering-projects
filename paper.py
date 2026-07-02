# Rock, Paper, Scissors Game
import random

options = ("paper", "scissors", "rock")

running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (paper, scissors, rock): ").strip().lower()
        
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    
    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("YOU WIN!!")
    elif player == "scissors" and computer == "paper":
        print("YOU WIN!!")
    elif player == "paper" and computer == "rock":
        print("YOU WIN!!")
    else:
        print("YOU LOSE!!")
        
    play_again = input("Play again (y/n): ").strip().lower()
    
    if play_again != "y":
        running = False
    
print("Thanks for playing!")
