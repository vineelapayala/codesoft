import random
options=("rock", "paper", "scissors")
going=True
score=0
computer_score=0
while going:
    player=None
    computer=random.choice(options)
    while player not in options:
        player=input("Enter a choice (rock, paper, scissors):")
    print(f"Player:{player}")
    print(f"Computer:{computer}")
    if player==computer:
        print("It's a tie!")
    elif player=="rock" and computer=="scissors":
        print("You win!")
        score+=1
    elif player=="paper" and computer=="rock":
        print("You win!")        
        score+=1
    elif player=="scissors" and computer=="paper":
        print("You win!")
        score+=1
    else:
        print("You lose!")
        computer_score+=1
    print("Current Score:")
    print(f"Player: {score}  Computer: {computer_score}")
    if not input("Play again? (y/n): ").lower() == "y":
        going=False
print("Final Score:")
print(f"Player:{score}  Computer:{computer_score}")
print("Thanks for playing the game!")