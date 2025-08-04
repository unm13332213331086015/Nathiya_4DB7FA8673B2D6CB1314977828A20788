import random

def roll_dice():
    return random.randint(1, 6)

def dice_simulator():
    print("🎲 Welcome to the Dice Rolling Simulator!")
    while True:
        user_input = input("\nPress Enter to roll the dice or type 'exit' to quit: ")
        if user_input.lower() == "exit":
            print("👋 Thanks for playing!")
            break
        rolled_number = roll_dice()
        print(f"You rolled a {rolled_number} 🎉")
        # Optional: Show dice face with ASCII art
        print_dice_face(rolled_number)

def print_dice_face(number):
    dice_faces = {
        1: ["+-------+", "|       |", "|   ●   |", "|       |", "+-------+"],
        2: ["+-------+", "| ●     |", "|       |", "|     ● |", "+-------+"],
        3: ["+-------+", "| ●     |", "|   ●   |", "|     ● |", "+-------+"],
        4: ["+-------+", "| ●   ● |", "|       |", "| ●   ● |", "+-------+"],
        5: ["+-------+", "| ●   ● |", "|   ●   |", "| ●   ● |", "+-------+"],
        6: ["+-------+", "| ●   ● |", "| ●   ● |", "| ●   ● |", "+-------+"],
    }
    for line in dice_faces[number]:
        print(line)

# Run the simulator
dice_simulator()
