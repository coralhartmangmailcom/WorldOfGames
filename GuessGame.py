import random


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    while True:
        guess = input(f'Please guess a number between 1 and {difficulty}: ')
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= difficulty:
                return guess
        print('Invalid input. Please enter a valid number.')


def compare_results(secret_number, guess):
    if secret_number == int(guess):
        print("Congratulations! Your guess is accurate. You won!")
        return True
    else:
        print(f"Sorry, your guess is wrong. The number was {secret_number}. You lost!")
        return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, guess)

