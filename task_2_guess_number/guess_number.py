import random


def play_game():
    """Run the Guess the Number game."""
    secret_number = random.randint(1, 100)
    attempts = 0

    print("===== GUESS THE NUMBER GAME =====")
    print("I have selected a number between 1 and 100.")
    print("Try to guess the number!")

    while True:
        user_input = input("Enter your guess: ").strip()

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        attempts += 1

        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            print(f"Total attempts: {attempts}")
            break


if __name__ == "__main__":
    play_game()
