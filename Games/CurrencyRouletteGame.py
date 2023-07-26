import random
import requests


def get_money_interval(difficulty, total_value):
    interval = (total_value - (5 - difficulty), total_value + (5 - difficulty))
    return interval


def get_currency_rate(from_currency, to_currency):
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][to_currency]
    return rate


def get_guess_from_user():
    while True:
        guess = input("Guess the value of a random number between 1-100 in USD: ")
        if guess.isdigit():
            return float(guess)
        print("Invalid input! Please enter a valid number.")


def play(difficulty):
    total_value = random.randint(1, 100)
    rate = get_currency_rate('USD', 'ILS')
    converted_value = total_value * rate
    interval = get_money_interval(difficulty, converted_value)

    guess = get_guess_from_user()
    print(f"The converted value of the random number in ILS is: {converted_value}")

    if interval[0] <= guess <= interval[1]:
        print("Congratulations! Your guess is within the interval. You won!")
        return True
    else:
        print("Sorry, your guess is outside the interval. You lost!")
        return False

