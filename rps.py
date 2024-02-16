import random

def main():
    print("Hello! Welcome to Rock, Paper, Scissors!")
    print("The rules of this game are as follows: ")
    print("You will choose rock, paper, or scissors. The program will also select either rock, paper, or scissors.")
    print("The goal is to beat the computer. Rock beats scissors. Scissors beats paper. Paper beats rock.")
    print("If you have the same selection, the game is a tie.")

    user = input("Enter rock, paper, or scissors: ")
    list = ["rock", "paper", "scissors"]
    computer = random.choice(list)

    if(user == computer):
        print("Tie!")
    elif((user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock")):
        print("You win!")
    else:
        print("Oh no! You lose!")

if __name__ == "__main__":
    main()
