import time
import random

duration = 0.7


def generate_sequence(difficulty):
    sequence = []
    for i in range(difficulty):
        number = random.randint(1, 101)
        sequence.append(number)
    return sequence


def display_numbers(sequence, duration):
    for number in sequence:
        print(number, end='', flush=True)
        time.sleep(duration)
        print("\r", end='', flush=True)


def get_list_from_user(difficulty):
    user_list = []
    for j in range(difficulty):
        number = input("Enter a number: ")
        if not number.isdigit():
            print('You have entered a wrong value. Try again from the start.')
            return get_list_from_user(difficulty)
        elif int(number) not in range(1, 102):
            print('Your guess is out of range. Try again from the start.')
            return get_list_from_user(difficulty)
        else:
            user_list.append(int(number))
    return user_list


def is_list_equal(sequence, user_list):
    if sequence == user_list:
        print("Congratulations! Your memory is outstanding! You won!")
        return True
    else:
        print(f"Sorry. The sequence was {sequence}. You lost!")
        return False


def play(difficulty):
    sequence = generate_sequence(difficulty)
    display_numbers(sequence, duration)
    user_list = get_list_from_user(difficulty)
    return is_list_equal(sequence, user_list)



