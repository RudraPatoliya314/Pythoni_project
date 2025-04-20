import random

def play():
    options = ["rock", "paper", "scissors"]
    user = input("Choose rock, paper, or scissors(eg:rock): ").lower()
    computer = random.choice(options)

    if user not in options:
        print("Invalid choice! Try again.")
        return

    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win! ")
    else:
        print("You lose.")

while True:
    play()
    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break
