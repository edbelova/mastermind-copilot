import random

# Wave 1
VALID_COLORS = ['R', 'O', 'Y', 'G', 'B', 'P']

def generate_code():
    return [random.choice(VALID_COLORS) for _ in range(4)]

def make_uppercase(guess):
    uppercase_guess = []
    for color in guess:
        if isinstance(color, str):
            uppercase_guess.append(color.upper())
        else:
            return None
    return uppercase_guess

def validate_guess(guess):
    if len(guess) != 4:
        return False

    uppercase_guess = make_uppercase(guess)

    if uppercase_guess is None:
        return False
    
    for color in uppercase_guess:
        if color not in VALID_COLORS:
            return False
    return True

def check_code_guessed(guess, code):
    uppercase_guess = make_uppercase(guess)
    return uppercase_guess == code

# Wave 2
def color_count(guess, code):
    guess_counts = {}
    code_counts = {}

    for color in guess:
        guess_counts[color] = guess_counts.get(color, 0) + 1

    for color in code:
        code_counts[color] = code_counts.get(color, 0) + 1

    total = 0
    for color in guess_counts:
        total += min(guess_counts[color], code_counts.get(color, 0))

    return total

def correct_pos_and_color(guess, code):
    count = 0
    for g, c in zip(guess, code):
        if g == c:
            count += 1
    return count

def generate_hint(guess, code):
    correct_position = correct_pos_and_color(guess, code)
    total_correct = color_count(guess, code)
    correct_color_wrong_position = total_correct - correct_position
    return (correct_position, correct_color_wrong_position)

# Wave 3
def get_win_percentage(wins, plays):
    if plays == 0:
        return 0
    return (wins * 100) // plays

def format_guess_stats(guess_stats):
    formatted_guess_stats = [""] * 8
    for num_of_guesses, num_of_games in guess_stats.items():
        formatted_guess_stats[num_of_guesses - 1] = "X" * num_of_games
    return formatted_guess_stats

# Wave 4
