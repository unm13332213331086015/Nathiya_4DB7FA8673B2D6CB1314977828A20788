import random

# List of valid choices
choices = ["rock", "paper", "scissors", "lizard", "spock"]

# Define win conditions as a dictionary
win_conditions = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif computer in win_conditions[player]:
        return f"You win! {player.capitalize()} beats {computer.capitalize()}."
    else:
        return f"You lose! {computer.capitalize()} beats {player.capitalize()}."

# Main game loop
def play_game():
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    print("Options: rock, paper, scissors, lizard, spock")

    player = input("Enter your choice: ").lower()

    if player not in choices:
        print("❌ Invalid choice! Please try again.")
        return

    computer = random.choice(choices)
    print(f"Computer chose: {computer.capitalize()}")

    result = determine_winner(player, computer)
    print(result)

# Run the game
play_game()
