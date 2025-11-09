import random

print("\nLet's play rock, paper, and scissors for fun!")
selection = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Enter your choice (rock, paper, or scissors), or 'quit' to exit: ").lower()
    if user_pick == 'quit':
        print("Thanks for playing!")
        break
    if user_pick not in selection:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue
    computer = random.choice(selection)
    print(f"Computer chose: {computer}")

    if user_pick == computer:
        print("Tie! How boring.")
    elif (user_pick == "rock" and computer == "paper") or \
         (user_pick == "scissors" and computer == "rock") or \
         (user_pick == "paper" and computer == "scissors"):
        print("Computer wins!")
    else:
        print("You win!")
print("------the end--------")