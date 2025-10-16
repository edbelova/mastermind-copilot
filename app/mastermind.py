from .game import (
    generate_code, validate_guess, check_code_guessed,
    generate_hint, get_win_percentage, format_guess_stats
)

# Wave 4

def play_one_round(guess_stats):
    """Play a single round. Return True if won, False otherwise."""
    print("Generating code...")
    code = generate_code()
    print("Code generated! " + "*" * len(code))

    guesses = 0
    while True:
        guess = input("Guess the code: ")
        if not validate_guess(guess):
            print("Invalid guess. Please try again.")
            continue

        guesses += 1
        if check_code_guessed(guess, code):
            print("Congratulations! You've guessed the code.")
            # record: won in `guesses` attempts
            guess_stats[guesses] = guess_stats.get(guesses, 0) + 1
            return True

        print("Incorrect guess. Try again.")
        print(f"Hint: {generate_hint(guess, code)}")

        if guesses >= 8:
            print("Sorry, you've run out of guesses.")
            print(f"The correct code was: {''.join(code)}")
            return False

def mastermind():
    plays = 0
    wins = 0
    guess_stats = {}

    print("Welcome to Mastermind!")
    print("I have generated a random 4-color code. \n"
          "Use the first letter of a color to make a guess.\n"
          "Possible colors: (R)ed, (G)reen, (B)lue, (Y)ellow, (O)range, (P)urple\n"
          "You have 8 tries to guess the code.")

    while True:
        won = play_one_round(guess_stats)
        plays += 1
        if won:
            wins += 1

        print("\nGame over. Here are your stats:")
        print(f"Total plays: {plays}")
        print(f"Total wins: {wins}")
        print(f"Win percentage: {get_win_percentage(wins, plays)}%")
        print("Guess distribution:")
        for i, line in enumerate(format_guess_stats(guess_stats), start=1):
            print(f"{i}| {line}")

        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing!")
            break