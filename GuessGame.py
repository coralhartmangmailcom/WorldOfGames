import random


def play(diff):
    difficulty = diff
    secret_number = random.randint(1, difficulty)
    get_guess_from_user = input(f'Please guess a number between 1 and {difficulty}:')
    if not get_guess_from_user.isdigit():
        print('You have entered a wrong value.')
        return play(difficulty)
    elif int(get_guess_from_user) not in range(1, difficulty+1):
        print('Your guess is out of range.')
        return play(difficulty)

    if secret_number == int(get_guess_from_user):
        print("Congratulations! Your guess is accurate. You won!")
        return True
    else:
        print(f"Sorry, your guess is wrong. The number was {secret_number}. You lost!")
        return False


